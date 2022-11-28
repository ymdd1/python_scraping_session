

スプレッドシート作成(名前は、スクレイピング結果)


gcpからクレデンシャル取得

スプレッドシートの共有にメアドを追加

クレデンシャルをローカルに保存(codes内)

pip installする
```bash
pip install gspread oauth2client
```


views.pyファイルの上部に下記のインポートを追加
```python

import gspread
from oauth2client.service_account import ServiceAccountCredentials

```

```python
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

sheet.update_cell(6, 1, "最新情報")

return render(
    request,
    "scraping/gs.html",
    {
        "target_url": target_url,
    },
)

```



書き込みは100回に制限されていることがわかります。

