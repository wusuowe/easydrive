#!/usr/bin/python
#coding = utf8
import urllib2
def crawl(url):
    opener = urllib2.urlopen(url)
    page = opener.read()
    try:
        page = page.decode('gb18030').encode('utf8')
    except:
        pass
    return page

