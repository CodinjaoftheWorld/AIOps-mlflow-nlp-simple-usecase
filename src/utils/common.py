import yaml
import os
import csv
import json
import logging
import time
import pandas as pd

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"yaml file: {path_to_yaml} loaded successfully.")
    return content


def create_directories(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        logging.info(f"directory created at {dir_path}")

def get_df(path_to_data: str, sep: str="\t") -> pd.DataFrame:
    df = pd.read_csv(
        path_to_data,
        encoding="utf8",
        header=None,
        delimiter=sep,
        names=["Id", "label", "text"]
    )
    logging.info(f"The input data frame {path_to_data} size is {df.shape}\n")
    return df

