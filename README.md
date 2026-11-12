# Village-Simulation-Python

A small Python simulation that tracks several villages over 100 days. Each day, every village's resources and population change randomly. When the run finishes, the script analyzes the results with pandas.

## Features

- Loads village data from a JSON file
- Simulates 100 days of random changes to Population, Food, Wood, Stone and Gold (values never drop below 0)
- Logs every village's daily state to `simulation.json`
- Prints an analysis of the final day:
  - Full village statistics
  - Richest village (by Gold)
  - Largest village (by Population)
  - Food statistics (mean, median, standard deviation, min, max)
  - Average daily food change for Northhold over its first five recorded days
  - Villages that are starving (Food < Population)

## Requirements

- Python 3.8+
- numpy
- pandas

```bash
pip install numpy pandas
```

## Input format

`village.json` must contain a list of villages, each with these fields:

```json
[
    {
        "Village": "Northhold",
        "Population": 500,
        "Food": 1000,
        "Wood": 800,
        "Stone": 600,
        "Gold": 300,
        "Day": 0
    }
]
```

## Usage

```bash
python village_simulation.py
```

The script runs 100 simulated days and then prints the analysis.

## Output

- `village.json` is updated with each village's current state
- `simulation.json` receives one record per village per day (generated file, ignored by git)

## Project structure

```
.
├── village_simulation.py
├── village.json
├── .gitignore
└── README.md
```

## Notes

- Running the script again continues from the state saved in `village.json`, and appends to `simulation.json`. To start fresh, restore the original `village.json` and delete `simulation.json`.
- Changes are random (-100 to +100 per resource per day), so results differ on every run.

## License

Choose a license, for example MIT, and add a `LICENSE` file.
