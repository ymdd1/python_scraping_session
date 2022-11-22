from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def post_list(request):
    target_url = request.GET.get("target_url")
    html_text = requests.get(target_url, verify=False).text
    origin_html = BeautifulSoup(html_text, "html.parser")

    result = origin_html.find_all(class_="gnav_label")
    return render(
        request,
        "scraping/post_list.html",
        {
            "target_url": target_url,
            "result": result,
            "origin_html": origin_html.prettify(),
        },
    )
