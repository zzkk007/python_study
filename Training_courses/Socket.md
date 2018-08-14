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

套接字：
	
	套接字是计算机网络数据结构，在任何类型的通信开始之前，网络应用程序必须创建套接字。
	可以它们比作电话插孔，没有它将无法进行通信
	
套接字对象(内置)方法：
 
 	服务器套接字方法：
 	
 		s.bind()
 		s.listen()
 		s.accept()
 		
 	客户端套接字方法：
 	
 		s.connect()
 		s.connect_ex()       扩展版，此时会以错误码的形式返回问题，而不是抛出异常
 		
 	普通的套接字方法：
 	
 		s.recv()
 		s.recv_into()      接受TCP消息到指定的缓冲区
 		
 		s.send()
 		s.sendall()        完整的发送TCP消息
 		      
 	UDP接受和发送：
 		s.recvfrom()
 		s.recvfrom_into()  接受到指定的缓冲区
 		s.sendto()
 		
 		
 		s.getpeername()    连接到套接字（TCP）的远程地址
 		s.getsockname()    当前套接字的地址
 		s.getsockopt()     返回给定套接字选项的值
		s.setsockopt()     设置给定套接字选项的值
		s.shutdown()       关闭链接
		s.close()          关闭套接字
		s.detach()         在未关闭文件描述符的情况下关闭套接字，返回文件描述符
		s.ioctl()          控制套接字的模式（仅支持windows）
		
	面向阻塞的套接字方法：
	
		s.setblocking()    设置套接字的阻塞和非阻塞模式
		s.settimeout()     设置阻塞套接字操作的超时时间
		s.getttimeout()    获取阻塞套接字操作的超时时间
		
		
	面向文件的套接字方法：
	
		s.fileno()        套接字的文件描述符
		s.makefile()      创建与套接字关联的文件对象
		
	数据属性：
	
		s.fmily          套接字家族
		s.type           套接字类型
		s.proto          套接字协议
		
		
----------------------------
tcp服务器：

	所有的套接字都是通过使用socket.socket()函数创建
			socket()          创建一个套接字（服务器、客户端）
			accept()          返回一个独立的客户端套接字，用来与将到来的消息进行交换。


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
	
1. select 原理:
	
	在多路复用的模型中，比较常用的有select模型和epoll模型。这两个都是系统接口，
	由操作系统提供。当然，Python的select模块进行了更高级的封装。
	
	网络通信被Unix系统抽象为文件的读写，通常是一个设备，由设备驱动程序提供，驱动可以知道自身的数据
	是否可以，支持阻塞操作的设备驱动会实现一组自身的等待队列，如读/写等待队列用于支持上层(用户层)
	所需的block或non-block操作，设备的文件的资源如果可用(可读或可写)则会通知进程，反之则会让进程
	睡眠，等到数据到来的时候，再唤醒进程。

	这些设备的文件描述符被放在一个数组中，然后select调用的时候遍历这个数组，
	如果对于的文件描述符可读则会返回改文件描述符。当遍历结束之后，如果仍然没有一个可用设备文件描述符，
	select让用户进程则会睡眠，直到等待资源可用的时候在唤醒，遍历之前那个监视数组。每次遍历都是依次进行判断。

	它通过一个select()系统调用来监视多个文件描述符的数组，当select()返回后，该数组中就绪的
	文件描述符便会被内核修改标志位，使得进程可以获得这些文件描述符从而进行后续的读写操作。

2. 使用select：

	在python中，select函数是一个对底层操作系统的直接访问的接口。
	它用来监控sockets、files和pipes，等待IO完成（Waiting for I/O completion）。
	当有可读、可写或是异常事件产生时，select可以很容易的监控到。 		

	select.select(rlist,wlist,xlist[,timeout])
	传递三个参数，一个为输入而观察的文件对象列表，
	一个为输出而观察的文件对象列表和一个观察错误异常的文件列表。
	第四个是一个可选参数，表示超时秒数。其返回3个tuple，
	每个tuple都是一个准备好的对象列表，它和前边的参数是一样的顺序。

	服务器：
	
	import select 
	import socket
	import Queue

	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.setblocking(Flase)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	server_address= ('192.168.1.102',10001)
	server.bind(server_address)

	server.listen(10)

	inputs = [server]
	outputs = []
	message_queues = {}
	timeout = 20

	while inputs:
		
		readable,writeable,exceptional = select.select(inputs,outputs,inputs,timeout)

		if not (readable or writeable or exceptional):
			break;

		for s in readable:
			
			if s is server:
				
				connection,client_address = s.accept()
				connection.setblocking(False)
				inputs.append(connection)
				message_queues[connection] = Queue.Queue()
			else:

				data = s.recv(1024)
				if data:
					message_queues[s].put(data)
					#Add output channel for response
					if s not in outputs:
						outputs.append(s)
				else:
					#Interpret empty result as closed connection
					if s in outputs:
						outputs.remove(s)
					inputs.remove(s)
					s.close()
					#remove message queue 
					del message_queues[s]

		for s in writeable:

			try:
				next_msg = message_queues[s].get_nowait()
			except Queue.Empty:
				outputs.remove(s)
			else:
				s.send(next_msg)

		for s in exception:

			#stop listening for input on the connection

			inputs.remove(s)
			if s in outputs:
				outputs.remove(s)
			s.close()
			del message_queues[s]


	客户端：
		
		import socket

		messages = ["This is the message" ,"It will be sent","in parts"]

		server_address =("192.168.1.102",10001)

		socks = []

		for i in range(10):
			socks.append(socket.socket(socket.AF_INET,socket.SOCK_STREAM))

		for s in socks:
			s.connect(server_address)
		
		cunter = 0
		for message in messages:
			counter += 1
			s.send(message+" version "+str(counter))

		for s in socks:
			data = s.recv(1024)
			print(" %s received %s" % (s.getpeername(),data))
			
			if not data:
				s.close()

3. 总结

优点:

	select目前几乎在所有的平台上支持，其良好跨平台支持也是它的一个优点。

缺点:

	select的一个缺点在于单个进程能够监视的文件描述符的数量存在最大限制，
	在Linux上一般为1024，可以通过修改宏定义甚至重新编译内核的方式提升这一限制，但是这样也会造成效率的降低。

	一般来说这个数目和系统内存关系很大，具体数目可以cat /proc/sys/fs/file-max察看。
	32位机默认是1024个。64位机默认是2048.

	对socket进行扫描时是依次扫描的，即采用轮询的方法，效率较低。

	当套接字比较多的时候，每次select()都要通过遍历FD_SETSIZE个Socket来完成调度，
	不管哪个Socket是活跃的，都遍历一遍。这会浪费很多CPU时间。



epoll版-TCP服务器:

1. epoll的优点：

	没有最大并发连接的限制，能打开的FD(指的是文件描述符，通俗的理解就是套接字对应的数字编号)的上限远大于1024
	效率提升，不是轮询的方式，不会随着FD数目的增加效率下降。
	只有活跃可用的FD才会调用callback函数；即epoll最大的优点就在于它只管你“活跃”的连接，
	而跟连接总数无关，因此在实际的网络环境中，epoll的效率就会远远高于select和poll。


2、epoll使用参考代码：

	import socket
	import select

	# 创建套接字
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	
	# 设置可以重复使用绑定的信息
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

	# 绑定本机信息
	s.bind(("",7788))
	s.listen(10)

	# 创建一个epoll对象
	epoll=select.epoll()

	# 测试，用来打印套接字对应的文件描述符
	# print s.fileno()
	
	# 注册事件到epoll中
	# epoll.register(fd[, eventmask])
	# 注意，如果fd已经注册过，则会发生异常
	# 将创建的套接字添加到epoll的事件监听中


	epoll.register(s.fileno(),select.EPOLLIN|select.EPOLLET)

	connections = {}
	addresses = {}

	# 循环等待客户端的到来或者对方发送数据
	while True:
		
		# epoll 进行 fd 扫描的地方 -- 未指定超时时间则为阻塞等待
		epoll_list=epoll.poll()

		# 对事件进行判断
	    for fd,events in epoll_list:
			
		# 如果是socket创建的套接字被激活
		if fd == s.fileno():
			conn,addr = s.accept()
			print('有新的客户端到来%s'%str(addr)

			# 将 conn 和 addr 信息分别保存起来
			connections[conn.fileno()] = conn
			addresses[conn.fileno()] = addr

			 # 向 epoll 中注册 连接 socket 的 可读 事件
			epoll.register(conn.fileno(), select.EPOLLIN | select.EPOLLET)

		elif events == select.EPOLLIN:

			# 从激活 fd 上接收
			recvData = connections[fd].recv(1024)

			if len(recvData)>0:
				print('recv:%s'%recvData)
			else:
			# 从 epoll 中移除该 连接 fd
				epoll.unregister(fd)

			# server 侧主动关闭该 连接 fd
			connections[fd].close()

			print("%s---offline---"%str(addresses[fd]))"")'')

			
说明：

	EPOLLIN （可读）
	EPOLLOUT （可写）
	EPOLLET （ET模式）

	epoll对文件描述符的操作有两种模式：LT（level trigger）和ET（edge trigger）。
	LT模式是默认模式，LT模式与ET模式的区别如下：

		LT模式：当epoll检测到描述符事件发生并将此事件通知应用程序，应用程序可以不立即处理该事件。
		下次调用epoll时，会再次响应应用程序并通知此事件。

		ET模式：当epoll检测到描述符事件发生并将此事件通知应用程序，应用程序必须立即处理该事件。
		如果不处理，下次调用epoll时，不会再次响应应用程序并通知此事件。
		





协程:
	
	协程，又称微线程，纤程。Corutine

	协程是比线程更小的执行单元，为啥说它是执行单元，因为他自带CPU上下文。
	这样我们可以把一个协程切到另一个协程。只要这个过程中保存或恢复CPU上下文那么程序还是可以执行的。

	通俗的理解：在一个线程中的某个函数，可以在任何地方保存当前函数的一些临时变量等信息，
	然后切换到另外一个函数中执行，注意不是通过调用函数的方式做到的，并且切换的次数
	以及什么时候再切换到原来的函数都由开发者自己确定

协程和线程差异：

	那么这个过程看起来比线程差不多。其实不然, 线程切换从系统层面远不止保存和恢复 CPU上下文这么简单。
	操作系统为了程序运行的高效性每个线程都有自己缓存Cache等等数据，操作系统还会帮你做这些数据的恢复操作。
	所以线程的切换非常耗性能。但是协程的切换只是单纯的操作CPU的上下文，所以一秒钟切换个上百万次系统都抗的住。

协程的问题：

	协程有一个问题，就是系统并不感知，所以操作系统不会帮你做切换，
	那谁帮你切换？让需要执行的协程更多获得CPU时间才是问题的关键。


例子：
	
	目前的协程框架一般都是设计成 1:N 模式。所谓 1:N 就是一个线程作为一个容器里面放置多个协程。
	那么谁来适时的切换这些协程？答案是有协程自己主动让出CPU，也就是每个协程池里面有一个调度器， 这个调度器是被动调度的。
	意思就是他不会主动调度。而且当一个协程发现自己执行不下去了(比如异步等待网络的数据回来，但是当前还没有数据到)，
	这个时候就可以由这个协程通知调度器，这个时候执行到调度器的代码，调度器根据事先设计好的调度算法找到当前最需要CPU的协程。
	切换这个协程的CPU上下文把CPU的运行权交个这个协程，直到这个协程出现执行不下去需要等等的情况，或者它调用主动让出CPU的API之类，
	触发下一次调度。
	
	其实是有问题的，假设这个线程中有一个协程是CPU密集型的他没有IO操作， 也就是自己不会主动触发调度器调度的过程，
	那么就会出现其他协程得不到执行的情况， 所以这种情况下需要程序员自己避免。这是一个问题，
	假设业务开发的人员并不懂这个原理的话就可能会出现问题。
	
协程好处：

	在IO密集型的程序中由于IO操作远远慢于CPU的操作，所以往往需要CPU去等IO操作。 
	同步IO下系统需要切换线程，让操作系统可以在IO过程中执行其他的东西。 
	这样虽然代码是符合人类的思维习惯但是由于大量的线程切换带来了大量的性能的浪费，尤其是IO密集型的程序。
	
	所以人们发明了异步IO。就是当数据到达的时候触发我的回调。来减少线程切换带来性能损失。 
	但是这样的坏处也是很大的，主要的坏处就是操作被 “分片” 了，代码写的不是 “一气呵成” 这种。
	而是每次来段数据就要判断 数据够不够处理哇，够处理就处理吧，不够处理就在等等吧。这样代码的可读性很低，其实也不符合人类的习惯。
	
	但是协程可以很好解决这个问题。比如 把一个IO操作 写成一个协程。当触发IO操作的时候就自动让出CPU给其他协程。
	要知道协程的切换很轻的。 协程通过这种对异步IO的封装 既保留了性能也保证了代码的容易编写和可读性。在高IO密集型的程序下很好。
	但是高CPU密集型的程序下没啥好处。
	
协程一个简单实现：

	import time

	def A():
	    while True:
		print("----A---")
		yield
		time.sleep(0.5)

	def B(c):
	    while True:
		print("----B---")
		c.next()
		time.sleep(0.5)

	if __name__=='__main__':
	    a = A()
	    B(a)

gevent

	greenlet已经实现了协程，但是这个还的人工切换，是不是觉得太麻烦了，不要捉急，
	python还有一个比greenlet更强大的并且能够自动切换任务的模块gevent

	其原理是当一个greenlet遇到IO(指的是input output 输入输出，比如网络、文件操作等)操作时，比如访问网络，就自动切换到其他的greenlet，
	等到IO操作完成，再在适当的时候切换回来继续执行。

	由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO

	1. gevent的使用

	#coding=utf-8

	#请使用python 2 来执行此程序

	import gevent

	def f(n):
    		for i in range(n):
        		print gevent.getcurrent(), i

	g1 = gevent.spawn(f, 5)
	g2 = gevent.spawn(f, 5)
	g3 = gevent.spawn(f, 5)
	g1.join()
	g2.join()
	g3.join()
	

gevent版-TCP服务器：

	import sys
	import time
	import gevent

	from gevent import socket,monkey
	monkey.patch_all()

	def handle_request(conn):
    	while True:
        	data = conn.recv(1024)
        	if not data:
            		conn.close()
            		break
        	print("recv:", data)
        	conn.send(data)
	def server(port):
    	s = socket.socket()
    	s.bind(('', port))
    	s.listen(5)
    	while True:
        	cli, addr = s.accept()
        	gevent.spawn(handle_request, cli)

	if __name__ == '__main__':
    	server(7788)

"----------------------------------------------------------------------------------------"
Python：Mix-in技术介绍:

1、什么是Mix-in技术：

	中文意思"混入"，作用是，在运行期间，动态改变类的基类或类方法，从而使得类的表现可以发生变化。
	可以用在一个通用类接口中，根据不同的选择使用不同的底层类实现，而高层类不用发生变化。
	而且这一实现可以在运行过程中动态进行改变。



网络服务框架:
 
socketserver模块：

	socketserver是标准库中的一个高级模块，它的目标是简化很多样板代码
	它们是创建网络客户端和服务器所必需的代码。这个模块中有为你创建的
	各种各样的类。
	
	socketserver,网络通信服务器，是python标准数据库的一个模板，其作用是创建网络服务器。
	socketserver模板定义了一些处理诸如TCP、UDP、UNIX流和UNIX数据报之上的同步网络请求。
	
	socketserver模块处理网络请求的功能，可以通过两个主要的类来实现：一个是服务器类，一个是请求处理类。
	
	服务器类:处理通信问题，如监听一个套接字并接受链接等。
	请求处理类：处理"协议"问题，如解释到来的数据，处理数据，并把数据返回给客户端等。

	这种实现将服务器实现过程和请求处理实现过程解耦，这意味着我们可以将不同的服务器实现
	和请求处理实现结合起来处理一下定制的协议。
	

	socketserver模块类：
	
		BaseServer      包含核心服务器功能和mix-in类的钩子；仅用于推导，这样不会创建这个类的实例
		
		TCPServer/UDPServer 基础的网络同步TCP/UDP服务器
		
		UnixStreamServer/UnixDatagramServer  基于文件的基础同步TCP/UDP服务器
		
		ForkingMixIn/ThreadingMixIn         核心派出和线程功能，只用于min-in类与一个服务器类配合实现以些异步性。
		
		ForkingTCPServer/ForkingUDPServer   ForkingMinIN和TCPServer/UDPserver的组合
		
		ThreadingTCPServer/ThreadingUDPServer  ThreadingMixIn和TCPServer/UDPServer的组合
		
		StreamRequestHandler/DatagramRequestHandler  实现TCP/UDP服务器的服务处理器



1、要实现本模块，必须定义一个继承于基类BaseRequestHandler的处理程序类。
	BaseRequestHandler类的实例可以实现以下方法：

		h.handle() 调用该方法执行实际的请求处理，调用该方法可以不带任何参数，但是几个实例
			变量包含有用的值：h.request包含请求、h.client_address包含客户端地址、
			h.server包含调用处理程序的实例。
			对于TCP之类的数据流服务，h.request属性是套接字对象
			
		h.setup() 该方法在handle()之前调用，不执行任何操作，
				如果希望实现更多链接设置，可以在这里实现
			
		h.finish()调用本方法可以执行完handle()之后执行清除操作
				 如果setup()和handle()都不产生异常，则无需调用该方法。

		
2、服务器，要处理程序，必须插入服务器对象，定义类四个基本的服务器类：

	TCPServer :TCP协议的服务器类
	UDPServer :UDP协议的服务器类
	UnixStreamServer:使用UNIX套接字实现面向数据流协议的服务器，集成自TCPserver
	UnixDatagramServer:集成UDPServer


	四个服务器类的实例都有一下四个方法和变量：

	s.socket  用于传入请求的套接字对象

	s.server_address 监听服务器的地址

	s.RequestHandleClass 传递给服务器构造函数并由用户提供的请求处理程序类

	s.server_forever() 处理无限请求

	s.shutdown()    停止server_forever()循环

	s.fileno()     返回服务器套接字的文件描述符。



server端：

	import sockerserver

	class Server(socketServer.BaseRequestHandler):
		def handle(self):
			print("new connection:",self.client_address)

			while True:

				data = self.request.recv(1024)
				if not data:break
				print('client data:',data.decode())

				self.request.send(data)


	if __name__=='__main__':

	host,port ='127.0.0.1',8080
	server = socketserver.ThreadingTCPServer((host,port),Server)
	
	server.server_forever()


===================================================================

Twisted	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	


















