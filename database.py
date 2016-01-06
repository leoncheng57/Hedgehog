import pymongo

client = pymongo.MongoClient()
db = client.hedgehog

users = db.users
datas = db.datas

tags = datas.tags
info = datas.info

def create_tag(name, info_list=[], parent_tags=[], child_tags=[]):
    result = tags.insert_one({
       'name': name,
       'info': info,
       'parents': parent_tags,
       'children': child_tags,
    })
    if not result.acknowledged:
        return False
    add_info_relationship(result.inserted_id, info_list)
    add_tags_relationship(result.inserted_id, parent_tags, child_tags)
    return True

#WIP
def create_info(title, body, author_id, tag_list):
    {'tags': tag_list}


def add_info_relationship(tag_id, info_list):
    for info_id in info_list:
        info.find_one_and_update({'_id': info_id}, {'$addToSet', {'tags', tag_id}})

def add_tags_relationship(tag_id, parent_tags=[], child_tags=[]):
    for ptag_id in parent_tags:
        tags.find_one_and_update({'_id': ptag_id}, {'$addToSet', {'children', tag_id}})
    for ctag_id in child_tags:
        tags.find_one_and_update({'_id': ctag_id}, {'$addToSet', {'parents', tag_id}})
