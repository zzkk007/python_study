
"------------------------------------------------------------"

					Docker教程

"------------------------------------------------------------"

1、Docker 是一个开源的应用容器引擎，基于go语言，遵循Apache2.0协议开源。

   Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，
   然后发布到任何流行的Linux机器上，也可以实现虚拟化。

   容器是完全适应沙箱机制，互相之间不会有任何接口，容器性能开销极低。


2、Docker 应用场景:
	
	Web 应用的自动化打包和发布。

	自动化测试和持续集成、发布。

	在服务型环境中部署和调整数据库或其他后台应用

	从头编译或者扩展现有的OpenShift或Cloud Foundry平台搭建自己的PaaS环境。


3、Docker 的优点:

	1、简化程序：
		
	Docker 改变了虚拟化的方式，是开发者可以直接将自己成果放入Docker中进行管理。
	方便快捷是Docker的最大优势

	2、避免选择恐惧症：

	Docker 镜像中包含了运行环境和配置，Docker简化部署多种应用实例工作。
	比如Web应用、后台应用、数据库应用、Hdoop集群、消息队列都可以打包成一个镜像部署。

	3、节省开支
	Docker 和云结合，让云空间充分利用，不经解决了硬件管理问题，也改变了虚拟机方式。

	Docker 官网：http://www.docker.com

	Github Docker 源码：https://github.com/docker/docker


4、Docker 架构：

	Docker 使用客户端-服务器(c/s)架构模式，使用远程API来管理和创建Docker容器。

	Docker 容器通过Docker镜像来创建

	镜像和容器的关系类似于面向对象编程中的类和对象。



	Docker 镜像(Images)  Docker 镜像是用于创建Docker容器的模板。

	Docker 容器(Container) 容器是独立运行的一个或一组应用

	Docker 客户端(Client) Docker 客户端通过命令或者其他工具使用Docker API 与Docker的守护进程通信。

	Docker 主机(Host) 一个物理或者虚拟机器用于执行Docker 守护进程和容器。

	Docker 仓库(Registry) Docker 创客用于保存镜像，可以理解为代码控制中的代码仓库。
						  Docker Hub 提供了庞大的镜像集合供使用。

	Docker Machine Docker Machine 是一个简化Docker 安装的命令行工具，通过一个简单的命令行即可在
			相应的平台上安装Docker。

	
	





































































