from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Establishing Connection
conn = MongoClient(os.getenv('MONGO_URI'))

db = conn['cosmocloud'] # Database selected
