import kagglehub
import shutil
import os

# Download latest version
path = kagglehub.dataset_download("saurabhshahane/patient-treatment-classification")

print("Path to dataset files:", path)

# Create the destination directory if it doesn't exist
destination_dir = "./data"
os.makedirs(destination_dir, exist_ok=True)

# Move files from path to destination directory
for file_name in os.listdir(path):
    shutil.move(os.path.join(path, file_name), destination_dir)


# Download latest version
path = kagglehub.dataset_download("krsna540/synthea-dataset-jsons-ehr")

print("Path to dataset files:", path)

# Create the destination directory if it doesn't exist
destination_dir = "./data"
os.makedirs(destination_dir, exist_ok=True)

# Move files from path to destination directory
for file_name in os.listdir(path):
    shutil.move(os.path.join(path, file_name), destination_dir)
