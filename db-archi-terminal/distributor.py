import pymongo
import sqlite3
from typing import NewType, Union
from mongo_handler import mongodb_collection_details, mongodb_collection_names,\
    mongodb_one_collection_fields, mongodb_client_details
from sqlite3_handler import sqlite3_tables


mongodb_instance = NewType('mongodb instance', pymongo.MongoClient)
sqlite3_instance = NewType("sqlite3 instance", sqlite3.Cursor)


def get_target_method(_instance):
    cls_to_method = {
        pymongo.database.Database: mongodb_collection_details,
        pymongo.collection.Collection: mongodb_one_collection_fields,
        pymongo.MongoClient: mongodb_client_details,
        sqlite3.Cursor: sqlite3_tables
    }

    return cls_to_method.get(_instance)


def fetch_data(db_instance: Union[mongodb_instance,
                                  sqlite3_instance],
               _fields=False) -> Union[list, dict, None]:

    related_method = get_target_method(db_instance.__class__)
    if related_method:
        data = related_method(db_instance, _fields=_fields)
        return data
    return



