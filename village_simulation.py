
import json
import numpy as np
import pandas as pd
from pathlib import Path

# File paths
BASE_DIR = Path(__file__).resolve().parent
FILEPATH = BASE_DIR / "village.json"
FILEPATH2 = BASE_DIR / "simulation.json"


def load(filepath):
    if not filepath.exists():
        return []

    try:
        with filepath.open("r", encoding="utf-8") as file:
            if filepath.stat().st_size == 0:
                return []
            return json.load(file)

    except json.JSONDecodeError:
        print(f"Error decoding JSON file: {filepath}")
        return []


def save(data, filepath):
    with filepath.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_villages():
    return load(FILEPATH)


def save_villages(villages):
    save(villages, FILEPATH)


def load_simulation():
    return load(FILEPATH2)


def save_simulation(simulation):
    save(simulation, FILEPATH2)


def simulate_day():
    village = load_villages()
    simulation = load_simulation()

    if not village:
        print("No villages found!")
        return

    for i in village:
        i["Day"] += 1

        i["Food"] = max(0, i["Food"] + np.random.randint(-100, 101))
        i["Wood"] = max(0, i["Wood"] + np.random.randint(-100, 101))
        i["Gold"] = max(0, i["Gold"] + np.random.randint(-100, 101))
        i["Population"] = max(
            0, i["Population"] + np.random.randint(-100, 101)
        )
        i["Stone"] = max(0, i["Stone"] + np.random.randint(-100, 101))

        simulation.append({
            "Village": i["Village"],
            "Population": i["Population"],
            "Food": i["Food"],
            "Wood": i["Wood"],
            "Stone": i["Stone"],
            "Gold": i["Gold"],
            "Day": i["Day"]
        })

    save_villages(village)
    save_simulation(simulation)


def analyze_simulation():
    """Analyze simulation results."""

    simulation = load_simulation()

    if not simulation:
        print("No simulation data available!")
        return

    df = pd.DataFrame(simulation)

    final_day_number = df["Day"].max()

    final_df = df[df["Day"] == final_day_number].copy()

    print(f"\nVillage statistics after {final_day_number} days:\n")
    print(final_df)

    print("\nRichest village:")
    print(
        final_df[["Village", "Gold"]]
        .sort_values("Gold", ascending=False)
    )

    print("\nLargest village in terms of population:")
    print(
        final_df[["Village", "Population"]]
        .sort_values("Population", ascending=False)
    )

    print("\nFood statistics:")

    food = final_df["Food"]

    print("Mean:", food.mean())
    print("Median:", food.median())
    print("Standard deviation:", food.std())
    print("Maximum:", food.max())
    print("Minimum:", food.min())

    print("\nNorthhold food growth:")

    northhold = df[df["Village"] == "Northhold"].sort_values("Day")

    if len(northhold) >= 2:
        growth = northhold["Food"].diff().dropna()

        first_five_days = growth.head(5)

        if not first_five_days.empty:
            print(
                "Average food change during the first five recorded days:",
                first_five_days.mean()
            )
    else:
        print("Not enough Northhold data to calculate growth.")

    print("\nStarving villages:")

    starving = final_df[
        final_df["Food"] < final_df["Population"]
    ]

    if starving.empty:
        print("No villages are currently starving.")
    else:
        for village_name in starving["Village"]:
            print(village_name)

def main():
    """Main application entry point."""

    villages = load_villages()

    if not villages:
        print("No village data found. Please populate village.json first.")
        return

    for day in range(100):
        simulate_day()

    analyze_simulation()


if __name__ == "__main__":
    main()
