from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


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
    result = soup.find_all(class_="gnav_label")

    return render(
        request,
        "scraping/index.html",
        {
            "target_url": target_url,
            "result": result,
            "origin_html": soup.prettify(),
        },
    )
