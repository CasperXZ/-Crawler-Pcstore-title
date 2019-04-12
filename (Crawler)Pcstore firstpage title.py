# -- coding: utf8 --

import requests
import base64
import urllib
from bs4 import BeautifulSoup
import re



class pcstore:
    def __init__(self):
        self.url1='https://www.pcstore.com.tw/adm/psearch.htm?'
        self.searching_key=''


    def key_word(self):
        key=input('請輸入商品')
        encode_url=urllib.parse.quote(key)
        url_key=base64.b64encode(bytes(encode_url,'utf-8'))
        self.searching_key=url_key
        

    def get_res(self):
        self.key_word()
        payload_data={'store_k_word':self.searching_key,'slt_k_option':'1'}
        #payload_data={'word':key_word,'slimit':'10'}
        pcstore_res=requests.get(self.url1,params=payload_data)
        #print(res.encoding)
        #print (res.apparent_encoding)
        pcstore_res.encoding='big5-hkscs'
        #pc_cookies=requests.get(self.url2,verify=False)
        return pcstore_res

    def Net(self):
        res=self.get_res()
        soup=BeautifulSoup(res.text)
        titles=soup.find_all('div',{'class':'pic2t pic2t_bg'})
        for title in titles:
            print (title.text)



        

        

if __name__=="__main__":

    obj=pcstore()
    obj.Net()
    
