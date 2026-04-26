#!/usr/bin/env python3
"""
function that lists all documents in a collection
"""
def list_all(mongo_collection):
    """
    List all the documents in a collection

    Args: mongo_collection

    Returns:
    A list of documents
    (dict) or an empty list
    """
    return list(mongo_collection.find())
