# coding: utf-8

from flask import Flask

app = Flask("project_flask")
app.config.from_object('settings')

import views
