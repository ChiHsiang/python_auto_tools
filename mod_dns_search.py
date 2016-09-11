#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dns.resolver
import os
import http.client

ip_list = []
app_domain = "www.google.com.tw"

def get_iplist(domain = ""):
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception as e:
        print("dns resolver error:" + str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            ip_list.append(j.address)

    return True
        
def check_ip(ip):
    check_url = ip + ":80"
    get_content = ""
    http.client.socket.setdefaulttimeout(5)
    conn = http.client.HTTPConnection(check_url)

    try:
        conn.request("GET", "/", headers = {"Host": app_domain})
        r = conn.getresponse()
        get_content = r.read(15)
    finally:
        if get_content.decode(encoding="UTF-8") == "<!doctype html>":
            print(ip + " [OK]")
        else:
            print(ip + " [Error]")
        
if __name__ == "__main__":
    if get_iplist(app_domain) and len(ip_list) > 0:
        for ip in ip_list:
            check_ip(ip)
    else:
        print("dns resolver error.")
