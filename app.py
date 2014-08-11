# coding: utf-8

# 設定ファイルを読み込む
from config import *


if __name__ == '__main__':
	# データベースを作成する
	if not os.path.exists( DATA_FILE ):
		db.connect()
		Tweets.create_table()
		db.close()

	# サーバーを起動！！
	run( host='127.0.0.1', port=8000, reloader=True )
