import json
from enum import Enum
from functools import lru_cache

class ModelConfigKeysEnum(Enum):
    CURRENT_MODEL ='current_model'
    AVAILABLE_MODELS = 'available_models'
    
@lru_cache(maxsize=None)
def get_model_config(key):
    key = key.value
    with open('Tools/model_config.json','r') as file:
        config  =json.load(file)
        if key in config:
            return config.get(key)
        else:
            raise ValueError(f'{key=} does not exist in config')
        