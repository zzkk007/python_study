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



























