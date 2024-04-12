import os
from src.utils.all_utils import read_yaml, create_directory
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split

def split_and_save(config_path):
    config = read_yaml(config_path)

    # save dataset in local directory 
    artifacts_dir = config['artifacts']['artifacts_dir']
    raw_local_dir = config['artifacts']['raw_local_dir']
    raw_local_file = config['artifacts']['raw_local_file']

    raw_local_file_path = os.path.join(artifacts_dir,raw_local_dir,raw_local_file)
    
    df = pd.read_csv(raw_local_file_path)

    train, test = train_test_split(df,test_size = ,random_state= )

if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")

    parsed_args = args.parse_args()

    split_and_save(config_path = parsed_args.config, params_path = parsed_args.params)