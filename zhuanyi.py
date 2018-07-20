# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 21:13:08 2018

@author: 许逸文
"""

import re
from baidu_trans import BaiduTranslation
from bing_trans import BingTranslation
#引入BaiduTranslation和BingTranslation翻译两大类，下面翻译时调用
class ZhuanyiTrans:
    """
    @function:查看语句是否包含转义符号并对文本进行翻译处理
    
    """
    def zhuanyi(self,content):
        """
        @function:查看语句是否包含转义符号并对文本进行翻译处理。若含转义符，则将转义符和文本拆离开，翻译文本后再拼接到一起；若不含转义符则直接机器翻译。
        @input param:content 字符串型 传入待处理的文本
        @output param: result 字符串型 翻译好的文本（包含翻译好的文本+转义字符拼到一起）
        @character：设计了异常处理，如果百度翻译API出错就自动调用必应翻译API
        """
        
        trans_baidu= BaiduTranslation("baidu调用") #建立百度翻译类的对象
        trans_bing=BingTranslation()    #建立有道翻译类的对象
        pp=re.compile(r'([^\\]*)(\\*[^\\]?)')#正则表达式识别模式
        #思路是：转义字符前的文本 转义字符 这样为一组，对每行内容进行循环查找
        biao=pp.findall(content)
        tupb=tuple(biao)#识别后放入tuple中
        if len(tupb)!=0:
            #如果可以被正则表达式匹配，则len(tupb)!=0
            #注意匹配上不一定意味着这个这个文本包含转义符号
            """
            这个语句可以把包含转义符号的文本和不包含转义符号的纯文本都匹配上，对两者进行处理：
                包含转义符号的文本:tupb[i][0]为待翻译的文本
                                 tupb[i][1]为需保留的转义字符
                不包含转义符号的纯文本：tupb[i][0]为待翻译的文本
                                      tupb[i][1]为空
            """
            stt=''
            result=''
            for i in range(len(tupb)) :
                #多次查找符合正则表达式的字符串，因为一行可以包括多个
                #tup[i][0] 需要翻译的文本 ttext
                #tup[i][1] 保留的转义字符 tupb[i][1]
                if tupb[i][0]=='':
                    ttext=''
                    #如果匹配后，发现tupb[i][0]为空，例如几个转义字符连在一起的时候，直接传空值给翻译api会出错
                    #所以如果出现这种情况，就直接赋值给ttext为空
                elif tupb[i][0]==' ':
                    ttext=' '
                    #如果匹配后，发现tupb[i][0]为空格，例如几个转义字符连在一起的时候，直接传空值给翻译api会出错
                    #所以如果出现这种情况，就直接赋值给ttext空格
                else:
                    #这里就是最通常的情况，tup[i][0]有待翻译的文本
                    '''
                    进行异常处理，如果百度翻译出错就自动调用必应翻译
                    
                    '''
                    try:
                        ttext=trans_baidu.use_baidu(tupb[i][0])
                        #差错处理
                        #先运行百度翻译API-BaiduTranslation类的use_baidu()函数进行翻译
                    except Exception as es:
                        ttext=trans_bing.use_bing(tupb[i][0])
                        #如果出错，比如百度翻译api的id和key出错的话，就调用必应翻译API-BingTranslation类的use_bing()函数
                        #这样就实现了出错也不会影响前端程序
                    
                    stt=ttext+tupb[i][1]#将翻译完的文本和转义符拼接在一起；对于纯文本而言，tupb[i][1]为空，所以这个也是该文本的翻译结果
                    result=result+stt#循环完毕后，result存的是这一句的完整翻译结果
            
        else:
            #经过测试目标文件，上述正则表达式，可匹配到不包含转义字符的纯文本，所以这种情况是不存在的
            #写在这里是为了日后运用到其他程序的可能的变化
            print("没有！")
            result='没有'
        return result    
        #返回翻译好的结果