from pymongo import MongoClient

#  MongoDB URI
MONGO_URI = 'mongodb+srv://vsarthak62:zC6FwnlEuJQOeX6R@cluster0.p3azv.mongodb.net/cosmocloud?retryWrites=true&w=majority'

# Establishing Connection
conn = MongoClient(MONGO_URI)

db = conn['cosmocloud'] # Database selected
