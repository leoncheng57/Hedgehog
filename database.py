import pymongo, time

client = pymongo.MongoClient()
db = client.hedgehog

users = db.users
datas = db.datas

tags = datas.tags
info = datas.info

def create_tag(name, info_list=[], parent_tags=[], child_tags=[]):
    result = tags.insert_one({
       'name': name,
       'info': info_list,
       'parents': parent_tags,
       'children': child_tags,
    })
    if not result.acknowledged:
        return False
    link_tag_to_info(result.inserted_id, info_list)
    link_tag_to_tags(result.inserted_id, parent_tags, child_tags)
    return True

def create_info(title, body, author_id, tag_list):
    result = info.insert_one({
        'title': title,
        'body': body,
        'author': author_id,
        'tags': tag_list,
        'last_updated': time.time(),
    })
    if not result.acknowledged:
        return False
    link_info_to_tags(result.inserted_id, tag_list)
    return True

def link_tag_to_info(tag_id, info_list):
    for info_id in info_list:
        info.find_one_and_update({'_id': info_id}, {'$addToSet', {'tags', tag_id}})

def link_tag_to_tags(tag_id, parent_tags=[], child_tags=[]):
    for ptag_id in parent_tags:
        tags.find_one_and_update({'_id': ptag_id}, {'$addToSet', {'children', tag_id}})
    for ctag_id in child_tags:
        tags.find_one_and_update({'_id': ctag_id}, {'$addToSet', {'parents', tag_id}})

def link_info_to_tags(info_id, tag_list):
    for tag_id in tag_list:
        tags.find_one_and_update({'_id': tag_id}, {'$addToSet', {'info', info_id}})
