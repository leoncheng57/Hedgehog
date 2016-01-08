from werkzeug.security import generate_password_hash, check_password_hash
import pymongo, time

client = pymongo.MongoClient()
db = client.hedgehog

users = db.users
datas = db.datas

tags = datas.tags
info = datas.info

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
    return tags.find_many()

# Info related functions
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
    link_info_to_user(result.inserted_id, author_id)
    return True

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

def verify_user(username, password):
    return check_password_hash(
        users.find_one({'username': username})['password'], password
    )

# Linkage functions
def link_tag_to_info(tag_id, info_list):
    for info_id in info_list:
        info.find_one_and_update({'_id': info_id}, {'$addToSet': {'tags': tag_id}})

def link_tag_to_tags(tag_id, parent_tags=[], child_tags=[]):
    for ptag_id in parent_tags:
        tags.find_one_and_update({'_id': ptag_id}, {'$addToSet': {'children': tag_id}})
    for ctag_id in child_tags:
        tags.find_one_and_update({'_id': ctag_id}, {'$addToSet': {'parents': tag_id}})

def link_info_to_tags(info_id, tag_list):
    for tag_id in tag_list:
        tags.find_one_and_update({'_id': tag_id}, {'$addToSet': {'info': info_id}})

def link_info_to_user(info_id, user_id):
    users.find_one_and_update({'_id': user_id}, {'$addToSet': {'info': info_id}})