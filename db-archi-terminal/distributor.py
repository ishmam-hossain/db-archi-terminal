import pymongo
import sqlite3
from typing import NewType, Union
from mongo_handler import mongo_all_collection_fields, mongo_all_collection_names, mongo_one_collection_fields
from sqlite3_handler import sqlite3_tables


mongodb_instance = NewType('mongodb instance', pymongo.MongoClient)
sqlite3_instance = NewType("sqlite3 instance", sqlite3.Cursor)


def get_target_method(_instance):
    cls_to_method = {
        pymongo.database.Database: mongo_all_collection_names,
        pymongo.collection.Collection: mongo_one_collection_fields,
        sqlite3.Cursor: sqlite3_tables
    }

    return cls_to_method.get(_instance)


def fetch_data(db_instance: Union[mongodb_instance,
                                  sqlite3_instance]) -> Union[list, None]:

    related_method = get_target_method(db_instance.__class__)
    if related_method:
        data = related_method(db_instance)
        return data

    return None



