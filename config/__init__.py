# coding: utf-8

# アプリのバージョン
__version__ = '1.0'

# MVC, ORMライブラリを読み込む用のパスを追加
import os, sys
BASE_DIR = os.getcwd()
sys.path.append( os.path.join(BASE_DIR, 'libs') )

# データベース用のパスの設定をする
DATA_FILE = os.path.join( os.path.join(BASE_DIR, 'database'), 'tweet.sqlite' )

# MVCライブラリを読み込む
from bottle import run, route, static_file

# データベースオブジェクトを作成する
from peewee import SqliteDatabase
db = SqliteDatabase( DATA_FILE )

# MVCの機能を読み込む
from controllers import *
from models import *


# 静的ファイル（cssやjavascript）用のパスを設定する
@route('/static/<filepath:path>')
def server_static( filepath ):
	return static_file( filepath, root='static' )