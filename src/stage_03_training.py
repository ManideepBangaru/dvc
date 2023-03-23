import os
import pandas as pd
import argparse
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from src.utils.all_utils import read_yaml, create_directory, save_to_local
import joblib


def train(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    # create paths to directories
    artifacts_dir = config["artifacts"]["artifacts_dir"]
    split_data_path = os.path.join(artifacts_dir, config["artifacts"]["split_data_dir"])
    train_data_path = os.path.join(split_data_path, config["artifacts"]["train_data_file"])
    
    # Reading the dataset
    train = pd.read_csv(train_data_path)
    train_y = train["quality"]
    train_x = train.drop("quality", axis=1)

    # Building model
    alpha = params["model_params"]["ElasticNet"]["alpha"]
    l1_ratio = params["model_params"]["ElasticNet"]["l1_ratio"]
    random_state = params["base"]["random_state"]
    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)
    lr.fit(train_x, train_y)

    # saving the model
    model_dir = os.path.join(artifacts_dir, config["artifacts"]["model_dir"])
    model_file_name = config["artifacts"]["model_file_name"]
    create_directory([model_dir])
    model_path = os.path.join(model_dir, model_file_name)
    joblib.dump(lr, model_path)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', "-c", type=str, default='config/config.yaml')
    args.add_argument('--params', "-p", type=str, default='params.yaml')

    parsed_args = args.parse_args()

    train(config_path=parsed_args.config, params_path=parsed_args.params)