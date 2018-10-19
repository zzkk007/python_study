"-------------------------------------------------------"

					Django 课程

"-------------------------------------------------------"

MVC框架：

	MVC 全名是Model View Controller,是模型(model)-视图(view)-控制器(controller)的缩写。
	一种软件设计典范，用一种业务逻辑，数据，界面显示分离的方法组织代码，将业务逻辑聚集
	到一个部件里面，在改进和个性化定制界面及用户交互的同时，不需要重新编写业务逻辑。

	大部分开发语言都有MVC框架

	MVC框架的核心思想是：解耦

	降低各功能模块之间的耦合性，方便变更，更容易重构代码，最大程度上实现代码的重用。

	M 表示model，主要用于对数据库的封装

	V 表示view,用于向用户展示结果

	C 表controller,是核心，用户处理请求，获取数据，返回结果。

MTV:
	
	M 表示model,与MVC中的M功能相同，负责和数据库交互，进行数据处理

	V 表示view, 与MVC中的C功能相同，接收请求，进行业务处理，返回应答

	T 表示template,与MVC中的V功能相同，负责封装构造要返回的html。


python虚拟环境管理：pyvenv、pyenv、virtualenv:


1、使用虚拟环境的原因：
		
	在使用python开发的过程中，工程一多，难免会碰到不同的工程依赖不同版本的库的问题；
	亦或者是在开发过程中不想让物理环境里充斥各种各样的库，引发未来的依赖灾难。
	此时，我们需要对于不同的工程使用不同的虚拟环境来保持开发环境以及系统环境的清洁。

2、virtualenv:

	virtualenv,一个可以帮助我们管理不同Python环境的工具，virtualenv可以在系统中
	建立多个不同并且互不干扰的虚拟环境。另外，值得一提的是，在 virtualenv 的虚拟环境中
	使用 pip 安装依赖还可以绕过某些系统的权限设置，因为不需要向系统目录写入数据。

	1. virtualenv 通过创建独立python开发及运行环境个工具，来解决依赖、版本以及间接权限问题
	
		解决库之间的版本依赖，比如同一个系统上不同应用依赖同一个库的不同版本。
		解决权限限制，比如没有root权限。
		套件升级不影响其他应用。


	2. 安装virtualenv:

		virtualenv 实际上是一个python包，可以使用pip安装

		pip install virtualenv

	3. 使用virtualenv

		为工程创建一个虚拟环境

		virtualenv [OPTIONS] DEST_DIR

			例如：virtualenv venv

			virtualenv venv 将会在当前的目录中创建一个文件夹，实际上就是将Python环境克隆了一份
			包括Python解释器，setuptools,pip,wheel以及python标准库。

		options:

			(1) -p PYTHON, --=PYTHON 可以指定一个Python解释器

				$ virtualenv -p /usr/bin/python2.7.5  venv
			
			(2) 是否集成global python的库

				virtualenv --system-site-packages  venv

			(3) --always-copy 复制库文件，而不是建立python库文件的syslink

			(4) --no-setuptools 在创建的虚拟环境中不安装setuptools

			(5) --no-pip 在虚拟环境中不安装pip

			(6) --no-wheel 在虚拟环境中不安装wheel

			(7) --prompt=PROMPT 定义隔离环境的命令行前缀。

		创建虚拟环境venv后， 在这个目录下面会有三个目录被建立: bin, lib, include。

		bin 目录中包含一些在这个虚拟环境中可用的命令，以及激活虚拟环境的脚本activate,
		bin/python 是在当前环境的python解释器。

		lib/include 中是一些依赖库文件，所有安装的python库都会放在这个目录中的
		lib/pythonx.x/site-packages/目录中。

		使用虚拟环境，需要先激活虚拟环境：$source venv/bin/activate

		如果暂时不用python虚拟环境，可以关闭： $deactivate

		要删除一个虚拟环境，只需删除它的文件夹：$rm -rf venv


	4. pyenv:

		pyenv 是第三方的、开源的多版本python管理工具，用以管理在一台机器上多个Python发行版本的共存问题，
		比如一台Linux机器上同时安装Python2.7、Python3.4、Python3.5三个版本的管理；

		
	5.pyvenv:

		pyvenv模块是Python3.3之后标准库自带的虚拟环境创建和管理工具，
		在一定程度上能够替代virtualenv。但venv是Python3.3才有的，Python2.X不能使用，
		而virtualenv同时支持Python2.X和Python3.X，特别是在当前的生产环境中Python2.X
		还占有很大比例的情况下我们依然需要virtualenv。
		

Python 包管理工具解惑：

	1、下面包管理工具有什么不同：

		distutils : distutils是python标准库的一部分，2000年发布，使用它能够进行python模块的安装和发布。
					setup.py就是利用distutils的功能写成的。要安装一个模块到当前的python环境中，可以使用
					模块提供的setup.py文件：

						python setup.py install

					下面的代码会发布一个python模块，将其打包成tar.gz或者zip压缩包：
						
						python setup.py sdist

					甚至能打包成rpm或者exe安装包：

						python setup.py bdist_rpm
						python setup.py bdist_wininst
		
		setuptools: setuptools 是一个为了增强distutils而开发的集合，2004年发布，它包含了
					easy_install 这个工具。

					ez_setup.py 是setuptools的安装工具。ez就是easy的缩写。

					简单的说，setuptools是一个项目的名称，是基础组件，easy_install是这个
					组件的工具，它依赖基础组件工作。

					为了方便描述，下面文章中提到的 setuptools 被认为与 easy_install 同义。

					例如：从PyPI 上安装一个包

						esay_instakk SQLObject

					下载一个包文件，然后安装它
						
						easy_install http://example.com/path/to/MyPackage-1.2.3.tgz

		distribute: distribute是setuptools的一个分支版本。
					分支的原因可能是有一部分开发者认为 setuptools 开发太慢了。
					但现在，distribute 又合并回了 setuptools 中。
					因此，我们可以认为它们是同一个东西。事实上，
					如果你查看一下 easy_install 的版本，会发现它本质上就是 distribute

					# easy_install --version
					distribute 0.6.28

		Eggs：Eggs 格式是setuptools引入的一种文件格式，它使用.egg扩展名，
					用于Python模块的安装，setuptools 可以识别这种格式。并解析它，安装它。

		pip:  注意，从此处开始，easy_install 和 setuptools 不再同义。

			 pip 是目前python包管理的事实标准，2008年发布，它被用作是easy_install的替代品
			 但是它仍有大量的功能建立在setuptools组件上。

			 pip 希望不再使用 Eggs 格式（虽然它支持 Eggs），而更希望采用"源码发行版"
			 （使用 python setup.py sdist 创建）。这可以充分利用 Requirements File Format 提供的方便功能。

			 pip 支持 git/svn/hg 等流行的 VCS 系统，可以直接从 gz 或者 zip 压缩包安装，
			 支持搜索包，以及指定服务器安装等等功能。

		wheel: wheel 本质上是一个zip包格式，它使用.whl扩展名，用于python模块的安装，
				它的出现是为了替代eggs。

				wheel 还提供了一个bdist_wheel作为setuptools的扩展命令，这个命令可以用来生成wheel包。
				pip 提供了一个wheel子命令来安装wheel包。当然，需要先安装wheel模块。
				setup.cfg 可以用来定义 wheel 打包时候的相关信息。
				Wheel vs Egg 详细介绍了 wheel 和 Eggs 格式的区别，很显然，wheel 优势明显。
				Python Wheels 网站展示了使用 Wheels 发行的 python 模块在 PyPI 上的占有率。
				pypip.in 也支持 wheel。

		
		distutils2 和 distlib：
				
				distutils2 被设计为 distutils 的替代品。
				从2009年开发到2012年。它包含更多的功能，并希望以 packaging 作为名称进入 python 3.3 
				成为标准库的一部分。但这个计划 后来停滞了 。

				distlib 是 distutils2 的部分，它为 distutils2/packaging 
				提供的低级功能增加高级 API，使其便于使用。

				这里 介绍了 distlib 没有进入 python 3.3 标准库的一些原因。
				因此，可以暂时不必了解这两个工具，静观其变即可。
	
	2、什么时候该用pip，什么时候该用 setup.py ，它们有关系么？
		
	3、easy_install、ez_setup.py、setup.py、setup.cfg 分别都是干啥的？
	
	4、wheel 和 pip 的关系？
		
	5、Egg 和 whl 的关系？
		
	6、如何发布自己的模块（发布到PyPI）？
		
	7、如何进行模块的私有发布（不发布到PyPI）？


"------------------------------------------------------------"

1、创建项目：

	命令:diango-admin startproject mysite

	进入mysite目录，目录结构如下：

		manage.py
		mysite
			__init__.py
			settings.py
			urls.py
			wsgi.py

	manage.py : 一个命令行工具，可以使你多种方式对Django项目进行交互。
	内层的目录：项目真正的python包。
		__init__.py: 一个空文件，它告诉Python这个目录应该被看做一个Python包。
		settings.py: 项目的配置。
		urls.py: 项目的URL声明,就像你网站的"目录"。
		wsgi.py: 项目与WSGI兼容的Web服务器入口。

2、用于开发的简易服务器：

	让我们来确认一下你的Django项目是否真的创建成功了，我们切换到外层的mysite目录下:
	然后运行下面的命令:

		$ python manage.py runserver

	你应该会看到如下的输出:
	
		Performing system checks...

		System check identified no issues (0 silenced).

		You have unapplied migrations; your app may not work properly until they are applied.
		Run 'python manage.py migrate' to apply them.
		
		八月 01, 2018 - 15:50:53
		Django version 2.0, using settings 'mysite.settings'
		Starting development server at http://127.0.0.1:8000/
		Quit the server with CONTROL-C.

	刚刚启动的是Django自带的用于开发的简易服务器，它是一个用纯python写的轻量级服务器。
	我们将这个服务器内置在Django中是为了让你能够快速的开发出想要的东西，因为你不需要
	配置生产级别的服务器(比如Apache)方面的工作，除非你已经准备好投入生产环境了。

	现在是个提醒你的好时机：千万不要 将这个服务器用于和生产环境相关的任何地方。
	这个服务器只是为了开发而设计的。(我们在 Web 框架方面是专家，在 Web 服务器方面并不是。)

	现在，服务器正在运行，浏览器访问 https://127.0.0.1:8000/。你将会看到一个"祝贺"页面，
	随着一只火箭发射，服务器已经运行了。


	更换端口:

		默认情况下，runserver命令会将服务器设置为监听本机内部 ip 的 8000 端口。

		如果你想更换服务器的监听端口，请使用命令行参数，举例，下面的服务器监听8080端口

			$ python $ python manage.py runserver 8080

		如果你想要修改服务器监听的IP，在端口之前输入新的。比如，为了监听所有服务器的公开IP
			
			$ python manage.py runserver 0:8000

			0 是 0.0.0.0 的简写

			并且在项目的settings.py配置文件中设置访问ip:ALLOWED_HOSTS = ['*']


3、创建投票应用：

	现在你的开发环境 -- 这个"项目"已经配置好了，可以干活了。

	在Django中，每一个应用都是一个python包，并且遵循着相同的约定，
	Django 自带一个工具，可以帮你生成应用的基础目录结构，这样你就可以
	专心写代码，而不是创建目录。

	项目 VS 应用：

		项目和应用有啥区别? 应用是一个专门做某件事的网络应用程序--比如博客系统
		或者公共记录的数据库，或者简单的投票程序。
		项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用。

	你的应用可以存放在任何 Python path 中定义的路径。
	在这个教程中，我们将在你的 manage.py 同级目录下创建投票应用。
	这样它就可以作为顶级模块导入，而不是 mysite 的子模块。

	在处于manage.py所在的目录下，然后运行下面命令来创建一个应用：

		$ python manage.py startapp polls

	这将会创建一个polls目录，它的目录结构大致如下：

		polls/
			__init__.py
			admin.py
			apps.py
			migrations/
					__init__.py
			models.py
			tests.py
			views.py
	
	这个目录结构包括了投票应用的全部内容。

4、编写第一个视图：

	让我们开始编写第一个视图，打开polls/views.py,把下面这些Python代码输入进去:

		polls/views.py
		
		from diango.http import HttpResponse
		def index(request):
			return HttpResponse("Hello,world,You're at the polls index.")
	
	这是Django 中最简单的视图，如果想看见效果，我们需要将一个URL映射它
	这是我们需要URLconf的原因了。为了创建URLconf,请在polls目录里新建
	一个urls.py文件。你应该目录现在看起来应该是这样的：

		polls/
			__init__.py
			admin.py
			apps.py
			migrations/
				__init__.py
			models.py
			tests.py
			urls.py
			views.py

	在polls/urls.py 中，输入如下代码：
		polls/urls.py

		from django.urls import path
		from . import views

		urlpatterns = [
			path('',views.index,name = 'index'),
		]	

	下一步是要根URLconf 文件中指定我们创建的polls.urls模块。
	在mysite/urls.py 文件的urlpatterns列表里插入一个include(),如下：

		mysite/urls.py

		from django.contrib import admin
		from django.urls import incluide,path

		urlpatterns = [
			path('polls/',include('polls.urls')),
			path('admin/',admin.site.urls),
		]

	函数include()允许引用其他的URLconfs。每当Django遇到：func:~django.urls.include时
	它会截断与此项匹配的URL部分，并将剩余的字符串发送到URLconf以供进一步的处理。

	我们设计include()的理念是使其可以即插即用，因为投票应用有它自己的URLconf(polls.urls)
	他们能够放在"/polls/","/fun_polls","/content/polls" 或者其他任何路径下都嫩够正常工作。

		何时使用include()
		当包括其它URL模式时你应该总是使用include(),admin.site.urls是唯一例外。

	你想在把index 视图添加进URLconf，可以验证是否正常工作，运行下面命令：

		$python manage.py runserver

	你用浏览器访问:http://localhost:8000/polls/，你应该可以看到"Hello, world. You're at the polls index."，
	这是你在 index 视图中定义的。

	如果我们浏览器访问:http://localhost:8000，你应该可以看到如下情况：

		Page not found (404)
		Request Method:		GET
		Request URL:	http://172.25.16.226:8000/
		
		Using the URLconf defined in mysite.urls, Django tried these URL patterns, in this order:

			1. admin/
			2. polls/

		The empty path didn't match any of these.
				
		You're seeing this error because you have DEBUG = True in your Django settings file.
		Change that to False, and Django will display a standard 404 page.
			

	函数path()具有四个参数，两个必须参数：route 和 view 两个可选参数：kwargs 和 name。

		path()参数：route

			route 是一个匹配URL的准则(类似正则表达式)。当Django响应一个请求时
			它会从urlpatterns的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项。

			这些准则不会匹配 GET 和 POST 参数或域名。
			例如，URLconf 在处理请求 https://www.example.com/myapp/ 时，它会尝试匹配 myapp/ 。
			处理请求 https://www.example.com/myapp/?page=3 时，也只会尝试匹配 myapp/。

		path()参数：view

			当Django找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个HttpRequest
			对象作为第一个参数，被"捕获"的参数以关键字参数的形式传入。

		path()参数：kwargs

			任意个关键字参数可以作为一个字典传递给目标视图函数。

		path()参数：name

			为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。
			这个有用的特性允许你只改一个文件就能全局地修改某个 URL 模式.
			
	
"---------------------------------------------------------------------------"

我们将建立数据库，创建您的第一个模型，并关注Django提供的自动生成的管理页面。

数据库配置：

	现在，打开mysite/settings.py。这是个包含了Django项目设置的Python模块。

	通常，这个配置文件使用SQLite作为默认数据库，Python内置了SQLite,所以
	你无需安装额外的东西就可以使用它，当你开始一个真正的项目的时候，你
	可能使用一个更具扩展性的数据库，例如 PostgreSQL，
	避免中途切换数据库这个令人头疼的问题。

	如果你想使用其他数据库，你需要安装合适的 database bindings，
	然后改变设置文件中 DATABASES 'default' 项目中的一些键值：

		DATABASES = {	
			
			'default': {
					'ENGINE': 'django.db.backends.sqlite3',
					'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
				}
			}

	ENGINE -- 可选值有:

		'django.db.backends.sqlite3','django.db.backends.postgresql',
		'django.db.backends.mysql'和'django.db.backends.oracle'。

	NAME--数据库名称。如果使用的是SQLite，数据库将是你电脑上的一个文件，在这种情况下，
	NAME应该是此文件的绝对路径，包括文件名。默认值os.path.join(BASE_DIR,'db.sqlite3')
	将会把数据库文件储存在项目的根目录。

	如果你不使用SQLite，则必须添加一些额外的设置，比如USER、PASSWORD、HOST等等。
	如果你使用了 SQLite 以外的数据库，请确认在使用前已经创建了数据库。
	你可以通过在你的数据库交互式命令行中使用 "CREATE DATABASE database_name;" 命令来完成这件事。
	另外，还要确保该数据库用户中提供 mysite/settings.py 具有 "create database" 权限。
	这使得自动创建的 test database 能被以后的教程使用。
	如果你使用SQLite，那么你不需要在使用前做任何事——数据库会在需要的时候自动创建。

	编辑mysite/settings.py文件前，先设置TIME_ZONE为你自己时区。

	此外，关注一下settings.py 头部文件的INSTALLED_APPS设置项。
	这里包括了会在你项目中启用的所有Django应用。应用能在多个项目中使用，
	你也可以打包并且发布应用，让别人使用。

	通常，INSTALLED_APPS默认包括了一下Django的自带应用：

		django.contrib.admin  管理员站点
		django.contrib.auth   认证授权系统
		django.contrib.contenttypes 内容类型框架
		django.contrib.sessions  会话框架
		django.contrib.messages  消息框架
		django.contrib.staticfiles 管理静态文件的框架

	这些应用被默认启用是为了给常规项目提供方便。

	默认开启的某些应用需要至少一个数据表，所以在使用之前需要在数据库中创建一些表，执行下面命令：

		$python manage.py migrate

	这个migrate命令检查INSTALLED_APPS设置，为其中每个应用创建需要的数据表，至于具体会创建什么
	这取决于你的mysite/setting.py设置文件和每个应用的数据库迁移文件。
	这个命令执行的每个迁移操作都会在终端中显示出来，如果你感兴趣的话
	运行你数据库的命令行工具，并输入 \dt (PostgreSQL)， 
	SHOW TABLES; (MySQL)， .schema (SQLite)或者 
	SELECT TABLE_NAME FROM USER_TABLES; (Oracle) 来看看 Django 到底创建了哪些表。

	就像之前说的，为了方便大多数项目，我们默认激活了一些应用，但并不是每个人都需要它们。
	如果你不需要某个或某些应用，你可以在运行 migrate 前毫无顾虑地从 INSTALLED_APPS 里注释或者删除掉它们。 
	migrate 命令只会为在 INSTALLED_APPS 里声明了的应用进行数据库迁移。


创建模型：

	在Django里写一个数据库驱动的Web应用的第一步是定义模型--也就是数据库结构设计和附加的其它元数据。

		模型是真实数据的简单明确的描述，它包含了储存的数据所必须的字段和行为。
		Django 遵守DRY Principle。它的目标是你只需要定义数据类型，然后其他的
		杂七杂八的代码你都不需要关心，它们会自动从模型生成。

		Django 的迁移代码时由你的模型文件自动生成的，它本质上只是个历史记录，
		Django 可以用它来进行数据库的滚动更新，通过这种方式使其能够和当前的
		模式匹配。

	
	在简单的投票系统中，需要创建两个模型：问题Question 和选项 Choice.
	Question模型包括问题描述和发布时间。Choice 模型有两个字段，选项
	描述和当前得票数。每个选项属于一个问题。

	这些概念可以通过一个简单的Python类来描述。按照下面的例子来编辑polls/models.py文件。

		polls/models.py:

		from django.db import models

		class Question(models.Model):
			question_text = models.CharField(max_length=200)
			pub_date = models.DateTimeField('date published')

		class Choice(models.Model):
			question = models.ForeignKey(Question,on_delete=models.CASCADE)
			choice_text = models.CharField(max_length=200)
			votes = models.IntegerField(default=0)

	代码非常直白。每个模型被表示为 django.db.models.Model 类的子类。
	每个模型有一些类变量，它们都表示模型里的一个数据库字段。



	


			
	
	



	


	



























