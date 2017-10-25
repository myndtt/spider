# -*- coding: utf-8 -*-
import random, base64


class ProxyMiddleware(object):
    proxyList = [ \
        '114.235.80.220:8118', '183.133.84.8:8118', '60.24.165.120:8118', '113.251.161.228:8123', '121.31.145.177:8123',
        '110.73.15.52:8123', '39.71.148.34:8118 	', '175.31.188.253:8118'
    ]

    def process_request(self, request, spider):
        # Set the location of the proxy
        pro_adr = random.choice(self.proxyList)
        print("USE PROXY -> " + pro_adr)
        request.meta['proxy'] = "http://" + pro_adr