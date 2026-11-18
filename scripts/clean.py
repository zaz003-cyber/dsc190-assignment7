from pathlib import Path

import pandas as pd

SOURCE = Path("data/raw/events.csv")
OUTPUT = Path("data/clean/events.csv")

VALID_EVENTS = {"click", "view", "scroll", "login", "purchase"}


def main() -> None:
    df = pd.read_csv(SOURCE, dtype=str)
    df = df.dropna().copy()

    for column in df.columns:
        df[column] = df[column].str.strip()

    df = df[(df != "").all(axis=1)].copy()
    df = df[df["event_type"].isin(VALID_EVENTS)].copy()

    durations = pd.to_numeric(
        df["duration_seconds"], errors="coerce"
    )
    df = df[
        durations.notna()
        & (durations > 0)
        & (durations % 1 == 0)
    ].copy()

    df["duration_seconds"] = durations.loc[df.index].astype(int)

    timestamps = pd.to_datetime(
        df["timestamp"], format="mixed", errors="coerce"
    )
    df = df[timestamps.notna()].copy()
    df["timestamp"] = timestamps.loc[df.index].dt.strftime(
        "%Y-%m-%dT%H:%M:%S"
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)
    print(f"Clean: {len(df)} rows")


if __name__ == "__main__":
    main()
