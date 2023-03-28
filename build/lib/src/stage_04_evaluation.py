import os
import pandas as pd
import numpy as np
import argparse
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from src.utils.all_utils import read_yaml, create_directory, save_reports
import joblib

def evaluate_metrics(actual_values, predicted_values):
    rmse = np.sqrt(mean_squared_error(actual_values,predicted_values))
    mae = mean_absolute_error(actual_values, predicted_values)
    r2 = r2_score(actual_values, predicted_values)
    return rmse, mae, r2

def evaluate(config_path):
    config = read_yaml(config_path)

    # create paths to directories
    artifacts_dir = config["artifacts"]["artifacts_dir"]
    split_data_path = os.path.join(artifacts_dir, config["artifacts"]["split_data_dir"])
    test_data_path = os.path.join(split_data_path, config["artifacts"]["test_data_file"])
    
    # Reading the dataset
    test = pd.read_csv(test_data_path)
    test_y = test["quality"]
    test_x = test.drop("quality", axis=1)

    # declare model path
    model_dir = os.path.join(artifacts_dir, config["artifacts"]["model_dir"])
    model_file_name = config["artifacts"]["model_file_name"]
    model_path = os.path.join(model_dir, model_file_name)

    # load model
    lr = joblib.load(model_path)

    # predict values
    predicted_values = lr.predict(test_x)

    # get metrics
    rmse, mae, r2 = evaluate_metrics(test_y, predicted_values)

    # export reports
    scores_dir_path = os.path.join(artifacts_dir,config["artifacts"]["scores_dir"])
    scores_file_name = config["artifacts"]["scores"]
    create_directory([scores_dir_path])

    scores = {
        "rmse" : rmse,
        "mae" : mae,
        "r2_score" : r2
    }
    save_reports(scores, os.path.join(scores_dir_path, scores_file_name))


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', "-c", type=str, default='config/config.yaml')

    parsed_args = args.parse_args()

    evaluate(config_path=parsed_args.config)