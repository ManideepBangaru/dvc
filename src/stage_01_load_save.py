from src.utils.all_utils import read_yaml
import argparse
import pandas as pd

if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument('--config', "-c", type=str, default='config.yaml')

    parsed_args = args.parse_args()

    print(parsed_args)