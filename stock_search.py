import json
from bson import json_util, ObjectId
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://jainambhavsar95:Gr8estSecr8Is%3F@stocks.3zfgscg.mongodb.net/"

mongo_client = MongoClient(MONGO_URI)
db = mongo_client.stocks
collection = db["nse"]


def search(query):
    cursor = collection.aggregate(
        [
            {
                "$search": {
                    "index": "stock_name_symbol",
                    "compound": {
                        "must": [
                            {
                                "autocomplete": {
                                    "query": query,
                                    "path": 'name'
                                },
                                "autocomplete": {
                                    "query": query,
                                    "path": "symbol"
                                }
                            },

                        ]
                    }
                }
            },
            {"$limit": 10},
        ]
    )
    return json.loads(json_util.dumps(list(cursor)))
