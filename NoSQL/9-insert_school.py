#!/usr/bin/env python3
"""
function that inserts a new document in a collection
"""
def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in collection based on kwargs
    Args: mongo_collection, **kwargs
    Returns: _id of newly inserted document
    """
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
