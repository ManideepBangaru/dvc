import yaml
import os

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