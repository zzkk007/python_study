"-----------------------------------------------------------------"

						Docker 

"------------------------------------------------------------------"

1、容器生态系统：

	Docker 现在几乎是容器的代名词。确实，是 Docker 将容器技术发扬光大。
	同时，大家也需要知道围绕 Docker 还有一个生态系统。
	Docker 是这个生态系统的基石，但完善的生态系统才是保障 Docker 
	以及容器技术能够真正健康发展的决定因素。
	
	大致来看，容器生态系统包含核心技术、平台技术和支持技术。

	1.1 容器核心技术：
		
		容器核心技术是指能够让 container 在 host 上运行起来的那些技术。

		这些技术包括容器规范、容器 runtime、容器管理工具、容器定义工具、Registry 以及 容器 OS，下面分别介绍。

		容器规范：

			容器不光是 Docker，还有其他容器，比如 CoreOS 的 rkt。
			为了保证容器生态的健康发展，保证不同容器之间能够兼容，
			包含 Docker、CoreOS、Google在内的若干公司共同成立了一个叫 Open Container Initiative（OCI）的组织，
			其目是制定开放的容器规范。
		
			目前 OCI 发布了两个规范：runtime spec 和 image format spec。
			有了这两个规范，不同组织和厂商开发的容器能够在不同的 runtime 上运行。
			这样就保证了容器的可移植性和互操作性。

		容器 runtime:

			runtime 是容器真正运行的地方。
			runtime 需要跟操作系统 kernel 紧密协作，为容器提供运行环境。
			
			lxc、runc 和 rkt 是目前主流的三种容器 runtime。
			lxc 是 Linux 上老牌的容器 runtime。Docker 最初也是用 lxc 作为 runtime。
			runc 是 Docker 自己开发的容器 runtime，符合 oci 规范，也是现在 Docker 的默认 runtime。
			rkt 是 CoreOS 开发的容器 runtime，符合 oci 规范，因而能够运行 Docker 的容器。

		容器管理工具:

			光有 runtime 还不够，用户得有工具来管理容器啊。
			容器管理工具对内与 runtime 交互，对外为用户提供 interface，比如 CLI。

			lxd 是 lxc 对应的管理工具。
			
			runc 的管理工具是 docker engine。docker engine 包含后台 deamon 和 cli 两个部分。
			我们通常提到 Docker，一般就是指的 docker engine。
			
			rkt 的管理工具是 rkt cli。


		容器定义工具:

			容器定义工具允许用户定义容器的内容和属性，这样容器就能够被保存，共享和重建。

			docker image 是 docker 容器的模板，runtime 依据 docker image 创建容器。
			dockerfile 是包含若干命令的文本文件，可以通过这些命令创建出 docker image。
			ACI (App Container Image) 与 docker image 类似，只不过它是由 CoreOS 开发的 rkt 容器的 image 格式。

		Registry:
		
			容器是通过 image 创建的，需要有一个仓库来统一存放 image，这个仓库就叫做 Registry。
			Docker Hub（https://hub.docker.com )是 Docker 为公众提供的托管 Registry，
			上面有很多现成的 image，为 Docker 用户提供了极大的便利。
			Quay.io（https://quay.io/  )是另一个公共托管 Registry，提供与 Docker Hub 类似的服务。

		容器 OS:

			由于有容器 runtime，几乎所有的 Linux、MAC OS 和 Windows 都可以运行容器。
			但这不并没有妨碍容器 OS 的问世。

			容器 OS 是专门运行容器的操作系统。与常规 OS 相比，容器 OS 通常体积更小，启动更快。
			因为是为容器定制的 OS，通常它们运行容器的效率会更高。

			目前已经存在不少容器 OS，CoreOS、atomic 和 ubuntu core 是其中的杰出代表。

	1.2 容器平台技术:

		容器核心技术使得容器能够在单个 host 上运行。而容器平台技术能够让容器作为集群在分布式环境中运行。

		容器平台技术包括容器编排引擎、容器管理平台和基于容器的 PaaS。

		容器编排引擎:

			基于容器的应用一般会采用微服务架构。在这种架构下，应用被划分为不同的组件，
			并以服务的形式运行在各自的容器中，通过 API 对外提供服务。为了保证应用的高可用，
			每个组件都可能会运行多个相同的容器。
			这些容器会组成集群，集群中的容器会根据业务需要被动态地创建、迁移和销毁。

			大家可以看到，这样一个基于微服务架构的应用系统实际上是一个动态的可伸缩的系统。
			这对我们的部署环境提出了新的要求，我们需要有一种高效的方法来管理容器集群。
			而这，就是容器编排引擎要干的工作。

			所谓编排（orchestration），通常包括容器管理、调度、集群定义和服务发现等。
			通过容器编排引擎，容器被有机的组合成微服务应用，实现业务需求。

			docker swarm 是 Docker 开发的容器编排引擎。
			kubernetes 是 Google 领导开发的开源容器编排引擎，同时支持 Docker 和 CoreOS 容器。
			mesos 是一个通用的集群资源调度平台，mesos 与 marathon 一起提供容器编排引擎功能。

			以上三者是当前主流的容器编排引擎。

		容器管理平台:

			容器管理平台是架构在容器编排引擎之上的一个更为通用的平台。
			通常容器管理平台能够支持多种编排引擎，抽象了编排引擎的底层实现细节，
			为用户提供更方便的功能，比如 application catalog 和一键应用部署等。

			Rancher 和 ContainerShip 是容器管理平台的典型代表。

		基于容器的 PaaS:

			基于容器的 PaaS 为微服务应用开发人员和公司提供了开发、部署和管理应用的平台，
			使用户不必关心底层基础设施而专注于应用的开发。

	1.3 容器支持技术:

		这些技术被用于支持基于容器的基础设施。包括，容器网络、服务发现、监控、数据管理、日志管理、安全性等。

		容器网络：
		
			容器的出现使网络拓扑变得更加动态和复杂。
			用户需要专门的解决方案来管理容器与容器，容器与其他实体之间的连通性和隔离性。

			docker network 是 Docker 原生的网络解决方案。除此之外，我们还可以采用第三方开源解决方案，
			例如 flannel、weave 和 calico。
			不同的方案设计和实现方式不同，各有优势和特定，我们可以根据实际需要来选型。

		服务发现：

			动态变化是微服务应用的一大特点。当负载增加时，集群会自动创建新的容器；负载减小，多余的容器会被销毁。
			容器也会根据 host 的资源使用情况在不同 host 中迁移，容器的 IP 和端口也会随之发生变化。

			在这种动态的环境下，必须要有一种机制让 client 能够知道如何访问容器提供的服务。
			这就是服务发现技术要完成的工作。

		监控：

			监控对于基础架构非常重要，而容器的动态特征对监控提出更多挑战。

		数据管理：

			容器经常会在不同的 host 之间迁移，如何保证持久化数据也能够动态迁移，
			是 Flocker 这类数据管理工具提供的能力。

		日志管理
			
			日志为问题排查和事件管理提供了重要依据。
			docker logs 是 Docker 原生的日志工具。而 logspout 对日志提供了路由功能，
			它可以收集不同容器的日志并转发给其他工具进行后处理。
	
		安全性：

			对于年轻的容器，安全性一直是业界争论的焦点。
			
			OpenSCAP 能够对容器镜像进行扫描，发现潜在的漏洞。

2、Docker 环境搭建：

	2.1 环境选择：

		管理工具 - Docker Engine,因为 Docker 最流行使用最广泛。
		runtime - runc,Docker 的默认 runtime
		操作系统 - Ubuntu
	
	2.2 安装Docker:

		我们将在 ubuntu 16.04 虚拟机中安装 Docker。因为安装过程需要访问 internet， 所以虚拟机必须能够上网。

		Docker 分为开源免费的 CE（Community Edition）版本和收费的 EE（Enterprise Edition）版本。
		下面我们将按照文档，通过以下步骤在 Ubuntu 16.04 上安装 Docker CE 版本。
			
		配置 Docker 的 apt 源:

			1. 安装包，允许 apt 命令 HTTPS 访问 Docker 源。

			$ sudo apt-get install \
				apt-transport-https \
				ca-certificates \
				curl \
				software-properties-common

			2. 添加 Docker 官方的 GPG

				$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

			3. 将 Docker 的源添加到 /etc/apt/sources.list:

				$ sudo add-apt-repository \
				  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
				  $(lsb_release -cs) \
				  stable"
		安装 Docker
	
			$ sudo apt-get update
			$  sudo apt-get install docker-ce

		运行第一个容器:

			环境就绪，马上运行第一个容器，执行命令：
			# docker run -d -p 80:80 httpd

			其过程可以简单的描述为：

				从 Docker Hub 下载 httpd 镜像。镜像中已经安装好了 Apache HTTP Server。

				启动 httpd 容器，并将容器的 80 端口映射到 host 的 80 端口。

			可以通过浏览器验证容器是否正常工作。在浏览器中输入 http://[your ubuntu host IP]

3、 容器 What，Why,How：

	3.1 What - 什么是容器:

		容器是一种轻量级、可移植、自包含的软件打包技术，使应用程序可以在几乎任何地方以相同的方式运行。
		开发人员在自己笔记本上创建并测试好的容器，无需任何修改就能够在生产系统的虚拟机、
		物理服务器或公有云主机上运行。

		容器由两部分组成：

			应用程序本身
			依赖：比如应用程序需要的库或其他软件

		容器在 Host 操作系统的用户空间中运行，与操作系统的其他进程隔离。这一点显著区别于的虚拟机。

		容器不虚拟机不同：

			传统的虚拟化技术，比如 VMWare, KVM, Xen，目标是创建完整的虚拟机。
			为了运行应用，除了部署应用本身及其依赖（通常几十 MB），还得安装整个操作系统（几十 GB）。

			由于所有的容器共享同一个 Host OS，这使得容器在体积上要比虚拟机小很多。
			另外，启动容器不需要启动整个操作系统，所以容器部署和启动速度更快，开销更小，也更容易迁移。


	3.2 Why - 为什么需要容器:

		为什么需要容器？容器到底解决的是什么问题？
		简要的答案是：容器使软件具备了超强的可移植能力。

		Docker 将集装箱思想运用到软件打包上，为代码提供了一个基于容器的标准化运输系统。
		Docker 可以将任何应用及其依赖打包成一个轻量级、可移植、自包含的容器。
		容器可以运行在几乎所有的操作系统上。

		容器意味着环境隔离和可重复性。开发人员只需为应用创建一次运行环境，
		然后打包成容器便可在其他机器上运行。
		另外，容器环境与所在的 Host 环境是隔离的，就像虚拟机一样，但更快更简单。

	3.3 How - 容器是如何工作的：

		首先会介绍 Docker 的架构，然后讨论 Docker 的镜像、容器、网络和存储。

		Docker 的核心组件包括：

			a. Docker 客户端 - Client
			b. Docker 服务器 - Docker daemon
			c. Docker 镜像 - Image
			d. Registry
			e. Docker 容器 - Container

		Docker 采用的是 Client/Server 架构。客户端向服务器发送请求，服务器负责构建、运行和分发容器。
		客户端和服务器可以运行在同一个 Host 上，客户端也可以通过 socket 或 REST API 与远程的服务器通信。

		Docker 客户端:

			最常用的Docker客户端是docker命令。通过docker我们可以方便地在Host上构建和运行容器。

			attach      Attach local standard input, output, and error streams to a running container
			build       Build an image from a Dockerfile
			commit      Create a new image from a container changes
			cp          Copy files/folders between a container and the local filesystem
			create      Create a new container
			diff        Inspect changes to files or directories on a container filesystem
			events      Get real time events from the server
			exec        Run a command in a running container
			export      Export a container filesystem as a tar archive
			history     Show the history of an image
			images      List images
			import      Import the contents from a tarball to create a filesystem image
			info        Display system-wide information
			inspect     Return low-level information on Docker objects
			kill        Kill one or more running containers
			load        Load an image from a tar archive or STDIN
			login       Log in to a Docker registry
			logout      Log out from a Docker registry
			logs        Fetch the logs of a container
			pause       Pause all processes within one or more containers
			port        List port mappings or a specific mapping for the container
			ps          List containers
			pull        Pull an image or a repository from a registry
			push        Push an image or a repository to a registry
			rename      Rename a container
			restart     Restart one or more containers
			rm          Remove one or more containers
			rmi         Remove one or more images
			run         Run a command in a new container
			save        Save one or more images to a tar archive (streamed to STDOUT by default)
			search      Search the Docker Hub for images
			start       Start one or more stopped containers
			stats       Display a live stream of container(s) resource usage statistics
			stop        Stop one or more running containers
			tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
			top         Display the running processes of a container
			unpause     Unpause all processes within one or more containers
			update      Update configuration of one or more containers
			version     Show the Docker version information
			wait        Block until one or more containers stop, then print their exit codes

		Docker 服务器:

			Docker daemon 是服务器组件，以 Linux 后台服务的方式运行。

			root@zk-virtual-machine:~# systemctl status docker.service
			● docker.service - Docker Application Container Engine
			   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
			   Active: active (running) since 二 2018-11-06 16:59:51 CST; 18h ago
				 Docs: https://docs.docker.com
			
			 Main PID: 14969 (dockerd)
		   	    Tasks: 54
		       Memory: 96.7M
		          CPU: 4min 13.542s
			   CGroup: /system.slice/docker.service
					   ├─14969 /usr/bin/dockerd -H fd://
					   ├─15000 docker-containerd --config /var/run/docker/containerd/containerd.toml
			           ├─15700 /usr/bin/docker-proxy -proto -host -port80 -container-ip 172.17.0.2
					   └─15707 docker-containerd-shim -namespace -workdir /var/lib/docker/containerd/daemon/io.con

			Docker daemon 运行在 Docker host 上，负责创建、运行、监控容器，构建、存储镜像。

			默认配置下，Docker daemon 只能响应来自本地 Host 的客户端请求。
			如果要允许远程客户端请求，需要在配置文件中打开 TCP 监听，步骤如下：
			
				a.  编辑配置文件 /etc/systemd/system/multi-user.target.wants/docker.service，
					在环境变量 ExecStart 后面添加 -H tcp://0.0.0.0，允许来自任意 IP 的客户端连接。

					[Service]
					Type = notify
						...
					ExecStart = /user/bin/docker -H fd://  -H tcp://0.0.0.0
			
				b. 重启 Docker daemon：

					#systemctl daemon-reload
					#systemctl restart docker.service

				c. 服务器 IP 为 192.168.56.102，客户端在命令行里加上 -H 参数，即可与远程服务器通信
					
					#docker -H 192.168.56.102 info


		Docker 镜像:

			可将 Docker 镜像看着只读模板，通过它可以创建 Docker 容器。

			例如某个镜像可能包含一个 Ubuntu 操作系统、一个 Apache HTTP Server 以及用户开发的 Web 应用。

			镜像有多种生成方法：
				可以从无到有开始创建镜像
				也可以下载并使用别人创建好的现成的镜像
				还可以在现有镜像上创建新的镜像

				我们可以将镜像的内容和创建步骤描述在一个文本文件中，这个文件被称作 Dockerfile，
				通过执行 docker build <docker-file> 命令可以构建出 Docker 镜像，后面我们会讨论。

		Docker 容器:

			Docker 容器就是 Docker 镜像的运行实例。

			用户可以通过 CLI（docker）或是 API 启动、停止、移动或删除容器。
			可以这么认为，对于应用软件，镜像是软件生命周期的构建和打包阶段，而容器则是启动和运行阶段。

		Registry：

			Registry 是存放 Docker 镜像的仓库，Registry 分私有和公有两种。

			Docker Hub（https://hub.docker.com/） 是默认的 Registry，
			由 Docker 公司维护，上面有数以万计的镜像，用户可以自由下载和使用。

			docker pull 命令可以从 Registry 下载镜像。
			docker run 命令则是先下载镜像（如果本地没有），然后再启动容器。


	3.4、Docker 组件是如何工作的：

		还记得我们运行的第一个容器吗？现在通过它来体会一下 Docker 各个组件是如何协作的。
		容器启动过程如下：

			root@ubuntu:~#docker run -d -p 80:80 httpd		(1)
			Unable to find image 'httpd:latest' locally		(2)
			latest:Pulling from library/httpd
			385a066cd84a:Pull complete                      (3)
				....
			Status: Downloaded newer image for httpd:latest (4)
			170edfc2054fsgfds3w43214324u2h52nr432194jdsfksjadfwer53fsa212 (5)

				(1)Docker 客户端执行 docker run 命令。
				(2)Docker daemon 发现本地没有 httpd 镜像。
				(3)daemon 从 Docker Hub 下载镜像。
				(4)下载完成，镜像 httpd 被保存到本地。
				(5)Docker daemon 启动容器。
		
			docker images 可以查看到下载到本地的镜像。	
			docker ps 或者 docker container ls 显示容器正在运行。

		Docker 借鉴了集装箱的概念。标准集装箱将货物运往世界各地，
		Docker 将这个模型运用到自己的设计哲学中，唯一不同的是：集装箱运输货物，而 Docker 运输软件。

		每个容器都有一个软件镜像，相当于集装箱中的货物。容器可以被创建、启动、关闭和销毁。
		和集装箱一样，Docker 在执行这些操作时，并不关心容器里到底装的什么，
		它不管里面是 Web Server，还是 Database。

		用户不需要关心容器最终会在哪里运行，因为哪里都可以运行。

		开发人员可以在笔记本上构建镜像并上传到 Registry，
		然后 QA 人员将镜像下载到物理或虚拟机做测试，最终容器会部署到生产环境。

		使用 Docker 以及容器技术，我们可以快速构建一个应用服务器、一个消息中间件、一个数据库、一个持续集成环境。
		因为 Docker Hub 上有我们能想到的几乎所有的镜像。

		如果你是一个开发人员，想学习怎么用 django 开发 Python Web 应用，执行 docker run django，
		在容器里随便折腾吧，不用担心会搞乱 Host 的环境。


4、 镜像



	








		
