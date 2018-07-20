---
title: 期末个人项目说明
tags: 期末个人项目,正则表达式,机器翻译
grammar_cjkRuby: true
---

# 期末个人项目说明

**作者：** 许逸文

**项目说明：**
本项目为期末个人项目，由个人完成，用 python 语言将LocaleResource_en_US.properties 文件用正则表达式和机器翻译API处理，翻译生成语言为中文的结果文件 LocaleResource_zh_CN.properties。

**项目构成：** 
本项目包含5个代码文件：4个类和1个主程序。  待处理文件为 LocaleResource_en_US.properties。处理后的文件为 LocaleResource_zh_CN.properties 。
在运行时请将5个代码文件和待处理文件放在同一个文件夹下，打开 main.py 运行即可。  

**项目特色：**

 1. 设计差错处理机制，当百度机器翻译API出错或失效时，系统自动调用必应机器翻译API。提高了系统的稳定性。
 2. 将不同的功能封装在不同的类中。主程序中引入这些类运行，使主程序更清晰简洁，同时代码的复用可能性大大提高
 3. 绘制了程序处理流程思维导图，使程序更易理解，同时提高代码的复用可能性。  

	
**具体文件说明：**

| 文件名称       | 说明                           |
| -------------- | ------------------------------ |
| main.py        | 主程序                         |
| preparation.py | 准备处理类（Preparation）      |
| baidu_trans.py | 百度翻译类（BaiduTranslation） |
| bing_trans.py  | 必应翻译类（BingTranslation）  |
| zhuanyi.py     | 转义处理类（ZhuanyiTrans）  |

**程序处理流程**
![文件处理流程思维导图](./images/文件处理流程思维导图.svg)

大图请见《文件处理流程思维导图》