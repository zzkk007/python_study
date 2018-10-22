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
		return HttpResponse("You're")


	


	



























