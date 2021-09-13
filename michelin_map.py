#!/usr/bin/env python
"""
A script that generates an import file for a Google Maps layer containing
details of all restaurants in the Michelin Guide UK.
"""
from pathlib import Path, PosixPath

import pandas as pd

URL = 'https://api.nicolaferracin.com/michelin/restaurants'
OUTPUT_FILE = (PosixPath()
               .home()
               .joinpath('tmp')
               .joinpath('google_maps_import.csv'))


def get_restaurants(url: str) -> pd.DataFrame:
    df = pd.read_json(url)
    return df


def clean_and_filter(df: pd.DataFrame) -> pd.DataFrame:
    columns_of_interest = ['name', 'rating', 'type', 'location', 'lat', 'lng', 'link']
    clean_df = df[
        df['year'] == 'MICHELIN Guide United Kingdom'
    ][columns_of_interest]
    return clean_df


def create_import_file(restaurants: pd.DataFrame,
                       path: Path) -> None:
    restaurants.to_csv(path_or_buf=path)


def main():
    all_restaurants = get_restaurants(url=URL)
    restaurants = clean_and_filter(df=all_restaurants)
    create_import_file(restaurants=restaurants, path=OUTPUT_FILE)


if __name__ == '__main__':
    main()
