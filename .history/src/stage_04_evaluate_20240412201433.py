import os
from src.utils.all_utils import read_yaml, create_directory
import argparse
import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

def evaluate(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts_dir = config['artifacts']['artifacts_dir']
    split_data_dir = config['artifacts']['split_data_dir']

    test_data_filename = config['artifacts']['test']

    test_data_path = os.path.join(artifacts_dir,split_data_dir,test_data_filename)
    
    test_data = pd.read_csv(test_data_path)

    test_y = test_data['quality']
    test_x = test_data.drop("quality",axis = 1)

    model_dir = config['artifacts']['model_dir']
    model_filename = config['artifacts']['model_file']
    model_path = os.path.join(artifacts_dir,model_dir,model_filename)

    lr = joblib.load(model_path)

if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")

    parsed_args = args.parse_args()

    evaluate(config_path = parsed_args.config, params_path = parsed_args.params)