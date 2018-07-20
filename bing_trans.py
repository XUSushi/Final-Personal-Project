# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 23:59:05 2018

@author: 许逸文
"""

# -*- coding: utf-8 -*-

import http.client, urllib.parse, uuid, json
import hashlib  
import random  

class BingTranslation:
    '''
    @function: 配置和使用必应机器翻译API
    '''
    def translate_bing (key,lang,content):
        """
        @function:配置必应机器翻译API的请求，相当于是请求必应机翻API的内核程序，为下面的使用做准备
        @input param:key 字符串，API密码
                     lang 字符串，目标语言
                     content 字符串 待翻译的内容
        @output param: js json格式列表 里面包含着翻译结果
        """
        params=lang #目标语言
        subscriptionKey=key #api密码
        host = 'api.cognitive.microsofttranslator.com'
        path = '/translate?api-version=3.0'
        #路径
        headers = {
            'Ocp-Apim-Subscription-Key': subscriptionKey,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4()),
           
        }
        #配置必应翻译api请求头文件
        conn = http.client.HTTPSConnection(host)#链接
        conn.request ("POST", path + params, content, headers)#请求
        response = conn.getresponse ()#得到回复
        
        a=response.read ().decode('utf-8')#解码
        js = json.loads(a)#转化为列表了
        return js#返回包含翻译结果的列表
    
    
    def use_bing(self,text):
        """
        @function:调用必应翻译
        @input param:text 字符串 待翻译的内容     
        @output param: result[0]['translations'][0]['text'] 字符串 翻译结果
        """
    
        params = "&to=zh"; #设置目标语言
        subscriptionKey = 'b4bd6dfb95374f9db66ae3f5a72f0762'#API密码
        requestBody = [{'Text' : text,}]
        content = json.dumps(requestBody, ensure_ascii=False).encode('utf-8')
        #变成字符串
        result = BingTranslation.translate_bing (subscriptionKey,params,content)
        #调用translate_bing（）完成对必应API的请求
        if result[0]['translations'][0]['text'] is not None:
            #如果翻译后的结果不为空就返回翻译结果
            return(result[0]['translations'][0]['text'])
        else:
            ##如果翻译后的结果为空就打印‘wrong’
            print("wrong")
        
'''  
if __name__ == "__main__":
    t=BingTranslation()
    c="GMT-11:00,GMT-10:00,GMT-9:00,GMT-8:00,GMT-7:00,GMT-6:00,GMT-5:00,GMT-4:00,GMT-3:00,GMT-2:00,GMT-1:00,GMT-0:00,GMT+1:00,GMT+2:00,GMT+3:00,GMT+4:00,GMT+5:00,GMT+6:00,GMT+7:00,GMT+8:00,GMT+9:00,GMT+10:00,GMT+11:00,GMT+12:00"
    text=t.use_bing(c)
    print(text)
'''