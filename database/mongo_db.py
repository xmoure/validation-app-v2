from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from pymongo.errors import PyMongoError


class MongoDB:
    def __init__(self):
        self.client = None
        self.db = None

    def connect(self):
        """Connect to MongoDB and return the database instance."""
        mongo_uri = os.getenv("MONGO_DB_CONNECTION_STRING")
        db_name = os.getenv("MONGO_DB")

        if not mongo_uri or not db_name:
            raise ValueError("MongoDB connection settings are not defined in environment variables.")

        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        return self.db

    def find_one_by_id(self, collection_name, doc_id):
        """Find a single document by its _id in the specified collection."""
        collection = self.db[collection_name]
        try:
            doc_id = ObjectId(doc_id)
        except:
            pass

        return collection.find_one({'_id': doc_id})

    def find_matches_with_not_validated_moves(self):
        matches_collection = self.db['matches']
        return matches_collection.aggregate([
            {
                "$match": {
                    "moves": {
                        "$elemMatch": {
                            "verified": False
                        }
                    }
                }
            },
            {
                "$project": {
                    "_id": 1,
                    "match_id": 1,
                    "source": 1,
                    "total_moves": 1,
                    "material": 1
                }
            }
        ])



    def find_match_by_id_and_moves_not_validated(self, doc_id,):
        matches_collection = self.db['matches']
        try:
            doc_id = ObjectId(doc_id)
        except:
            pass
        pipeline = [
            { "$match": { "_id": doc_id } },
            { "$project": {
                "moves": {
                    "$filter": {
                        "input": "$moves",
                        "as": "move",
                        "cond": { "$eq": ["$$move.verified", False] }
                    }
                }
            }}
        ]
        result = list(matches_collection.aggregate(pipeline))
        return result[0] if result else None


    def is_connected(self):
        """Check if the database connection is already established."""
        return self.db is not None


    def update_match_move_verified_and_fen(self, match_id, move_id, new_fen, starting_fen):
        """Update the verified status and FEN string of a specific move in a match."""
        matches_collection = self.db['matches']
        try:
            match_oid = ObjectId(match_id)
            move_oid = ObjectId(move_id)
        except:
            raise ValueError("Invalid match_id or move_id.")


        fen_changed = new_fen != starting_fen

        # Update the move's verified status and fen where the move id matches
        update_result = matches_collection.update_one(
            {
                '_id': match_oid,
                'moves._id': move_oid
            },
            {
                '$set': {
                    'moves.$.verified': True,
                    'moves.$.fen': new_fen,
                    'moves.$.fen_corrected': fen_changed,
                    'moves.$.initial_fen': starting_fen
                }
            }
        )
        return update_result.matched_count, update_result.modified_count


    def update_board_material_by_match_id(self, match_id, material):
        matches_collection = self.db['matches']
        try:
            match_oid = ObjectId(match_id)
        except:
            raise ValueError("Invalid match_id.")

        result = matches_collection.update_one(
            {"_id": match_oid},
            {"$set": {"material": material}}
        )
        return result.matched_count, result.modified_count



mongo_db_instance = MongoDB()

def get_db():
    """Get the MongoDB database instance."""
    if mongo_db_instance.db is None:
        return mongo_db_instance.connect()
    return mongo_db_instance.db
