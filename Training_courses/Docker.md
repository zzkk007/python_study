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

		
















