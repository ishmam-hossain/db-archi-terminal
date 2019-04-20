def mongo_all_collection_names(db):
    collections = db.collection_names(include_system_collections=False)
    return collections


def mongo_all_collection_fields(db):
    collections = mongo_all_collection_names(db)
    data = {}
    for collection in collections:
        cursor = db[collection].find({})
        for document in cursor:
            data[collection] = [key for key in document.keys()]
            break

    return data


def mongo_one_collection_fields(collection_instance):
    cursor = collection_instance.find_one()
    field_names = [key for key in cursor]

    return field_names

# def drop_collection():
#     collections = get_all_collection_names()
#
#     for collection in collections:
#         try:
#             db.db[collection].drop()
#             print(f"Deleted {collection}!")
#         except:
#             print(f"Error occurred deleting: {collection}!!!")


