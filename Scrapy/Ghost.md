"------------------------------------------------------"

			Ghost.py

"------------------------------------------------------"

1、安装Ghost.py工具：

	1. 安装pyside环境:
		#apt-get install build-essential cmake libqt4-dev libxml2-dev libxslt1-dev python-dev qtmobility-dev
	2.  安装pyside

		apt-get install python-pyside
		apt-get install xvfb
		#pip install pyside
		pip install flask

	3. 安装Ghost

		pip install Ghost.py

2、如果使用Ghost.py来保存网页的图片，会出现乱码，需要导入windows字体。

	1、copy windows上的中文字体，在C:\Windows\Fonts目录下

	2、我们就可以使用fc-list命令查看系统中已经安装的字体

		mkdir /usr/share/fonts/chinese
		chomd 775 /usr/share/fonts/chinese
		cp windows字体 /usr/share/fonts/chinese 目录下
		然后建立字体索引信息，更新字体缓存，使用如下命令：
		cd /usr/share/fonts/
		mkfontscale
		mkfontdir
		fc-cache

3、编写代码(版本0.2.3)：

	#!/bin/python
	#_*_coding:utf-8_*_

	from ghost import Ghost, Session
	gh = Ghost() 
	se = Session(gh, display = True)
	se.open("http://www.ytpp.com.cn/data/2018/2018-10-17/53074.html")
	se.capture_to("/home/zhangkun/444.png")
	
4、上面这个功能其实可以用Selenium来实现，一样的都有webkit

	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	driver = webdriver.PhantomJS()
	driver.get("http://www.ytpp.com.cn/data/2018/2018-10-17/53074.html")
	print driver.title
	driver.save_screenshot("test001.png")
	driver.quit()




