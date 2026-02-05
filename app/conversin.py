def convert_objectid_to_str(results):
    for doc in results:
        doc["_id"] = doc["_id"].__str__()
    return results