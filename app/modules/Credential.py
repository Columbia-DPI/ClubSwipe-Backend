from dotenv import load_dotenv
load_dotenv()
import os

def get_key(key):
	os.getenv(key)