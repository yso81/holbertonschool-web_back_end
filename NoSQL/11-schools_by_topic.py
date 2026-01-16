#!/usr/bin/env python3
"""
Docstring for NoSQL.11-schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic
    
    :param mongo_collection: The pymongo collection object
    :param topic: The list of topics searched

    returns:
    A list of school documents
    """
    return list(mongo_collection.find({"topics": topic}))
