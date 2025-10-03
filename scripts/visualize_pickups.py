# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib",
#     "numpy",
#     "polars",
# ]
# ///

"""A python script for visualizing NYC Yellow Taxi Pickup Density."""

import numpy as np
import polars as pl
from pathlib import Path

# Visualization libraries
import matplotlib.pyplot as plt
from matplotlib.colors import FuncNorm


# ===================================================
#
#               Functions Definition
#
# ===================================================
def _forward(x):
    return np.log1p(x)


def _inverse(x):
    return np.expm1(x)


# ===================================================
#
#                    MAIN LOOP
#
# ===================================================
def main() -> None:
    """The main loop."""

    # Defining some paths
    CURRENT: Path = Path('.')
    DATA_PATH: Path = CURRENT / 'data'
    IMG_PATH: Path = CURRENT / 'img'

    # Create the IMG_PATH if it doesn't exist
    IMG_PATH.mkdir(parents=True, exist_ok=True)

    # Define some variables
    long_min: float = -74.05
    long_max: float = -73.75
    lat_min: float = 40.58
    lat_max: float = 40.90

    log1p_norm = FuncNorm((_forward, _inverse), vmin=0, vmax=None)

    # Load the data
    print('Trying to load some data...', end='\t')
    df: pl.LazyFrame = pl.scan_parquet(
        DATA_PATH / '*', extra_columns='ignore', missing_columns='insert'
    )
    print('[DONE]')

    print()
    print('Number of rows contained:', df.select(pl.len()).collect().item())

    df = (
        df.select(['Start_Lon', 'Start_Lat']).filter(
            (pl.col('Start_Lon').is_between(long_min, long_max))
            & (pl.col('Start_Lat').is_between(lat_min, lat_max))
        )
    ).collect(engine='streaming')

    print()
    print(
        'Number of rows contained after filtering:', df.select(pl.len()).item()
    )

    # Create 2D histogram manually
    counts, xedges, yedges = np.histogram2d(
        df['Start_Lon'],
        df['Start_Lat'],
        bins=400,
        range=[[long_min, long_max], [lat_min, lat_max]],
    )

    # Plot with pcolormesh
    plt.figure(figsize=(10, 8))
    plt.pcolormesh(xedges, yedges, counts.T, cmap='inferno', norm=log1p_norm)
    plt.xlim(long_min, long_max)
    plt.ylim(lat_min, lat_max)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('NYC Yellow Taxi Pickups Density (2009–2025)')
    plt.savefig(
        str(IMG_PATH / 'pickups.png'),
        bbox_inches='tight',
    )
    plt.clf()
    plt.cla()

    return None


if __name__ == '__main__':
    main()
