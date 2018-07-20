# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 21:51:00 2018

@author: 许逸文
"""

class Preparation:
    """
    @function: 该类用于对文本进行设置，将文本转化为raw_string，方便程序处理转义字符
    
    
    """
    def raw(self,text):  
    #将每个可能的转义字符都进行了替换
        """
        @function: 替换转义字符变为raw string的形式，使之可以作为字符被后面的程序识别，并进行处理
        @input param: text 字符串，待处理的文本
        @output param: new_string 字符串，处理后的文本       
        """
        esscape_dict={'\:':r'\:',
                     '\n':r'\n',
                     '\!':r'\!',
                     '\=':r'\=',
                     '\\\,':r"\\\,",
                     '\<':r'\<',
                     '\>':r'\>',
                     '\&':r'\&',
                     '\#':r'\#',
                     '\:':r'\:',
                     '\\n':r'\\n'}
        #观察目标文件，将所有涉及到的需要处理的转义字符放到字典里。键是原来的值，值是替换的值
        new_string=''
        for char in text[0:-1]:
            #遍历字符串，但是只遍历到倒数第二个字符前，因为最后两个字符是\n，所以先不处理最后这个换行符
         
           try:
               new_string=new_string+esscape_dict[char]
               #如果有字典里的键，则替换为值
               #print('这里改变了',new_string)
           except KeyError:
               #如果出错，也就是这行文本没有字典中的键，则直接加到new_string中
               new_string+=char
        '''
        if text[-2:]=='\n':
            print('你好',char)
        '''
        new_string+='\n'#在字符串的最后加上\n换行符
        return new_string#返回处理好的字符串
        
