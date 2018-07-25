"-----------------------------------------------------------------"

				系统编程

"-----------------------------------------------------------------"

系统编程，主要是进程和线程

1、进程：

	fork()：

		Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：

		程序执行到os.fork()时，操作系统会创建一个新的进程（子进程），
		然后复制父进程的所有信息到子进程中.然后父进程和子进程都会从fork()函数中得到一个返回值，
		在子进程中这个值一定是0，而父进程中是子进程的 id号。

		这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，
		而子进程只需要调用getppid()就可以拿到父进程的ID。

	getpid()、getppid()：
		
		getpid()：得到当前进程的进程号
		getppid()：在子进程中得到父进程的进程号，
		
	
	multiprocessing:

		multiprocessing模块提供了一个Process类来代表一个进程对象

		创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，
		用start()方法启动，这样创建进程比fork()还要简单。
		join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

		Process语法结构如下：

			Process([group [, target [, name [, args [, kwargs]]]]])
			
			target：表示这个进程实例所调用对象；

			args：表示调用对象的位置参数元组；

			kwargs：表示调用对象的关键字参数字典；

			name：为当前进程实例的别名；

			group：大多数情况下用不到；

		Process类常用方法：

			is_alive()：判断进程实例是否还在执行；

			join([timeout])：是否等待进程实例执行结束，或等待多少秒；

			start()：启动进程实例（创建子进程）；

			run()：如果没有给定target参数，对这个对象调用start()方法时，就将执行对象中的run()方法；

			terminate()：不管任务是否完成，立即终止；

		Process类常用属性：

			name：当前进程实例别名，默认为Process-N，N为从1开始递增的整数；

			pid：当前进程实例的PID值；


	
	进程的创建-Process子类:

		创建新的进程还能够使用类的方式，可以自定义一个类，继承Process类，
		每次实例化这个类的时候，就等同于实例化一个进程对象

		class Process_Class(Process):
			    def __init__(self,interval):
					Process.__init__(self)
					self.interval = interval

				def run(delf):


	进程池：

		当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态成生多个进程，
		但如果是上百甚至上千个目标，手动的去创建进程的工作量巨大，
		此时就可以用到multiprocessing模块提供的Pool方法。

		初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满，
		那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到指定的最大值，
		那么该请求就会等待，直到池中有进程结束，才会创建新的进程来执行。


		multiprocessing.Pool常用函数解析：

			apply_async(func[, args[, kwds]]) ：使用非阻塞方式调用func
			（并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程），
			args为传递给func的参数列表，kwds为传递给func的关键字参数列表；

			apply(func[, args[, kwds]])：使用阻塞方式调用func

			close()：关闭Pool，使其不再接受新的任务；

			terminate()：不管任务是否完成，立即终止；

			join()：主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用；

	进程间通信-Queue：
	
		multiprocessing模块的Queue实现多进程之间的数据传递，Queue本身是一个消息列队程序。
		
		from multiprocessing import Queue

		说明：

			初始化Queue()对象时（例如：q=Queue()），若括号中没有指定最大可接收的消息数量，
			或数量为负值，那么就代表可接受的消息数量没有上限（直到内存的尽头）；

			Queue.qsize()：返回当前队列包含的消息数量；
			Queue.empty()：如果队列为空，返回True，反之False ；
			Queue.full()：如果队列满了，返回True,反之False；
			Queue.get([block[, timeout]])：获取队列中的一条消息，然后将其从列队中移除，block默认值为True；

		1）如果block使用默认值，且没有设置timeout（单位秒），消息列队如果为空，
		此时程序将被阻塞（停在读取状态），直到从消息列队读到消息为止，如果设置了timeout，则会等待timeout秒，
		若还没读取到任何消息，则抛出"Queue.Empty"异常；
		
		2）如果block值为False，消息列队如果为空，则会立刻抛出"Queue.Empty"异常；
		

		Queue.get_nowait()：相当Queue.get(False)；
		
		Queue.put(item,[block[, timeout]])：将item消息写入队列，block默认值为True；
		
		1）如果block使用默认值，且没有设置timeout（单位秒），消息列队如果已经没有空间可写入，
		   此时程序将被阻塞（停在写入状态），直到从消息列队腾出空间为止，如果设置了timeout，
		   则会等待timeout秒，若还没空间，则抛出"Queue.Full"异常；
		
		2）如果block值为False，消息列队如果没有空间可写入，则会立刻抛出"Queue.Full"异常；
		
		Queue.put_nowait(item)：相当Queue.put(item, False)；


	进程池中的Queue：

		如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()，
		而不是multiprocessing.Queue()，否则会得到一条如下的错误信息：

		RuntimeError: Queue objects should only be shared between processes through inheritance.




		from multiprocessing import Manager,Pool
		import os,time,random

		def reader(q):
			print("reader启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
			for i in range(q.qsize()):
				print("reader从Queue获取到消息：%s"%q.get(True))

		def writer(q):
			print("writer启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
			for i in "dongGe":
				q.put(i)

		if __name__=="__main__":
		    print("(%s) start"%os.getpid())
			q=Manager().Queue() #使用Manager中的Queue来初始化
			po=Pool()
			#使用阻塞模式创建进程，这样就不需要在reader中使用死循环了，可以让writer完全执行完成后，
			#再用reader去读取
				
			po.apply(writer,(q,))
			po.apply(reader,(q,))
			po.close()
			po.join()
			print("(%s) End"%os.getpid())



线程：

	python的thread模块是比较底层的模块，python的threading模块是对thread做了一些包装的，可以更加方便的被使用。

	每个线程一定会有一个名字，尽管上面的例子中没有指定线程对象的name，但是python会自动为线程指定一个名字。

	当线程的run()方法结束时该线程完成。

	无法控制线程调度程序，但可以通过别的方式来影响线程调度的方式。

	线程的几种状态
		
		新建-->就绪 <--等待（阻塞）--> 运行--->死亡	


	在一个进程内的所有线程共享全局变量，能够在不适用其他方式的前提下完成多线程之间的数据共享

	缺点就是，线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱（即线程非安全）

	进程VS线程：

		进程，能够完成多任务，比如 在一台电脑上能够同时运行多个QQ
		线程，能够完成多任务，比如 一个QQ中的多个聊天窗口

		进程是系统进行资源分配和调度的一个独立单位.

		线程是进程的一个实体,是CPU调度和分派的基本单位,它是比进程更小的能独立运行的基本单位.
		线程自己基本上不拥有系统资源,只拥有一点在运行中必不可少的资源(如程序计数器,一组寄存器和栈),
		但是它可与同属一个进程的其他的线程共享进程所拥有的全部资源.

		一个程序至少有一个进程,一个进程至少有一个线程.

		线程的划分尺度小于进程(资源比进程少)，使得多线程程序的并发性高。

		进程在执行过程中拥有独立的内存单元，而多个线程共享内存，从而极大地提高了程序的运行效率

		线线程不能够独立执行，必须依存在进程中


	什么是同步：

		同步就是协同步调，按预定的先后次序进行运行。

		"同"字从字面上容易理解为一起动作
		其实不是，"同"字应是指协同、协助、互相配合。
		
		如进程、线程同步，可理解为进程或线程A和B一块配合，A执行到一定程度时要依靠B的某个结果，
		于是停下来，示意B运行;B依言执行，再将结果给A;A再继续操作。

	互斥锁：

		当多个线程几乎同时修改某一个共享数据的时候，需要进行同步控制

		互斥锁为资源引入一个状态：锁定/非锁定。

		threading模块中定义了Lock类，可以方便的处理锁定：

			#创建锁
			mutex = threading.Lock()
			#锁定
			mutex.acquire([blocking])
			#释放
			mutex.release()
					

		当一个线程调用锁的acquire()方法获得锁时，锁就进入“locked”状态。
		每次只有一个线程可以获得锁。如果此时另一个线程试图获得这个锁，
		该线程就会变为“blocked”状态，称为“阻塞”，直到拥有锁的线程调用锁的release()方法释放锁之后，
		锁进入“unlocked”状态。

		线程调度程序从处于同步阻塞状态的线程中选择一个来获得锁，并使得该线程进入运行（running）状态。

		
		锁的好处：
			确保了某段关键代码只能由一个线程从头到尾完整地执行
		锁的坏处：
			阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了
			由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁

	死锁：

		在线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。

		避免死锁：
			程序设计时要尽量避免（银行家算法）
			添加超时时间等

	多个线程有序执行：
	
		可以使用互斥锁完成多个任务，有序的进程工作，这就是线程的同步

	



