#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: __init__.py
# Project: url
# Created Date: Friday, April 2nd 2021, 4:13:38 pm
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
from flask_restful import Resource
from flask import current_app
from flask_restful_swagger import swagger
from flask import request
from ....tools import *
from app.tools import APIReturn


class InsertUrl(Resource):
    "新增新的短網址"
    @swagger.operation(
        notes="新增新的短網址",
        nickname="Url",
        parameters=[
              {
                  "name": "url",
                  "description": "你想要縮短的網址",
                  "required": True,
                  "allowMultiple": False,
                  "dataType": "string",
                  "paramType": "query",
              },
        ]
    )
    def post(self):
        try:
            from app.models import URL
            url = request.values.get('url')
            if url == None or url == '':
                return APIReturn(status=False, message="need url")

                #!/usr/bin/python3

            import random

            chars = "abcdefghijklmnopqrstuvwxyziABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
            newId = ""

            while len(newId) != 10:
                newId = newId + random.choice(chars)

            u = URL(
                id=newId,
                webURL=url
            )
            u.save()
            return APIReturn(status=True, data=newId)
        except Exception as e:
            return APIReturn(status=False, message=str(e))
