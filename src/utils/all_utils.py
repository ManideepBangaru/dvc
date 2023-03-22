import yaml
import os

def read_yaml(path_to_yaml : str) -> dict:
    with open(path_to_yaml, 'r') as yaml_file:
        try:
            content = yaml.safe_load(yaml_file)
            return content
        except yaml.YAMLError as exc:
            print(exc)