# Visualizing NYC Yellow Taxi Pickup Density

The [NYC Taxi & Limousine Commission (TLC) trip record data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) provides detailed information on every yellow taxi trip in New York City. Each record includes pickup and drop-off times and locations, trip distances, fares, payment types, and passenger counts. The data is collected from taxi technology providers, released monthly, and is widely used to study urban mobility, transportation patterns, and economic activity.

## Scripts
### Data Downloader (`download_data.py`)

A Python script to download monthly TLC Yellow Taxi Trip Record datasets in Parquet format from 2009 to 2025.

- Iterates through years and months to build dataset filenames (e.g., `yellow_tripdata_2015-06.parquet`).
- Skips downloads if the file already exists locally.
- Saves the data in a data/ directory.
- Sleeps for 10 minutes after each year to avoid server overload.

👉 In short: Downloads and stores NYC Yellow Taxi trip data (2009–2025).

### Data Visualization (`visualize_pickups.py`)

<div>
  <img src=".\img\pickups.png" alt="pickups heatmap" width=100%/>
</div>

A Python script to load the downloaded taxi data and visualize pickup densities across New York City.

- Loads trip data from Parquet files using Polars.
- Filters trips to a geographic bounding box around NYC.
- Creates a 2D histogram of pickup longitude and latitude.
- Applies a logarithmic normalization for clearer density visualization.
- Generates a heatmap using Matplotlib and saves it to `img/pickups.png`.

👉 In short: Produces a heatmap of NYC yellow taxi pickup densities (2009–2025).

## Dependencies

### Using `pip` package manager

It is highly recommended to create a Python virtual environment before installing dependencies. In a terminal, navigate to the root folder and run:

```bash
python -m venv <venv_name>
```

Activate the environment:

- On macOS/Linux:

  ```bash
  source <venv_name>/bin/activate
  ```

- On Windows:

  ```bash
  <venv_name>\Scripts\activate
  ```

Once the virtual environment is active, install the dependencies:

```bash
pip install -r requirements.txt
```

You're ready to go! 🚀

### Using `uv` package manager (Highly Recommended)

[`uv`](https://github.com/astral-sh/uv) is a modern Python package manager that is significantly faster than `pip`.

#### Install `uv`

To install `uv`, follow the instructions from the [official installation guide](https://github.com/astral-sh/uv#installation).

#### Set up the environment and install dependencies

Run the following command in the root folder:

```bash
uv sync
```

This will automatically create a virtual environment (if none exists) and install all dependencies.

You're ready to go! 🚀
