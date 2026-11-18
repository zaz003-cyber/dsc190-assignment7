import marimo

app = marimo.App()


@app.cell
def _():
    from pathlib import Path

    import matplotlib.pyplot as plt
    import pandas as pd

    return Path, pd, plt


@app.cell
def _(Path, pd):
    csv_path = (
        Path(__file__).resolve().parent.parent
        / "data/features/events.csv"
    )
    df = pd.read_csv(csv_path)
    return (df,)


@app.cell
def _(df, plt):
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.hist(df["duration_minutes"], bins=25, edgecolor="black")
    ax.set_title("Distribution of Event Durations")
    ax.set_xlabel("Duration (minutes)")
    ax.set_ylabel("Number of Events")

    fig.tight_layout()
    fig
    return (fig,)


if __name__ == "__main__":
    app.run()
