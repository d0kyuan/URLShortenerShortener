#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: url.py
# Project: models
# Created Date: Friday, April 2nd 2021, 4:09:55 pm
# Author: Ray
# -----
# Last Modified:
# Modified By:
# -----
# Copyright (c) 2021 Ray
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###
from sqlalchemy.dialects.postgresql import UUID, TEXT
import uuid
from flask_sqlalchemy import SQLAlchemy
from flask import current_app
db = current_app.config['db']
BaseModel = current_app.config['BaseModel']


class URL(BaseModel):
    __tablename__ = 'tb_url'
    id = db.Column(db.String(10), unique=True, primary_key=True)
    webURL = db.Column(TEXT)
    _default_fields = [
        "id",
        "webId",
        "name",
    ]

    def __init__(self, id, webURL):
        self.webURL = webURL
        self.id = id

    def delete(self):
      #  self.deletedAt = datetime.datetime.now()
        db.session.commit()

    def update(self):
     #   self.updatedAt = datetime.datetime.now()
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()
