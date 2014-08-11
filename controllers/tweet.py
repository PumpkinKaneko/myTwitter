# coding: utf-8

# MVC用の機能を読み込む
from datetime import datetime
from bottle import route, get, post, request, redirect, response, template
from models.tweet import Tweets

# 最初のページの時のサーバーの処理
@get('/')
def index():
	# ツイートのデータをデータベースから持ってくる
	tweets = Tweets.select()

	# テンプレートエンジンにツイートのデータを渡す
	return template( 'index', tweets=tweets )



# ツイートを送信された時のサーバーの処理
@post('/tweet')
def tweetMessage():
	# フロントエンド側からポストされたデータを受け取る
	name = request.forms.decode().get('name')
	tweet = request.forms.decode().get('tweet')
	create_at = datetime.now()
	
	# データベースに登録する
	Tweets.create( name=name, text=tweet, create_at=create_at )

	# 最初のページにリダイレクトする
	return redirect('/')


"""
from wtforms import *
class RegistrationForm( Form ):
    username = TextField('Username', [validators.Length(min=4, max=25)])

@get('/register')
@post('/register')
def register():
	req = request.forms
	form = RegistrationForm( req )
	if not req:
		return template('form', form=form)
	else:
		if form.validate():
			return u'Der Name ist {0}'.format(form.username.data)
		else:
			return template('form', form=form)
"""
