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
		Django 可以用它来进行数据库的滚动更新，通过这种方式使其能够和当前的模式匹配。

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
	
	每个字段都是 Field 类的实例 - 比如，字符字段被表示为 CharField ，日期时间字段被表示为 DateTimeField 。
	这将告诉 Django 每个字段要处理的数据类型。

	每个Field类实例变量的名字(question_text或pub_date)也是字段名，所以最好使用对机器友好的格式。

	定义某些 Field 类实例需要参数。例如 CharField 需要一个 max_length 参数。
	这个参数的用处不止于用来定义数据库结构，也用于验证数据，我们稍后将会看到这方面的内容。

	注意在最后，我们使用 ForeignKey 定义了一个关系。这将告诉 Django，每个 Choice 对象都关联到一个 Question 对象。
	Django 支持所有常用的数据库关系：多对一、多对多和一对一。


激活模块：
	
	上面的一小段用于创建模型的代码给了Django很多信息，通过这些信息，Django可以：

		1、为这个应用创建数据库 schema(生成 CREATE TABLE语句)
		2、创建可以与Question 和 Choice 对象进行交互的Python 数据库API。

	但是，首先得把polls应用安装到我们的项目里。

		设计哲学
		Django 应用是“可插拔”的。你可以在多个项目中使用同一个应用。除此之外，你还可以发布自己的应用，
		因为它们并不会被绑定到当前安装的 Django 上。

	为了在我们的工程中包含这个应用，我们需要在配置类INSTALLED_APPS中添加设置。
	因为PollsConfig类写在文件polls/apps.py中,所以它的点式路径是'polls.apps.PollsConfig'。
	在文件mysite/settings.py中INSTALLED_APPS子项添加点式路径后，它看起来是这样的：

		mysite/settings.py

		INSTALLED_APPS =[
			
		'polls.apps.PollsConfig',
		'django.confib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles',	
		]
	
	现在你的Django项目会包含polls应用，接着运行下面的命令：

		$python manage.py makemigrations polls

	你讲会看到类似于下面这样的输出：

		Migrations for 'polls':
			polls/migrations/001_initial.py:
				- Create model Choice
				- Create model Question
				- Add field question to choice

	通过运行makemigrations命令，Django会检测你对模型文件的修改
	(在这种情况下，你已经取得了新的)，并且把修改的部分存储为一次迁移。

	迁移是Django对模型定义(也就是你的数据库结构)的变化的储存形式-没那么玄乎。
	它们其实也只是一些你磁盘上的文件，如果你想的话，你可以阅读一下你模型的迁移数据，
	它被储存在 polls/migrations/0001_initial.py 里。别担心，你不需要每次都阅读迁移文件，
	但是它们被设计成人类可读的形式，这是为了便于你手动修改它们。

	Django 有一个自动执行数据库迁移并同步管理你的数据库结构的命令--这个命令就是migrate,
	我们马上就会接触它，但是首先，让我们看看迁移命令会执行哪些 SQL 语句。
	sqlmigrate 命令接收一个迁移的名称，然后返回对应的 SQL：

		$python manage.py sqlmigrate polls 0001

	你将会看到类似下面这样的输出(我把输出重组成了人类可读的格式)：

		BEGIN;
		--
		-- Create model Choice
		--
		CREATE TABLE "polls_choice" (
			"id" serial NOT NULL PRIMARY KEY,
			"choice_text" varchar(200) NOT NULL,
			"votes" integer NOT NULL
			);
		--
		-- Create model Question
		--
		CREATE TABLE "polls_question" (
			"id" serial NOT NULL PRIMARY KEY,
			"question_text" varchar(200) NOT NULL,
			"pub_date" timestamp with time zone NOT NULL
			);
		--
		-- Add field question to choice
		--
		ALTER TABLE "polls_choice" ADD COLUMN "question_id" integer NOT NULL;
		ALTER TABLE "polls_choice" ALTER COLUMN "question_id" DROP DEFAULT;
		CREATE INDEX "polls_choice_7aa0f6ee" ON "polls_choice" ("question_id");
		ALTER TABLE "polls_choice"
		ADD CONSTRAINT "polls_choice_question_id_246c99a640fbbd72_fk_polls_question_id"
		FOREIGN KEY ("question_id")
		REFERENCES "polls_question" ("id")
		DEFERRABLE INITIALLY DEFERRED;

		COMMIT;
	

	请注意以下几点：

		输出的内容和你使用的数据有关，上面的输出示例使用的是PostgreSQL

		数据库的表名是由应用名(polls)和模型名的小写形式( question 和 choice)连接而来.

		主键(IDs)会被自动创建。(当然，你也可以自定义。)

		默认的，Django 会在外键字段名后追加字符串 "_id" 。

		外键关系由 FOREIGN KEY 生成。你不用关心 DEFERRABLE 部分，它只是告诉 PostgreSQL，
		请在事务全都执行完之后再创建外键关系。

		生成的 SQL 语句是为你所用的数据库定制的，所以那些和数据库有关的字段类型，
		比如 auto_increment (MySQL)、 serial (PostgreSQL)和 integer primary key autoincrement (SQLite)，
		Django 会帮你自动处理。那些和引号相关的事情 - 例如，是使用单引号还是双引号 - 也一样会被自动处理。

		这个 sqlmigrate 命令并没有真正在你的数据库中的执行迁移 - 它只是把命令输出到屏幕上，
		让你看看 Django 认为需要执行哪些 SQL 语句。这在你想看看 Django 到底准备做什么，
		或者当你是数据库管理员，需要写脚本来批量处理数据库时会很有用。

		如果你感兴趣，你也可以试试运行 python manage.py check ;这个命令帮助你检查项目中的问题，
		并且在检查过程中不会对数据库进行任何操作。
	
	现在，再次运行migrate命令，在数据库里创建新定义的模型的数据表：

		$Python manage.py migrate
		Operations	to perform:
			Apply all migrations:admin,auth,contenttypes,polls,sessions
		Running migrations:
			Rendering model states ... DONE
			Applying polls.001_inital ...  ok

	这个 migrate 命令选中所有还没有执行过的迁移
	（Django 通过在数据库中创建一个特殊的表 django_migrations 来跟踪执行过哪些迁移）并应用在数据库上 -
	也就是将你对模型的更改同步到数据库结构上。

	迁移是非常强大的功能，它能让你在开发过程中持续的改变数据库结构而不需要重新删除和创建表 
	- 它专注于使数据库平滑升级而不会丢失数据。我们会在后面的教程中更加深入的学习这部分内容，
	现在，你只需要记住，改变模型需要这三步：

		1、编辑models.py 文件，改变模型

		2、运行python manage.py makemigrations 为模型的改变生产迁移文件。

		3、运行python manage.py migrate 来应用数据库迁移。

	数据库迁移被分解成生成和应用两个命令是为了让你能够在代码控制系统上提交
	迁移数据库并使其能在多个应用里使用；这不仅仅会让开发更加简单，也给别的开发者和生产环境中的使用带来方便。

"-----------------------------------------------------------------------------"

初试 API：

	现在让我们进入交互式Python命令行，尝试一下Django为你创建各种API.通过以下命令打开
	Python命令行：

		$python manage.py shell

	我们使用这个命令而不是简单的使用"Python"是因为manage.py会设置DJANGO_SETTINGS_MODULE环境变量
	这个变量让Django根据mysite/settings.py文件来设置Python包的导入路径。

	当你成功进入命令后，来试试database API吧：
		
	>>> from polls.models import Choice, Question  # Import the model classes we just wrote.

	# No questions are in the system yet.
	>>> Question.objects.all()
		<QuerySet []>

	# Create a new Question.
	# Support for time zones is enabled in the default settings file, so
	# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
	# instead of datetime.datetime.now() and it will do the right thing.
	
	>>> from django.utils import timezone
	>>> q = Question(question_text="What's new?", pub_date=timezone.now())

	# Save the object into the database. You have to call save() explicitly.
	>>> q.save()

	# Now it has an ID.
	>>> q.id
	1

	# Access model field values via Python attributes.
	>>> q.question_text
	"What's new?"
	>>> q.pub_date
	datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

	# Change values by changing the attributes, then calling save().
	>>> q.question_text = "What's up?"
	>>> q.save()

	# objects.all() displays all the questions in the database.
	>>> Question.objects.all()
	<QuerySet [<Question: Question object (1)>]>

	<Question: Question object (1)> 对于我们了解这个对象的细节没什么帮助。
	让我们通过编辑 Question 模型的代码（位于 polls/models.py 中）来修复这个问题。
	给 Question 和 Choice 增加 __str__() 方法。

	polls/models.py
	from django.db import models
	
	class Question(models.Model):
		#...
		def __str__(self):
			return self.question_text

	class Choice(models.Model):
		#...
		def __str__(self):
			return self.choice_text

	给模型增加 __str__() 方法是很重要的，这不仅仅能给你在命令行里使用带来方便，
	Django 自动生成的 admin 里也使用这个方法来表示对象。

"----------------------------------------------------"

介绍Django 管理界面:

	设计哲学:
	
		为你的员工或客户生成一个用户添加，修改和删除内容的后台是一项缺乏创造性和乏味的工作。
		因此，Django 全自动地根据模型创建后台界面。

		Django 产生于一个公众页面和内容发布者页面完全分离的新闻类站点的开发过程中。
		站点管理人员使用管理系统来添加新闻、事件和体育时讯等，这些添加的内容被显示在公众页面上。
		Django 通过为站点管理人员创建统一的内容编辑界面解决了这个问题。

		管理界面不是为了网站的访问者，而是为管理者准备的。

	创建一个管理员账号：

		首先，我们得创建一个能登录管理页面的用户，请运行下面命令：
			$python manage.py createsuperuser

		键入你想要使用的用户名，然后按下回车键：
			Username: admin

		然后提示你输入想要使用的邮件地址：
			Email address: admin@example.com

		最后一步是输入密码。你会被要求输入两次密码，第二次的目的是为了确认第一次输入的确实是你想要的密码。

			Password: **********
			Password (again): *********
			Superuser created successfully.
	

	启动开发服务器：

		Django 的管理界面默认就是启用的，让我们启动开发服务器，看看它到底是什么样的。

		如果开发服务器未启动，用下面命令启动它：

			$python manage.py runserver

		现在，打开浏览器，转到你本地域名的 "/admin/" 目录， -- 比如 "http://127.0.0.1:8000/admin/" 。
		你应该会看见管理员登录界面：


	向管理页面中加入投票应用:

		但是我们的投票应用在哪呢？它没在索引页面里显示。

		只需要做一件事：我们得告诉管理页面，问题 Question 对象需要被管理。
		打开 polls/admin.py 文件，把它编辑成下面这样

		polls/admin.py
		from django.contrib import admin
		from .models import Question
		admin.site.register(Question)


"---------------------------------------------------------------------"

视图

概况：

	Django 中的视图的概念是[一类具有相同功能和模板的网页的集合]。比如，在一个博客应用中
	你可能会创建下面几种视图：

		1、博客首页--展示最近的几项内容。

		2、内容"详情"页--详细展示某项内容

		3、以年为单位的归档页——展示选中的年份里各个月份创建的内容。
		
		4、以月为单位的归档页——展示选中的月份里各天创建的内容。
		
		5、以天为单位的归档页——展示选中天里创建的所有内容。
		
		6、评论处理器——用于响应为一项内容添加评论的操作。

	而我们的投票应用中，我们需要下来几个视图：

		1、问题索引页--展示最近的几个投票问题。

		2、问题详情也--展示某个投票的问题和不带结果的选项列表

		3、问题结果页--展示某个投票结果

		4、投票处理器--用于响应用户为某个问题的特定选项投票的操作。

	在django中，网页和其他内容都是从视图派生而来。每一个视图表现为一个简单的python函数
	（或者说方法，如果是基于类的话）。Django将会根据用户的请求的URL来选择使用哪个视图
	（更准确的说，根据URL中域名之后的部分）

	为了将URL和视图关联起来，Django使用了'URLconfs'来配置。URLconf将URL模式映射到视图。

编写更多视图：
		
	现在我们想polls/views.py 里添加多视图，这些视图有些不同，因为他们接受参数：

		polls/views.py

		def detail(request,question_id):
			return HttpResponse("You're looking at question %s." % question_id)

		def results(request,question_id):
			response = "You're looking at the results of question %s."
			return HttpResponse(response % question_id)

		def vote(request,question_id):
			return HttpResponse("You're voting on question %s." question_id)

	把这些新视图添加polls.urls模块里，只要添加几个url()函数调用就行：

		polls/urls.py

		from django.urls import path

		form . import view

		urlpatterns = [
			
			path('',view.index,name = 'index'),

			path('<int:question_id>/',views.detail,name='detail').

			path('<int:question_id>/results/',view.results,name='results'),
			
			path('<int:question_id>/vote/',view.vote,name='vote'),
		]
	
	然后看看你的浏览器，如果你转到"/polls/34",Django将会运行detail()方法并且展示你在URL里
	提供的问题ID。再试试"/polls/34/vote"和"/polls/34/vote"你将会看到暂时用于占位的结果和投票页。

	当某人请求你的某一个网页时--比如说，"/polls/34/",Django将会载入mysite.urls模块，因为这在配置
	项ROOT_URLCONF中设置了。然后Django寻找名为urlpatterns变量并且按序匹配正则表达式。
	在找到匹配项"polls/"，它切掉了匹配的文本("polls/"),将剩余文本--"34/",发送至polls.urls，URLconf
	做进一步的处理，在这里剩余文本匹配了'<int:question_id>/',使得我们Django以如下的形式调用detail():

		detail(request=<HttpRequest object>,question_id=34)
	
	question_id=34 由<int:question_id>匹配生产，使用尖括号"捕获"这部分URL,且以关键字的形式
	发送给视图函数，上述字符串的 :question_id 部分定义了将被用于区分匹配模式的变量名，
	而 int: 则是一个转换器决定了应该以什么变量类型匹配这部分的 URL 路径。

	为每个 URL 加上不必要的东西，例如 .html ，是没有必要的。不过如果你非要加的话，也是可以的:
		path('polls/latest.html', views.index),
	但是，别这样做，这太傻了。
	

"---------------------------------------------------------------------------"

写一个真正有用的视图:

	每个视图必须要做的只有两件事:返回一个包含请求也内容的HttpResponse对象，
	或者抛出一个异常，比如Http404。至于你还想干什么，随便你。

	你的视图可以从数据库里读取记录，可以使用一个模板引擎(比如Django自带的，或者其他第三方)
	可以生产一个PDF文件，可以输出一个XML,创建一个ZIP文件，你可以想做任何事情，使用任何python库。

	Django 只要求返回的是一个HttpResponse，或者抛出一个异常。

	因为Django自带的数据库API 很方便，所以我们在视图里使用它，我们在index()函数里插入了一些新内容。
	让它能展示数据库里发布日期的最近5个投票问题，以空格分割：

		polls/views.py

		from django.http import HttpResponse

		form .models import Question

		def index(request):

			latest_question_list = Question.objects.order_by('-pub_date')[:5]
			output = ','.join([q.question_text for q in	latest_question_list])
			return HttpResponse(output)

	这里有一个问题：页面的设计是死在视图函数的代码里的，如果你想改变页面的样子，你需要编辑Python代码。
	所以我们使用Django的模板系统，只要创建一个视图，就可以将页面的设计从代码里分离出来。

	首先，在你的polls目录里创建一个template目录，Django将会在这个目录里查找模板文件。

	你项目的TEMPLATES配置项描述了Django如何载入和渲染模块。默认的设置文件设置了DjangoTemplates后端。
	并将APP_DIRS设置成了True,这一选项会让DjangoTemplates在每个INSTALLED_APPS文件夹中寻找"templates"
	子目录。这就是为什么尽管我们没有想在DIRS 设置，Django也能正确找到polls的模板位置的原因。

	在你刚刚创建的templates目录里，再创建一个目录polls,然后在其中创建一个文件index.html。
	换句话说，你的模板文件的路径应该是polls/templates/polls/index.html。因为Django会寻找到
	对应的app_directories,所以你只需要是用polls/index.html就可以引用到这一模块了。

	将下面的代码输入到刚刚创建的模板文件中：

		polls/templates/polls/index.html

		{% if latest_question_list %}
			<ul>
			{% for question in latest_question_list %}
				<li><a href="/polls/{{question.id }}/">{{question.question_text }}</a></li>
			{% endfor %}
			</ul>
		{% else %}
			<p>No polls are available.</p>
		{% endif %}

	然后，让我们更新一下 polls/views.py 里的 index 视图来使用模板：


		polls/views.py
		from django.http import HttpResponse
		from django.template import loader

		from .models import Question

		def index(request):
			latest_question_list = Question.objects.order_by('-pub_date')[:5]
			template = loader.get_template('polls/index.html')
			context = {
				'latest_question_list':latest_question_list,
			}
			return  HttpResponse(template.render(context, request))

	上述代码的作用是，载入polls/index.html模板文件，并且向它传递一个上下文(context).
	这个上下文是一个字典，它将模板内的变量映射为Python对象。
		

	一个快捷函数：render():

	[载入模板，填充上下文，再返回由它生产的HttpResponse对象]是一个非常常用的操作流程。
	于是Django提供了一个快捷函数，我们用它来重写index()视图：

	polls/view.py

	form django.shortcuts import render
	from .models import Question
	def index(request):
		latest_question_list = Question.objects.order_by('-pub_date')[:5]
		context = {'latest_question_list':latest_question_list}
		return render(request,'polls/index.html',context)

	注意到，我们不再需要导入 loader 和 HttpResponse 。
	不过如果你还有其他函数（比如说 detail, results, 和 vote ）需要用到它的话，
	就需要保持 HttpResponse 的导入。


抛出404错误：

	现在，我们来处理投票详情视图--它会显示指定投票的问题标题，下面是这个视图代码：

		polls/views.py

		form django.http import Http404
		from django.shortcuts import render

		from .models import Question

		def detail(request,question_id):
			try:
				question = Question.objects.get(pk=question_id)
			except Question.DoesNotExist:
				raise Http404("Question does not exist")
			return render(request, 'polls/detail.html', {'question': question})

	这里有个新原则。如果指定问题 ID 所对应的问题不存在，这个视图就会抛出一个 Http404 异常。
	我们稍后再讨论你需要在 polls/detail.html 里输入什么，
	但是如果你想试试上面这段代码是否正常工作的话，你可以暂时把下面这段输进去：

		polls/templates/polls/detail.html
		{{question }}

一个快捷函数： get_object_or_404():

	尝试用get()函数获取一个对象，如果对象不存在就抛出Http404错误也是一个普遍的流程。
	Django也提供了一个快捷函数，下面是修改后的detail()视图代码：

		polls/views.py
		from django.shortcuts import get_object_or_404,render

		from .models import Question

		def detail(request,question_id):
			question = get_object_or_404(Question,pk=question_id)
			return render(request, 'polls/detail.html', {'question': question})

	设计哲学

		为什么我们使用辅助函数 get_object_or_404() 而不是自己捕获 ObjectDoesNotExist 异常呢？
		还有，为什么模型 API 不直接抛出 ObjectDoesNotExist 而是抛出 Http404 呢？

		因为这样做会增加模型层和视图层的耦合性。指导 Django 设计的最重要的思想之一就是要保证松散耦合。
		一些受控的耦合将会被包含在 django.shortcuts 模块中。
					
		也有 get_list_or_404() 函数，工作原理和 get_object_or_404() 一样，
		除了 get() 函数被换成了 filter() 函数。如果列表为空的话会抛出 Http404 异常。	
			

使用模板系统：

	看我们的detail()视图，它像模板传递了上下文变量question。下面是polls/detail.html模板里正式的代码：

		polls/templates/polls/detail.html
		<h1>{{question.question_text }}</h1>
		<ul>
		{% for choice in question.choice_set.all %}
			<li>{{ choice.choice_text }}</li>
		{% endfor %}
		</ul>

	模板系统统一使用点符号来访问变量的属性。在示例 {{question.question_text }} 中，
	首先 Django 尝试对 question 对象使用字典查找（也就是使用 obj.get(str) 操作），
	如果失败了就尝试属性查找（也就是 obj.str 操作），结果是成功了。
	如果这一操作也失败的话，将会尝试列表查找（也就是 obj[int] 操作）。

	在 {% for %} 循环中发生的函数调用：question.choice_set.all 被解释为 Python 代码 
	question.choice_set.all() ，将会返回一个可迭代的 Choice 对象，这一对象可以在 {% for %} 标签内部使用。


去除模板中的硬编码 URL:

	我们在 polls/index.html 里编写投票链接时，链接是硬编码的：
		<li><a href="/polls/{{question.id }}/">{{question.question_text }}</a></li>

	问题在于，硬编码和强耦合的链接，对于一个包含很多应用的项目来说，修改起来十分困难。
	然而，因为你在polls.urls的url() 函数中通过name参数为URL定义了名字，你可以使用{% url %}标签来代替它。

		<li><a href="{% url 'detail' question.id %}">{{ question.question_text}}</a></li>

	这个标签的工作方式是在 polls.urls 模块的 URL 定义中寻具有指定名字的条目。
	你可以回忆一下，具有名字 'detail' 的 URL 是在如下语句中定义的:

		...

		# the 'name' value as called by the {% url %} template tag
		path('<int:question_id>/', views.detail, name='detail'),
		
		...
	

为URL名称添加命名空间：


	教程项目只有一个应用，polls 。在一个真实的 Django 项目中，可能会有五个，十个，二十个，
	甚至更多应用。Django 如何分辨重名的 URL 呢？举个例子，polls 应用有detail视图，
	可能另一个博客应用也有同名的视图。Django 如何知道 {% url %} 标签到底对应哪一个应用的 URL 呢？
	
	答案是：在根 URLconf 中添加命名空间。在 polls/urls.py 文件中稍作修改，加上 app_name 设置命名空间：

		polls/urls.py

		app_name = 'polls'
		urlpatterns = [
		    path('', views.index, name='index'),
			path('<int:question_id>/', views.detail, name='detail'),
			path('<int:question_id>/results/', views.results, name='results'),
			path('<int:question_id>/vote/', views.vote, name='vote'),
		]

	现在，编辑 polls/index.html 文件，从：

		polls/templates/polls/index.html
		<li><a href="{% url 'detail' question.id %}">{{question.question_text }}</a></li>

	修改为指向具有命名空间的详细视图：

		polls/templates/polls/index.html

		<li><a href="{% url 'polls:detail' question.id %}">{{question.question_text }}</a></li>
	


"-------------------------------------------------------------------------------------------"


ORM简介：

	MVC 框架中包括一个重要的部分，就是ORM,它实现了数据模型和数据库的解耦，
	即数据模型的设计不需要依赖特定的数据库，统计简单的配置就可以轻松更换数据库。

	ORM 是"对象--关系--映射"的简称，主要任务是：
		根据对象的类型生产表结构。
		将对象、列表的操作、转换成sql语句。
		将sql查询到的结果转换为对象、列表。

	这极大的减轻了开发人员的工作量，不需要面对因数据库变更而导致的无效的劳动。
	Django中的模型包含存储数据的字段和约束，对应着数据库中唯一的表。

		django(对象的增、删、改) ----> ORM(转换为特定数据库的 insert、delete、update)---> MySql

		diango(查)<--->ORM(转换为特定数据库的selete语句，从数据库中返回数据集再转换为python中的列表)--> Mysql


使用MySql 数据库：


	1、在虚拟环境中安装mysql包:

		pip install mysql-python

		pip install mysqlclient

		这里一定要注意mysqlclient版本和Django版本的兼容性，在
	
		pthon3 manage.py makemigrateions 时报：

			raise MigrationSchemaMissing("Unable to create the django_migrations table (%s)" % exc)
			django.db.migrations.exceptions.MigrationSchemaMissing: 
			Unable to create the django_migrations table ((1064, 
			"You have an error in your SQL syntax; check the manual that corresponds to your 
			MySQL server version for the right syntax to use near '(6) NOT NULL)' at line 1"))

	2、在mysql中创建数据库

		create databases test2 charset=utf8

	3、打开settings.py文件，修改DATABASES项

		DATABASES = {

			'default': {

				'ENGINE': 'django.db.backends.mysql',
				'NAME': 'test2',
				'USER': '用户名',
				'PASSWORD': '密码',
				'HOST': '数据库服务器ip，本地可以使用localhost',
				'PORT': '端口，默认为3306',
			}
		}

	4、执行命令，生成迁移文件，生成表

		python manage.py makemigrations
		python manage.py migrate
		
	5、使用数据库生成模型类
	
		 inspectdb 是Django 附带的一个实用程序，它可以通过现有的数据库来创建模型
		 运行以下命令来查看输出:

		 $python manage.py inspectdb
		

		 使用标准Unix输出重定向将其另存为文件：
		 $python manage.py inspectdb > booktest/models.py

		此功能用作快捷方式，而不是确定的模型生成。

	6、数据库中生成的表：

		auth_group
		auth_group_permissions
		auth_permission
		auth_user
		auth_user_groups
		auth_user_user_permissions
		booktest_bookinfo
		booktest_heroinfo
		django_admin_log
		django_content_type
		django_migrations
		django_session
		

	manage.py inspectdb 的内容是：


定义模型：

	在模型中定义属性，会生成表中的字段

	django根据属性的类型确定一下信息：
		当前现在的数据库支持字段的类型
		渲染管理表单时使用的默认html控件
		在管理站点最低限度的验证

	django 会为表增加自动增长的主键列，每个模型只能有一个主键列，
	如果使用选项设置某属性为主键列后，则django不会再生成默认的主键列。

	属性命名限制：
		不能是python的保留关键字
		由于django的查询方式，不允许使用连续的下划线。

定义属性：

	定义属性时，需要字段类型
	字段类型被定义在django.db.models.fields目录下，为了方便使用，被导入到django.db.models中
	使用方式：
		导入 from django.db import models。
		通过models.Field创建字段类型的对象，赋值给属性。
	
	对于重要数据都做逻辑删除，不做物理删除，实现方法是定义isDelete属性，类型为BooleanField,
	默认值为False。

	字段类型：
		
		AutoField: 一个根据实际ID自动增长的integerField,通常不指定，如果不指定，一个主键字段将自动添加到模型中。
		
		BooleanField: true/false字段，此字段的默认表单控制是Checkboxinput
		
		NullBooleanField: 支持null,true、false 三种值

		CharField(max_length=字段长度): 字符串，默认的表单样式是Textinput

		TextField: 大文本字段，一般超过4000使用，默认的表单控件是Textarea

		integerField:整数

		DecimalField(max_digits=None,decimal_places=None):使用python的Decimal实例表示的十进制浮点数
			DecimalField.max_digits: 位数总数
			DecimalField.decimal_places:小数点后面的数字

		FloatField：用python 的float实例来表示的浮点数。

		DateField[auto_now=False,auto_now_add=False]:使用python的datetime.date实例表示的日期
			参数DateField.auto_now:每次保存对象时，自动设置该字段当前时间，用于"最后一次修改"
			的时间戳，它总是使用当前日期，默认为flase
			参数DateField.auto_now_add：当对象第一次被创建时自动设置当前时间，用于创建的时间戳，
			它总是使用当前日期，默认为false
			该字段默认对应的表单控件是一个TextInput. 在管理员站点添加了一个JavaScript写的日历控件，
			和一个"Today"的快捷按钮，包含了一个额外的invalid_date错误消息键
			auto_now_add, auto_now, and default 这些设置是相互排斥的，他们之间的任何组合将会发生错误的结果
		
		TimeField: 使用Python的datetime.time实例表示的时间，参数同DateField

		DateTimeField:使用Python的datetime.datetime实例表示的日期和时间，参数同DateField

		FileField：一个上传文件的字段

		ImageField: 继承了FileField的所有属性和方法，但对上传的对象进行校验，确保它是个有效的image。

	字段选项:

		通过字段选项，可以实现对字段的约束
		在字段对象时通过关键字参数指定
		null:如果为True,Django将空值以NULL存储到数据库中，默认值是False
		blank:如果为True,则该字段允许为空白，默认值是False
		对比：null 是数据库范畴的概念，blank是表单验证范畴的
		db_column:字段的名称，如果未指定，则使用属性的名称
		db_index: 若值为True,则在表示会为此字段创建索引
		default:默认值
		primary_key:若为True,则改字段会成为模型的主键字段
		unique:如果为True,这个字段在表中必须是唯一值。

	关系：

		关系的类型包括：

			ForeignKey:一对多，将字段定义在多的端中
			ManyToManyField: 多对多，将字段定义在两端中
			OneToOneField: 一对一，将字段定义在任意一端中

		可以维护递归的关联关系，使用"self"指定，
		
		用一访问多：对象.模型类小写_set

			bookinfo.heroinfo_set

		用一访问一：对象.模型类小写

			heroinfo.bookinfo

		访问id:对象.属性_id

			heroinfo.book_id

元选项：

	在模型类中定义类Meta,用于设置元信息
	元信息db_table：定义数据表名称，推荐使用小写字母，数据表的默认名称

		<app_name>_<model_name>
	
	ordering:对象的默认排序字段，获取对象的列表时使用，接收属性构成的列表

		class BookInfo(models.Model)
			...
			class Meta():
				ordering = ['id']

	字符串前加-表示倒序，不加-表示正序

		class BookInfo(models.Model)
			...
			class Meta():
				ordering=['-id']

	排序会增加数据库开销。


示例演示：

	定义图书模型:

		class BookInfo(models.Model):
			btitle = models.CharField(max_length=20)
			bpub_date = models.DateTimeField()
			bread = models.IntegerField(default=0)
			bcommet = models.IntegerField(default=0)
			isDelete = models.BooleanField(default=False)

	英雄模型:

		class HeroInfo(models.Model):
			hname = models.CharField(max_length=20)
			hgender = models.BooleanField(default=True)
			isDelete = models.BooleanField(default=False)
			hcontent = models.CharField(max_length=100)
			hbook = models.ForeignKey('BookInfo')

	定义index、detail视图
	index.html,detail.html模板
	配置url,能够完成图书以及英雄的展示

	生成的数据库中的表如下：

		auth_group
		auth_group_permissions
		auth_permission
		auth_user
		auth_user_groups
		auth_user_user_permissions

		booktest_bookinfo
		booktest_heroinfo

		django_admin_log
		django_content_type
		django_migrations
		django_session


"------------------------------------"
		
类是属性：

	objects: 是Manager类型的对象，用于与数据库进行交互
	当定义模型类时没有指定管理器，则Django会为模型提供一个名为objects的管理器。
	支持明确指定模型类的管理器

		class BookInfo(models.Model):
			...
			books = models.Manager()

	当为模型类指定管理器之后，django不再为模型类生成名为objects的默认管理器。


管理器Manager:

	管理器是Django的模型进行数据库的查询操作的接口，Django应用的每个模型都拥有至少一个管理器。
	自定义管理器类主要用于两种情况：

		情况1：向管理器类中添加额外的方法:见下面"创建对象"中的方式二。
		情况2：修改管理器返回的原始查询集：重写get_queryset()方法。

		class BookInfoManager(models.Manager):
			def get_queryset(self):
				return super(BookInfoManager,self).get_queryset().filter(isDelete=False)

		class BookInfo(models.Model):
			...
			books = BookInfoManager()

创建对象:

	当创建对象时，django不会对数据库进行读写操作
	调用save()方法才与数据库交互，将对象保存到数据库中
	使用关键字参数构造模型对象很麻烦，推荐使用下面的两种方式
	说明：__init__ 方法已经在基类models.Model中使用，在自定义模型中无法使用，

	方式一: 在模型类中增加一个类方法

		class BookInfo(models.Model):
			...
			@classmethod
			def create(cls,title,pub_date):
				book = cls(btitle=titile,bpub_date=pub_date)
				book.bread=0
				book.bcomment=0
				book.isDelete=False
				return book
		
		引入时间包:from datetime import *
		调用：book = BookInfo.create("hello",datetine(1990,9,21));
		保存: book.save()

	方式二: 在自定义管理器中添加一个方法
	在给管理器的方法中，可以通过self.model来得到它所属的模型类

		class BookInfoManager(nodels.Manager):
			def create_book(self,title,pub_date):
				book = self.model()
				book.btitle = title
				book.bpub_date = pub_date
				book.bread=0
				book.bcommet=0
				book.isDelete = False
				return book

		class BookInfo(models.Model):
			...
			
			books= BookInfoManager()
		调用：book=BookInfo.books.create_book("abc",datetime(1980,1,1))
		保存：book.save()

	在方式二中，可以调用self.create()创建并保存对象，不需要再手动save()

		class BookInfoManager(models.Manager):
			def create_book(self, title, pub_date):
				book = self.create(btitle = title,bpub_date = pub_date,bread=0,bcommet=0,isDelete = False)
				return book

		class BookInfo(models.Model):
			...
			books = BookInfoManager()
		调用：book=Book.books.create_book("abc",datetime(1980,1,1))
		查看：book.pk


实例属性:

	DoesNotExist:在进行单个查询时，模型的对象不存在时会引发此异常，结合try/except使用。

实例的方法：

	str(self): 重写object方法，此方法在将对象转换成字符串时会被调用
	save() :将模型对象保存到数据库表中
	delete():将模型对象从数据表中删除

"-----------------------------------"

模型查询：

简介：

	查询集表示从数据库中获取的对象集合
	查询集可以包含有零个、一个或多个过滤器
	过滤器基于所给的参数限制查询的结果
	从SQL的角度，查询集合select语句等价，过滤器像where 和 limit字句。
	接下来主要讨论如下知识点：

		查询集
		字段查询：比较运算符、F对象、Q对象

查询集：

	在管理器上调用过滤器方法会返回查询集

	查询集经过过滤器筛选后返回新的查询集，因此可以写成链式过滤
	
	惰性执行:创建查询集不会带来任何数据库的访问，直到调用数据时，才会访问数据库
	
	何时对查询集求值：迭代、序列化、与if合用。
	
	返回查询集的方法，称为过滤器：

		all()
		filter()
		exclude()
		order_by()
		values():一个对象构成一个字典，然后构成一个列表返回
	
	写法：
		filter(键1=值1，键2=值2)
		等价于
		filter(键1=值1).filter(键2=值2)

	返回单个值的方法：

		get():返回单个满足条件的对象
			如果未找到会引发"模型类.DoesNotExist"异常
			如果多条被返回，会引发"模型类.MultipleObjectsReturned"异常
		count():返回当前查询的总条数
		first():返回第一个对象
		last():返回最后一个对象
		exists():判断查询集中是否有数据，如果有数据则返回Ture

	限制查询集:
		
		查询集返回列表，可以使用下标的方式进行限制，等同于sql中的limit和offset字句
		
		注意：不支持负数索引
		
		使用下标后返回一个新的查询集，不会立即执行查询
		
		如果获取一个对象，直接使用[0]，等同于[0:1].get()，
		但是如果没有数据，[0]引发IndexError异常，[0:1].get()引发DoesNotExist异常
		
	查询集的缓存：

		每个查询集都包含一个缓存来最小化对数据库的访问

		在新建的查询集中，缓存为空，首次对查询集求值时，会发生数据库查询，
		django会将查询的结果存在查询集的缓存中，并返回请求的结果，接下来对查询集求值将重用缓存的结果

		情况一：这构成了两个查询集，无法重用缓存，每次查询都会与数据库进行一次交互，增加了数据库的负载
			print([e.title for e in Entry.objects.all()])
			print([e.title for e in Entry.objects.all()])
			
		情况二：两次循环使用同一个查询集，第二次使用缓存中的数据

			querylist=Entry.objects.all()
			print([e.title for e in querylist])
			print([e.title for e in querylist])

		何时查询集不会被缓存：当只对查询集的部分进行求值时会检查缓存，
		但是如果这部分不在缓存中，那么接下来查询返回的记录将不会被缓存，
		这意味着使用索引来限制查询集将不会填充缓存，如果这部分数据已经被缓存，则直接使用缓存中的数据。

字段查询：

		实现where子名，作为方法filter()、exclude()、get()的参数

		语法：属性名称_比较运算符=值

		表示两个下划线，左侧是属性名称，右侧是比较类型

		对应键外，使用"属性名_id"表示外键的原始值

		转义：like语句中使用了%与，匹配数据中的%与，在过滤器中直接写，例如：
			filter(title__contains="%")=>where title like '%\%%'，表示查找标题中包含%的

	比较运算符：

		exact:表示判等、大小写敏感;如果没有写"比较运算符"，表示判等
			filter(isDelete=False)

		contains：是否包含，大小写敏感
			exclude(btitle__contains='传')

		startswith、endswith：以value开头或结尾，大小写敏感
			exclude(btitle__endswith='传')

		isnull、isnotnull：是否为null
			filter(btitle__isnull=False)

		在前面加个i表示不区分大小写，如iexact、icontains、istarswith、iendswith
		in：是否包含在范围内
			filter(pk__in=[1, 2, 3, 4, 5])

		gt、gte、lt、lte：大于、大于等于、小于、小于等于
			filter(id__gt=3)

		year、month、day、week_day、hour、minute、second：对日期间类型的属性进行运算
			filter(bpub_date__year=1980)
			filter(bpub_date__gt=date(1980, 12, 31))
			
		跨关联关系的查询：处理join查询
			
			语法：模型类名 <属性名> <比较>
			注：可以没有__<比较>部分，表示等于，结果同inner join
			可返向使用，即在关联的两个模型中都可以使用
			filter(heroinfo_ _hcontent_ _contains='八')

		查询的快捷方式：pk，pk表示primary key，默认的主键是id
			filter(pk__lt=6)
	
	聚合函数:

		使用aggregate()函数返回聚合函数的值
		函数：Avg，Count，Max，Min，Sum

		from django.db.models import Max
		maxDate = list.aggregate(Max('bpub_date'))
		
		count的一般用法：
		count = list.count()

	F对象:

		可以使用模型的字段A与字段B进行比较，如果A写在了等号的左边，则B出现在等号的右边，
		需要通过F对象构造
			list.filter(bread__gte=F('bcommet'))

		django支持对F()对象使用算数运算
			list.filter(bread__gte=F('bcommet') * 2)

		F()对象中还可以写作"模型类__列名"进行关联查询
			list.filter(isDelete=F('heroinfo__isDelete'))

		对于date/time字段，可与timedelta()进行运算
			list.filter(bpub_date__lt=F('bpub_date') + timedelta(days=1))

	Q对象:

		过滤器的方法中关键字参数查询，会合并为And进行
	
		需要进行or查询，使用Q()对象
		
		Q对象(django.db.models.Q)用于封装一组关键字参数，这些关键字参数与“比较运算符”中的相同
		
			from django.db.models import Q
			list.filter(Q(pk_ _lt=6))

		Q对象可以使用&（and）、|（or）操作符组合起来

		当操作符应用在两个Q对象时，会产生一个新的Q对象
			
			list.filter(pk_ _lt=6).filter(bcommet_ _gt=10)
			
			list.filter(Q(pk_ _lt=6) | Q(bcommet_ _gt=10))

		使用~（not）操作符在Q对象前表示取反

			list.filter(~Q(pk__lt=6))

		可以使用&|~结合括号进行分组，构造做生意复杂的Q对象

		过滤器函数可以传递一个或多个Q对象作为位置参数，如果有多个Q对象，这些参数的逻辑为and
		
		过滤器函数可以混合使用Q对象和关键字参数，所有参数都将and在一起，Q对象必须位于关键字参数的前面
			

自连接：

	对于地区信息，属于一对多关系，使用一张表，存储所有的信息
	
	类似的表结构还应用于分类信息，可以实现无限级分类
	
	新建模型AreaInfo，生成迁移

		class AreaInfo(models.Model):
			atitle = models.CharField(max_length=20)
			aParent = models.ForeignKey('self', null=True, blank=True)

	访问关联对象

		上级对象：area.aParent

		下级对象：area.areainfo_set.all()

	加入测试数据（在workbench中，参见“省市区mysql.txt”）

	在booktest/views.py中定义视图area

		from models import AreaInfo
		def area(request):
			area = AreaInfo.objects.get(pk=130100)
			return render(request, 'booktest/area.html', {'area': area})
	定义模板area.html
	<!DOCTYPE html>
	<html>
	<head>
	    <title>地区</title>
		</head>
		<body>
		当前地区：{{area.atitle}}
		<hr/>
		上级地区：{{area.aParent.atitle}}
		<hr/>
		下级地区：
		<ul>
			{%for a in area.areainfo_set.all%}
			<li>{{a.atitle}}</li>
			{%endfor%}
		</ul>
		</body>
	</html>


在booktest/urls.py中配置一个新的urlconf

	urlpatterns = [
	    url(r'^area/$', views.area, name='area')
		]


"----------------------------------------------------------------------"

视图：

	视图接受Web请求请求并且返回Web响应。

	视图就是一个python函数，被定义在views.py中。

	响应可以是一张网页的HTML内容，一个重定义向，一个404错误等等。

	响应处理过程如下图：

		用户在浏览器中输入网址www.itcast.cn/1/100 ---> django获取地址信息，去除域名与端口部分，1/100--->
		将请求地址，按定义顺序逐个匹配urlconf的正则部分，一旦匹配成功，则记录下来对应的方法名称--->
		调用找到的方法，接收request及正则中获取的值，处理并返回response对象。


URLconf:

	在settings.py 文件中通过ROOT_URLCONF指定根级url的配置

	urlpatterns 是一个url()实例的列表

	一个url()对象包括：
		正则表达式
		视图函数
		名称name

	编写URLconf的注意：
		若要从url中获取一个值，需要在它周围设置一对圆括号
		不需要添加一个前导的反斜杠，如应该写作'test/',而不应该写作'/test/'
		每个正则表达式清明的r表示字符串不转义

	请求的url被看做是一个普通的python字符串，进行匹配时不包括get或post请求的参数及域名。
		http://www.itcast.cn/python/1/?i=1&p=new，只匹配“/python/1/”部分

	正则表达式非命名组，通过位置参数传递给视图
		url(r'^([0-9]+)/$', views.detail, name='detail'),

	正则表达式命名组，通过关键字参数传递给视图，本例中关键字参数为id
		url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),

	参数匹配规则：优先使用命名参数，如果没有命名参数则使用位置参数

	每个捕获的参数都作为一个普通的python字符串传递给视图

	性能：urlpatterns中的每个正则表达式在第一次访问它们时被编译，这使得系统相当快


包含其它的URLconfs:

	在应用中创建urls.py文件，定义本应用中的urlconf，再在项目的settings中使用include()

		from django.conf.urls import include, url
		urlpatterns = [url(r'^', include('booktest.urls', namespace='booktest')),]

	匹配过程：先与主URLconf匹配，成功后再用剩余的部分与应用中的URLconf匹配
		请求http://www.itcast.cn/booktest/1/
		在主url中配置：
			url(r'^booktest/', include('booktest.urls', namespace='booktest')),
		在booktest应用urls.py中配置
			url(r'^([0-9]+)/$', views.detail, name='detail'),
		匹配部分是：/booktest/1/
		匹配过程：在settings.py中与"booktest/"成功，再用"1/"与booktest应用的urls匹配

	使用include可以去除urlconf的冗余
	参数：视图会收到来自父URLconf、当前URLconf捕获的所有参数
	在include中通过namespace定义命名空间，用于反解析

URL的反向解析:

	如果在视图、模板中使用硬编码的链接，在urlconf发生改变时，维护是一件非常麻烦的事情
	解决：在做链接时，通过指向urlconf的名称，动态生成链接地址
	视图：使用django.core.urlresolvers.reverse()函数
	模板：使用url模板标签
		

定义视图:

	本质就是一个函数

	视图参数：

		一个HttpRequest实例
		通过正则表达式组获取的位置参数
		通过正则表达式组获取得到关键字参数

	在应用目录下默认有views.py文件，一般视图都定义在这个文件中

	如果处理功能过多，可以将函数定义到不同的py文件中

		新建views1.py
		from django.http import HttpResponse
		def index(request):
			return HttpResponse("您好")

		在urls.py中修改配置
		from . import views1
		url(r'^$',views1.index,name='index'),

错误视图:

	Django原始自带几个默认视图用于处理HTTP错误

	404 (page not found) 视图:
		defaults.page_not_found(request, template_name='404.html')
		默认的404视图将传递一个变量给模板：request_path，它是导致错误的URL
		如果Django在检测URLconf中的每个正则表达式后没有找到匹配的内容也将调用404视图
		如果在settings中DEBUG设置为True，那么将永远不会调用404视图，而是显示URLconf 并带有一些调试信息
		在templates中创建404.html

			<!DOCTYPE html>
			<html>
			<head>
			<title></title>
			</head>
			<body>
			找不到了
			<hr/>
			{{request_path}}
			</body>
			</html>


	在settings.py中修改调试:
		DEBUG = False
		ALLOWED_HOSTS = ['*', ]


	请求一个不存在的地址:
		http://127.0.0.1:8000/test/

	500 (server error) 视图:

		defaults.server_error(request, template_name='500.html')
		在视图代码中出现运行时错误
		默认的500视图不会传递变量给500.html模板
		如果在settings中DEBUG设置为True，那么将永远不会调用505视图，而是显示URLconf 并带有一些调试信息.

	400 (bad request) 视图:

		defaults.bad_request(request, template_name='400.html')
		错误来自客户端的操作
		当用户进行的操作在安全方面可疑的时候，例如篡改会话cookie

HttpReqeust对象:

	服务器接收到http协议的请求后，会根据报文创建HttpRequest对象
	视图函数的第一个参数是HttpRequest对象
	在django.http模块中定义了HttpRequest对象的API

	属性：
		
		下面除非特别说明，属性都是只读的
		path：一个字符串，表示请求的页面的完整路径，不包含域名
		
		method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'
		
		encoding：一个字符串，表示提交的数据的编码方式
				如果为None则表示使用浏览器的默认设置，一般为utf-8
			
				这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，
				接下来对属性的任何访问将使用新的encoding值

		GET：一个类似于字典的对象，包含get请求方式的所有参数

		POST：一个类似于字典的对象，包含post请求方式的所有参数

		FILES：一个类似于字典的对象，包含所有的上传文件

		COOKIES：一个标准的Python字典，包含所有的cookie，键和值都为字符串

		session：一个既可读又可写的类似于字典的对象，表示当前的会话，
				只有当Django 启用会话的支持时才可用，详细内容见“状态保持”
		

	方法：

		is_ajax()：如果请求是通过XMLHttpRequest发起的，则返回True

QueryDict对象：

	定义在django.http.QueryDict

	request对象的属性GET、POST都是QueryDict类型的对象

	与python字典不同，QueryDict类型的对象用来处理同一个键带有多个值的情况

	方法get()：根据键获取值

			只能获取键的一个值
			如果一个键同时拥有多个值，获取最后一个值
			
			dict.get('键',default)
			或简写为
			dict['键']

	方法getlist()：根据键获取值
			将键的值以列表返回，可以获取一个键的多个值
			dict.getlist('键',default)


GET属性:

	QueryDict类型的对象

	包含get请求方式的所有参数

	与url请求地址中的参数对应，位于?后面

	参数的格式是键值对，如key1=value1

	多个参数之间，使用&连接，如key1=value1&key2=value2

	键是开发人员定下来的，值是可变的

	示例如下
	创建视图getTest1用于定义链接，getTest2用于接收一键一值，getTest3用于接收一键多值:

		def getTest1(request):
			return render(request,'booktest/getTest1.html')
		def getTest2(request):
			return render(request,'booktest/getTest2.html')
		def getTest3(request):
			return render(request,'booktest/getTest3.html')
	
	配置url:

		url(r'^getTest1/$', views.getTest1),
		url(r'^getTest2/$', views.getTest2),
		url(r'^getTest3/$', views.getTest3),

	创建getTest1.html，定义链接:

		<html>
		<head>
		<title>Title</title>
		</head>
		<body>
		链接1：一个键传递一个值
		<a href="/getTest2/?a=1&b=2">gettest2</a><br>
		链接2：一个键传递多个值
		<a href="/getTest3/?a=1&a=2&b=3">gettest3</a>
		</body>
		</html>

	完善视图getTest2的代码:

		def getTest2(request):
			a=request.GET['a']
			b=request.GET['b']
			context={'a':a,'b':b}
			return render(request,'booktest/getTest2.html',context)

	创建getTest2.html，显示接收结果:

		<html>
		<head>
		<title>Title</title>
		</head>
		<body>
		a:{{ a }}<br>
		b:{{ b }}
		</body>
		</html>

	完善视图getTest3的代码:

		def getTest3(request):
			a=request.GET.getlist('a')
			b=request.GET['b']
			context={'a':a,'b':b}
			return render(request,'booktest/getTest3.html',context)

	创建getTest3.html，显示接收结果:

		<html>
		<head>
		<title>Title</title>
		</head>
		<body>
		a:{% for item in a %}
		{{ item }}
		{ % endfor %}
		<br>
		b:{{ b }}
		</body>
		</html>


POST属性:

	QueryDict类型的对象

	包含post请求方式的所有参数

	与form表单中的控件对应

	问：表单中哪些控件会被提交?

		答：控件要有name属性，则name属性的值为键，value属性的值为键，构成键值对提交
		对于checkbox控件，name属性一样为一组，当控件被选中后会被提交，存在一键多值的情况

	键是开发人员定下来的，值是可变的
	示例如下
	定义视图postTest1:

		def postTest1(request):
			return render(request,'booktest/postTest1.html')

	配置url:
		url(r'^postTest1$',views.postTest1)

	创建模板postTest1.html:

		<html>
		<head>
		<title>Title</title>
		</head>
		<body>
		<form method="post" action="/postTest2/">
			姓名：<input type="text" name="uname"/><br>
			密码：<input type="password" name="upwd"/><br>
			性别：<input type="radio" name="ugender" value="1"/>男
			<input type="radio" name="ugender" value="0"/>女<br>
			爱好：<input type="checkbox" name="uhobby" value="胸口碎大石"/>胸口碎大石
			<input type="checkbox" name="uhobby" value="跳楼"/>跳楼
			<input type="checkbox" name="uhobby" value="喝酒"/>喝酒
			<input type="checkbox" name="uhobby" value="爬山"/>爬山<br>
			<input type="submit" value="提交"/>
		</form>
		</body>
		</html>


	创建视图postTest2接收请求的数据:

		def postTest2(request):
			uname=request.POST['uname']
			upwd=request.POST['upwd']
			ugender=request.POST['ugender']
			uhobby=request.POST.getlist('uhobby')
			context={'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby}
			return render(request,'booktest/postTest2.html',context)


	配置url:

		url(r'^postTest2$',views.postTest2)

	创建模板postTest2.html:

		<html>
		<head>
		<title>Title</title>
		</head>
		<body>
		{{uname }}<br>
		{{upwd }}<br>
		{{ugender }}<br>
		{{uhobby }}
		</body>
		</html>

	注意：使用表单提交，注释掉settings.py中的中间件crsf


HttpResponse对象:

	在django.http模块中定义了HttpResponse对象的API
	HttpRequest对象由Django自动创建，HttpResponse对象由程序员创建
	不调用模板，直接返回数据:

		#coding=utf-8
		from django.http import HttpResponse

		def index(request):
		    return HttpResponse('你好')

	调用模板:

		from django.http import HttpResponse
		from django.template import RequestContext, loader

		def index(request):
			t1 = loader.get_template('polls/index.html')
			context = RequestContext(request, {'h1': 'hello'})
			return HttpResponse(t1.render(context))
	
	属性:

		content：表示返回的内容，字符串类型
		charset：表示response采用的编码字符集，字符串类型
		status_code：响应的HTTP响应状态码
		content-type：指定输出的MIME类型


	方法:

		init ：使用页内容实例化HttpResponse对象

		write(content)：以文件的方式写

		flush()：以文件的方式输出缓存区

		set_cookie(key, value='', max_age=None, expires=None)：设置Cookie
			
			key、value都是字符串类型
			
			max_age是一个整数，表示在指定秒数后过期
			
			expires是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期，
			
			注意datetime和timedelta值只有在使用PickleSerializer时才可序列化
			
			max_age与expires二选一
			
			如果不指定过期时间，则两个星期后过期

		
			from django.http import HttpResponse
			from datetime import *

			def index(request):
				response = HttpResponse()
				if request.COOKIES.has_key('h1'):
					response.write('<h1>' + request.COOKIES['h1'] + '</h1>')
				response.set_cookie('h1', '你好', 120)
				# response.set_cookie('h1', '你好', None, datetime(2016, 10, 31))
				return response

		delete_cookie(key)：删除指定的key的Cookie，如果key不存在则什么也不发生


	子类HttpResponseRedirect:

		重定向，服务器端跳转

		构造函数的第一个参数用来指定重定向的地址

			在views1.py中
			from django.http import HttpResponse,HttpResponseRedirect
			def index(request):
			    return HttpResponseRedirect('js/')
			def index2(request,id):
				return HttpResponse(id)
						
			在应用的urls.py中增加一个url对象
			url(r'^([0-9]+)/$', views1.index2, name='index2'),


	推荐使用反向解析:

		from django.core.urlresolvers import reverse

		def index(request):
			    return HttpResponseRedirect(reverse('booktest:index2', args=(1,)))

	
	子类JsonResponse:

		返回json数据，一般用于异步请求
		_init _(data)
		帮助用户创建JSON编码的响应
		参数data是字典对象
		JsonResponse的默认Content-Type为application/json

		from django.http import JsonResponse

		def index2(requeset):
			return JsonResponse({'list': 'abc'})


简写函数:

	render

		render(request, template_name[, context])
		结合一个给定的模板和一个给定的上下文字典，并返回一个渲染后的HttpResponse对象
		request：该request用于生成response
		template_name：要使用的模板的完整名称
		context：添加到模板上下文的一个字典，视图将在渲染模板之前调用它

		from django.shortcuts import render
		def index(request):
			return render(request, 'booktest/index.html', {'h1': 'hello'})
				

	重定向:

	redirect(to)
	为传递进来的参数返回HttpResponseRedirect
	to推荐使用反向解析

		from django.shortcuts import redirect
		from django.core.urlresolvers import reverse

		def index(request):
			return redirect(reverse('booktest:index2'))

	得到对象或返回404

		get_object_or_404(klass, args, *kwargs)

		通过模型管理器或查询集调用get()方法，如果没找到对象，不引发模型的DoesNotExist异常，而是引发Http404异常
		
		klass：获取对象的模型类、Manager对象或QuerySet对象
	
		**kwargs：查询的参数，格式应该可以被get()和filter()接受
	
		如果找到多个对象将引发MultipleObjectsReturned异常

		
			 from django.shortcuts import *

			 def detail(request, id):
				try:
					book = get_object_or_404(BookInfo, pk=id)
				except BookInfo.MultipleObjectsReturned:
					book = None
				return render(request, 'booktest/detail.html', {'book': book})
							   
			将settings.py中的DEBUG改为False
			将请求地址输入2和100查看效果

	得到列表或返回404:

		get_list_or_404(klass, args, *kwargs)
		klass：获取列表的一个Model、Manager或QuerySet实例
		**kwargs：查寻的参数，格式应该可以被get()和filter()接受
		
		from django.shortcuts import *

		def index(request):
			# list = get_list_or_404(BookInfo, pk__lt=1)
			list = get_list_or_404(BookInfo, pk__lt=6)
			return render(request, 'booktest/index.html', {'list': list})
		
		将settings.py中的DEBUG改为False


状态保持:

	http协议是无状态的：每次请求都是一次新的请求，不会记得之前通信的状态

	客户端与服务器端的一次通信，就是一次会话

	实现状态保持的方式：在客户端或服务器端存储与会话有关的数据

	存储方式包括cookie、session，会话一般指session对象

	使用cookie，所有数据存储在客户端，注意不要存储敏感信息

	推荐使用sesison方式，所有数据存储在服务器端，在客户端cookie中存储session_id

	状态保持的目的是在一段时间内跟踪请求者的状态，可以实现跨页面访问当前请求者的数据

	注意：不同的请求者之间不会共享这个数据，与请求者一一对应


	启用session:
		
		使用django-admin startproject创建的项目默认启用

		在settings.py文件中

			项INSTALLED_APPS列表中添加：
			'django.contrib.sessions',
			
			项MIDDLEWARE_CLASSES列表中添加：
			'django.contrib.sessions.middleware.SessionMiddleware',

			禁用会话：删除上面指定的两个值，禁用会话将节省一些性能消耗

	使用session:

		启用会话后，每个HttpRequest对象将具有一个session属性，它是一个类字典对象
		get(key, default=None)：根据键获取会话的值
		clear()：清除所有会话
		flush()：删除当前的会话数据并删除会话的Cookie
		del request.session['member_id']：删除会话


	用户登录示例:

		在views.py文件中创建视图:

			from django.shortcuts import render, redirect
			from django.core.urlresolvers import reverse

			def index(request):
				uname = request.session.get('uname')
				return render(request, 'booktest/index.html', {'uname': uname})

			def login(request):
				return render(request, 'booktest/login.html')

			def login_handle(request):
				request.session['uname'] = request.POST['uname']
				return redirect(reverse('main:index')

			def logout(request):
				# request.session['uname'] = None
			    # del request.session['uname']
			    # request.session.clear()
			    request.session.flush()
				return redirect(reverse('main:index'))

		配置url:

			主url：

			from django.conf.urls import include, url
			urlpatterns = [
			    url(r'^', include('booktest.urls', namespace='main'))
				]

			应用url：
			from django.conf.urls import url
			from . import views
				urlpatterns = [
						url(r'^$', views.index, name='index'),
					    url(r'login/$', views.login, name='login'),
						url(r'login_handle/$', views.login_handle, name='login_handle'),
						url(r'logout/$', views.logout, name='logout')
						]

		创建模板index.html:
			
			<!DOCTYPE html>
			<html>
			<head>
			<title>首页</title>
			</head>
			<body>
			你好：{{uname}}
			<hr/>
			<a href="{%url 'main:login'%}">登录</a>
			<hr/>
			<a href="{%url 'main:logout'%}">退出</a>
			</body>
			</html>

		创建模板login.html：

			<!DOCTYPE html>
			<html>
			<head>
			<title>登录</title>
			</head>
			<body>
			<form method="post" action="/login_handle/">
				<input type="text" name="uname"/>
				<input type="submit" value="登录"/>
			</form>
			</body>
			</html>


	会话过期时间：

		set_expiry(value)：设置会话的超时时间
		如果没有指定，则两个星期后过期
		如果value是一个整数，会话将在values秒没有活动后过期
		若果value是一个imedelta对象，会话将在当前时间加上这个指定的日期/时间过期
		如果value为0，那么用户会话的Cookie将在用户的浏览器关闭时过期
		如果value为None，那么会话永不过期
		修改视图中login_handle函数，查看效果

		def login_handle(request):
			request.session['uname'] = request.POST['uname']
			# request.session.set_expiry(10)
			# request.session.set_expiry(timedelta(days=5))
			# request.session.set_expiry(0)
			# request.session.set_expiry(None)
			return redirect(reverse('main:index'))

	存储session:

		使用存储会话的方式，可以使用settings.py的SESSION_ENGINE项指定
		基于数据库的会话：这是django默认的会话存储方式，需要添加django.contrib.sessions到的
		INSTALLED_APPS设置中，运行manage.py migrate在数据库中安装会话表，可显示指定为

			SESSION_ENGINE='django.contrib.sessions.backends.db'

		基于缓存的会话：只存在本地内在中，如果丢失则不能找回，比数据库的方式读写更快

			SESSION_ENGINE='django.contrib.sessions.backends.cache'

		可以将缓存和数据库同时使用：优先从本地缓存中获取，如果没有则从数据库中获取

			SESSION_ENGINE='django.contrib.sessions.backends.cached_db'


	使用Redis缓存session:

		会话还支持文件、纯cookie、Memcached、Redis等方式存储，下面演示使用redis存储
		安装包

		pip install django-redis-sessions

		修改settings中的配置，增加如下项

			SESSION_ENGINE = 'redis_sessions.session'
			SESSION_REDIS_HOST = 'localhost'
			SESSION_REDIS_PORT = 6379
			SESSION_REDIS_DB = 0
			SESSION_REDIS_PASSWORD = ''
			SESSION_REDIS_PREFIX = 'session'

		管理redis的命令
			
			启动：sudo redis-server /etc/redis/redis.conf
			停止：sudo redis-server stop
			重启：sudo redis-server restart
			redis-cli：使用客户端连接服务器
			keys *：查看所有的键
			get name：获取指定键的值
			del name：删除指定名称的键

"-------------------------------------------------------------"

模板介绍:

	作为Web框架，Django提供了模板，可以很便利的动态生成HTML

	模版系统致力于表达外观，而不是程序逻辑

	模板的设计实现了业务逻辑(view)与显示内容（template）的分离，一个视图可以使用任意一个模板，
	一个模板可以供多个视图使用

	模板包含:
		HTML的静态部分
		动态插入内容部分

	Django模板语言，简写DTL，定义在django.template包中

	由startproject命令生成的settings.py定义关于模板的值：

		DIRS定义了一个目录列表，模板引擎按列表顺序搜索这些目录以查找模板源文件

		APP_DIRS告诉模板引擎是否应该在每个已安装的应用中查找模板

	常用方式：在项目的根目录下创建templates目录，设置DIRS值

		DIRS=[os.path.join(BASE_DIR,"templates")]

模板处理:

	Django处理模板分为两个阶段

	Step1 加载：根据给定的标识找到模板然后预处理，通常会将它编译好放在内存中

		loader.get_template(template_name)，返回一个Template对象


	Step2 渲染：使用Context数据对模板插值并返回生成的字符串

		Template对象的render(RequestContext)方法，使用context渲染模板

	加载渲染完整代码：

		from django.template import loader, RequestContext
		from django.http import HttpResponse

		def index(request):
			tem = loader.get_template('temtest/index.html')
			context = RequestContext(request, {})
			return HttpResponse(tem.render(context))

快捷函数:

	为了减少加载模板、渲染模板的重复代码，django提供了快捷函数
	render_to_string("")
	render(request,'模板',context)

	from django.shortcuts import render

	def index(request):
		return render(request, 'temtest/index.html')


定义模板:

		模板语言包括:

			变量

			标签 {% 代码块 %}

			过滤器

			注释{# 代码或html #}

变量：

	语法：{{ variable }}
		
	当模板引擎遇到一个变量，将计算整个变量，然后将结果输出

	变量名必须由字母、数字、下划线(不能以下划线开头)和点组成

	当模板引擎遇到点("."),会按照下列顺序查询：
		1、字典查询，例如：foo["bar"]
		2、属性或方法查询，例如：foo.bar
		3、数字索引查询，例如：foo[bar]

	如果变量不存在， 模版系统将插入' ' (空字符串) 

	在模板中调用方法时不能传递参数


在模板中调用对象的方法:

	在models.py 中定义类HeroInfo

		from django.db import models
		class HeroInfo(models.Model):
			...
			def showName(self):
				return self.hname

	在 view.py中传递HeroInfo对象

		from django.shortcuts import render
		from models import *

		def index(request):
			hero = HeroInfo(hname='abc')
			context = {'hero': hero}
			return render(request, 'temtest/detail.html', context)

	在模板detail.html中调用:

		{{hero.showName}}


标签:

	语法：{{% tag %}}
	作用：
		在输出中创建文本
		控制循环或逻辑
		加载外部信息到模板中供以后的变量使用

	for标签：

		{%for ... in ...%}
		循环逻辑
		{{forloop.counter}}表示当前是第几次循环
		{%empty%}
		给出的列表为或列表不存在时，执行此处
		{%endfor%}
	
	if标签:

		{%if ...%}
			逻辑1
		{%elif ...%}
			逻辑2
		{%else%}
			逻辑3
		{%endif%}
		
	comment标签：

		{% comment % }
			多行注释
		{% endcomment % }
	
	include：加载模板并以标签内的参数渲染：

		{%include "foo/bar.html" % }

	url：反向解析：

		{% url 'name' p1 p2 %}

	csrf_token：这个标签用于跨站请求伪造保护：

		{% csrf_token %}

	布尔标签：and、or，and比or的优先级高
	block、extends：详见“模板继承”
	autoescape：详见“HTML转义”

过滤器：

	语法: {{变量|过滤器 }}，例如{{name|lower }}，表示将变量name的值变为小写输出

	使用管道符号 (|)来应用过滤器

	通过使用过滤器来改变变量的计算结果

	可以在if标签中使用过滤器结合运算符
		if list1|length > 1

	过滤器能够被“串联”，构成过滤器链
		name|lower|upper
				
	过滤器可以传递参数，参数使用引号包起来
		list|join:", "

	default：如果一个变量没有被提供，或者值为false或空，则使用默认值，否则使用变量的值
		value|default:"什么也没有"

	date：根据给定格式对一个date变量格式化
		value|date:'Y-m-d'

注释

	单行注释:{#...#}

	注释可以包含任何模版代码，有效的或者无效的都可以
	{# {% if foo % }bar{% else % } #}

	使用comment标签注释模版中的多行内容


模板继承:

	模板继承可以减少页面内容的重复定义，实现页面内容的重用
	典型应用：网站的头部、尾部是一样的，这些内容可以定义在父模板中，子模板不需要重复定义
	block标签：在父模板中预留区域，在子模板中填充
	extends继承：继承，写在模板文件的第一行

	定义父模板base.html:

		{%block block_name%}
		 这里可以定义默认值
		 如果不定义默认值，则表示空字符串
		{%endblock%}

	定义子模板index.html:
		{% extends "base.html" %}
	
	在子模板中使用block填充预留区域:
		{%block block_name%}
		实际填充内容
		{%endblock%}
	
	说明:

		如果在模版中使用extends标签，它必须是模版中的第一个标签
		不能在一个模版中定义多个相同名字的block标签
		子模版不必定义全部父模版中的blocks，如果子模版没有定义block，则使用了父模版中的默认值
		如果发现在模板中大量的复制内容，那就应该把内容移动到父模板中
		使用可以获取父模板中block的内容
		为了更好的可读性，可以给endblock标签一个名字

		{% block block_name %}
		 区域内容
		{% endblock block_name %}


	
