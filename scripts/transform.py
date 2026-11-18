from pathlib import Path

import pandas as pd

SOURCE = Path("data/clean/events.csv")
OUTPUT = Path("data/transformed/events.csv")


def main() -> None:
    df = pd.read_csv(SOURCE)
    df["date"] = df["timestamp"].str[:10]

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)
    print(f"Transform: {len(df)} rows")


if __name__ == "__main__":
    main()
