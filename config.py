import yaml

with open("assets/config.yaml") as file:
    config = yaml.safe_load(file)
    panic_key = config["panic_key"]
