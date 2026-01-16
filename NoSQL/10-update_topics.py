#!/usr/bin/env python3
"""
Docstring for NoSQL.10-update_topics
"""


def update_topics(mongo_collection, name, topics):
    """
    Docstring for update_topics
    
    :param mongo_collection: The pymongo collection object
    :param name: The name of the school to update
    :param topics: The list of topics approached in the school
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
