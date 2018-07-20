# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 22:23:18 2018

@author: 许逸文
@function:读取LocaleResource_en_US.properties文件，遍历每一行，使用正则表达式处理要保留的DO NOT TRANSLATE部分、含标签的部分、含转义字符的部分。
          然后调用机器翻译，使文件中的所有内容可以正确地翻译为中文。
          翻译后的结果写入LocaleResource_zh_CN.properties中。
"""


import re
from baidu_trans import BaiduTranslation
from bing_trans import BingTranslation
from preparation import Preparation
from zhuanyi import ZhuanyiTrans
#从baidu_trans.py, bing_trans.py,preparation.py,zhuanyi.py中
#分别引入百度翻译类（BaiduTranslation）、必应翻译类（BingTranslation）、准备处理类（Preparation）和转义处理类(ZhuanyiTrans)

    
if __name__ == '__main__':


    pre=Preparation()
    zhuan_obj=ZhuanyiTrans()
    trans_baidu= BaiduTranslation("baidu调用") #建立百度翻译类的对象
    trans_bing=BingTranslation()
    #创建百度翻译类、必应翻译类、准备处理类和转义类的对象
    
    f = open('E:/LocaleResource_zh_CN.properties','a', encoding="utf-8")
    #写入文档的地址
    with open('LocaleResource_en_US.properties') as g:
        #打开待处理的文件，遍历每一行
        for line in g:
            '''先分为三类：空行、有#的行、无#的行'''
            if (line=='\n'):
                #若为空行直接写入新文件
                print('写入空行')
                f.write(line)
            
            
            elif re.search('#', line):
                #若包含#，则为注释句也直接写进文件中
                print('写入注释句');
                f.write(line)
            else:
                #这种情况为，这一行没有#，意味着是要具体处理的内容
               # string = 'applet_need_java_support = <I>A Java Applet here\! If it does not work, you need to install Java plugin. <a href\="http\://www.java.com/en/download/manual.jsp" target\="_blank">Get Java</a></I>'
                pattern = '([^=]*)=( ?.+)' 
                
                #'(\w+ ?)=( ?.+)'
                match = re.match(pattern, line)
                #识别带有=的句子，
                #因为之前已经排除了空行和注释句，所以在这个情况下的每句话都有=，都会被匹配上
                if match is None:
                    #如果匹配为空，则打印出‘无’。但这种情况其实并不存在，为了程序的完整和日后拓展处理其他程序方便，所以写在这里
                    print("无=",line)
                #print (match)
                else:
                    #如果能匹配上，即包含=，则用group()函数将等号两侧的内容分离开
                    before=match.group(1)#=前面的内容
                    after=match.group(2) #=后面的内容
                    
                   #下面对=后面的内容进行处理
                    '''这一部分有三类需要处理：DO NOT TRANSLATE的部分、带有网页标签的内容、包含转义字符的内容和普通内容'''
                    '''其中DO NOT TRANSLATE的部分比较复杂：观察整理后发现，该部分内容有一定的共同点，可分为三类处理：.gif结尾，.htm结尾和其他特殊 '''
                    #处理=后面的内容包含.gif的
                    if re.search('.gif', after):    
                        print("发现.gif")
                        f.write(line)
                    #处理=后面的内容包含.htm的，但是同时也包含.html的，因为文件中有包含.html的内容是需要翻译的
                    elif (re.search('.htm', after))and(re.search('.html', after) is None):
                        print("发现.htm")
                        f.write(line)
                    #下面5个是处理“DO NOT TRANSLATE的部分”里的特殊情况,分别在文件的153，3678，3905，3907，3983行
                    #这五个句子非常特殊，如果用整个相同匹配的话会使程序不简洁，所以用=前面的内容进行匹配    
                    elif re.search('applet_need_java_support',before):
                        print('处理特殊情况中:',before,":153")
                        f.write(line)
                    elif re.search('help_comment_reference_upload',before):
                        print('处理特殊情况中:',before,":3678")
                        f.write(line)
                        
                    elif re.search('help_dir_offline_listview',before):
                        print('处理特殊情况中:',before,":3905")
                        f.write(line)
                    elif re.search('help_dir_offline_paraview',before):
                        print('处理特殊情况中:',before,":3906")
                        f.write(line)
                    elif re.search('help_dir_root',before):
                        print('处理特殊情况中:',before,":3907")
                        f.write(line)
                    elif re.search('timezone',before):
                        print('处理特殊情况中:',before,":3983")
                        f.write(line)
                        
                    #这以上已经完成了对“DO NOT TRANSLATE THIS SECTION”内容的处理
                        """下面处理需要进行翻译处理的内容，包含有<>网页标签的句子、有转义字符的句子和普通文本句子"""
                    else:
                        raw_line=pre.raw(line)
                        #调用Preparation类的raw()函数，将每一行转化为raw_string，方便后面识别处理
                       
                        match_raw = re.match(pattern, raw_line)
                        #先识别=前后的内容；pattern之前已经定义过 '([^=]*)=( ?.+)'  
                        if match_raw is None:
                            #如果匹配为空，则打印出‘无’。但这种情况其实并不存在，为了程序的完整和日后拓展处理其他程序方便，所以写在这里
                            print("无=",raw_line)
                        #print (match)
                        else:
                            #如果能匹配上，即包含=，则用group()函数将等号两侧的内容分离开
                            before_raw=match_raw.group(1)#=前面的内容
                            after_raw=match_raw.group(2) #=后面的内容
                            p = re.compile(r'([^<]*)(<[^>]*>)([^<]*)')
                            #正则表达式识别网页标记，思路是 标记前文本、标记、标记后文本 三个一组，对每行循环识别
                            shi=p.findall(after_raw)
                            #用正则表达式对=后的内容进行匹配
                            tup1=tuple(shi)
                            
                            #句子里有<>网页标签
                            if len(tup1)!=0:
                                #这种情况极为句子里有<>网页标签
                                print("对有网页标签的内容进行处理")
                                head=before_raw+'='
                                strr=''
                                body=''
                                #处理网页标签
                                for i in range(len(tup1)):
                                    #tup1[i][0] 标签前的文本 翻译这个内容
                                    #tup[i][1] 标签 保留
                                    #tup[i][2] 标签后的文本 翻译这个内容
                                    
                                    #处理#tup1[i][0] 需要翻译这个内容
                                    #若tup1[i][0]为空或空格，直接写到文件中
                                    if tup1[i][0]=='':
                                        trans_p0=''
                                        
                                    elif tup1[i][0]==' ':
                                         trans_p0=' '
                                         
                                    #若#tup1[i][2]不为空
                                    else:
                                        #tup1[i][0]不为空
                                        #这时文本还有可能包含转义字符，所以调用ZhuanyiTrans类的zhuanyi()对文本进行查找转义字符和翻译的工作
                                        trans_p0=zhuan_obj.zhuanyi(tup1[i][0])
                                        #trans_p0为翻译后的tup1[i][0]值
                                        
                                    #处理#tup1[i][2] 需要翻译这个内容
                                    #若tup1[i][2]为空或空格，直接写到文件中
                                    if tup1[i][2]=='':
                                        trans_p2=''
                                    elif  tup1[i][2]==' ': 
                                        trans_p2=' '
                                        
                                    #若#tup1[i][2]不为空
                                    else:
                                        #这时文本还有可能包含转义字符，所以调用ZhuanyiTrans类的zhuanyi()对文本进行查找转义字符和翻译的工作
                                        trans_p2=zhuan_obj.zhuanyi(tup1[i][2]) 
                                        #trans_p2为翻译后的tup1[i][2]值
                                        
                                   
                                    strr= trans_p0+tup1[i][1]+trans_p2
                                    #将tup1[i][0]、tup1[i][1]、tup1[i][2]加在一起放入strr中   
                                    body=body+strr
                                    #循环结束后，body里存的是这一行=后翻译完的内容
                                final=head+body+'\n'
                                #将=前的内容、=和=后的内容拼接在一起，结尾加上换行符，写入文件中
                                f.write(final)
                                
                            
                           #下面这种情况是该行不包含网页标记     
                            else:
                                #因为这一行可能包含转义字符，所以调用ZhuanyiTrans类的zhuanyi()对文本进行查找转义字符和翻译的工作
                                print("对不包含网页标记的内容进行转义查找和翻译-%-")                                
                                trans=zhuan_obj.zhuanyi(after_raw) 
                                result=before_raw+'='+trans+'\n'
                                #将=前的内容、=和=后的内容拼接在一起，结尾加上换行符，写入文件
                                f.write(result)#写入文件
        print("-"*36)
        print("文件翻译完成！")                        

    g.close()
    f.close()
    #关闭文件
    
