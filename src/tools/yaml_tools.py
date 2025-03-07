def parse_yaml(file_path):
    import yaml
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def generate_yaml(data, file_path):
    import yaml
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

def validate_yaml(file_path):
    import yaml
    try:
        with open(file_path, 'r') as file:
            yaml.safe_load(file)
        return True
    except yaml.YAMLError as e:
        print(f"YAML validation error: {e}")
        return False

def merge_yaml(yaml1, yaml2):
    import deepmerge
    return deepmerge.Merger(
        [(list, "override"), (dict, "merge")],
        ["override", "override"],
        [],
    ).merge(yaml1, yaml2)