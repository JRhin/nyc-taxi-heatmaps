# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "polars",
#     "tqdm",
# ]
# ///

"""A python script to download the TLC Trip Record Data, contained at:

https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
"""

import polars as pl
from time import sleep
from pathlib import Path
from tqdm.auto import tqdm


# ===================================================
#
#                    MAIN LOOP
#
# ===================================================
def main() -> None:
    """the main loop."""

    # Define some paths
    CURRENT = Path('.')
    DATA_PATH = CURRENT / 'data'

    # Define some variables
    url: str = 'https://d37ci6vzurychx.cloudfront.net/trip-data/'
    years = range(2009, 2026)

    for y in years:
        for m in tqdm(list(range(1, 13)), desc=str(y)):
            fname = f'yellow_tripdata_{y}-{m:02}.parquet'

            # If the .parquet file already exists then skip
            if (DATA_PATH / fname).exists():
                continue

            pl.read_parquet(url + fname).write_parquet(DATA_PATH / fname)

        # Get some sleep to make the API rest a bit
        sleep(60 * 10)  # 10 min sleep

    return None


if __name__ == '__main__':
    main()
