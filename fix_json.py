import json
import glob
import os

json_files = glob.glob('cov_cnn_web/predictor/model_weights/**/*.json', recursive=True)

for file in json_files:
    print(f"Processing {file}")
    with open(file, 'r') as f:
        content = f.read()
    
    # Replace the class_name Functional with Model
    new_content = content.replace('"class_name": "Functional"', '"class_name": "Model"')
    
    with open(file, 'w') as f:
        f.write(new_content)
    print("Done")
