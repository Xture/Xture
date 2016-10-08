#!/bin/bash

mongo localhost:27017/xture --eval "db.createCollection('adventure')"
mongo localhost:27017/xture --eval "db.adventure.createIndex({'location': '2dsphere'})"
mongo localhost:27017/xture --eval "db.createCollection('users')"

