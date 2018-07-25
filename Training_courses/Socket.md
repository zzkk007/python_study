"---------------------------------------------------------------"

						网络编程

"---------------------------------------------------------------"

1、什么是网络？

	网络就是一种辅助双方或者多方能够连接在一起的工具
	如果没有网络，单机的世界是多么孤单

2、使用网络的目的？

	就是为了联通多方然后进行通信用的，即把数据从一方传递到另一方。

	为了让在不同的电脑上运行软件，之间能够互相传递数据，就需要借助网络功能。

	使用网络能够把多方链接在一起，然后可以进行数据传递，所谓的网络编程就是，让在不同的
	电脑上的软件能够进行数据传递，即进程之间的通信。


3、什么是协议？

	就像说不同语言的人沟通一样，只要有一种大家都认可都遵守的协议即可，
	那么这个计算机都遵守的网络通信协议叫做TCP/IP协议

	因为互联网协议包含了上百种协议标准，但是最重要的两个协议是TCP和IP协议，
	所以，大家把互联网的协议简称TCP/IP协议

	常用的网络协议有四层：应用层（应用进程）、传输层（tcp/udp）、网络层(ip)、链路层(网络接口层)

4、什么是端口

	端口就好像一个房子的门，是出入这间房子的必经之路。
	如果一个进程需要收发网络数据，那么就需要由这样的端口。
	在Linux系统中，端口可以有65536(2的16次方)之多。
	操作系统为了统一管理，进行了编号，就是端口号。
	
	端口号的分配：
		
		端口号不是随机使用的，而是按照一定的规定进行分配
		端口的分类标准有好几种，我们这里不做详细讲解，只介绍一下知名端口和动态端口

	知名端口号（Well Know Ports）:

		知名端口是众所周知的端口号，范围从0到1023
		一般情况下，如果一个程序需要使用知名端口的需要有root权限

	动态端口（Dynamic Ports）:

		动态端口的范围是从1024到65535
		之所以称为动态端口，是因为它一般不固定分配某种服务，而是动态分配。
	
		动态分配是指当一个系统进程或应用程序需要网络通信时，它向主机申请一个端口，
		主机从可用的端口中分配一个提供它使用。

		当这个进程关闭时，同时也就释放了所占用的端口号。

	怎样查看端口 ：
		netstat －an

	端口有什么用：
		
		一台拥有IP地址的主机可以提供许多服务，比如HTTP（万维网服务）、FTP（文件传输）、SMTP（电子邮件）等，
		这些服务完全可以通过1个IP地址来实现。那么主机是怎样区分不同的网络服务的呢？显然不能只靠ip地址，
		因为ip地址与网络服务的关系是一对多的关系。实际上是通过"ip地址+端口号"来区分不同的服务的，
		注意：端口并不是一一对应的。比如你的电脑作为客户机访问一台www服务器时，WWW服务器使用“80”端口与你的电脑通信，
		但你的电脑则可能使用“3457”这样的端口。


IP地址：

	ip地址：用来在网络中标记一台电脑的一串数字，比如192.168.1.1；在本地局域网上是惟一的。

ip地址的分类：

	每一个ip地址包括两部分：网络地址和主机地址

	A类IP地址：

		一个A类IP地址由1字节的网络地址和3字节主机地址组成，网络地址的最高位必须是“0”，

		地址范围1.0.0.1-126.255.255.254

		二进制表示为：00000001 00000000 00000000 00000001 - 01111110 11111111 11111111 11111110

		可用的A类网络有126个，每个网络能容纳1677214个主机

	B类IP地址：

		一个B类IP地址由2个字节的网络地址和2个字节的主机地址组成，网络地址的最高位必须是“10”，
		地址范围128.1.0.1-191.255.255.254
		二进制表示为：10000000 00000001 00000000 00000001 - 10111111 11111111 11111111 11111110
		可用的B类网络有16384个，每个网络能容纳65534主机

	C类IP地址：

		一个C类IP地址由3字节的网络地址和1字节的主机地址组成，网络地址的最高位必须是“110”
		范围192.0.1.1-223.255.255.254
		二进制表示为: 11000000 00000000 00000001 00000001 - 11011111 11111111 11111110 11111110
		C类网络可达2097152个，每个网络能容纳254个主机

	D类地址用于多点广播：
		
		D类IP地址第一个字节以“1110”开始，它是一个专门保留的地址。

		它并不指向特定的网络，目前这一类地址被用在多点广播（Multicast）中

		多点广播地址用来一次寻址一组计算机

		地址范围224.0.0.1-239.255.255.254

	E类IP地址：

		以“1111”开始，为将来使用保留
		E类地址保留，仅作实验和开发用

	私有ip：

		在这么多网络IP中，国际规定有一部分IP地址是用于我们的局域网使用，也就
		是属于私网IP，不在公网中使用的，它们的范围是：

		10.0.0.0～10.255.255.255

		172.16.0.0～172.31.255.255

		192.168.0.0～192.168.255.255

	注意：
		
		IP地址127．0．0．1~127．255．255．255用于回路测试
		127.0.0.1可以代表本机IP地址，用http://127.0.0.1就可以测试本机中配置的Web服务器。


子网掩码:

	要想理解什么是子网掩码，就不能不了解IP地址的构成。互联网是由许多小型网络构成的，
	每个网络上都有许多主机，这样便构成了一个有层次的结构。
	IP地址在设计时就考虑到地址分配的层次特点，
	将每个IP地址都分割成网络号和主机号两部分，以便于IP地址的寻址操作。

	IP地址的网络号和主机号各是多少位呢？
	如果不指定，就不知道哪些位是网络号、哪些是主机号，这就需要通过子网掩码来实现。
	子网掩码不能单独存在，它必须结合IP地址一起使用。
	子网掩码只有一个作用，就是将某个IP地址划分成网络地址和主机地址两部分.
	子网掩码的设定必须遵循一定的规则。

	与IP地址相同，子网掩码的长度也是32位，

		左边是网络位，用二进制数字“1”表示；
		右边是主机位，用二进制数字“0”表示。

	假设IP地址为“192.168.1.1”子网掩码为“255.255.255.0”

		其中，“1”有24个，代表与此相对应的IP地址左边24位是网络号；
		“0”有8个，代表与此相对应的IP地址右边8位是主机号。
		这样，子网掩码就确定了一个IP地址的32位二进制数字中哪些是网络号、哪些是主机号。
		这对于采用TCP/IP协议的网络来说非常重要，只有通过子网掩码，
		才能表明一台主机所在的子网与其他子网的关系，使网络正常工作。

	子网掩码是“255.255.255.0”的网络：

		最后面一个数字可以在0~255范围内任意变化，因此可以提供256个IP地址。
		但是实际可用的IP地址数量是256-2，即254个，因为主机号不能全是“0”或全是“1”。

		主机号全为0，表示网络号
		主机号全为1，表示网络广播


	如果将子网掩码设置过大，也就是说子网范围扩大，那么，根据子网寻径规则，
	很可能发往和本地主机不在同一子网内的目标主机的数据，会因为错误的判断而认为目标主机是在同一子网内，
	那么，数据包将在本子网内循环，直到超时并抛弃，使数据不能正确到达目标主机，导致网络传输错误；
	如果将子网掩码设置得过小，那么就会将本来属于同一子网内的机器之间的通信当做是跨子网传输，
	数据包都交给缺省网关处理，这样势必增加缺省网关(文章下方有解释)的负担，造成网络效率下降。
	因此，子网掩码应该根据网络的规模进行设置。如果一个网络的规模不超过254台电脑，
	采用“255.255.255.0”作为子网掩码就可以了，现在大多数局域网都不会超过这个数字，
	因此“255.255.255.0”是最常用的IP地址子网掩码；假如在一所大学具有1500多台电脑，
	这种规模的局域网可以使用“255.255.0.0”。

"---------------------------------------------------------------------------------------------"

Socket:

	1、本地的进程间通信(IPC)有很多种方式：
		队列
		同步（互斥锁、条件变量等）

	2、网络中的进程之间如何通信:

		首先解决的问题是如何唯一标识一个进程，否则通信无从谈起，
		在本地可以通过进程pid来唯一标识一个进程，但是在网络中行不通。

		其实TCP/IP协议族已经帮我们解决了这个问题，网络层的“IP地址”可以唯一标识网络中的主机，
		而传输层的"协议+端口"可以唯一标识主机中的应用程序(进程)。

		这样利用 ip地址、协议、端口就可以标识网络的进程了，网络中的进程通信就可以利用
		这个标志和其他进程进行交互。

	3、什么是SOCKET:

		socket(简称 套接字)是进程间通信的一种方式，他与其他进程间通信的一个主要不同是：
		它能实现不同主机间的进程间通信，我们网络上各种各样的服务大多都是基于socket来完成
		通信的。例如：浏览网页、QQ、email等


	4、创建SOCKET：

		在python中使用socket模块的函数socket就可以完成：
		
			socket.socket(AddressFamily,Type)
			
			函数socket.socket,返回该socket的描述符，该函数带有两个参数：

			AddressFamily:
						可以选择AF_INT（用于internet进程间通信）或者AF_UNIX(用于同一台机器进程间通信)
					    实际工作中常用AF_INT

			Type:
				套接字类型，可以是SOCK_STREAM（流式套接字，主要用于TCP协议）
							SOCK_DGRAM（数据报套接字，主要用于UDP）

		创建一个tcp socket（tcp套接字）

			import socket

			s = socket.socket(socket.AF_INT,socket.SOCK_STREAM)

			print("Socket Created")


		创建一个UDP socket（udp套接字）

			import socket

			s = socket.socket(socket.AF_INT,socket.SOCK_DGRAM)

			print("Socket Created")


UDP介绍：
	
	UDP--用户数据报协议，是一个无连接的简单的面向数据报的运输层协议。
	UDP不提供可靠性，它只是把应用程序传给ip层的数据报发送出去，但是
	并不能保证它们能够到达目的地。
	由于UDP在传输数据报前不用在客户和服务器之间建立一个链接，切没有
	超时重发等机制，故而传输速度很快。

	UDP是一种面向无连接的协议，每个数据包都会是一个独立的信息，包括
	完整的源地址和目的地址，它在网络上以任何可能的路径传往目的地，
	因此能否到达目的地，到达目的地的时间以及内容的正确性都是不能被保证的。

	UDP特点:

		UDP是面向无连接的通讯协议，UDP数据包括目的端口号和源端口号信息
		由于通讯不需要连接，可以实现广播发送。
		UDP传输数据时有大小限制，每个被传输的数据报必须限定在64KB之内。
		UDP是一个不可靠的协议，发送方所发送的数据并不一定以相同的
		次序到达接收方。

	UDP是面向消息的协议，通讯时不需要建立连接，数据的传输自然是不可靠
		UDP一般用于多点通信和实时的数据业务。
		比如：
			语音广播、视频、QQ、TFTP(简单文件传输)、SNMP(简单网络管理协议)
			RIP（路由信息协议）、DNS（域名解释）

		注重速度流程

	UDP操作简单，而且仅需要较少的监护，因此通常用于局域网高可靠性的分散系统中client/server应用程序。
	例如视频会议系统，并不要求音频视频数据绝对的正确，只要保证连贯性就可以了，
	这种情况下显然使用UDP会更合理一些。



UDP网络程序-发送数据：
	
	创建一个UDP客户端程序的流程简单，步骤如下：
	
	UDP客户端:
		
		1、socket()创建客户端套接字

		2、sendto()发送

		3、recvfrom()接收

		4、close()关闭

		
	from socket import *

	1、创建套接字
	udpsocket = socket(AF_INT,SOCK_DGRAM)

	2、准备接收方地址
	sendAddr = ('172.25.16.226',8080)

	3、准备发送数据
	sendData = input("input send data:")

	4、发送数据到指定服务器
	udpsocket.sendto(sendData,dendAdrr)
	
	5、等待接收对方发送的数据，1024表示接收的最大字节数
	recvData = udpsocket.recvfrom(1024)

	6、显示数据
	print(recvData)
	
	7、关闭套接字
	udpsoclet.close

	每次重新运行一次网络程序，客户端的进程号是不确定的，系统默认随机分配
	记住一点：网络程序运行过程中，这就是唯一的标识，如果其他电脑上的网络程序
	想要向次程序发送数据，就需要向这个数字（端口）标识的程序发送。
	
	一般情况下，在一天电脑上运行的网络程序有很多，而各自用的端口号很多情况下不知道，
	为了不与其他的网络程序占用同一个端口号，往往在编程中，客户端udp的端口号一般不绑定。


	UDP服务器：服务器端的端口是绑定的。

		1、socket()创建服务器套接字

		2、bind()绑定ip和端口

		3、recvfrom()接收请求

		4、处理数据

		5、sendto()发送



	form  socket import *

	1、创建套接字
	udpsocket = socket(AF_INT,SOCK_DGARM)


	2、绑定Ip和端口,ip一般不用写，表示本机的任何一个ip
	bindAddr = ('',7788)
	udpsocket.bind(bindAddr)

	num = 1
	while True:

		3、等待接收对方发送的数据
		recvData = udpsocket.recvfrom(1024)

		4、将接收的数据再发送回去

		recvfData[0]接收到的数据
		print("recvfData[0]:%s")%(recvfData[0])  
		recvfData[1] ip和端口
		print("recvfData[1]:%s")%(str(recvfData[1]))

		udpsocket.sendto(recvData[0],recvData[1])
		
		5、统计信息
		print('已经将接收到的第%d个数据返回给对方,内容为:%s'%(num,recvData[0]))

		num += 1
		print(recvDatap地址，端口号）
	
	5、udpSocket.close()


	一个udp网络程序，可以不绑定，此时操作系统会随机进行分配一个端口，
		如果重新运行次程序端口可能会发生变化
	一个udp网络程序，也可以绑定信息（ip地址，端口号），如果绑定成功，
		那么操作系统用这个端口号来进行区别收到的网络数据是否是此进程的
	

udp网络通信过程：


	应用层：				hello

	运输层(传输层）：       目的端口|hello

	网络层：				目的IP|目的端口|hello

	链路层：                目的MAC|目的IP|目的端口|hello




udp总结:

	1、udp是TCP/IP协议族中的一种协议能够完成不同机器上的程序间的数据通信

	2、udp服务器、客户端

		udp的服务器和客户端的区分：往往是通过请求服务和提供服务来进行区分
		请求服务的一方称为：客户端
		提供服务的一方称为：服务器

	3、udp绑定问题

		一般情况下，服务器端，需要绑定端口，目的是为了让其他的客户端能够正确发送到此进程
		客户端，一般不需要绑定，而是让操作系统随机分配，
		这样就不会因为需要绑定的端口被占用而导致程序无法运行的情况


TFTP协议介绍：

	TFTP（Trivial File Transfer Protocol,简单文件传输协议）
	是TCP/IP协议族中的一个用来在客户端与服务器之间进行简单文件传输的协议
	
	特点：

		简单
		占用资源小
		适合传递小文件
		适合在局域网进行传递
		端口号为69
		基于UDP实现

	
	TFTP下载过程:

		TFTP服务器默认监听69号端口
		当客户端发送“下载”请求（即读请求）时，需要向服务器的69端口发送
		服务器若批准此请求,则使用一个新的、临时的 端口进行数据传输

		当服务器找到需要现在的文件后，会立刻打开文件，把文件中的数据通过TFTP协议发送给客户端。
		如果文件的总大小较大（比如3M），那么服务器分多次发送，每次会从文件中读取512个字节的数据发送过来

		因为发送的次数有可能会很多，所以为了让客户端对接收到的数据进行排序，
		所以在服务器发送那512个字节数据的时候，会多发2个字节的数据，用来存放序号，
		并且放在512个字节数据的前面，序号是从1开始的

		因为需要从服务器上下载文件时，文件可能不存在，那么此时服务器就会发送一个错误的信息过来，
		为了区分服务发送的是文件内容还是错误的提示信息，所以又用了2个字节 
		来表示这个数据包的功能（称为操作码），并且在序号的前面


		因为udp的数据包不安全，即发送方发送是否成功不能确定，所以TFTP协议中规定，
		为了让服务器知道客户端已经接收到了刚刚发送的那个数据包，
		所以当客户端接收到一个数据包的时候需要向服务器进行发送确认信息，
		即发送收到了，这样的包成为ACK(应答包)

		为了标记数据已经发送完毕，所以规定，当客户端接收到的数据小于516
		（2字节操作码+2个字节的序号+512字节数据）时，就意味着服务器发送完毕了
		
"----------------------------------------------------------------------------------"

TCP:

	客户端：

	1、socket()
	
	2、connect()

	3、write()

	4、read()

	5、close()


	from socket import *

	tcpClientSocket = socket(AF_INET,SOCK_STREAM)

	serAddr = ('172.168.1.102',7788)

	tcpClientSocket.conntct(serAddr)

	sendData = input("send data:")
	
	tcpClientSocket.send(sendData)

	recvData = tcpClientSocket.recv(1024)

	tcpClientSocket.close()


	服务器：

	1、socket()

	2、bind()

	3、listen()

	4、accept()

	5、read()

	6、write()

	7、close()

	from socket import *

	tcpSerSocket = socket(AF_INET,SOCK_STREAM)

	address = ('',7788)
	tcpSerSocket.bind(address)

	tcpSerSocket.listen(5)

	
	如果有新的客户端连接服务器，那么就产生一个新的套接字专门为这个客户端服务器
	newSocket用来为这个客户端服务
	tcpSerSocket就可以专门等待其他新客户端的连接

	newSocket,clientAddr = tcpSerSocket.accet()

	接收对方发送过来的数据，最大接收1024个字节

	recvData = newSocket.recv(1024)
	
	发送一些数据到客户端
	newSocket.send("thank you")

	关闭这个客户端的套接字，只有关闭，就意味着不能再为这个客户端服务了，
	如果需要服务，只能再次重新连接

	newSocket.close()

	关闭监听套接字，只要监听套接字关闭了，就意味着程序不能再次接收任何新的客户端的连接

	tcpSerSocket.close()
	
	

tcp长连接和短连接:

	TCP在真正的读写操作之前，server与client之间必须建立一个连接，

	当读写操作完成后，双方不再需要这个连接时它们可以释放这个连接，

	连接的建立通过三次握手，释放则需要四次握手，

	所以说每个连接的建立都是需要资源消耗和时间消耗的。


	TCP短连接:

		模拟一种TCP短连接的情况:

		client 向 server 发起连接请求
		server 接到请求，双方建立连接
		client 向 server 发送消息
		server 回应 client
		一次读写完成，此时双方任何一个都可以发起 close 操作
		在第 步骤5中，一般都是 client 先发起 close 操作。当然也不排除有特殊的情况。
		从上面的描述看，短连接一般只会在 client/server 间传递一次读写操作！


	TCP长连接:

		再模拟一种长连接的情况:

		client 向 server 发起连接
		server 接到请求，双方建立连接
		client 向 server 发送消息
		server 回应 client
		一次读写完成，连接不关闭
		后续读写操作...
		长时间操作之后client发起关闭请求

	
		长连接可以省去较多的TCP建立和关闭的操作，减少浪费，节约时间。
		对于频繁请求资源的客户来说，较适用长连接。
		client与server之间的连接如果一直不关闭的话，会存在一个问题，
		随着客户端连接越来越多，server早晚有扛不住的时候，这时候server端需要采取一些策略，
		如关闭一些长时间没有读写事件发生的连接，这样可以避免一些恶意连接导致server端服务受损；
		如果条件再允许就可以以客户端机器为颗粒度，限制每个客户端的最大长连接数，
		这样可以完全避免某个蛋疼的客户端连累后端服务。
		短连接对于服务器来说管理较为简单，存在的连接都是有用的连接，不需要额外的控制手段。
		但如果客户请求频繁，将在TCP的建立和关闭操作上浪费时间和带宽。

	
	listen的队列长度:


		服务器端运行:

		from socket import *
		from time import sleep

		# 创建socket
		tcpSerSocket = socket(AF_INET, SOCK_STREAM)

		# 绑定本地信息
		address = ('', 7788)
		tcpSerSocket.bind(address)
	
		connNum = int(input("请输入要最大的链接数:"))
	
		# 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
		tcpSerSocket.listen(connNum)
	
		while True:
	
			# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务器
			newSocket, clientAddr = tcpSerSocket.accept()
			print clientAddr
		    sleep(1)


		客户端运行:

		#coding=utf-8
		from socket import *
		connNum = raw_input("请输入要链接服务器的次数:")
		for i in range(int(connNum)):
			s = socket(AF_INET, SOCK_STREAM)
			s.connect(("192.168.1.102", 7788))
			print(i)

	
	listen中的black表示已经建立链接和半链接的总数
	如果当前已建立链接数和半链接数以达到设定值，那么新客户端就不会connect成功，而是等待服务器



手动配置ip

	设置IP和掩码
		ifconfig eth0 192.168.5.40 netmask 255.255.255.0

	设置网关
		route add default gw 192.168.5.1

常见网络攻击案例
	
	1、tcp半链接攻击
		
		tcp半链接攻击也称为：SYN Flood (SYN洪水)
		是种典型的DoS (Denial of Service，拒绝服务) 攻击
		效果就是服务器TCP连接资源耗尽，停止响应正常的TCP连接请求

	2、dns攻击

		我们知道一个域名服务器对其区域内的用户解析请求负责，
		但是并没有一个机制去监督它有没有真地负责。
		也就是说域名服务器的权力并没有被关在笼子里，
		所以它既可以认真地“为人民服务”，也可以“指鹿为马”。
		于是有些流氓的域名服务器故意更改一些域名的解析结果，
		将用户引向一个错误的目标地址。这就叫作 DNS 劫持，
		主要用来阻止用户访问某些特定的网站，或者是将用户引导到广告页面。

		dns欺骗

		DNS 欺骗简单来说就是用一个假的 DNS 应答来欺骗用户计算机，
		让其相信这个假的地址，并且抛弃真正的 DNS 应答。
		在一台主机发出 DNS 请求后，它就开始等待应答，
		如果此时有一个看起来正确（拥有和DNS请求一样的序列号）的应答包，
		它就会信以为真，并且丢弃稍晚一点到达的应答。


		查看域名解析的ip地址方法

			nslookup 域名

			例如：
			    nslookup baidu.com
	3、arp攻击


"-----------------------------------------------------------------------------------"

并发服务器、HTTP协议

单进程服务器：

	from socket import *

	serSocket = socket(AF_INET,SOCK_STREAM)
	
	#重复使用绑定的信息
	serSocket.setsockopt(SOL_SOCKET,SO_SEUSEADDR,1)
	
	localAddr = ('',7788)

	serSocket.bind(localAddr)

	serSocket.listen(5)

	while True:

		newSocket,destAddr = serSocket.accept()

		try:
			while True:
				recvData = newSocket.recv(1024)
				if len(recvData) > 0:
					print('recv[%s]:%s'%(str(destAddr),recvData))

				else:
					print('[%s] close'%str(destAddr))
					break

		finally:
			newSocket.close()

	serSocket.close()

	同一时刻只能为一个客户进行服务，不能同时为多个客户服务
	类似于找一个“明星”签字一样，客户需要耐心等待才可以获取到服务
	当服务器为一个客户端服务时，而另外的客户端发起了connect，只要服务器listen的队列有空闲的位置，
	就会为这个新客户端进行连接，并且客户端可以发送数据，但当服务器为这个新客户端服务时，
	可能一次性把所有数据接收完毕
	
	当recv接收数据时，返回值为空，即没有返回数据，那么意味着客户端已经调用了close关闭了；
	因此服务器通过判断recv接收数据是否为空 来判断客户端是否已经下线


多进程服务器:


	from socket import *
	from multiprocessing import *
	from time import sleep

	def dealWithClient(newSocket,destAddr):
		while True:
			recvData = newSocket.recv(1024)
			if len(recvData)>0:
		        print('recv[%s]:%s'%(str(destAddr), recvData))
		    else:
				print('[%s]客户端已经关闭'%str(destAddr))
				break
		newSocket.close()


	def main():
		
		serSocket = socket(AF_INET,SOCK_STREAM)
		serSocket.setsockopt(SOL_SOCKET,SO_SEUSEADDR,1)

		serAddr = ('',7788)

		serSocket.bind(serAddr)

		serSocket.listen(5)

		try:
			while True:

				newSocket,cliAddr = serSocket.accept()

				client = Process(target=dealWithClient,args=(newSocket,cliAddr))
				client.start()

				因为已经向子进程中copy了一份（引用），并且父进程中这个套接字也没有用处了
				所以关闭

				newSocket.close()

		finally:
			#当为所有的客户端服务完之后再进行关闭，表示不再接收新的客户端的链接
			serSocket.close()


	if __name__ == '__main__':
		main()


	通过为每个客户端创建一个进程的方式，能够同时为多个客户端进行服务
	当客户端不是特别多的时候，这种方式还行，如果有几百上千个，就不可取了，
	因为每次创建进程等过程需要好较大的资源

	

多线程服务器：

	from socket import *
	from multiprocessing import *
	from time import sleep
	
	def dealWithClient(newSocket,destAddr):
		while True:
			recvData = newSocket.recv(1024)
			if len(recvData)>0:
		        print('recv[%s]:%s'%(str(destAddr), recvData))
		    else:
				print('[%s]客户端已经关闭'%str(destAddr))
				break
		newSocket.close()


	def main():

		serSocket = socekt(AF_INET,SOCK_STREAM)
		serSocket.setsockopt(SOL_SOCKET,SO_SEUSEADDR,1)

		serAddr = ('',7788)
		serSocket.listen(5)

		try:
			while True:

				newSocket,cliAddr = serSocket.accept()

				client = Trhead(target=dealWithClient,args=(newSocket,cliAddr))
				client.start()
				
				#因为线程中共享这个套接字，如果关闭了会导致这个套接字不可用，
				#但是此时在线程中这个套接字可能还在收数据，因此不能关闭
				#newSocket.close() 

		finally:

			serSocket.close()

	
	if __name__=='__main__':
		main()


单进程服务器-非堵塞模式:

	
服务器：

	from socket import *
	import time

	g_socketList = []

	def main():
		    
		serSocket = socket(AF_INET, SOCK_STREAM)
		serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR  , 1)
		localAddr = ('', 7788)
		serSocket.bind(localAddr)
		#可以适当修改listen中的值来看看不同的现象
		serSocket.listen(1000)

		#将套接字设置为非堵塞
	    #设置为非堵塞后，如果accept时，恰巧没有客户端connect，那么accept会
	    #产生一个异常，所以需要try来进行处理
	    serSocket.setblocking(False)
		
		while True:
			
			try:
				
				newClientInfo = serSocket.accept()
			
			except Exception as result:

				pass

			else:

				print("一个新的客户端到来:%s"%str(newClientInfo))
				newClientInfo[0].setblocking(False)
				g_socketList.append(newClientInfo)
		
			# 用来存储需要删除的客户端信息
			needDelClientInfoList = []

			for clientSocket,clientAddr in g_socketList:
				
				try:
					recvData = clientSocket.recv(1024)
	                if len(recvData)>0:
					    print('recv[%s]:%s'%(str(clientAddr), recvData))
					else:
						print('[%s]客户端已经关闭'%str(clientAddr))
						clientSocket.close()
	                    g_needDelClientInfoList.append((clientSocket,clientAddr))
				except Exception as result:
				        pass

			for needDelClientInfo in needDelClientInfoList:
				g_socketList.remove(needDelClientInfo)

	if __name__== '__main__':

		main()


客户端：

	#coding=utf-8
	from socket import *
	import random
	import time

	serverIp = input("请输入服务器的ip:")
	connNum =  input("请输入要链接服务器的次数(例如1000):")
	g_socketList = []

	for i in range(int(connNum)):
		s = socket(AF_INET, SOCK_STREAM)
		s.connect((serverIp, 7788))
		g_socketList.append(s)
		print(i)

	while True:
		for s in g_socketList:
		    s.send(str(random.randint(0,100)))


"----------------------------------------------------------------"
Socket IO多路复用：

I/O 模型：

	同步模型(synchronous I/O)
		
		1、阻塞I/O(bloking I/O)

		2、非阻塞I/O(non-blocking I/O)

		3、多路复用I/O(multiplexing I/O)

		4、信号驱动式I/O (signal-driven I/O)
		
	异步模型（asynchronous I/O）
		

I/O多路复用：
	
	IO多路复用常用的方法有：select、poll以及epoll三种。
	IO多路复用的好处就在于单个process就可以同时处理多个网络连接的IO。

	I/O 多路复用是为了解决进程或线程阻塞到某个 I/O 系统调用而出现的技术，
	使进程或线程不阻塞于某个特定的 I/O 系统调用。

	I/O多路复用通过一种机制，可以监视多个描述符，一旦某个就绪（一般是读就绪或者写就绪，就是
	这个文件描述符进行读写操作之前），能够通知程序进行相应多写操作。

	但select()，poll()，epoll()本质上都是同步I/O，因为他们都需要在读写事件就绪后自己负责进行读写，
	也就是说这个读写过程是阻塞的，而异步I/O则无需自己负责进行读写，
	异步I/O的实现会负责把数据从内核拷贝到用户空间。


	与多线程(TPC（Thread Per Connection）模型)和多进程(典型的Apache模型（Process Per Connection，简称PPC）)相比，
	I/O 多路复用的最大优势是系统开销小，系统不需要建立新的进程或者线程，也不必维护这些线程和进程。



select版-TCP服务器:
	
1. select 原理

	在多路复用的模型中，比较常用的有select模型和epoll模型。这两个都是系统接口，
	由操作系统提供。当然，Python的select模块进行了更高级的封装。

















































