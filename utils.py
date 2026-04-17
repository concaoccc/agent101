import json
import yaml
import os
import time
from functools import wraps

def load_json(file_path: str):
    """Load and return JSON data from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_yaml(file_path: str):
    """Load and return YAML data from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def get_env_variable(var_name: str, default=None):
    """Retrieve an environment variable, or return default if not found."""
    return os.getenv(var_name, default)

def timing_decorator(func):
    """A decorator that measures and prints the execution time of the decorated function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper