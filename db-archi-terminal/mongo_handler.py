def mongodb_collection_names(_db, _fields=False):
    collections = _db.collection_names(include_system_collections=False)
    return collections


def mongodb_collection_fields(_db, _fields=False):
    collections = mongodb_collection_names(_db)
    data = {}
    for collection in collections:
        cursor = _db[collection].find({})
        for document in cursor:
            data[collection] = [key for key in document.keys()]
            break

    return data


def mongodb_collection_details(_db, _fields=False):
    if _fields:
        collections = mongodb_collection_names(_db)
        data = {}
        for collection in collections:
            cursor = _db[collection].find({})
            for document in cursor:
                data[collection] = [key for key in document.keys()]
                break

        return data

    return mongodb_collection_names(_db)


def mongodb_one_collection_fields(_collection_instance, _fields=False):
    cursor = _collection_instance.find_one()
    field_names = [key for key in cursor]

    return field_names


def mongodb_client_details(_mongodb_client, _fields=False):
    print(_mongodb_client)
    return _mongodb_client

