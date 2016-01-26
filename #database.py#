import time

import pymongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

client = pymongo.MongoClient()
db = client.hedgehog
users = db.users
tags = db.datas.tags
info = db.datas.info

# Tag related functions
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

def get_all_tags():
    return list(tags.find(projection=['name']))

def get_top_level_tags():
    return list(tags.find({'parents': []}, ['name']))

def get_parent_tags(child_id):
    parents = []
    for parent_id in tags.find_one(child_id)['parents']:
        parents.append(tags.find_one(parent_id, ['name']))
    return parents

def get_child_tags(parent_id):
    children = []
    for child_id in tags.find_one(parent_id)['children']:
        children.append(tags.find_one(child_id, ['name']))
    return children

# Info related functions
def create_info(title, body, author_id, tag_list):
    author_id = ObjectId(author_id)
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
    link_info_to_user(result.inserted_id, author_id)
    return True

def get_all_info():
    return list(info.find(projection=['title', 'author', 'body']))

# User related functions
def create_user(username, password):
    if users.find_one({'username': username}):
        return False
    password = generate_password_hash(password)
    result = users.insert_one({
        'username': username,
        'password': password,
        'info': [],
    })
    if not result.acknowledged:
        return False
    return True

def check_user(username, password):
    user = users.find_one({'username': username})
    if user:
        if check_password_hash(user['password'], password):
            return {'id': str(user.get('_id')),
                'name': str(user.get('username'))}
        return False
    return None

# Linkage functions
def link_tag_to_info(tag_id, info_list):
    for info_id in info_list:
        info.find_one_and_update({'_id', info_id}, {'$addToSet': {'tags': tag_id}})

def link_tag_to_tags(tag_id, parent_tags=[], child_tags=[]):
    for ptag_id in parent_tags:
        tags.find_one_and_update({'_id', ptag_id}, {'$addToSet': {'children': tag_id}})
    for ctag_id in child_tags:
        tags.find_one_and_update({'_id', ctag_id}, {'$addToSet': {'parents': tag_id}})

def link_info_to_tags(info_id, tag_list):
    for tag_id in tag_list:
        tags.find_one_and_update({'_id', tag_id}, {'$addToSet': {'info': info_id}})

def link_info_to_user(info_id, user_id):
    users.find_one_and_update({'_id': user_id}, {'$addToSet': {'info': info_id}})
