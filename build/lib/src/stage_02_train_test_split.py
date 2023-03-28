import os
import pandas as pd
import argparse
from sklearn.model_selection import train_test_split
from src.utils.all_utils import read_yaml, create_directory, save_to_local


def split_and_save(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    # create paths to directories
    artifacts_dir = config["artifacts"]["artifacts_dir"]
    raw_local_dir = config["artifacts"]["raw_local_dir"]
    raw_local_file = config["artifacts"]["raw_local_file"]
    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)
    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)

    split_data_path = os.path.join(artifacts_dir, config["artifacts"]["split_data_dir"])
    create_directory(dirs=[split_data_path])
    train_data_path = os.path.join(split_data_path, config["artifacts"]["train_data_file"])
    test_data_path = os.path.join(split_data_path, config["artifacts"]["test_data_file"])
    
    # Reading the dataset
    df = pd.read_csv(raw_local_file_path)

    # split the data to train and test
    split_ratio = params["base"]["test_size"]
    random_state_number = params["base"]["random_state"]
    train, test = train_test_split(df, test_size=split_ratio, random_state=random_state_number)

    # exporting data
    for data, data_path in (train, train_data_path),(test, test_data_path):
        save_to_local(data, data_path)


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument('--config', "-c", type=str, default='config/config.yaml')
    args.add_argument('--params', "-p", type=str, default='params.yaml')

    parsed_args = args.parse_args()

    split_and_save(config_path=parsed_args.config, params_path=parsed_args.params)