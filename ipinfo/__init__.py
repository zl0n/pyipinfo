#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import sys
from ipinfo.utils import ip_list_from_string


def request_to_ipinfo(ip):
    ''' return a json from the request '''
    full_url = 'http://ipinfo.io/{}'.format(ip)
    headers = {'User-Agent': 'curl/7.30.0'}
    req = requests.get(full_url, headers=headers)
    if req.status_code == 200:
        return req.json()


def main():
    string = sys.stdin.read()
    ip_list = ip_list_from_string(string)

    if ip_list == []:
        exit()

    ip_set = set(ip_list)
    for ip in ip_set:
        print request_to_ipinfo(ip)


if __name__ == '__main__':
    main()