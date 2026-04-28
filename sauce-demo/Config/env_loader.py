'''
env_loader.py  file is created to access the env.qa/.dev files
the env.qa/.dev is created so that we don't need to pass the values like first_name/last_name all the time in .robot file
we can just edit the env.qa/.dev files and run the .py loader file to run the test scripts
Each prod env will have its own unique url, password, api_key, etc for security practices.
'''
import os
from dotenv import load_dotenv

def load_env(env_name):
    env_file = f'config/.env.{env_name}'
    load_dotenv(env_file)

def get_env(key):
    return os.getenv(key)