# スクレイピング結果をスプレッドシートに保存する

## スプレッドシートを作成
まずは、スプレッドシートを作成してください。
スプレッドシートの名前は、`スクレイピング結果`にしてください。


## gcpでサービスアカウントを登録する

下記の記事を参考にして、gcp上でサービスアカウントを作成します。

[PythonでGoogle Sheetsを編集する方法](https://www.twilio.com/blog/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python-jp)

これは、スプレッドシートとpythonコードを繋ぐための設定です。
`client_secret.json`は、codesフォルダに保存してください。

## スプレッドシートの共有にメアド追加
先程作成した`スクレイピング結果`シートの共有ボタンを押下して、jsonにあるメアドを登録してください。

## パッケージ追加
設定も終わったので、サンプルコードを動かしてみます。
まずは、ターミナルで、pythonのパッケージをインストールします。下記のコマンドを実行してください。

```bash
pip install gspread oauth2client
```

`codes/scraping/views.py`ファイルの上部に下記のインポートを追加してください。
先程インストールしたパッケージを使うことができるようになります。

```python

import gspread
from oauth2client.service_account import ServiceAccountCredentials

```

## サンプルコードを追加

`def gs(request):`関数を下記のように書き直してください。インデントを間違えると、動かなくなるのでご注意ください。

```python
def gs(request):
  scope = [
      "https://spreadsheets.google.com/feeds",
      "https://www.googleapis.com/auth/drive",
  ]
  creds = ServiceAccountCredentials.from_json_keyfile_name(
      os.path.join(settings.BASE_DIR, "client_secret.json"), scope
  )
  client = gspread.authorize(creds)

  target_url = request.GET.get("target_url")

  if not target_url:
      return render(
          request,
          "scraping/gs.html",
          {
              "target_url": "",
          },
      )

  # 指定したページのhtmlを取得
  html_text = requests.get(target_url, verify=False).text

  # BeautifulSoupオブジェクトに変換
  soup = BeautifulSoup(html_text, "html.parser")

  # データ抽出
  header_result = soup.find_all(class_="gnav_label")

  # スプレッドシートを取得
  sheet = client.open("スクレイピング結果").sheet1

  # シートの内容を全てクリア
  sheet.clear()

  sheet.update_cell(1, 1, "対象URL")
  sheet.update_cell(1, 2, target_url)

  sheet.update_cell(3, 1, "ヘッダー")

  # ヘッダーコンテンツをスプレッドシートに書き込み
  for i, r in enumerate(header_result):
      text = r.text
      sheet.update_cell(4, i + 2, text)

  sheet.update_cell(6, 1, "新着情報")

  return render(
      request,
      "scraping/gs.html",
      {
          "target_url": target_url,
      },
  )

```

ブラウザで、下記のアドレスを開いてください。
```
http://127.0.0.1:8000/gs
```

`データ抽出が完了しました`というページが表示されれば、先程のスプレッドシートに下記のようなデータが登録されているはずです。
<br><br>
![gs_sample](https://github.com/ymdd1/python_scraping_session/blob/main/docs/images/gs_sample.png?raw=true) 


## 新着情報をスプレッドシートに書き込む

先程スクレイピングで取得した新着情報を、スプレッドシートに書き込んでみましょう。

下記のように表示されているのが目標です。日付表示は余力のある方で構いません。
<br><br>
![gs_sample](https://github.com/ymdd1/python_scraping_session/blob/main/docs/images/gs_news_contents.png?raw=true) 


タイトル文字列が入った配列をループで回し、`sheet.update_cell()`関数を使って、1行ずつスプレッドシートに書き込んでいきます。

### sheet.update_cell()について
`sheet.update_cell()`関数は、スプレッドシートのセルにデータを入力できる関数です。使用の際には、3つの引数が必要です。
- 第一引数は、行番号です。スプレッドシートの`横グリッド`に値します。int型で指定しましょう。
- 第ニ引数は、列番号です。スプレッドシートの`縦グリッド`に値します。int型で指定しましょう。
- 第三引数は、テキストです。表示したい内容を指定しましょう。


```python
sheet.update_cell(1,2, "テスト") // B1のセルに"テスト"と表示されます。
```

### ヒント

1. `enumerate`関数を使ってループ処理をすると、現在実行中の配列番号が取得できます。この番号を使って、行番号を動的に指定できます。

```python
for index, content in enumerate(list):
  print(index) // 配列番号です。0から始まります。
  print(content) // 配列の要素です。
```

### 注意事項
たまに、429エラーとdjangoのページ（`/gs`）に表示されることがあります。
読み書きの回数制限に達したというエラーです。少し待つと解消されるので、問題ありません。


