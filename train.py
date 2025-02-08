import json
from dotenv import load_dotenv
from ultralytics import YOLO
import os
from huggingface_hub import hf_hub_download

config = json.load(open("./config.json"))
load_dotenv()

path_to_models = os.getenv("MODEL_PATH")
if path_to_models == None:
    raise Exception("No path to models found in the environment")

path_to_dataset = os.getenv("DATASET_PATH")
if path_to_dataset == None:
    raise Exception("No path to dataset found in the environment")

if config["base_model"] == None:
    raise Exception("No base model found in config.json")
model_file = f"{config['base_model']}.pt"

hf_hub_download(repo_id="Ultralytics/YOLO11", filename=model_file, local_dir=path_to_models)

model = YOLO(os.path.join(path_to_models, model_file))
results = model.train(
    data = path_to_dataset,
    **config["training"]
)
model.export()
