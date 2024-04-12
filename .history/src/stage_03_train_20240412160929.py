import os
from src.utils.all_utils import read_yaml, create_directory, save_local_df
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet

def train(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    # save dataset in local directory 
    artifacts_dir = config['artifacts']['artifacts_dir']
    split_data_dir = config['artifacts']['split_data_dir']

    train_data_filename = config['artifacts']['train']

    train_data_path = os.path.join(artifacts_dir,split_data_dir,train_data_filename)
    
    train_data = pd.read_csv(train_data_path)

    train_y = train_data['quality']
    train_x = train_data.drop("quality",axis = 1)

    lr = ElasticNet(alpha= 0.5, l1_ratio=0.5, random_state=40)
    lr.fit(train_x,train_y)
    print(done)

if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")

    parsed_args = args.parse_args()

    train(config_path = parsed_args.config, params_path = parsed_args.params)