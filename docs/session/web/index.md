## 最新のリポジトリをpull
下記コマンドでmainブランチの最新差分を取り込んでください。
```
$ git pull origin main
```

## djangoを立ち上げる

/codes内のコードは、`django`というフレームワークで実装されています。
下記のコマンドでサーバーを立ち上げましょう。

※実行前に仮想環境を立ち上げていることを確認してください。
```
// すでにcodesディレクトリにいる場合は、実行しなくて大丈夫です。
$ cd codes

// webサーバーを立ち上げる。
$ python manage.py runserver
```

## Webサイトが動いていることを確認
ブラウザで以下のアドレスを開いてみましょう。（Firefox, Chrome, Safari, Internet Explorerなど、好きなブラウザを使って大丈夫です）

```
http://127.0.0.1:8000/
```

## スクレイピングを実行させてみる
すでにこのサーバーには、スクレイピングの実行処理が実装されています。
早速試してみましょう。

ページのinputフォームに、下記のURLを入力し、submitを押下してください。

```
https://www2.teijin-frontier.com/
```

データ抽出結果とデータ取得結果に、たくさんの文字が表示されたかと思います。

データ抽出結果には、指定したURLのトップページのヘッダー要素が表示されています。

データ取得結果には、スクレイピングして取得できた全てのhtmlが表示されています。

## データを抽出してみる
ヘッダー要素からテキストのみを抽出してみます。

`/codes/scraping/views.py`ファイル内の下記コードを
```
result = soup.find_all(class_="gnav_label")
```

下記のように書き換えてください。
```
result = [e.text for e in soup.find_all(class_="gnav_label")]
```

再度、submitしてみてください。
下記のように表示されたかと思います。
```
['企業情報', '研究開発', '製品', '財務情報', 'サステナビリティ', '採用情報']
```

## コードを理解する
今度は、スクレイピングの処理をコードから見ていきます。

`/codes/scraping/views.py`ファイル内の`index`関数がそれに当たります。
下記は、index関数の全体のコードです。
```
def index(request):
    target_url = request.GET.get("target_url")

    if not target_url:
        return render(
            request,
            "scraping/index.html",
            {
                "target_url": "",
                "result": "",
                "origin_html": "",
            },
        )

    # 指定したページのhtmlを取得
    html_text = requests.get(target_url, verify=False).text

    # BeautifulSoupオブジェクトに変換
    soup = BeautifulSoup(html_text, "html.parser")

    # データ抽出ロジック
    result = [e.text for e in soup.find_all(class_="gnav_label")]

    return render(
        request,
        "scraping/index.html",
        {
            "target_url": target_url,
            "result": result,
            "origin_html": soup.prettify(),
        },
    )
```

この中でスクレイピングの処理をしているのは、下記の3行のみです。

```
# 指定したページのhtmlを取得
html_text = requests.get(target_url, verify=False).text ・・・・❶

# BeautifulSoupオブジェクトに変換
soup = BeautifulSoup(html_text, "html.parser") ・・・・❷

# データ抽出ロジック
result = [e.text for e in soup.find_all(class_="gnav_label")] ・・・・❸
```

### 1行目のコード解説

`requests.get()`で指定したURLからデータを取得してきます。
`verify=False`は、ssl関係のオプションです。今回は無視して構いません。

`.text`で、取得したhtmlを文字列形式で取得します。

### 2行目のコード解説

`BeautifulSoup`は、コード解析ツールになります。
特定のhtmlタグのみを抽出したり、class名からデータを抽出することができます。
第一引数で、1行目に取得した文字列を指定しています。これにより、BeautifulSoupに抽出対象のhtmlを認識させます。

第二引数には、解析対象の種類を指定します。今回は、htmlなので`html.parser`を指定しています。

### ３行目のコード解説

`soup.find_all(class_="gnav_label")`で、html全体からクラス名が`gnav_label`のタグを配列で取得します。

` [e.text for e in xxxx]`のコードにより、取得したヘッダー要素1つずつに対してテキストを取得し、配列にしています。
これにより、ヘッダーのテキストが配列で取得できました。

`BeautifulSoup`のメソッドなどは、下記の記事が参考になります。
- [https://yu-nix.com/archives/bs4-class/](https://yu-nix.com/archives/bs4-class/)
- [https://python.civic-apps.com/beautifulsoup4-selector/](https://python.civic-apps.com/beautifulsoup4-selector/)


## 実践してみる

トップページの新着情報を取得してみましょう。新着情報のタイトルを抽出し、文字列の配列で表示させてください。

下記のように表示されればOKです。
![titles](https://github.com/ymdd1/python_scraping_session/blob/main/docs/images/titles.png?raw=true) 

### ヒント
1. まずは、下記のリンクにアクセスして、新着情報のhtmlタグを探してみましょう。ブラウザのデベロッパーツールを開くと、htmlタグを確認することができます。
```
https://www2.teijin-frontier.com/
```

2. 対象のhtmlタグを見つけたら、抽出するクラス名は何か見てみましょう。`js-tab_body c-tab_body is-show`というclassが指定されているdivタグの中に`news-compo`というclassが指定されたdivタグがありますね。その中身に新着情報が格納されているようです。タイトルはどんなクラス名でしょうか？

3. 処理の流れは、findメソッドで、`js-tab_body c-tab_body is-show`クラス配下を抽出します。その中から、find_allメソッドでタイトルだけを抽出する（2で調査したタイトルのクラス名が重要です）。あとは、`.text`を用いて文字列の配列を作ればできます。




