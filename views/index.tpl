<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
<!-- cssのファイルを読み込む -->
		<link rel="stylesheet" type="text/css" href="static/css/style.css">
<!-- javascriptのファイルを読み込む -->
		<script type="text/javascript" src="static/js/jquery.js"></script>
		<title>まいついったー</title>
	</head>

	<body>
<!-- ツイート用のフォーム -->
		<form action="tweet" method="post">
			<p>
				<div>名前</div>		
				<input type="textarea" name="name" size="50" maxlength="10">
			</p>
			<p>
				<div>ツイートする</div>		
				<textarea name="tweet" cols=50 rows=8></textarea>
			</p>
			<p>
				<input type=submit value="ツイート">
			</p>
		</form>
<!-- ツイート用のフォームここまで -->

<!-- ツイートを表示するテーブル -->
		<table>
			<tr>
				<th>ユーザー名</th>
				<th>ツイート</th>
				<th>時間</th>
			</tr>
		% for tweet in tweets:
			<tr>
				<td>{{tweet.name}}</td>
				<td>{{tweet.text}}</td>
				<td>{{tweet.create_at}}</td>
			</tr>
		% end
		</table>
<!-- ツイートを表示するテーブルここまで -->
	</body>
	
</html>
