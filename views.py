from typing import List
import flask
from flask.templating import render_template
import pymongo
import bson

import schema


def init_db() -> pymongo.MongoClient:
    CONNECTION_STRING = "mongodb://admin:admin@localhost:27017/json-admin"

    client = pymongo.MongoClient(CONNECTION_STRING)
    return client


def get_db() -> pymongo.MongoClient:
    if 'db' not in flask.g:
        flask.g.db = init_db()

    return flask.g.db


def create_view(s: schema.Schema):
    def view() -> str:
        return render_template("create_template.j2", schema=s)

    return view

def get_render_fields(items: List[dict]):
    fields = set()
    for item in items:
        for key in item:
            fields.add(key)
    return fields

def prepare_items(items: List[dict], render_fields: List[str]):
    item_list = []
    for item in items:
        new_item = {}
        for field in render_fields:
            new_item[field] = item.get(field, "")
        item_list.append(new_item)
    return item_list
    

def list_view(s: schema.Schema):
    def view1() -> str:
        db: pymongo.MongoClient = get_db()
        items_collection = db["json-admin"]["items"]
        items = list(items_collection.find())

        render_fields = ["_id"]
        if not s.meta.list_fields:
            f = get_render_fields(items)
            f.remove("_id")
            render_fields += f
        else:
            render_fields += s.meta.list_fields


        items = [x.values() for x in prepare_items(items, render_fields)]

        return render_template("list_template.j2", items=items, headers=render_fields)

    return view1

def update_view(s: schema.Schema):
    def view2(item_id: str) -> str:
        db: pymongo.MongoClient = get_db()
        items_collection = db["json-admin"]["items"]
        item = items_collection.find({"_id": bson.ObjectId(item_id)})[0]
        return flask.render_template("create_template.j2", schema=s, item=item)



    return view2

def delete_view(item_id: str):
    db: pymongo.MongoClient = get_db()
    items_collection = db["json-admin"]["items"]
    items_collection.delete_one({"_id": bson.ObjectId(item_id)})
    return flask.redirect("/list/")



def create_item():
    db: pymongo.MongoClient = get_db()

    data = flask.request.form
    
    items_collection = db["json-admin"]["items"]
    items_collection.insert(dict(data))

    return flask.redirect("/list/")
