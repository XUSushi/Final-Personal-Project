# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 18:40:15 2018

@author: 许逸文
"""
import http.client, urllib.parse, uuid, json
import hashlib  
import random  

class BaiduTranslation:
    
    '''
     @function: 配置和使用百度机器翻译API
    '''
     
    def __init__(self,number):
        
        self.number=number        
    
    def translate_baidu (appid,key,fromlang,tolang,content):
        '''
        @function:配置百度机器翻译API的请求，相当于是请求百度机翻API的内核程序，为下面的使用做准备
        @input param:appid 字符串，API的ID
                     key 字符串，API密码
                     fromlang 字符串，源语言
                     tolang 字符串，目标语言
                     content 字符串， 待翻译的内容
        @output param: result 字符串， 翻译结果        
        '''
        appid=appid
        secretKey=key
        fromLang=fromlang
        toLang=tolang
        text=content
        #接收传进来的值
        httpClient = None  
        myurl = '/api/trans/vip/translate'  
        salt = random.randint(32768,65536)  
        sign = appid + text + str(salt) + secretKey  
        sign = hashlib.md5(sign.encode()).hexdigest()  
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(  
                text) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(  
                salt) + '&sign=' + sign  
        #拼成请求链接
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')  
        httpClient.request('GET', myurl)  
        #请求
        response = httpClient.getresponse()  
        #接收回复
        jsonResponse = response.read().decode("utf-8")  
        js = json.loads(jsonResponse) 
        result = str(js["trans_result"][0]["dst"]) 
        #提取出翻译结果
        return (result)

    def use_baidu(self,text):
        """
        @function:调用百度翻译API
        @input param:text 字符串 待翻译的内容     
        @output param: result 字符串 翻译结果
        """
        fromLang='en'
        toLang = 'zh'
        appid='20170601000049695'
        secretKey = 'gOxjP2r4I9SsWRDF2ozO'
        #配置语言对、ID和KEY
        result = BaiduTranslation.translate_baidu (appid,secretKey,fromLang,toLang,text)
        #调用同类下的translate_baidu()函数，取得翻译结果
        return(result)
'''        
if __name__ == "__main__":
    a="This migrate "
    text=use_baidu(a)
    print("baidu:",text)
'''