from src.utils.all_utils import read_yaml, create_directory
import argparse
import os
import pandas as pd

def get_data(config_path):
    config = read_yaml(config_path)
    # Read dataset 
    remote_data_path = config['data_source']
    df = pd.read_csv(remote_data_path, sep=";")

    # create paths to directory
    artifacts_dir = config["artifacts"]["artifacts_dir"]
    raw_local_dir = config["artifacts"]["raw_local_dir"]
    raw_local_file = config["artifacts"]["raw_local_file"]
    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)
    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)
    create_directory([raw_local_dir_path])
    
    # save dataset
    df.to_csv(raw_local_file_path, sep=",", index=False)

if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument('--config', "-c", type=str, default='config/config.yaml')

    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)