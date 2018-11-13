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

	镜像是 Docker 容器的基石，容器是镜像的运行实例，有了镜像才能启动容器。

	本章内容安排如下：

		首先通过研究几个典型的镜像，分析镜像的内部结构。
		然后学习如何构建自己的镜像。
		最后介绍怎样管理和分发镜像。

	4.1 镜像的内部结构:
		
		为什么我们要讨论镜像的内部结构？
		如果只是使用镜像，当然不需要了解，直接通过 docker 命令下载和运行就可以了。
		但如果我们想创建自己的镜像，或者想理解 Docker 为什么是轻量级的，就非常有必要学习这部分知识了。
		
		hello-world - 最小的镜像：

			hello-world 是 Docker 官方提供的一个镜像，通常用来验证 Docker 是否安装成功。

			我们先通过 docker pull 从 Docker Hub 下载它。
				#docker pull hello-world

			用 docker images 命令查看镜像的信息。
				#docker images hello-workd	

			通过 docker run 运行。
				#docker run hello-world

		其实我们更关心 hello-world 镜像包含哪些内容。
		
		Dockerfile 是镜像的描述文件，定义了如何个构建 Docker 镜像。
		Dockerfile 的语法简洁且可读性强，后面我们会专门讨论如何编写 Dockerfile。

		hello-world 的 Dockerfile内容如下：

			FROM scratch
			COPY hello /
			CMD ["/hello"]

		只有短短三条指令。
			
			(1) FROM scratch
				此镜像是从白手起家，从 0 开始构建。

			(2) COPY hello /
				将文件“hello”复制到镜像的根目录。
			
			(3) CMD ["/hello"]
				容器启动时，执行 /hello

		镜像hello-world中就只有一个可执行文件"hello",其功能就是打印出"Hello from Docker ......"等信息。

		/hello 就是文件系统的全部内容，连最基本的 /bin，/usr, /lib, /dev 都没有。

		hello-world 虽然是一个完整的镜像，但它并没有什么实际用途。
		通常来说，我们希望镜像能提供一个基本的操作系统环境，用户可以根据需要安装和配置软件。
		这样的镜像我们称作 base 镜像。


	4.2 base 镜像：

		base 镜像有两层含义：
		
			a. 不依赖其他镜像，从 scratch 构建。
			b. 其他镜像可以之为基础进行扩展。

		所以，能称作base镜像的通常都是各种Linux发行版的Docker镜像，比如 Ubuntu, Debian, CentOS等。

		我们以 CentOS 为例考察 base 镜像包含哪些内容。

		下载镜像：

			#docker pull centos

		查看镜像信息：
			
			#docker images

				REPOSITORY      TAG         IMAGE ID            CREATED             SIZE
				httpd           latest      55a118e2a010        13 days ago         132MB
				ubuntu          latest      ea4c82dcd15a        2 weeks ago         85.8MB
				centos          latest      75835a67d134        4 weeks ago         200MB
				hello-world     latest      4ab4c602aa5e        2 months ago        1.84kB

		镜像大小才200MB，等一下！一个 CentOS 才 200MB ？
		平时我们安装一个 CentOS 至少都有几个 GB，怎么可能才 200MB !
		相信这是几乎所有 Docker 初学者都会有的疑问，包括我自己。
		
		下面我们来解释这个问题。
		Linux 操作系统由内核空间bootfs(Kernel)和用户空间rootfs(/dev,/bin,/erc,/user,/temp ....)组成。
		
			bootfs (boot file system) 主要包含 bootloader 和 kernel, bootloader主要是引导加载kernel,
			当boot成功后 kernel 被加载到内存中后 bootfs就被umount了.
			
			rootfs (root file system) 包含的就是典型Linux系统中的 /dev, /proc,/bin, /etc 等标准目录和文件。
		

		对于base镜像来说，底层直接用Host的kernel，自己只需要提供rootfs就行了
		而对于一个精简的 OS，rootfs 可以很小，只需要包括最基本的命令、工具和程序库就可以了。
		我们平时安装的 CentOS 除了 rootfs 还会选装很多软件、服务、图形桌面等，需要好几个 GB 就不足为奇了。


		base 镜像提供的是最小安装的 Linux 发行版。

			下面是 CentOS 镜像的 Dockerfile 的内容：

				FROM scratch
				ADD centos-7-docker.tar.xz /
				CMD ["/bin/bash"]
			
			第二行 ADD 指令添加到镜像的 tar 包就是 CentOS 7 的 rootfs。
			在制作镜像时，这个 tar 包会自动解压到 / 目录下，生成 /dev, /proc, /bin 等目录。

			注：可在 Docker Hub 的镜像描述页面中查看 Dockerfile 。


		不同 Linux 发行版的区别主要就是 rootfs。
		比如 Ubuntu 14.04 使用 upstart 管理服务，apt 管理软件包；
		而 CentOS 7 使用 systemd 和 yum。
		这些都是用户空间上的区别，Linux kernel 差别不大。

		所以 Docker 可以同时支持多种 Linux 镜像，模拟出多种操作系统环境。
		
		这里需要说明的是：

			base 镜像只是在用户空间与发行版一致，kernel 版本与发行版是不同的。
			例如 CentOS 7 使用 3.x.x 的 kernel，如果 Docker Host 是 Ubuntu 16.04（比如我们的实验环境），
			那么在 CentOS 容器中使用的实际是是 Host 4.x.x 的 kernel。

			root@zk-virtual-machine:~# uname -r
			4.15.0-29-generic                           (1)
			root@zk-virtual-machine:~# docker run -it centos  (2)
			[root@ae7186116373 /]# cat /etc/redhat-release 
			CentOS Linux release 7.5.1804 (Core)    (3)
			[root@ae7186116373 /]# uname -r
			4.15.0-29-generic                      (4)

			(1) Host kernel 为4.15.0-29
			(2)	启动并进入 CentOS 容器
			(3)	验证容器是 CentOS 7
			(4)	容器的 kernel 版本与 Host 一致

		容器只能使用 Host 的 kernel，并且不能修改。
		所有容器都共用 host 的 kernel，在容器中没办法对 kernel 升级。
		如果容器对 kernel 版本有要求（比如应用只能在某个 kernel 版本下运行），则不建议用容器，
		这种场景虚拟机可能更合适。
			
	
	4.3 镜像的分层结构：

		Docker 支持通过扩展现有镜像，创建新的镜像。

		实际上，Docker Hub 中 99% 的镜像都是通过在 base 镜像中安装和配置需要的软件构建出来的。
		比如我们现在构建一个新的镜像，Dockerfile 如下：

			FROM debian      (1)
			RUN apt-get install emacs   (2)
			RUN apt-get install apache2 (3)
			CMD ["/bin/bash"]  (4)

			(1) 新镜像不再是从 scratch 开始，而是直接在 Debian base 镜像上构建。
			(2) 安装 emacs 编辑器。
			(3) 安装 apache2。
			(4) 容器启动时运行 bash。

		可以看到，新镜像是从base镜像一层一层叠加生成的。每安装一个软件,就在现有镜像的基础上增加一层。

		问什么 Docker 镜像要采用这种分层结构呢？
			最大的一个好处就是 - 共享资源。

		比如：有多个镜像都从相同的 base 镜像构建而来，
		那么 Docker Host 只需在磁盘上保存一份 base 镜像；同时内存中也只需加载一份 base 镜像，
		就可以为所有容器服务了。而且镜像的每一层都可以被共享，我们将在后面更深入地讨论这个特性。

		这时可能就有人会问了：如果多个容器共享一份基础镜像，当某个容器修改了基础镜像的内容，
		比如 /etc 下的文件，这时其他容器的 /etc 是否也会被修改？

			答案是不会！
			修改会被限制在单个容器内。
			这就是我们接下来要学习的容器 Copy-on-Write 特性。
				
		可写的容器层:

			当容器启动时，一个新的可写层被加载到镜像的顶部。
			这一层通常被称作“容器层”，“容器层”之下的都叫“镜像层”。

			所有对容器的改动 - 无论添加、删除、还是修改文件都只会发生在容器层中。
			只有容器层是可写的，容器层下面的所有镜像层都是只读的。

			下面我们深入讨论容器层的细节。

				镜像层数量可能会很多，所有镜像层会联合在一起组成一个统一的文件系统。
				如果不同层中有一个相同路径的文件，比如 /a，上层的 /a 会覆盖下层的 /a，
				也就是说用户只能访问到上层中的文件 /a。
				在容器层中，用户看到的是一个叠加之后的文件系统。

				a. 添加文件:
					在容器中创建文件时，新文件被添加到容器层中。

				b. 读取文件:
					在容器中读取某个文件时，Docker 会从上往下依次在各镜像层中查找此文件。
					一旦找到，立即将其复制到容器层，然后打开并读入内存。
			
				c. 修改文件:
					在容器中修改已存在的文件时，Docker 会从上往下依次在各镜像层中查找此文件。
					一旦找到，立即将其复制到容器层，然后修改之。
				
				d. 删除文件:
					在容器中删除文件时，Docker 也是从上往下依次在镜像层中查找此文件。
					找到后，会在容器层中记录下此删除操作。

			只有当需要修改时才复制一份数据，这种特性被称作 Copy-on-Write。
			可见，容器层保存的是镜像变化的部分，不会对镜像本身进行任何修改。

			这样就解释了我们前面提出的问题：容器层记录对镜像的修改，所有镜像层都是只读的，
			不会被容器修改，所以镜像可以被多个容器共享。
	
	4.4 如何构建镜像:

		对于 Docker 用户来说，最好的情况是不需要自己创建镜像。
		几乎所有常用的数据库、中间件、应用软件等都有现成的 Docker 官方镜像或其他人和组织创建的镜像，
		我们只需要稍作配置就可以直接使用。
		
		使用现成镜像的好处除了省去自己做镜像的工作量外，更重要的是可以利用前人的经验。
		特别是使用那些官方镜像，因为 Docker 的工程师知道如何更好的在容器中运行软件。

		当然，某些情况下我们也不得不自己构建镜像，比如：
			
			1. 找不到现成的镜像，比如自己开发的应用程序。
			2. 需要在镜像中加入特定的功能，比如官方镜像几乎都不提供 ssh。

		所以本节我们将介绍构建镜像的方法。同时分析构建的过程也能够加深我们对前面镜像分层结构的理解。

		Docker 提供了两种构建镜像的方法：
			
			1. docker commit 命令
			2. Dockerfile 构建文件

			docker commit：

				docker commit 命令是创建新镜像最直观的方法，其过程包含三个步骤：
					
					a. 运行容器
					b. 修改容器
					c. 将容器保存为新的镜像

				举个例子：在 ubuntu base 镜像中安装 vi 并保存为新镜像。

					a. 第一步， 运行容器
						root@zk-virtual-machine:~#docker run -it ubuntu
						root@b268b625358e:/# 
						
						-it 参数的作用是以交互模式进入容器，并打开终端。b268b625358e是容器的内部 ID。
				
					b. 安装vi

						root@b268b625358e:/# vim
						bash: vim:command not found
						
						确认没有安装。

						root@b268b625358e:/# apt-get install -y vim

					c. 保存为新镜像

						在新窗口中查看当前运行的容器。

						root@zk-virtual-machine:/home/zk# docker ps
						CONTAINER ID    IMAGE    COMMAND         CREATED        STATUS         PORTS  NAMES
						b268b625358e    ubuntu   "/bin/bash"    4 minutes ago   Up 4 minutes          zen_lewin						
							zen_lewin是 Docker 为我们的容器随机分配的名字。	

						执行 docker commit 命令将容器保存为镜像。
							root@zk-virtual-machine:/home/zk# docker commit zen_lewin ubuntu-with-vi
							sha256:ed7d16aabc34c230bbf2526d3086b798cd620cc5f6d1bd2a51fe8c81663a4396

							root@zk-virtual-machine:/home/zk# docker images
							REPOSITORY      TAG         IMAGE ID        CREATED        SIZE
							ubuntu-with-vi  latest      ed7d16aabc34    5 seconds ago  85.8MB  
							ubuntu          latest      ea4c82dcd15a    2 weeks ago    85.8MB

							因为上面的apt-get install -y vim 执行失败，其实ubuntu-with-vi 和 ubuntu 一样。

							新镜像命名为 ubuntu-with-vi。

						从新镜像启动容器，验证 vi 已经可以使用。
							root@zk-virtual-machine:docker run -it ubuntu-with-vi

				以上演示了如何用 docker commit 创建新镜像。然而，Docker 并不建议用户通过这种方式构建镜像。
				原因如下：

					这是一种手工创建镜像的方式，容易出错，效率低且可重复性弱。
					比如要在 debian base 镜像中也加入 vi，还得重复前面的所有步骤。

					更重要的：使用者并不知道镜像是如何创建出来的，里面是否有恶意程序。
					也就是说无法对镜像进行审计，存在安全隐患。

					既然 docker commit 不是推荐的方法，我们干嘛还要花时间学习呢？

					原因是：即便是用 Dockerfile（推荐方法）构建镜像，
					底层也 docker commit 一层一层构建新镜像的。
					学习 docker commit 能够帮助我们更加深入地理解构建过程和镜像的分层结构。


			Dockerfile 构建镜像：
				
				Dockerfile 是一个文本文件，记录了镜像构建的所有步骤。

				第一个 Dockerfile：

					用 Dockerfile 创建上节的 ubuntu-with-vi，其内容则为：

						FROM ubuntu
						RUN apt-get update && apt-get install -y vim

					下面我们运行 docker build 命令构建镜像并详细分析每个细节。
						
						root@ubuntu:~# pwd  (1)
						/root 

						root@ubuntu:~# ls   (2)
						Dockerfile   

						root@ubuntu:~# docker build -t ubuntu-with-vi-dockerfile .  (3)
						Sending build context to Docker daemon 32.26 kB     (4)
						Step 1 : FROM ubuntu									 (5)
						---> f753707788c5   
						Step 2 : RUN apt-get update && apt-get install -y vim    (6)
						---> Running in 9f4d4166f7e3                       (7)

						  ...
						
						Setting up vim (2:7.4.1689-3ubuntu1.1) ... 
						---> 35ca89798937                              (8)
						Removing intermediate container 9f4d4166f7e3    (9)
						Successfully built 35ca89798937  (10)
						root@ubuntu:~#  

						(1) 当前目录为 /root。

						(2) Dockerfile 准备就绪。 创建Dockerfile文件

						(3) 运行 docker build 命令，-t 将新镜像命名为 ubuntu-with-vi-dockerfile，
							命令末尾的 . 指明 build context 为当前目录。
							Docker 默认会从 build context 中查找 Dockerfile 文件，
							我们也可以通过 -f 参数指定 Dockerfile 的位置。

						(4)	从这步开始就是镜像真正的构建过程。 
							首先 Docker 将 build context 中的所有文件发送给 Docker daemon。
							build context 为镜像构建提供所需要的文件或目录。
							
							Dockerfile 中的 ADD、COPY 等命令可以将 build context 中的文件添加到镜像。
							此例中，build context 为当前目录 /root，
							该目录下的所有文件和子目录都会被发送给 Docker daemon。

							所以，使用 build context 就得小心了，不要将多余文件放到 build context，
							特别不要把 /、/usr 作为 build context，否则构建过程会相当缓慢甚至失败。

						(5) Step 1：执行 FROM，将 ubuntu 作为 base 镜像。
							ubuntu 镜像 ID 为 f753707788c5。

						(6) Step 2：执行 RUN，安装 vim，具体步骤为 ⑦、⑧、⑨。

						(7) 启动 ID 为 9f4d4166f7e3 的临时容器，在容器中通过 apt-get 安装 vim。

						(8) 安装成功后，将容器保存为镜像，其 ID 为 35ca89798937。
							这一步底层使用的是类似 docker commit 的命令。

						(9) 删除临时容器 9f4d4166f7e3。

						(10) 镜像构建成功。 

				通过 docker images 查看镜像信息。 

					root@zk-virtual-machine:/home/zk# docker images
					REPOSITORY                  TAG         IMAGE ID            CREATED             SIZE
					ubuntu-with-vi-dockerfile   latest      de6f4ab21567        20 hours ago        169MB
					httpd                       latest      55a118e2a010        13 days ago         132MB
					ubuntu                      latest      ea4c82dcd15a        2 weeks ago         85.8MB
					centos                      latest      75835a67d134        4 weeks ago         200MB
					hello-world                 latest      4ab4c602aa5e        2 months ago        1.84kB
				
				查看镜像分层结构：

					ubuntu-with-vi-dockerfile 是通过在 base 镜像的顶部添加一个新的镜像层而得到的。

					这个新镜像层的内容由 RUN apt-get update && apt-get install -y vim 生成。
					这一点我们可以通过 docker history 命令验证。
					
				root@zk-virtual-machine:/home/zk# docker history ubuntu
				IMAGE               CREATED             CREATED BY                                      SIZE 
				ea4c82dcd15a        2 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B
				<missing>           2 weeks ago         /bin/sh -c mkdir -p /run/systemd && echo do…   7B
				<missing>           2 weeks ago         /bin/sh -c rm -rf /var/lib/apt/lists/*          0B
				<missing>           2 weeks ago         /bin/sh -c set -xe   && echo '#!/bin/sh' > /…   745B
				<missing>           2 weeks ago         /bin/sh -c #(nop) ADD file:bcd068f67af2788db…   85.8MB 

				root@zk-virtual-machine:/home/zk# docker history ubuntu-with-vi-dockerfile
				IMAGE               CREATED             CREATED BY                                      SIZE  
				de6f4ab21567        20 hours ago        /bin/sh -c apt-get update && apt-get install…   83.3MB  
				ea4c82dcd15a        2 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B
				<missing>           2 weeks ago         /bin/sh -c mkdir -p /run/systemd && echo do…   7B  
				<missing>           2 weeks ago         /bin/sh -c rm -rf /var/lib/apt/lists/*          0B
				<missing>           2 weeks ago         /bin/sh -c set -xe   && echo '#!/bin/sh' > /…   745B
				<missing>           2 weeks ago         /bin/sh -c #(nop) ADD file:bcd068f67af2788db…   85.8MB


			docker history 会显示镜像的构建历史，也就是 Dockerfile 的执行过程。	
			
				ubuntu-with-vi-dockerfile 与 ubuntu 镜像相比，确实只是多了顶部的一层 de6f4ab21567，
				由 apt-get 命令创建，大小为 83.3MB。docker history 也向我们展示了镜像的分层结构，
				每一层由上至下排列。

				注：  表示无法获取 IMAGE ID，通常从 Docker Hub 下载的镜像会有这个问题。


	4.5 镜像的缓存特性:

		Docker 会缓存已有镜像的镜像层，构建新镜像时，如果某镜像层已经存在，就直接使用，无需重新创建。

		举例说明。
		在前面的 Dockerfile 中添加一点新内容，往镜像中复制一个文件：

			FROM ubuntu
			RUN apt-get update && apt-get install -y vim
			COPY testfile /

		root@ubuntu:~# ls              (1)
		Dockerfile  testfile
		root@ubuntu:~#
		root@ubuntu:~# docker build -t ubuntu-with-vi-dockerfile-2 .
		Sending build context to Docker daemon 32.77 kB
		Step 1 : FROM ubuntu
		---> f753707788c5
		Step 2 : RUN apt-get update && apt-get install -y vim
		---> Using cache               (2)
		---> 35ca89798937
		Step 3 : COPY testfile /        (3)
		---> 8d02784a78f4
		Removing intermediate container bf2b4040f4e9
		Successfully built 8d02784a78f4


		(1) 确保 testfile 已存在。

		(2) 重点在这里：之前已经运行过相同的 RUN 指令，这次直接使用缓存中的镜像层 35ca89798937。

		(3) 执行 COPY 指令。
			其过程是启动临时容器，复制 testfile，提交新的镜像层 8d02784a78f4，删除临时容器。
			在ubuntu-with-vi-dockerfile 镜像上直接添加一层就得到了新的镜像 ubuntu-with-vi-dockerfile-2。
		
		如果我们希望在构建镜像时不使用缓存，可以在 docker build 命令中加上 --no-cache 参数。
		
		Dockerfile 中每一个指令都会创建一个镜像层，上层是依赖于下层的。
		无论什么时候，只要某一层发生变化，其上面所有层的缓存都会失效。

		也就是说，如果我们改变 Dockerfile 指令的执行顺序，或者修改或添加指令，都会使缓存失效。

		举例说明，比如交换前面 RUN 和 COPY 的顺序：
			
			FROM ubuntu
			COPY testfile /
			RUN apt-get update && apt-get install -y vim

		虽然在逻辑上这种改动对镜像的内容没有影响，但由于分层的结构特性，Docker 必须重建受影响的镜像层。

			root@ubuntu:~# docker build -t ubuntu-with-vi-dockerfile-3 .
			Sending build context to Docker daemon 37.89 kB
			Step 1 : FROM ubuntu
			---> f753707788c5
			Step 2 : COPY testfile /
			---> bc87c9710f40
			Removing intermediate container 04ff324d6af5
			Step 3 : RUN apt-get update && apt-get install -y vim
			---> Running in 7f0fcb5ee373
			Get:1 http://archive.ubuntu.com/ubuntu xenial InRelease [247 kB]
			......

		从上面的输出可以看到生成了新的镜像层 bc87c9710f40，缓存已经失效。
		除了构建时使用缓存，Docker 在下载镜像时也会使用。
		

	4.6 调试 Dockerfile:

		包括Dockerfile 在内的任何脚本和程序都会出错。有错并不可怕，但必须有办法排查，
		所以本节讨论如何 debug Dockerfile。
	
		先回顾一下通过 Dockerfile 构建镜像的过程：

			(1) 从 base 镜像运行一个容器。

			(2) 执行一条指令，对容器做修改。

			(3) 执行类似 docker commit 的操作，生成一个新的镜像层。

			(4) Docker 再基于刚刚提交的镜像运行一个新容器。

			(5) 重复 2-4 步，直到 Dockerfile 中的所有指令执行完毕。

		从这个过程可以看出，如果 Dockerfile 由于某种原因执行到某个指令失败了，
		我们也将能够得到前一个指令成功执行构建出的镜像，这对调试 Dockerfile 非常有帮助。
		我们可以运行最新的这个镜像定位指令失败的原因。

		我们来看一个调试的例子。Dockerfile 内容如下：

			FROM  busybox
			RUN  touch tempfile
			RUN  /bin/bash -c echo "continue to build..."
			COPY testfile /

		执行 docker build:

			root@ubuntu:~# docker build -t image-debug .

			root@zk-virtual-machine:~# docker build -t image-debug .
			Sending build context to Docker daemon  12.29kB
			Step 1/4 : FROM busybox
			latest: Pulling from library/busybox
			90e01955edcd: Pull complete 
			Digest: sha256:2a03a6059f21e150ae84b0973863609494aad70f0a80eaeb64bddd8d92465812
			Status: Downloaded newer image for busybox:latest
			---> 59788edf1f3e
			Step 2/4 : RUN touch tmpfile
			---> Running in 4191f31e37dc
			Removing intermediate container 4191f31e37dc
			---> b49b56c46860
			Step 3/4 : RUN /bin/bash -c echo "continue to build ..."
			---> Running in 15461112c08a
			/bin/sh: /bin/bash: not found
			The command '/bin/sh -c /bin/bash -c echo "continue to build ..."' returned a non-zero code: 127

			Dockerfile 在执行第三步 RUN 指令时失败。
			我们可以利用第二步创建的镜像 4191f31e37dc 进行调试，方式是通过 docker run -it 启动镜像的一个容器。

			root@zk-virtual-machine:~# docker run -it b49b56c46860
			/ # 
			/ # /bin/sh -c /bin/bash -c echo "continue to build ..."
			sh: /bin/bash: not found
			/#

			手工执行 RUN 指令很容易定位失败的原因是 busybox 镜像中没有 bash。
			虽然这是个极其简单的例子，但它很好地展示了调试 Dockerfile 的方法。

			到这里相信大家对 Dockerfile 的功能和使用流程有了比较完整的印象，
			但还没有系统学习 Dockerfile 的各种指令和实际用法
	
	4.7 Dockerfile 常用指令：

		下面列出了 Dockerfile 中最常用的指令：

			FROM : 指定 base 镜像。

			MAINTAINER : 设置镜像的作者，可以是任意字符串。

			COPY : 将文件从 build context 复制到镜像。
		
				COPY 支持两种形式：

				1. COPY src dest
				2. COPY ["src", "dest"]
		
				注意：src 只能指定 build context 中的文件或目录。
		
			ADD: 与 COPY 类似，从 build context 复制文件到镜像。
				不同的是，如果 src 是归档文件（tar, zip, tgz, xz 等），文件会被自动解压到 dest。
		
			ENV : 设置环境变量，环境变量可被后面的指令使用。
				例如：
				...
				ENV MY_VERSION 1.3
				RUN apt-get install -y mypackage=$MY_VERSION
				...
		
		
			EXPOSE: 指定容器中的进程会监听某个端口，Docker 可以将该端口暴露出来。我们会在容器网络部分详细讨论。
		
			VOLUME: 将文件或目录声明为 volume。我们会在容器存储部分详细讨论。
		
			WORKDIR: 为后面的 RUN, CMD, ENTRYPOINT, ADD 或 COPY 指令设置镜像中的当前工作目录。
		
			RUN : 在容器中运行指定的命令。
		
			CMD : 容器启动时运行指定的命令。
				Dockerfile 中可以有多个 CMD 指令，但只有最后一个生效。
				CMD 可以被 docker run 之后的参数替换。
		
			ENTRYPOINT:	设置容器启动时运行的命令。
						Dockerfile 中可以有多个 ENTRYPOINT 指令，但只有最后一个生效。
						CMD 或 docker run 之后的参数会被当做参数传递给 ENTRYPOINT。
		
		下面我们来看一个较为全面的 Dockerfile：

			# my dockerfile

			FROM busybox						  "指定base镜像"
			MAINTAINER cloudman@example.net		  "设置镜像的作者"
			WORKDIR   /testdir					  "指令设置镜像中的当前工作目录,如果WORKDIR不存在，Docker会自动为我们创建"
			RUN   touch tmpfile1				  "创建tmpfile1文件"	
			COPY ["tmpfile2","."]                 "从build context 复制到当前工作目录"
			ADD ["buch.tar.gz","."]               "令从 build context 复制的归档文件 bunch.tar.gz已经自动解压。"
			ENV WELCOME "You are in my container,welcome!"  "设置环境变量"

			注：Dockerfile 支持以“#”开头的注释。

			构建前确保 build context 中存在需要的文件(buch.tar.gz、tempfile2、Dockerfile)。

			依次执行 Dockerfile 指令，完成构建。

	
	4.8 RUN vs CMD vs ENTRYPOINT:

		RUN、CMD 和 ENTRYPOINT 这三个 Dockerfile 指令看上去很类似，很容易混淆。
		本节将通过实践详细讨论它们的区别。简单的说：

			1. RUN 执行命令并创建新的镜像层，RUN 经常用于安装软件包。

			2. CMD 设置容器启动后默认执行的命令及其参数，但 CMD 能够被 docker run 后面跟的命令行参数替换。

			3. ENTRYPOINT 配置容器启动时运行的命令。

		Shell 和 Exec 格式:

			我们可用两种方式指定 RUN、CMD 和 ENTRYPOINT 要运行的命令：
			Shell 格式和 Exec 格式二者在使用上有细微的区别。

			Shell 格式:

				<instruction> <command>

				例如：

					RUN apt-get install python3  
					CMD echo "Hello world"  
					ENTRYPOINT echo "Hello world"

				当指令执行时，shell 格式底层会调用 /bin/sh -c <command> 。

				例如下面的 Dockerfile 片段：

					ENV name Cloud Man  
					ENTRYPOINT echo "Hello, $name"

				执行 docker run <image> 将输出：
					Hello, Cloud Man

				注意环境变量 name 已经被值 Cloud Man 替换。


			Exec 格式:

				<instruction> ["executable", "param1", "param2", ...]

				例如：

					RUN ["apt-get", "install", "python3"]  
					CMD ["/bin/echo", "Hello world"]  
					ENTRYPOINT ["/bin/echo", "Hello world"]

				当指令执行时，会直接调用 <command>，不会被 shell 解析。
				例如下面的 Dockerfile 片段：

					ENV name Cloud Man  
					ENTRYPOINT ["/bin/echo", "Hello, $name"]

				运行容器将输出：
					Hello, $name

				注意环境变量“name”没有被替换。
				如果希望使用环境变量，照如下修改

				ENV name Cloud Man  
				ENTRYPOINT ["/bin/sh", "-c", "echo Hello, $name"]
				运行容器将输出：
					Hello, Cloud Man
		
			CMD 和 ENTRYPOINT 推荐使用 Exec 格式，因为指令可读性更强，更容易理解。RUN 则两种格式都可以。
		
		RUN:

			RUN 指令通常用于安装应用和软件包。		
			
			RUN apt-get update && apt-get install -y \  
				bzr \
				cvs \
				git \
			    mercurial \
				subversion

			注意：apt-get update 和 apt-get install 被放在一个 RUN 指令中执行，
			这样能够保证每次安装的是最新的包。
			如果 apt-get install 在单独的 RUN 中执行，则会使用 apt-get update 创建的镜像层，
			而这一层可能是很久以前缓存的。

		CMD:

			CMD 指令允许用户指定容器的默认执行的命令。

			此命令会在容器启动且 docker run 没有指定其他命令时运行。

				1. 如果 docker run 指定了其他命令，CMD 指定的默认命令将被忽略。
				2. 如果 Dockerfile 中有多个 CMD 指令，只有最后一个 CMD 有效。

			CMD 有三种格式：

				1.  Exec 格式：CMD ["executable","param1","param2"]
					这是 CMD 的推荐格式。
				
				2. CMD ["param1","param2"] 为 ENTRYPOINT 提供额外的参数，此时 ENTRYPOINT 必须使用 Exec 格式。
				
				3. Shell 格式：CMD command param1 param2
			
			Exec 和 Shell 格式前面已经介绍过了。
			第二种格式 CMD ["param1","param2"] 要与 Exec 格式 的 ENTRYPOINT 指令配合使用，
			其用途是为 ENTRYPOINT 设置默认的参数。我们将在后面讨论 ENTRYPOINT 时举例说明。

			下面看看 CMD 是如何工作的。Dockerfile 片段如下：

				CMD echo "Hello world"
			运行容器 docker run -it [image] 将输出：
				Hello world
			但当后面加上一个命令，比如 docker run -it [image] /bin/bash，CMD 会被忽略掉，命令 bash 将被执行：
			root@10a32dc7d3d3:/#
		

		ENTRYPOINT:

			ENTRYPOINT 指令可让容器以应用程序或者服务的形式运行。

			ENTRYPOINT 看上去与 CMD 很像，它们都可以指定要执行的命令及其参数。
			不同的地方在于 ENTRYPOINT 不会被忽略，一定会被执行，即使运行 docker run 时指定了其他命令。
	
			ENTRYPOINT 有两种格式：
				1. Exec 格式：ENTRYPOINT ["executable", "param1", "param2"] 这是 ENTRYPOINT 的推荐格式。
				2. Shell 格式：ENTRYPOINT command param1 param2

			在为 ENTRYPOINT 选择格式时必须小心，因为这两种格式的效果差别很大。

			Exec 格式:

				ENTRYPOINT 的 Exec 格式用于设置要执行的命令及其参数，同时可通过 CMD 提供额外的参数。
				ENTRYPOINT 中的参数始终会被使用，而 CMD 的额外参数可以在容器启动时动态替换掉。

				比如下面的 Dockerfile 片段：

					ENTRYPOINT ["/bin/echo", "Hello"]  
				
					CMD ["world"]
				
				当容器通过 docker run -it [image] 启动时，输出为：
					Hello world
		
				而如果通过 docker run -it [image] CloudMan 启动，则输出为：
				
					Hello CloudMan

			Shell 格式:

				ENTRYPOINT 的 Shell 格式会忽略任何 CMD 或 docker run 提供的参数。

			最佳实践:

				使用 RUN 指令安装应用和软件包，构建镜像。

				如果 Docker 镜像的用途是运行应用程序或服务，
				比如运行一个 MySQL，应该优先使用 Exec 格式的 ENTRYPOINT 指令。
				CMD 可为 ENTRYPOINT 提供额外的默认参数，同时可利用 docker run 命令行替换默认参数。

				如果想为容器设置默认的启动命令，可使用 CMD 指令。用户可在 docker run 命令行中替换此默认命令。

				到这里，我们已经具备编写 Dockerfile 的能力了。如果大家还觉得没把握，
				推荐一个快速掌握 Dockerfile 的方法：去 Docker Hub 上参考那些官方镜像的 Dockerfile。

	4.9 镜像命名最佳实践：

		我们已经学会构建自己的镜像了。接下来的问题是如何在多个 Docker Host 上使用镜像。

			1. 用相同的 Dockerfile 在其他 host 构建镜像。
			2. 将镜像上传到公共 Registry（比如 Docker Hub），Host 直接下载使用。
			3. 搭建私有的 Registry 供本地 Host 使用。

		第一种方法没什么特别的，前面已经讨论很多了。我们将讨论如何使用公共和私有 Registry 分发镜像。

		为镜像命名:

			无论采用何种方式保存和分发镜像，首先都得给镜像命名。
			当我们执行 docker build 命令时已经为镜像取了个名字，例如前面：
			docker build -t ubuntu-with-vi-dockerfile
			这里的 ubuntu-with-vi 就是镜像的名字。通过 dock images 可以查看镜像的信息。

			root@zk-virtual-machine:~# docker images  ubuntu-with-vi-dockerfile
			REPOSITORY                  TAG                 IMAGE ID            CREATED             SIZE
			ubuntu-with-vi-dockerfile   latest              de6f4ab21567        40 hours ago        169MB

			这里注意到 ubuntu-with-vi-dockerfile 对应的是 REPOSITORY，而且还有一个叫 latest 的 TAG。
			
			实际上一个特定镜像的名字由两部分组成：repository 和 tag。
			[image name] = [repository]:[tag]

			如果执行 docker build 时没有指定 tag，会使用默认值 latest。其效果相当于：
			docker build -t ubuntu-with-vi:latest
			tag 常用于描述镜像的版本信息。

			小心 latest tag
			千万别被 latest tag 给误导了。latest 其实并没有什么特殊的含义。
			当没指明镜像 tag 时，Docker 会使用默认值 latest，仅此而已。

			虽然 Docker Hub 上很多 repository 将 latest 作为最新稳定版本的别名，
			但这只是一种约定，而不是强制规定。

			所以我们在使用镜像时最好还是避免使用latest明确指定某个 tag，比如 httpd:2.3，ubuntu:xenial。

			tag 使用最佳实践：

				借鉴软件版本命名方式能够让用户很好地使用镜像。
				一个高效的版本命名方案可以让用户清楚地知道当前使用的是哪个镜像，同时还可以保持足够的灵活性。
				每个 repository 可以有多个 tag，而多个 tag 可能对应的是同一个镜像。
				下面通过例子为大家介绍 Docker 社区普遍使用的 tag 方案。
				假设我们现在发布了一个镜像 myimage，版本为 v1.9.1。
				那么我们可以给镜像打上四个 tag：1.9.1、1.9、1 和 latest。

				我们可以通过 docker tag 命令方便地给镜像打 tag。
				docker tag myimage-v1.9.1 myimage:1
				docker tag myimage-v1.9.1 myimage:1.9
				docker tag myimage-v1.9.1 myimage:1.9.1
				docker tag myimage-v1.9.1 myimage:latest

				过了一段时间，我们发布了 v1.9.2。这时可以打上 1.9.2 的 tag，
				并将 1.9、1 和 latest 从 v1.9.1 移到 v1.9.2。
				
				命令为：
				docker tag myimage-v1.9.2 myimage:1
				docker tag myimage-v1.9.2 myimage:1.9
				docker tag myimage-v1.9.2 myimage:1.9.2
				docker tag myimage-v1.9.2 myimage:latest
				
				这种 tag 方案使镜像的版本很直观，用户在选择非常灵活：

				myimage:1 始终指向 1 这个分支中最新的镜像。
				myimage:1.9 始终指向 1.9.x 中最新的镜像。
				myimage:latest 始终指向所有版本中最新的镜像。
				如果想使用特定版本，可以选择 myimage:1.9.1、myimage:1.9.2 或 myimage:2.0.0。

				Docker Hub 上很多 repository 都采用这种方案，所以大家一定要熟悉。

	4.10 公用Registry:

		保存和分发镜像的最直接方法就是使用 Docker Hub。

		Docker Hub 是 Docker 公司维护的公共 Registry。
		用户可以将自己的镜像保存到 Docker Hub 免费的 repository 中。
		如果不希望别人访问自己的镜像，也可以购买私有 repository。

		除了 Docker Hub，quay.io 是另一个公共 Registry，提供与 Docker Hub 类似的服务。
		
		下面介绍如何用 Docker Hub 存取我们的镜像。

			1. 首先得在 Docker Hub 上注册一个账号。

			2. 在 Docker Host 上登录。

				root@zk-virtual-machine:~# docker login -u zhangkun09211916
				Password: 
				WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
				Configure a credential helper to remove this warning. See
				https://docs.docker.com/engine/reference/commandline/login/#credentials-store

				Login Succeeded

			3. 修改镜像的 repository 使之与 Docker Hub 账号匹配。

				Docker Hub 为了区分不同用户的同名镜像，
				镜像的 registry 中要包含用户名，完整格式为：[username]/xxx:tag
				我们通过 docker tag 命令重命名镜像。

				root@zk-virtual-machine:~# docker tag httpd zhangkun09211916/httpd:v1
				root@zk-virtual-machine:~# docker images zhangkun09211916/httpd:v1
				REPOSITORY               TAG                 IMAGE ID            CREATED             SIZE
				zhangkun09211916/httpd   v1                  55a118e2a010        2 weeks ago         132MB
				root@zk-virtual-machine:~# 


				注：Docker 官方自己维护的镜像没有用户名，比如 httpd。

			4. 通过 docker push 将镜像上传到 Docker Hub。
				
				Docker 会上传镜像的每一层。
				因为 cloudman6/httpd:v1 这个镜像实际上跟官方的 httpd 镜像一模一样，
				Docker Hub 上已经有了全部的镜像层，所以真正上传的数据很少。
				同样的，如果我们的镜像是基于 base 镜像的，也只有新增加的镜像层会被上传。
				如果想上传同一 repository 中所有镜像，省略 tag 部分就可以了，
				例如：
				 
				root@zk-virtual-machine:~# docker push zhangkun09211916/httpd:v1
				The push refers to repository [docker.io/zhangkun09211916/httpd]
				d8e904686bfd: Mounted from library/httpd 
				584c122df5a0: Mounted from library/httpd 
				355bd981febe: Mounted from library/httpd 
				504b6a6a6fd2: Mounted from library/httpd 
				237472299760: Mounted from library/httpd 
				v1: digest: sha256:cd6abe0e1cae37c81a53486f216379c59aae8f9ea790923f23dcf7542853e895 size: 1367
				root@zk-virtual-machine:~# 

			5. 登录 https://hub.docker.com，在Public Repository 中就可以看到上传的镜像.
				如果要删除上传的镜像，只能在 Docker Hub 界面上操作。

			6. 这个镜像可被其他 Docker host 下载使用了。 
				
				root@zk-virtual-machine:~#docker pull zhangkun09211916/httpd:v1

	4.11 搭建本地 Registry:

		Docker Hub 虽然非常方便，但还是有些限制，比如：

			1. 需要 internet 连接，而且下载和上传速度慢。
			2. 上传到 Docker Hub 的镜像任何人都能够访问，虽然可以用私有 repository，但不是免费的。
			3. 安全原因很多组织不允许将镜像放到外网。
		
		解决方案就是搭建本地的 Registry。
		
			Docker 已经将 Registry 开源了，同时在 Docker Hub 上也有官方的镜像 registry。
			下面我们就在 Docker 中运行自己的 registry。

			1. 启动 registry 容器。

				root@ubuntu:~# docker run -d -p 5000:5000 -v /myregistry:/var/lib/registry registry:2

				我们使用的镜像是 registry:2。
				-d 是后台启动容器。
				-p 将容器的 5000 端口映射到 Host 的 5000 端口。5000 是 registry 服务端口。
					端口映射我们会在容器网络章节详细讨论。
				-v 将容器 /var/lib/registry 目录映射到 Host 的 /myregistry，用于存放镜像数据。
				-v 的使用我们会在容器存储章节详细讨论。

			2. 通过 docker tag 重命名镜像，使之与 registry 匹配。

				root@ubuntu:~# docker tag zhangkun09211916/httpd:v1 registry.example.net:5000/zhangkun09211916/httpd:v1
				我们在镜像的前面加上了运行 registry 的主机名称和端口。

				前面已经讨论了镜像名称由 repository 和 tag 两部分组成。
				而 repository 的完整格式为：[registry-host]:[port]/[username]/xxx
				
				只有 Docker Hub 上的镜像可以省略 [registry-host]:[port] 。

			3. 通过 docker push 上传镜像。

				root@ubuntu:~# docker push  registry.example.net:5000/zhangkun09211916/httpd:v1          

			4. 现在已经可通过 docker pull 从本地 registry 下载镜像了。

				root@ubuntu:~#docker pull registry.example.net:5000/zhangkun09211916/httpd:v1  

			以上是搭建本地 registry 的简要步骤。当然 registry 也支持认证，https 安全传输等特性，
			具体可以参考官方文档 https://docs.docker.com/registry/configuration/
	
	4.12  Docker 镜像小结:

		这一部分我们首先讨论了镜像的分层结构，然后学习了如何构建镜像，
		最后实践使用 Docker Hub 和本地 registry。
	
		下面是镜像的常用操作子命令：

			images    显示镜像列表
			history   显示镜像构建历史

			commit    从容器创建新镜像
			build     从 Dockerfile 构建镜像
		
			tag       给镜像打 tag

			pull      从 registry 下载镜像
			push      将 镜像 上传到 registry

			rmi       删除 Docker host 中的镜像
			search    搜索 Docker Hub 中的镜像

		除了 rmi 和 search，其他命令都已经用过了。

			rmi 
				只能删除 host 上的镜像，不会删除 registry 的镜像。

				如果一个镜像对应了多个 tag，只有当最后一个 tag 被删除时，镜像才被真正删除。
				例如 host 中 debian 镜像有两个 tag：

			search:

				search 让我们无需打开浏览器，在命令行中就可以搜索 Docker Hub 中的镜像。

				root@ubuntu:~# docker search httpd

5、容器：

	我们学习了如何构建 Docker 镜像，并通过镜像运行容器。
	本章将深入讨论容器：学习容器的各种操作，容器各种状态之间如何转换，以及实现容器的底层技术。

	5.1 如何运行容器：

		docker run 是启动容器的方法。
		在讨论 Dockerfile 时我们已经学习到，可用三种方式指定容器启动时执行的命令：

			1. CMD 指令

			2. ENTRYPOINT 指令

			3. 在docker run 命令行中指定。

		例如下面的例子：
		
			root@zk-virtual-machine:~# docker run ubuntu pwd
			/
			root@zk-virtual-machine:~# 

		容器启动时执行 pwd，返回的 / 是容器中的当前目录。 
		执行docker ps或docker container ls 可以查看Docker host中当前运行的容器：

			root@zk-virtual-machine:~# docker ps
			CONTAINER ID        IMAGE   COMMAND    CREATED      STATUS      PORTS        NAMES
			a82555f4986f        httpd   "httpd-foreground"   46 hours ago Up 46 hours         0.0.0.0:80->80/tcp   agitated_sammet

		怎么没有容器？用 docker ps -a 或 docker container ls -a 看看。

			root@zk-virtual-machine:~# docker ps -a
			CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS                NAMES
			a19ce8409ead        ubuntu              "pwd"                    2 minutes ago       Exited (0) 2 minutes ago                         cocky_hamilton
			e14f3e6bdb79        b49b56c46860        "sh"                     21 hours ago        Exited (130) 21 hours ago                        goofy_clarke
			15461112c08a        b49b56c46860        "/bin/sh -c '/bin/ba…"   21 hours ago        Exited (127) 21 hours ago                        stoic_bose
			b268b625358e        ubuntu              "/bin/bash"              25 hours ago        Exited (100) 22 hours ago                        zen_lewin
			6ddb67368e71        ubuntu              "/bin/bash"              25 hours ago        Exited (0) 25 hours ago                          kind_ride
			ae7186116373        centos              "/bin/bash"              25 hours ago        Exited (0) 25 hours ago                          angry_ardinghelli
			4592ec02e89b        hello-world         "/hello"                 26 hours ago        Exited (0) 26 hours ago                          cocky_noether
			e57e23f06daa        centos              "/bin/bash"              44 hours ago        Exited (127) 44 hours ago                        brave_gates
			a76762160ae8        hello-world         "/hello"                 45 hours ago        Exited (0) 45 hours ago                          elegant_yalow
			8609f530f520        hello-world         "/hello"                 45 hours ago        Exited (0) 45 hours ago                          stupefied_villani
			a82555f4986f        httpd               "httpd-foreground"       46 hours ago        Up 46 hours                 0.0.0.0:80->80/tcp   agitated_sammet

		-a 会显示所有状态的容器，可以看到，之前的容器已经退出了，状态为Exited。

		这种“一闪而过”的容器通常不是我们想要的结果，我们希望容器能够保持 runing 状态，这样才能被我们使用。

		
		让容器长期运行:

			如何让容器保存运行呢？
			因为容器的生命周期依赖于启动时执行的命令，只要该命令不结束，容器也就不会退出。
			理解了这个原理，我们就可以通过执行一个长期运行的命令来保持容器的运行状态。例如执行下面的命令：

			root@ubuntu:~# docker run ubuntu /bin/bash -c "while true;do sleep 1;done"

			while 语句让 bash 不会退出。我们可以打开另一个终端查看容器的状态：

			可见容器仍处于运行状态。不过这种方法有个缺点：它占用了一个终端。

			我们可以加上参数 -d 以后台方式启动容器。

			root@ubuntu:~# docker run -d unbuntu /bin/bash -c "while true;do sleep 1;done"

			容器启动后回到了 docker host 的终端。
			这里看到 docker 返回了一串字符，这是容器的 ID。通过 docker ps 查看容器：


			现在我们有了两个正在运行的容器。这里注意一下容器的 CONTAINER ID和 NAMES 这两个字段。

			CONTAINER ID 是容器的 “短ID”，前面启动容器时返回的是 “长ID”。短ID是长ID的前12个字符。

			NAMES 字段显示容器的名字，在启动容器时可以通过 --name 参数显示地为容器命名，
			如果不指定，docker 会自动为容器分配名字。

			对于容器的后续操作，我们需要通过"长ID","短ID"或者"名称"来指定要操作的容器。
			
			比如下面停止一个容器：

			root@ubuntu:~# docker stop fe39cc3ccc5b

			这里我们就是通过 “短ID” 指定了要停止的容器

			通过 while 启动的容器虽然能够保持运行，但实际上没有干什么有意义的事情。
			容器常见的用途是运行后台服务，例如前面我们已经看到的 http server：
			

			这一次我们用 --name 指定了容器的名字。 我们还看到容器运行的命令是httpd-foreground，
			通过 docker history 可知这个命令是通过 CMD 指定的。

			root@zk-virtual-machine:~# docker run --name "my_http_server" -d httpd
			229d6290867189f35029a405399c09b3d13b1f51ad9b27d4be4bb6ba2f5a4495
			root@zk-virtual-machine:~# 
			root@zk-virtual-machine:~# 
			root@zk-virtual-machine:~# docker ps
			CONTAINER ID   IMAGE   COMMAND   CREATED   STATUS       PORTS            NAMES
			229d62908671   httpd "httpd-foreground"   4 seconds ago Up 2 seconds 80/tcp     my_http_server
			
			root@zk-virtual-machine:~# docker history httpd
			IMAGE               CREATED             CREATED BY                                  SIZE COMMENT
			55a118e2a010        2 weeks ago         /bin/sh -c #(nop)  CMD ["httpd-foreground"]     0B
			<missing>           2 weeks ago         /bin/sh -c #(nop)  EXPOSE 80/tcp                0B          
			<missing>           2 weeks ago         /bin/sh -c #(nop) COPY file:761e313354b918b6…   133B         
			
			我们经常需要进到容器里去做一些工作，比如查看日志、调试、启动其他进程等。

	5.2 如何进入容器内部:

		我们经常需要进到容器里去做一些工作，比如查看日志、调试、启动其他进程等。
		有两种方法进入容器：attach 和 exec。
		
		docker attach:

			通过 docker attach 可以 attach 到容器启动命令的终端，例如：

			root@zk-virtual-machine:~#docker run -d ubuntu /bin/bash -c "while true;do sleep1;echo I_am_in_container;done"
			ed7d16aabc34c230bbf2526d3086b798cd620cc5f6d1bd2a51fe8c81663a4396
			root@zk-virtual-machine:docker attach ed7d16aabc34c230bbf2526d3086b798cd620cc5f6d1bd2a51fe8c81663a4396
			I_am_in_container
			I_am_in_container
			I_am_in_container
			I_am_in_container

			这次我们通过 “长ID” attach 到了容器的启动命令终端，之后看到的是echo 每隔一秒打印的信息。
			注：可通过 Ctrl+p 然后 Ctrl+q 组合键退出 attach 终端。

		docker exec:

			通过 docker exec 进入相同的容器：

			root@ubuntu:~# docker exec -it 969fac2f0e41 bash (1)
			root@969fac2f0e41:/#		(2)
			root@969fac2f0e41:/# ps -elf (3)
			...
			root@969fac2f0e41:/#exit		(4)
			root@ubuntu:~#


			(1) -it 以交互模式打开 pseudo-TTY，执行 bash，其结果就是打开了一个 bash 终端。
			(2) 进入到容器中，容器的 hostname 就是其 “短ID”。
			(3) 可以像在普通 Linux 中一样执行命令。ps -elf 显示了容器启动进程while 以及当前的 bash 进程。
			(4) 执行 exit 退出容器，回到 docker host。

			docker exec -it <container> bash|sh 是执行 exec 最常用的方式。

		attach VS exec:

			attach 直接进入容器 启动命令 的终端，不会启动新的进程。

			exec 则是在容器中打开新的终端，并且可以启动新的进程。

			如果想直接在终端中查看启动命令的输出，用 attach；其他情况使用 exec。

			当然，如果只是为了查看启动命令的输出，可以使用 docker logs 命令：

			root@ubuntu:~#docker logs -f 969fac2f0e41

			f 的作用与 tail -f 类似，能够持续打印输出。


	5.3  运行容器的最佳实践:

		按用途容器大致可分为两类：服务类容器和工具类的容器。

		1. 服务类容器以 daemon 的形式运行，对外提供服务。比如 web server，数据库等。
			通过 -d 以后台方式启动这类容器是非常合适的。
			如果要排查问题，可以通过 exec -it 进入容器。
	
		2. 工具类容器通常给能我们提供一个临时的工作环境，通常以 run -it 方式运行，
			比如：

			root@zk-virtual-machine:~# docker run -it busybox
			/ # wget www.baidu.com
			Connecting to www.baidu.com (104.193.88.77:80)index.html           100% |*******|  2381  0:00:00 ETA
			/ # exit
			root@zk-virtual-machine:~# 

			运行 busybox，run -it 的作用是在容器启动后就直接进入。
			我们这里通过 wget 验证了在容器中访问 internet 的能力。
			执行 exit 退出终端，同时容器停止。

			工具类容器多使用基础镜像，例如 busybox、debian、ubuntu 等。

		3. 容器运行相关的知识点：

				当 CMD 或 Entrypoint 或 docker run 命令行指定的命令运行结束时，容器停止。

				通过 -d 参数在后台启动容器。

				通过 exec -it 可进入容器并执行命令。

			指定容器的三种方法：

				短ID。
	
				长ID。

				容器名称。 可通过 --name 为容器命名。重命名容器可执行docker rename。

			容器按用途可分为两类：

				服务类的容器。

				工具类的容器

	5.4 容器的其他操作:

		stop/start/restart 容器

		1. 通过 docker stop 可以停止运行的容器。
			
			容器在 docker host 中实际上是一个进程，docker stop 命令本质上是向该进程发送一个 SIGTERM 信号。
			如果想快速停止容器，可使用 docker kill 命令，其作用是向容器进程发送 SIGKILL 信号。

		2. 对于处于停止状态的容器，可以通过 docker start 重新启动

			docker start 会保留容器的第一次启动时的所有参数。
			docker restart 可以重启容器，其作用就是依次执行 docker stop 和docker start。

			容器可能会因某种错误而停止运行。对于服务类容器，我们通常希望在这种情况下容器能够自动重启。
			启动容器时设置 --restart 就可以达到这个效果。

			root@ubuntu:~# docker run -d --restart=always httpd

			--restart=always 意味着无论容器因何种原因退出（包括正常退出），就立即重启。
			该参数的形式还可以是 --restart=on-failure:3，意思是如果启动进程退出代码非0，则重启容器，最多重启3次。

		3. pause/unpause 容器

			有时我们只是希望暂时让容器暂停工作一段时间，比如要对容器的文件系统打个快照，
			或者 dcoker host 需要使用 CPU，这时可以执行 docker pause。

			处于暂停状态的容器不会占用 CPU 资源，直到通过 docker unpause 恢复运行。

		4. 删除容器

			root@ubuntu:~#docker ps -a

			使用 docker 一段时间后，host 上可能会有大量已经退出了的容器。
			
			这些容器依然会占用 host 的文件系统资源，如果确认不会再重启此类容器，可以通过 docker rm 删除。

			docker rm 一次可以指定多个容器，如果希望批量删除所有已经退出的容器，可以执行如下命令：

			root@ubuntu:~# docker rm -v $(docker ps -aq -f status=exited)

			顺便说一句：docker rm 是删除容器，而 docker rmi 是删除镜像。

	5.5 容器的各种状态：

		容器大致有：create、running、paused、stopped、deleted记住状态。

		1. 可以先创建容器，稍后再启动。

			docker create 创建的容器处于 Created 状态。
			docker start 将以后台方式启动容器。 
			
			docker run 命令实际上是 docker create 和 docker start 的组合。

		2. 只有当容器的启动进程 退出 时，--restart 才生效。 

			退出包括正常退出或者非正常退出。
			
			这里举了两个例子：启动进程正常退出或发生 OOM，
			此时 docker会根据 --restart的策略判断是否需要重启容器。
			但如果容器是因为执行 docker stop 或docker kill 退出，则不会自动重启

	5.6	限制容器对内存使用：

		一个 docker host 上会运行若干容器，每个容器都需要 CPU、内存和 IO 资源。
		对于 KVM，VMware 等虚拟化技术，用户可以控制分配多少 CPU、内存资源给每个虚拟机。
		对于容器，Docker 也提供了类似的机制避免某个容器因占用太多资源而影响其他容器乃至整个 host 的性能。

		1. 内存限额:

			与操作系统类似，容器可使用的内存包括两部分：物理内存和 swap。 
			Docker 通过下面两组参数来控制容器内存的使用量。

				-m 或 --memory：设置内存的使用限额，例如 100M, 2G。

				--memory-swap：设置 内存+swap 的使用限额。
			
			当我们执行如下命令：

				docker run -m 200M --memory-swap=300M ubuntu

				其含义是允许该容器最多使用 200M 的内存和 100M 的 swap。
				默认情况下，上面两组参数为 -1，即对容器内存和 swap 的使用没有限制。

			下面我们将使用 progrium/stress 镜像来学习如何为容器分配内存。
			该镜像可用于对容器执行压力测试。执行如下命令：

				docker run -it -m 200M --memory-swap=300M progrium/stress --vm 1 --vm-bytes 280M

				--vm 1：启动 1 个内存工作线程。

				--vm-bytes 280M：每个线程分配 280M 内存。
			因为 280M 在可分配的范围（300M）内，所以工作线程能够正常工作，其过程是：
				分配 280M 内存。
				释放 280M 内存。
				再分配 280M 内存。
				再释放 280M 内存。
				一直循环......

			如果让工作线程分配的内存超过 300M，结果如下：
				分配的内存超过限额，stress 线程报错，容器退出。
				如果在启动容器时只指定 -m 而不指定 --memory-swap，那么 --memory-swap 默认为 -m 的两倍，比如：
				docker run -it -m 200M ubuntu
				容器最多使用 200M 物理内存和 200M swap。
	
	5.7 限制容器对 CPU 资源的使用:

			默认设置下，所有容器可以平等地使用 host CPU 资源并且没有限制。

			Docker 可以通过 -c 或 --cpu-shares 设置容器使用 CPU 的权重。如果不指定，默认值为 1024。

			与内存限额不同，通过 -c 设置的 cpu share 并不是 CPU 资源的绝对数量，而是一个相对的权重值。
			某个容器最终能分配到的 CPU 资源取决于它的 cpu share 占所有容器 cpu share 总和的比例。

			换句话说：通过 cpu share 可以设置容器使用 CPU 的优先级。

			比如在 host 中启动了两个容器：
			docker run --name "container_A" -c 1024 ubuntu
			docker run --name "container_B" -c 512 ubuntu
			
			container_A 的 cpu share 1024，是 container_B 的两倍。
			当两个容器都需要 CPU 资源时，container_A 可以得到的 CPU 是 container_B 的两倍

			需要特别注意的是，这种按权重分配 CPU 只会发生在 CPU 资源紧张的情况下。
			如果 container_A 处于空闲状态，这时，为了充分利用 CPU 资源，container_B 也可以分配到全部可用的 CPU。

			下面我们继续用 progrium/stress 做实验。

				1. 启动 container_A，cpu share 为 1024： 

					root@ubuntu:~# docker run --name container_A -it -c 1024 progrium/stress --pu 1

					--cpu 用来设置工作线程的数量。
					因为当前 host 只有 1 颗 CPU，所以一个工作线程就能将 CPU 压满。
					如果 host 有多颗 CPU，则需要相应增加 --cpu 的数量。

				2. 启动 container_B，cpu share 为 512： 

					root@ubuntu:~# docker run --name container_B -it -c 512 progrium/stress --pu 1

				3. 在 host 中执行 top，查看容器对 CPU 的使用情况： 

				4. 现在暂停 container_A： 

					root@ubuntu:~# docker pause container_A

				5. top 显示 container_B 在 container_A 空闲的情况下能够用满整颗 CPU： 

	5.8 限制容器对 Block IO 带宽资源的使用:

		Block IO 是另一种可以限制容器使用的资源。
		Block IO 指的是磁盘的读写，docker 可通过设置权重、限制 bps 和 iops 的方式控制容器读写磁盘的带宽，
		下面分别讨论。

		注：目前 Block IO 限额只对 direct IO（不使用文件缓存）有效。

		1. block IO 权重:

			默认情况下，所有容器能平等地读写磁盘，可以通过设置 --blkio-weight 参数来改变容器 block IO 的优先级。

			--blkio-weight 与 --cpu-shares 类似，设置的是相对权重值，默认为 500。
			在下面的例子中，container_A 读写磁盘的带宽是 container_B 的两倍

			docker run -it --name container_A --blkio-weight 600 ubuntu   
			docker run -it --name container_B --blkio-weight 300 ubuntu

		2. 限制 bps 和 iops:

			bps 是 byte per second，每秒读写的数据量。
			iops 是 io per second，每秒 IO 的次数。

			可通过以下参数控制容器的 bps 和 iops：
			--device-read-bps，限制读某个设备的 bps。
			--device-write-bps，限制写某个设备的 bps。
			--device-read-iops，限制读某个设备的 iops。
			--device-write-iops，限制写某个设备的 iops。

			下面这个例子限制容器写 /dev/sda 的速率为 30 MB/s
				docker run -it --device-write-bps /dev/sda:30MB ubuntu

			通过 dd 测试在容器中写磁盘的速度。因为容器的文件系统是在 host /dev/sda 上的，
			在容器中写文件相当于对 host /dev/sda 进行写操作。
			另外，oflag=direct 指定用 direct IO 方式写文件，这样 --device-write-bps 才能生效。

			root@ubuntu:~# docker run -it --device-write-bps /dev/sda:30MB ubuntu
			root@fdfff2033d:/#
			root@fdfff2033d:/#time dd if=/dev/zero of=test.out bs=1M count=800 oflag=dirct

			结果表明，bps 25.6 MB/s 没有超过 30 MB/s 的限速。

			作为对比测试，如果不限速，结果如下：
			root@ubuntu:~# docker run -it  ubuntu
			root@fdfff2033d:/
			root@fdfff2033d:/#time dd if=/dev/zero of=test.out bs=1M count=800 oflag=dirct

	5.9 容器的底层实现技术

		cgroup 和 namespace 是最重要的两种技术。cgroup 实现资源限额， namespace 实现资源隔离

		1.cgroup:

			cgroup 全称 Control Group。
			Linux 操作系统通过 cgroup 可以设置进程使用 CPU、内存 和 IO 资源的限额。
			相信你已经猜到了：前面我们看到的--cpu-shares、-m、--device-write-bps 实际上就是在配置 cgroup。	

			cgroup 到底长什么样子呢？我们可以在 /sys/fs/cgroup 中找到它。
			还是用例子来说明，启动一个容器，设置 --cpu-shares=512：

			root@ububtu:~#docker run -it --cpu-shares 512 progrium/stress -c 1
			查看容器的 ID：
			在/sys/fs/cgroup/cpu/docker目录中,Linux会为每个容器创建一个cgroup目录，以容器长ID 命名：
			目录中包含所有与 cpu 相关的 cgroup 配置，文件 cpu.shares 保存的就是 --cpu-shares 的配置，值为 512。
			同样的/sys/fs/cgroup/memory/docker和/sys/fs/cgroup/blkio/docker中保存的是内存以及Block IO的cgroup配置

		2. namespace:

			在每个容器中，我们都可以看到文件系统，网卡等资源，这些资源看上去是容器自己的。
			拿网卡来说，每个容器都会认为自己有一块独立的网卡，即使 host 上只有一块物理网卡。
			这种方式非常好，它使得容器更像一个独立的计算机。
			
			Linux 实现这种方式的技术是 namespace。namespace 管理着 host 中全局唯一的资源，
			并可以让每个容器都觉得只有自己在使用它。换句话说，namespace 实现了容器间资源的隔离。

			Linux 使用了六种 namespace，分别对应六种资源：Mount、UTS、IPC、PID、Network和User下面我们分别讨论。

			a. Mount namespace
			
				Mount namespace 让容器看上去拥有整个文件系统。

				容器有自己的 / 目录，可以执行 mount 和 umount 命令。
				当然我们知道这些操作只在当前容器中生效，不会影响到 host 和其他容器。

			b. UTS namespace

				简单的说，UTS namespace 让容器有自己的 hostname。 
				默认情况下，容器的 hostname 是它的短ID，可以通过 -h 或 --hostname 参数设置。
				root@ububtu:~#docker run -h myhost -it ubuntu

			c. IPC namespace

				IPC namespace 让容器拥有自己的共享内存和信号量（semaphore）来实现进程间通信，
				而不会与 host 和其他容器的 IPC 混在一起。

			d. PID namespace

				我们前面提到过，容器在 host 中以进程的形式运行。例如当前 host 中运行了两个容器：
				通过 ps axf 可以查看容器进程：
				所有容器的进程都挂在 dockerd 进程下，同时也可以看到容器自己的子进程。
				如果我们进入到某个容器，ps 就只能看到自己的进程了：
				
				而且进程的 PID 不同于 host 中对应进程的 PID，容器中 PID=1 的进程当然也不是 host 的 init 进程。
				也就是说：容器拥有自己独立的一套 PID，这就是 PID namespace 提供的功能。

			e. Network namespace

				Network namespace 让容器拥有自己独立的网卡、IP、路由等资源。我们会在后面网络章节详细讨论。

			f. User namespace

				User namespace 让容器能够管理自己的用户，host 不能看到容器中创建的用户。

		小结

			本章首先通过大量实验学习了容器的各种操作以及容器状态之间如何转换，
			然后讨论了限制容器使用 CPU、内存和 Block IO 的方法，
			最后学习了实现容器的底层技术：cgroup 和 namespace。
	
			下面是容器的常用操作命令：

				create      创建容器  
				run         运行容器  
				pause       暂停容器  
				unpause     取消暂停继续运行容器  
				stop        发送 SIGTERM 停止容器  
				kill        发送 SIGKILL 快速停止容器  
				start       启动容器  
				restart     重启容器  
				attach      attach 到容器启动进程的终端  
				exec        在容器中启动新进程，通常使用 "-it" 参数  
				logs        显示容器启动进程的控制台输出，用 "-f" 持续打印  
				rm          从磁盘中删除容器

6、Docker 网络

	我们会首先学习Docker提供的几种原生网络，以及如何创建自定义网络。
	然后探讨容器之间如何通信，以及容器与外界如何交互。

	Docker 网络从覆盖范围可分为单个 host 上的容器网络和跨多个 host 的网络，本章重点讨论前一种。
	对于更为复杂的多 host 容器网络，我们会在后面进阶技术章节单独讨论。

	Docker 安装时会自动在 host 上创建三个网络，我们可用 docker network ls 命令查看：

		[root@iz2ze0lvzs717097h32rpcz ~]# docker network ls
		NETWORK ID          NAME                DRIVER              SCOPE
		b6b0664a7260        bridge              bridge              local
		fbefa9342c84        host                host                local
		7c5a4eaacb63        none                null                local

	1、none 网络:

		故名思议，none 网络就是什么都没有的网络。
		挂在这个网络下的容器除了lo，没有其他任何网卡。
		容器创建时，可以通过 --network=none 指定使用 none 网络。

		[root@iz2ze0lvzs717097h32rpcz ~]# docker run -it --network=none busybox
		/ # ifconfig
		lo      Link encap:Local Loopback  
		        inet addr:127.0.0.1  Mask:255.0.0.0
				UP LOOPBACK RUNNING  MTU:65536  Metric:1
				RX packets:0 errors:0 dropped:0 overruns:0 frame:0
				TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
				collisions:0 txqueuelen:1 
				RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
		/ # 
		/ # exit

		我们不禁会问，这样一个封闭的网络有什么用呢？
		其实还真有应用场景。封闭意味着隔离，一些对安全性要求高并且不需要联网的应用可以使用 none 网络。
		比如某个容器的唯一用途是生成随机密码，就可以放到 none 网络中避免密码被窃取。
		当然大部分容器是需要网络的，我们接着看 host 网络。

	2、host 网络：

		连接到 host 网络的容器共享 Docker host 的网络栈，容器的网络配置与 host 完全一样。
		可以通过 --network=host 指定使用 host 网络。
		
		[root@iz2ze0lvzs717097h32rpcz ~]# docker run -it --network=host busybox
		/ # ip l
		1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue qlen 1
			link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
		2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast qlen 1000
			link/ether 00:16:3e:2e:82:b9 brd ff:ff:ff:ff:ff:ff
		3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue 
			link/ether 02:42:86:69:17:1e brd ff:ff:ff:ff:ff:ff
		/ # hostname
			iz2ze0lvzs717097h32rpcz

		在容器中可以看到 host 的所有网卡，并且连 hostname 也是 host 的。host 网络的使用场景又是什么呢？
		直接使用 Docker host 的网络最大的好处就是性能，如果容器对网络传输效率有较高要求，则可以选择 host 网络。
		当然不便之处就是牺牲一些灵活性，比如要考虑端口冲突问题，Docker host 上已经使用的端口就不能再用了。

		Docker host 的另一个用途是让容器可以直接配置 host 网路。
		比如某些跨 host 的网络解决方案，其本身也是以容器方式运行的，这些方案需要对网络进行配置，
		比如管理 iptables，大家将会在后面进阶技术章节看到。

	3、 bridge 网络：

		本节学习应用最广泛也是默认的 bridge 网络。

		brctl 命令详解:

			安装网桥管理工具包：bridge-utile
			# yum install bridge-utils -y
			
			使用brctl命令创建网桥br1
			# brctl addbr br1

			删除网桥br1
			# brctl delbr br1

			将eth0端口加入网桥br1 
			# brctl addif br1 eth0

			删除eth0端口加入网桥br1 
			# brctl delif br1 eth0
			
			查询网桥信息
			# brctl show
			# brctl show br1

		Docker 安装时会创建一个 命名为 docker0 的 linux bridge。
		如果不指定--network，创建的容器默认都会挂到 docker0 上。

		[root@iz2ze0lvzs717097h32rpcz ~]# brctl show                 
		bridge name     bridge id               STP enabled     interfaces
		docker0         8000.02428669171e       no

		当前 docker0 上没有任何其他网络设备，我们创建一个容器看看有什么变化。
		[root@iz2ze0lvzs717097h32rpcz ~]# docker run -d httpd
		[root@iz2ze0lvzs717097h32rpcz ~]# brctl show         
		bridge name     bridge id               STP enabled     interfaces
		docker0         8000.02428669171e       no              vethffb98de

		一个新的网络接口 vethffb98de被挂到了docker0上，vethffb98de就是新创建容器的虚拟网卡。

		让我们通过 docker network inspect bridge 看一下 bridge 网络的配置信息:
			[root@iz2ze0lvzs717097h32rpcz ~]# docker network inspect bridge
			[
				{
					"Name": "bridge",
					"Id": "b6b0664a7260f4ad916887a9b1c459788583da3946b9b83106616e471f060fcb",
					"Created": "2018-11-08T19:40:59.367568543+08:00",
					"Scope": "local",
					"Driver": "bridge",
					"EnableIPv6": false,
					"IPAM": {

						"Driver": "default",
						"Options": null,
						"Config": [
						{

							"Subnet": "172.18.0.0/16"
						}
						]
						}
				.....
			}
			]
		原来 bridge 网络配置的 subnet 就是 172.18.0.0/16，并且网关是172.18.0.1
		这个网关在哪儿呢？大概你已经猜出来了，就是 docker0。

			[root@iz2ze0lvzs717097h32rpcz ~]# ifconfig docker0
			docker0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
			        inet 172.18.0.1  netmask 255.255.0.0  broadcast 172.18.255.255
					        ether 02:42:86:69:17:1e  txqueuelen 0  (Ethernet)
	        RX packets 0  bytes 0 (0.0 B)
	        RX errors 0  dropped 0  overruns 0  frame 0
			        TX packets 0  bytes 0 (0.0 B)
	        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

		容器创建时，docker 会自动从 172.18.0.0/16 中分配一个 IP，这里 16 位的掩码保证有足够多的 IP 可以供容器使用。

		除了 none, host, bridge 这三个自动创建的网络，用户也可以根据业务需要创建 user-defined 网络，
		
	4、user-defined 网络:

		除了 none, host, bridge 这三个自动创建的网络，用户也可以根据业务需要创建 user-defined 网络。

		Docker 提供三种 user-defined 网络驱动：bridge, overlay 和 macvlan。
		overlay 和 macvlan 用于创建跨主机的网络，我们后面有章节单独讨论。

		我们可通过 bridge 驱动创建类似前面默认的 bridge 网络，例如：

		[root@iz2ze0lvzs717097h32rpcz ~]# docker network create --driver bridge my_net
		8f000ca6b52427ad9c6275ca00732f3b21d7a60a43931d2c72b62499c05242dc
		[root@iz2ze0lvzs717097h32rpcz ~]# 
		[root@iz2ze0lvzs717097h32rpcz ~]# brctl show
		bridge name     bridge id               STP enabled     interfaces
		br-8f000ca6b524         8000.02429acd9623       no
		docker0         8000.02428669171e       no              vethffb98de

		新增了一个网桥 br-8f000ca6b524，这里 8f000ca6b524正好新建 bridge 网络 my_net 的短 id。
		
		执行 docker network inspect 查看一下 my_net 的配置信息：

		[root@iz2ze0lvzs717097h32rpcz ~]# docker network inspect my_net
		[
			{

				"Name": "my_net",
				"Id": "8f000ca6b52427ad9c6275ca00732f3b21d7a60a43931d2c72b62499c05242dc",
				"Created": "2018-11-13T17:27:38.894223995+08:00",
				"Scope": "local",
				"Driver": "bridge",
				"EnableIPv6": false,
				"IPAM": {

							"Driver": "default",
							"Options": {},
							"Config": [
								{
									"Subnet": "172.19.0.0/16",
									"Gateway": "172.19.0.1"
								}
							]
						},
				"Internal": false,
				"Attachable": false,
				"Ingress": false,
				"ConfigFrom": {
					"Network": ""
				},
				"ConfigOnly": false,
				"Containers": {},
				"Options": {},
				"Labels": {}
		}
		
		这里 172.19.0.0/16 是 Docker 自动分配的 IP 网段。

		我们可以自己指定 IP 网段吗？
		答案是：可以。

		只需在创建网段时指定 --subnet 和 --gateway 参数：
		
		[root@iz2ze0lvzs717097h32rpcz ~]# docker network create --driver bridge --subnet 172.22.16.0/24 --gateway 172.22.16.1 my_net2 
		8e12d35334c681a0509aa553a7bfb6cfa84b60865fc638cbc0e99cd274a09995
		[root@iz2ze0lvzs717097h32rpcz ~]# 
		[root@iz2ze0lvzs717097h32rpcz ~]# 
		[root@iz2ze0lvzs717097h32rpcz ~]# docker network inspect my_net2
		[
			{

				"Name": "my_net2",
				"Id": "8e12d35334c681a0509aa553a7bfb6cfa84b60865fc638cbc0e99cd274a09995",
				"Created": "2018-11-13T17:36:57.759583113+08:00",
				"Scope": "local",
				"Driver": "bridge",
				"EnableIPv6": false,
				"IPAM": {

						"Driver": "default",
						"Options": {},
						"Config": [
							{

								"Subnet": "172.22.16.0/24",
								"Gateway": "172.22.16.1"
							}
						]
					},
				"Internal": false,
				"Attachable": false,
				"Ingress": false,
				"ConfigFrom": {		"Network": ""},
				"ConfigOnly": false,
				"Containers": {},
				"Options": {},
				"Labels": {}
			}
		]
	
		这里我们创建了新的 bridge 网络 my_net2，网段为 172.22.16.0/24，网关为 172.22.16.1。
		与前面一样，网关在 my_net2 对应的网桥 br-8e12d35334c6 上：
		[root@iz2ze0lvzs717097h32rpcz ~]# brctl show
		bridge name     bridge id               STP enabled     interfaces
		br-8e12d35334c6         8000.024247ad143d       no
		br-8f000ca6b524         8000.02429acd9623       no
		docker0         8000.02428669171e       no              vethffb98de
		[root@iz2ze0lvzs717097h32rpcz ~]# ifconfig br-8e12d35334c6   
		br-8e12d35334c6: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
			inet 172.22.16.1  netmask 255.255.255.0  broadcast 172.22.16.255
			ether 02:42:47:ad:14:3d  txqueuelen 0  (Ethernet)
			RX packets 0  bytes 0 (0.0 B)
			RX errors 0  dropped 0  overruns 0  frame 0
			TX packets 0  bytes 0 (0.0 B)
			TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

	
		容器要使用新的网络，需要在启动时通过 --network 指定：

		[root@iz2ze0lvzs717097h32rpcz ~]# docker run -it --network=my_net2 busybox
		/ # 
		/ # ip a
		1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue qlen 1
			link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
			inet 127.0.0.1/8 scope host lo
			valid_lft forever preferred_lft forever
		20: eth0@if21: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue 
			link/ether 02:42:ac:16:10:02 brd ff:ff:ff:ff:ff:ff
			inet 172.22.16.2/24 brd 172.22.16.255 scope global eth0
			valid_lft forever preferred_lft forever
		
		容器分配到的 IP 为 172.22.16.2。
		到目前为止，容器的 IP 都是 docker 自动从 subnet 中分配，我们能否指定一个静态 IP 呢？
		答案是：可以，通过--ip指定。

		[root@iz2ze0lvzs717097h32rpcz ~]# docker run -it --network=my_net2 --ip 172.22.16.8 busybox
		/ # ip a
		1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue qlen 1
		    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
			inet 127.0.0.1/8 scope host lo
			valid_lft forever preferred_lft forever
		22: eth0@if23: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue 
			link/ether 02:42:ac:16:10:08 brd ff:ff:ff:ff:ff:ff
			inet 172.22.16.8/24 brd 172.22.16.255 scope global eth0
			valid_lft forever preferred_lft forever
		/ #

		注：只有使用 --subnet 创建的网络才能指定静态 IP。

		my_net 创建时没有指定 --subnet，如果指定静态 IP 报错如下：

		[root@iz2ze0lvzs717097h32rpcz ~]# docker run -it --network=my_net2 --ip 172.18.0.8 busybox     
		docker: Error response from daemon: Invalid address 172.18.0.8: It does not belong to any of this network subnets.
		[root@iz2ze0lvzs717097h32rpcz ~]# 


	5、	几个容器之间的连通性：

		同一网络中的容器、网关之间都是可以通信的。

		my_net2 与默认 bridge 网络能通信吗？
		两个网络属于不同的网桥，应该不能通信，我们通过实验验证一下，让 busybox 容器 ping httpd 容器：
		确实 ping 不通，符合预期,不同的网络如果加上路由应该就可以通信了。
		确实，如果 host 上对每个网络的都有一条路由，同时操作系统上打开了 ip forwarding，
		host 就成了一个路由器，挂接在不同网桥上的网络就能够相互通信。
		下面我们来看看 docker host 满不满足这些条件呢？

		ip r 查看 host 上的路由表：                                              
		[root@iz2ze0lvzs717097h32rpcz ~]# ip r
		default via 172.17.223.253 dev eth0 
		169.254.0.0/16 dev eth0 scope link metric 1002 
		172.17.208.0/20 dev eth0 proto kernel scope link src 172.17.216.16 
		172.18.0.0/16 dev docker0 proto kernel scope link src 172.18.0.1 
		172.19.0.0/16 dev br-8f000ca6b524 proto kernel scope link src 172.19.0.1 
		172.22.16.0/24 dev br-8e12d35334c6 proto kernel scope link src 172.22.16.1 
		
		怎样才能让 busybox 与 httpd 通信呢？
		答案是：为 httpd 容器添加一块 net_my2 的网卡。这个可以通过docker network connect 命令实现。

		[root@iz2ze0lvzs717097h32rpcz ~]# docker ps 
		CONTAINER ID        IMAGE               COMMAND              CREATED             STATUS              PORTS               NAMES
		036ee44facdc        httpd               "httpd-foreground"   30 hours ago        Up 30 hours         80/tcp              unruffled_jennings
		[root@iz2ze0lvzs717097h32rpcz ~]# docker network coonet my_net2 036ee44facdc


	6、容器之间可通过 IP，Docker DNS Server 或 joined 容器三种方式通信。

		1. IP 通信:

			从上一节的例子可以得出这样一个结论：两个容器要能通信，必须要有属于同一个网络的网卡。

			满足这个条件后，容器就可以通过 IP 交互了。
			具体做法是在容器创建时通过 --network 指定相应的网络，
			或者通过 docker network connect 将现有容器加入到指定网络。
			可参考上一节 httpd 和 busybox 的例子，这里不再赘述.

		2. Docker DNS Server:

			
















