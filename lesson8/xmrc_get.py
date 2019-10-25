'''
https://www.xmrc.com.cn/net/info/Resultg.aspx?
a=a&
g=g&
recordtype=1&
searchtype=1&
keyword=python&
releasetime=365&
worklengthflag=0&
place=350205&
sortby=updatetime&
ascdesc=Desc
'''
import requests


url = 'https://www.xmrc.com.cn/net/info/Resultg.aspx?'
d = {
    'a':'a',
    'g':'g',
    'recordtype': '1',
    'searchtype': '1',
    'keyword': 'python',
    'releasetime': '',
    'worklengthflag': '',
    'place': '',
    'sortby': '',
    'ascdesc': '',
}
