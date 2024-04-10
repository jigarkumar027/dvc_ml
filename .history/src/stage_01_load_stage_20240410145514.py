from src.utils.all_utils import read_yaml
import argparse
import pandas as pd

def get_data(config_path):
    config = read_yaml(config_path)

    remote_data_path = config['data_Source']
    df = pd.read_csv(remote_data_path,sep=";")
    print(df)

if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")

    parsed_args = args.parse_args()

    print(parsed_args.config)