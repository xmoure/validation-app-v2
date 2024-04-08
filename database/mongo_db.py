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
        return matches_collection.find({"verified": False}, {"moves": 0})

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


    def update_match_move_verified_and_fen(self, match_id, move_id, new_fen):
        """Update the verified status and FEN string of a specific move in a match."""
        matches_collection = self.db['matches']
        try:
            match_oid = ObjectId(match_id)
            move_oid = ObjectId(move_id)
        except:
            raise ValueError("Invalid match_id or move_id.")

        # Update the move's verified status and fen where the move id matches
        update_result = matches_collection.update_one(
            {
                '_id': match_oid,
                'moves._id': move_oid
            },
            {
                '$set': {
                    'moves.$.verified': True,
                    'moves.$.fen': new_fen
                }
            }
        )
        return update_result.matched_count, update_result.modified_count


    def all_moves_verified(self, match_id):
        match = self.db['matches'].find_one({'_id': ObjectId(match_id)}, {'moves': 1, 'verified': 1})

        if match:
            if match.get('verified', False):
                return True
            # Check if all moves in the 'moves' array are verified
            return all(move.get('verified', False) for move in match['moves'])
        else:
            raise ValueError("Match not found with the provided match_id.")

    def update_match_verified_status(self, match_id):
        try:
            # If the match is already verified, there's nothing to update.
            if self.db['matches'].find_one({'_id': ObjectId(match_id), 'verified': True}, {'_id': 1}):
                print("The match is already verified.")
                return True

            if self.all_moves_verified(match_id):
                # All moves are verified, so update the match verified status
                result = self.db['matches'].update_one(
                    {'_id': ObjectId(match_id)},
                    {'$set': {'verified': True}}
                )
                return result.modified_count > 0
            else:
                print("Verified at match level was not updated since there are still pending moves to validate.")
                return False
        except PyMongoError as e:
            print(f"An error occurred while updating the match: {e}")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False


mongo_db_instance = MongoDB()

def get_db():
    """Get the MongoDB database instance."""
    if mongo_db_instance.db is None:
        return mongo_db_instance.connect()
    return mongo_db_instance.db
