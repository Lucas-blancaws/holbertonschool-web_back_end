#!/usr/bin/env python3
"""
Module that returns schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic
    Returns:
        List of schools that have the specified topic
    """
    schools = list(mongo_collection.find({"topics": topic}))
    return schools
