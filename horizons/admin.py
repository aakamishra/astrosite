# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question, Post

admin.site.register(Question)
admin.site.register(Post)

# Register your models here.
