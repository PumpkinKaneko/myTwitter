# coding: utf-8

# ORM用の機能を読み込む
from config import db
from peewee import Model, CharField, TextField, DateTimeField


# ツイートを保存するテーブル
class Tweets( Model ):
	name = CharField()
	text = TextField()
	create_at = DateTimeField()

	# データベースオブジェクトと関連付ける
	class Meta:
		database = db