import yaml
import os
import json

def read_yaml(path_to_yaml : str) -> dict:
    with open(path_to_yaml, 'r', encoding="utf-8") as yaml_file:
        try:
            content = yaml.safe_load(yaml_file)
            return content
        except yaml.YAMLError as exc:
            print(exc)

def create_directory(dirs : list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"Path created at {dir_path}")

def save_to_local(data, data_path, index_option = False):
    data.to_csv(data_path, index = index_option)

def save_reports(report : dict, report_path : str):
    with open(report_path,"w") as f:
        json.dump(report, f, indent = 4)
    print(f"Reports are saved at {report_path}")
