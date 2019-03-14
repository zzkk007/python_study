
"-------------------------------------------------"

			Flask					
	
"-------------------------------------------------"

1、安装Flask

	依赖:
	当安装 Flask 时，以下配套软件会被自动安装。

		Werkzeug 用于实现 WSGI ，应用和服务之间的标准 Python 接口。
		Jinja 用于渲染页面的模板语言。
		MarkupSafe 与 Jinja 共用，在渲染页面时用于避免不可信的输入，防止注入攻击。
		ItsDangerous 保证数据完整性的安全标志数据，用于保护 Flask 的 session cookie.
		Click 是一个命令行应用的框架。用于提供 flask 命令，并允许添加自定义 管理命令。

	可选依赖
	以下配套软件不会被自动安装。如果安装了，那么 Flask 会检测到这些软件。

		Blinker 为 信号 提供支持。
		SimpleJSON 是一个快速的JSON实现兼容Python’s json模块。
			如果安装了这个软件那么会优先使用这个软件来进行 SON 操作。
		python-dotenv 当运行 flask 命令时为 通过 dotenv 设置环境变量 提供支持。
		Watchdog 为开发服务器提供快速高效的重载。

	虚拟环境:

		Python 3 内置了用于创建虚拟环境的 venv 模块。
			创建一个项目文件夹，然后创建一个虚拟环境。创建完成后项目文件夹中会有一个 venv 文件夹：

			mkdir myproject
			cd myproject
			python3 -m venv venv

		Python 2 安装 virtualenv

			# Debian, Ubuntu
			sudo apt-get install python-virtualenv

			# CentOS, Fedora
			sudo yum install python-virtualenv

			在老版本的 Python 中要使用下面的命令创建虚拟环境：

				virtualenv venv

		激活虚拟环境

			. venv/bin/activate
			source ./active

	在已激活的虚拟环境中可以使用如下命令安装 Flask：

		pip install Flask

		pip list

			Package    Version
			---------- -------
			pip        18.1   
			setuptools 28.8.0 
			wheel      0.29.0 

			但是现在最新的pip要求源必须是https的，不然会报错：
			The repository located at mirrors.aliyun.com is not a trusted or secure host and is being ignored.
			If this repository is available via HTTPS we recommend you use HTTPS instead,
			otherwise you may silence this warning and allow it anyway with 
			'--trusted-host mirrors.aliyun.com'.

			修改方法：
				添加国内pip源（主要是豆瓣和阿里云），~/.pip/pip.conf文件配置大概如下

				[global]
				index-url=http://mirrors.aliyun.com/pypi/simple/
				trusted-host = mirrors.aliyun.com

				[install]
				trusted-host=mirrors.aliyun.com

	
2、快速上手：

	























