from dotenv import load_dotenv
import os

# Manually load the .env file
env_path = '/Users/stepanderiavko/Desktop/FinalprojectPython/.env'
load_dotenv(dotenv_path=env_path)

# Check if the environment variable is loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("The OPENAI_API_KEY environment variable is not set.")

print("OPENAI_API_KEY successfully loaded:", api_key)