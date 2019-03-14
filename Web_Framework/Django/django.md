#Django 学习笔记  
##环境安装  
### 我在安装环境的时候遇到了一些问题  
####1、linux（debian）系统上python版本混乱问题
当我在虚拟机中安装好Django，运行命令 python manage.py test，出现如下错误
raise ImproperlyConfigured("Error loading either pysqlite2 or sqlite3 modules (tried in that order): %s" % exc)
django.core.exceptions.ImproperlyConfigured: Error loading either pysqlite2 or sqlite3 modules
为了解决这个问题，在系统上安装 libsqlite3-dev  
执行命令apt-get install libsqlite3-dev，出现如下错误
执行命令apt-get install libsqlite3-dev，出现如下错误：  
root@debian:/usr/local/Python-2.7.14/bin/ENV2.7/bin/test0504# apt-get install libsqlite3-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
libsqlite3-dev is already the newest version.
You might want to run 'apt-get -f install' to correct these:
The following packages have unmet dependencies:
 python-pkg-resources : Depends: python (>= 2.6) but it is not going to be installed
                         Depends: python (< 2.8) but it is not going to be installed
						 E: Unmet dependencies. Try 'apt-get -f install' with no packages
用dpkg命令看系统上安装的python版本，dpkg -l|grep python 如下   
572:ii  libpython3.2          3.2.3-7+deb7u1    amd64 
964:pF  python-minimal        2.7.3-4+deb7u1    all   
965:rF  python-pkg-resources  0.6.24-1          all   
966:pc  python2.6-minimal     2.6.8-1.1+deb7u1  amd64 
967:iU  python2.7             2.7.3-6+deb7u4    amd64 
968:iF  python2.7-minimal     2.7.3-6+deb7u4    amd64 
969:ii  python3               3.2.3-6           all   
970:ii  python3-dev           3.2.3-6           all   
971:ii  python3-minimal       3.2.3-6           all   
972:ii  python3-pip           1.1-3             all   
973:ii  python3-pkg-resources 0.6.24-1          all   
974:ii  python3-setuptools    0.6.24-1          all   
975:ii  python3.2             3.2.3-7+deb7u1    amd64 
976:ii  python3.2-dev         3.2.3-7+deb7u1    amd64 
977:ii  python3.2-minimal     3.2.3-7+deb7u1    amd64   
由于在系统上频繁的安装卸载不同的版本，导致一些文件产生相互依赖，很难处理，记住一条原则，宁装不卸载。


####2、django.db.utils.NotSupportedError: URIs not supported
当运行python3 manage.py runserver 命令时出现django.db.utils.NotSupportedError: URIs not supported错误，在google上搜了好久，有的说django和python的版本不兼容问题，我用的是python3.6，django是2.0.5，版本是兼容的，但是这个问题还是没有解决，不知道谁知道这个问题的答案，求教！！


####3、pip工具
我在debian系统上安装了一个python3.6,在用命令安装django时报错，错误信息如下：
pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.  
解决办法如下：
首先安装 openssl-devel      apt-get install  libssl-dev
从新编译并且安装python  
./configure --with-ssl 
make
make install
可能还需要升级一下pip的版本。 


####4、浏览器访问Django被拒  
创建一个Django项目之后，用浏览器访问的时候为拒，需要使用命令  
python manage.py runserver 0:8000 启动端口，并且在项目的settings.py配置文件中设置访问ip:  
ALLOWED_HOSTS = ['*']  
设置过之后就可以访问了。



##编写你的第一个 Django 应用
通过https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial01/
通过这个教程，创建一个基本的投票应用程序。
代码见django-polls.tar




