# -*- coding: utf-8 -*-

from peewee import *

db = SqliteDatabase('observer.db')

print("Preparing database observer.db...")
class Members(Model):
    memberid = IntegerField()
    username = CharField()
    discriminator = CharField()

    class Meta:
        database = db