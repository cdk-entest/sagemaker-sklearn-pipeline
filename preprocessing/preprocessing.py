import argparse
import os

def read_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_size", type=float, default=0.6)
    parser.add_argument("--val_size", type=float, default=0.2)
    parser.add_argument("--test_size", type=float, default=0.2)
    parser.add_argument("--random_state", type=int, default=42)
    parser.add_argument("--target_col", type=str, default="PRICE")
    params, _ = parser.parse_known_args()
    return params

print(f"=========================================================")
print(f"start preprocessing task")
args = read_parameters()
print(f"parameters: {args}")

input_data_path = "/opt/ml/processing/input/house_pricsing.csv"
train_data_path = "/opt/ml/processing/output/train"
val_data_path =   "/opt/ml/processing/output/validation"
test_data_path =  "/opt/ml/processing/output/test"

try:
    os.makedirs(train_data_path)
    os.makedirs(val_data_path)
    os.makedirs(test_data_path)
except:
    pass
