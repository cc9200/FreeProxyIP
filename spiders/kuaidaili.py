import requests
from lxml import etree
from ..common.header import ua

def get_html():
    index=1
    sess=requests.Session()
    sess.headers={"User-Agent":ua.random}
    while index:
        #高匿代理
        url='https://www.kuaidaili.com/free/inha/%d'%index
        r=sess.get(url)
        parse(r.text)
        #普通代理
        url='https://www.kuaidaili.com/free/intr/%d'%index
        r=sess.get(url)
        parse(r.text)

        index+=1

def parse(html):
    selector=etree.HTML(html)
    eles_ls=selector.xpath("//table[@class='table table-bordered table-striped']/tbody/tr")
    for ele in eles_ls:
        IP=ele.xpath("./td[@data-title='IP']/text()")
        PORT=ele.xpath("./td[@data-title='PORT']/text()")