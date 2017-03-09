import itertools
import json

import time
from webbrowser import browser

import requests
import scrapy
from scrapy.http.cookies import CookieJar
from scrapy.selector import Selector
from scrapy.spider import Spider, Request
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from meituzz.items import MeituItem, ImageItem
import uuid


class DmozSpider(Spider):
    name = "meituzz"
    allowed_domains = ["a.mt8z.com"]
    start_urls = [
        # "http://a.mt8z.com/ab/brv1?y=3256m09005",
        # "http://zz.meituzz.com/ab/brV9?y=57e4m00009",
        # "http://a.mt8z.com/album/browse12?albumID=9823",
        # "http://a.mt8z.com/album/browse14?albumID=12983",
        # "http://a.mt8z.com/album/browse13?albumID=11591",
        # "http://a.mt8z.com/album/browse12?albumID=10828",
        "http://zz.meituzz.com/ab/brV9?y=6663m06530"
    ]

    def start_requests(self):
        return [Request('http://zz.meituzz.com/ab/brV9?y=6663m06530', meta={'cookiejar': 1}, callback=self.parse)]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename + ".html", 'wb').write(response.body)
        sel = Selector(response)

        cookie = response['set-cookie']
        print(cookie)

        downHeaders = {
            'Accept': "application/json, text/javascript, */*; q = 0.01",
            'Accept-Encoding': "gzip, deflate",
            'Accept-Language': "zh-CN, zh;q = 0.8, en;q = 0.6",
            'Cache-Control': "no-cache",
            'Connection': "keep-alive",
            'Content-Length': "42",
            'Content-Type': "application / x-www-form-urlencoded;charset = UTF-8",
            'Host': "zz.meituzz.com",
            'Origin': "http://zz.meituzz.com",
            'Pragma': "no-cache",
            'Cookie': cookie,
            'Referer': "http://zz.meituzz.com/ab/brV9?y=6663m06530",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            'X-Requested-With': "XMLHttpRequest",
        }
        print(downHeaders)
        # #
        url = "http://zz.meituzz.com/ab/bd?y=26211&s=HmvgQ2EE43qczD9KygCsHA-wKkwMc_47"
        torrent = requests.post(url, header=downHeaders,  timeout=2000)
        print(torrent.text)
