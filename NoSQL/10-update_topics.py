#!/usr/bin/env python3
"""
function that changes all topics of a school document based on the name
"""
def update_topics(mongo_collection, name, topics):
    """
    module to update topics name in a collection
    Args: mongo_collection, name, topics
    Returns: updated_topics
    """
    mongo_collection.update_many({ "name": name }, { "$set": { "topics": topics } })
    