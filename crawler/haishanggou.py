# -*- encoding: utf-8 -*-
'''
@File    :   haishanggou.py
@Time    :   2021/10/18 15:34:08
@Author  :   James 
@Desc    :   海尚购获奖
@Version :   1.0
'''

from bs4 import BeautifulSoup
from requests import Request, Session
import os,time
import requests
import hashlib
import base64

proxies = {
    "http": "http://user:password@10.185.113.100:8002",
    "https": "http://user:password@10.185.113.100:8002",
}
def get_html(url):
    '''获取海尚购获奖名单网页'''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.8 Safari/537.36'
    }
    s = Session()
    req = Request('GET',url=url,headers=headers)
    prepped = req.prepare()
    resp = s.send(prepped,proxies=proxies)
    if resp.status_code == 200:
        return resp.content
    return None

def parse_html(html):
    '''解析html，获取图片url'''
    soap = BeautifulSoup(html,'lxml')
    eles = soap.find_all('img',class_='rich_pages')
    if eles:
        pic_urls = [ele['data-src'] for ele in eles]
        return pic_urls
    return None

def download_pic(urls,path):
    '''下载中签名单图片'''
    suffix = '.png'
    count = 0
    if not os.path.exists(path):
        os.makedirs(path)
        print(f'创建目录{path}成功')
    for url in urls:
        content = get_html(url)
        if content:
            name = path + hashlib.md5(url.encode(encoding='utf-8')).hexdigest() + suffix
            print(f'文件名是{name}')
            write_file_to_disk(content,name)
            count += 1
        time.sleep(3)
    print(f'成功下载{count}个文件')
    return count
    

def write_file_to_disk(content,path):
    '''将图片写入本地磁盘'''
    with open(path,'wb') as f:
        f.write(content)

def get_token():
    '''获取调用百度接口所需token'''
    host = 'https://aip.baidubce.com/oauth/2.0/token'
    payload = {
        'grant_type':'client_credentials',
        'client_id':'',
        'client_secret':''
    }
    response = requests.get(host,params=payload,proxies=proxies)
    if response and response.status_code == 200:
        #print(response.json())
        return response.json()['access_token']

def parse_pic(folder):
    '''调用百度文字识别接口识别图片文字'''
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件
    file_list = os.listdir(folder)
    if file_list:
        for file in file_list:
            filename = folder + file
            print(filename)
            # with open(filename,'rb') as f:
            #     img = base64.b64encode(f.read())
            # params = {"image":img}
            # access_token = get_token()
            # request_url = request_url + "?access_token=" + access_token
            # headers = {'content-type': 'application/x-www-form-urlencoded'}
            # response = requests.post(request_url, data=params, headers=headers)
            # if response and response.status_code == 200:
                #print (response.json())

def main(folder):
    '''获取完整获奖名单清单'''
    # 1.获取html
    third_winner_url = 'https://mp.weixin.qq.com/s?__biz=MzkyMTIyMjkxMg==&mid=2247485748&idx=1&sn=8b4db8ff914df54a6c414f14ef6bdbf9&chksm=c187a35bf6f02a4db574f342a69833e4bf24ff6789a28ec2788f8793c21f495de949870911ea&mpshare=1&scene=1&srcid=101826ueXDB80Zy6470XEM09&sharer_sharetime=1634542070178&sharer_shareid=7411eb034d1de4483abc7820e46b9eca&exportkey=AVN3GSEQB6cKguAufDFHMac%3D&pass_ticket=OnNagiwiiKmyPSotLnEHjhE5CKpWWWTMcVKeXF%2B0Rx%2B5T3iFaMEmBlZizoDH4tcA&wx_header=0#rd'
    html = get_html(third_winner_url)
    # 2.解析html，获取中奖图片
    if html:
        pic_urls = parse_html(html.decode(encoding='utf-8'))      
        count = download_pic(pic_urls,folder)
        if count > 0:
            parse_pic(folder)
        


if __name__ == '__main__':
    folder = 'E:\\Python\\liaoxuefeng\\pachong\\haishang\\third\\'
    #main()
    print(get_token())