"------------------------------------------------------"

				python 数据结构与算法

"-----------------------------------------------------"

算法概念：

	算法是计算机处理信息的本质，因为计算机程序本质上是一个算法来告诉计算机确切的步骤来执行一个指定的任务。
	
	算法是独立存在的一种解决问题的方法和思想。


	算法的五大特性
	
		1、输入: 算法具有0个或多个输入
		2、输出: 算法至少有1个或多个输出
		3、有穷性: 算法在有限的步骤之后会自动结束而不会无限循环，并且每一个步骤可以在可接受的时间内完成
		4、确定性：算法中的每一步都有确定的含义，不会出现二义性
		5、可行性：算法的每一步都是可行的，也就是说每一步都能够执行有限的次数完成
		

算法效率衡量：

	实现算法程序的执行时间可以反应出算法的效率，即算法的优劣。
	单纯依靠运行的时间来比较算法的优劣并不一定是客观准确的！

时间复杂度与“大O记法”：

	对于算法的时间效率，我们可以用“大O记法”来表示。
	
	“大O记法”：对于单调的整数函数f，如果存在一个整数函数g和实常数c>0，
	使得对于充分大的n总有f(n)<=c*g(n)，就说函数g是f的一个渐近函数（忽略常数），记为f(n)=O(g(n))。
	也就是说，在趋向无穷的极限意义下，函数f的增长速度受到函数g的约束，亦即函数f与函数g的特征相似。

	时间复杂度：假设存在函数g，使得算法A处理规模为n的问题示例所用时间为T(n)=O(g(n))，
	则称O(g(n))为算法A的渐近时间复杂度，简称时间复杂度，记为T(n)

	
	最坏时间复杂度:

		算法完成工作最少需要多少基本操作，即最优时间复杂度
		算法完成工作最多需要多少基本操作，即最坏时间复杂度
		算法完成工作平均需要多少基本操作，即平均时间复杂度


	时间复杂度的几条基本计算规则：
		
		1、基本操作，即只有常数项，认为其时间复杂度为O(1)
		2、顺序结构，时间复杂度按加法进行计算
		3、循环结构，时间复杂度按乘法进行计算
		4、分支结构，时间复杂度取最大值
		5、判断一个算法的效率时，往往只需要关注操作数量的最高次项，其它次要项和常数项可以忽略
		6、在没有特殊说明时，我们所分析的算法的时间复杂度都是指最坏时间复杂度
		
	算法分析：

		for a in range(0, 1001):
			for b in range(0, 1001):
				for c in range(0, 1001):
					if a**2 + b**2 == c**2 and a+b+c == 1000:
						print("a, b, c: %d, %d, %d" % (a, b, c))

		时间复杂度：T(n) = O(n*n*n) = O(n3)


		for a in range(0, 1001):
			for b in range(0, 1001-a):
				c = 1000 - a - b
				if a**2 + b**2 == c**2:
					print("a, b, c: %d, %d, %d" % (a, b, c))

		时间复杂度：T(n) = O(n*n*(1+1)) = O(n*n) = O(n2)


	常见时间复杂度:

		
	执行次数函数举例	   阶	                  非正式术语
	12	                  O(1)                   	常数阶
	2n+3	              O(n)                    	线性阶
	3n2+2n+1	          O(n2)	                    平方阶
	5log2n+20	          O(logn)	                对数阶
	2n+3nlog2n+19         O(nlogn)	                nlogn阶
	6n3+2n2+3n+4	      O(n3)	                    立方阶
	2^n	                  O(2^n)	                指数阶


	所消耗的时间从小到大

	O(1) < O(logn) < O(n) < O(nlogn) < O(n2) < O(n3) < O(2n) < O(n!) < O(nn)



Python内置类型性能分析:


timeit模块:

	timeit模块可以用来测试一小段Python代码的执行速度。	

	class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>)

		Timer是测量小段代码执行速度的类。
		stmt参数是要测试的代码语句（statment）；
		setup参数是运行代码时需要的设置；
		timer参数是一个定时器函数，与平台有关。
	
	timeit.Timer.timeit(number=1000000)

	Timer类中测试语句执行速度的对象方法。number参数是测试代码时的测试次数，默认为1000000次。
	方法返回执行代码的平均耗时，一个float类型的秒数。

	from timeit import Timer
	def test1():
		l = []
		for i in range(1000):
			l = l + [i]

	t1 = Timer("test1()", "from __main__ import test1")
	print("concat ",t1.timeit(number=1000), "seconds")




数据结构：

	1、概念：

		数据是一个抽象的概念，将其进行分类后得到程序设计语言中的基本类型。如：int，float，char等。
		数据元素之间不是独立的，存在特定的关系，这些关系便是结构。数据结构指数据对象中数据元素之间的关系。

		Python给我们提供了很多现成的数据结构类型，这些系统自己定义好的，不需要我们自己去定义的数据结构叫
		做Python的内置数据结构，比如列表、元组、字典。而有些数据组织方式，Python系统里面没有直接定义，
		需要我们自己去定义实现这些数据的组织方式，这些数据组织方式称之为Python的扩展数据结构，比如栈，队列等。

	
	2、算法与数据结构的区别：

		数据结构只是静态的描述了数据元素之间的关系。	
		高效的程序需要在数据结构的基础上设计和选择算法。
		程序 = 数据结构 + 算法
		总结：算法是为了解决实际问题而设计的，数据结构是算法需要处理的问题载体。

	3、抽象数据类型(Abstract Data Type)：

		抽象数据类型(ADT)的含义是指一个数学模型以及定义在此数学模型上的一组操作。
		即把数据类型和数据类型上的运算捆在一起，进行封装。
		引入抽象数据类型的目的是把数据类型的表示和数据类型上运算的实现与这些数据类型和
		运算在程序中的引用隔开，使它们相互独立。

		最常用的数据运算有五种：

			插入
			删除
			修改
			查找
			排序

	
顺序表：

	根据线性表的实际存储方式，分为两种实现模型：

	顺序表，将元素顺序地存放在一块连续的存储区里，元素间的顺序关系由它们的存储顺序自然表示。
	链表，将元素存放在通过链接构造起来的一系列存储块中。

	顺序表的结构与实现:

		一个顺序表的完整信息包括两部分，一部分是表中的元素集合，
		另一部分是为实现正确操作而需记录的信息，即有关表的整体情况的信息，
		这部分信息主要包括元素存储区的容量和当前表中已有的元素个数两项。


	顺序表的两种基本实现方式:

		一体式结构，存储表信息的单元与元素存储区以连续的方式安排在一块存储区里，
		两部分数据的整体形成一个完整的顺序表对象。

		分离式结构，表对象里只保存与整个表有关的信息（即容量和元素个数），
		实际数据元素存放在另一个独立的元素存储区里，通过链接与基本表对象关联。


	元素存储区替换:

		一体式结构由于顺序表信息区与数据区连续存储在一起，所以若想更换数据区，则只能整体搬迁，
		即整个顺序表对象（指存储顺序表的结构信息的区域）改变了。

		分离式结构若想更换数据区，只需将表信息区中的数据区链接地址更新即可，而该顺序表对象不变。

	元素存储区扩充:

		采用分离式结构的顺序表，若将数据区更换为存储空间更大的区域，
		则可以在不改变表对象的前提下对其数据存储区进行了扩充，所有使用这个表的地方都不必修改。
		只要程序的运行环境（计算机系统）还有空闲存储，这种表结构就不会因为满了而导致操作无法进行。
		人们把采用这种技术实现的顺序表称为动态顺序表，因为其容量可以在使用中动态变化。

		扩充的两种策略:

			每次扩充增加固定数目的存储位置，如每次扩充增加10个元素位置，这种策略可称为线性增长。

			特点：节省空间，但是扩充操作频繁，操作次数多。

			每次扩充容量加倍，如每次扩充增加一倍存储空间。

			特点：减少了扩充操作的执行次数，但可能会浪费空间资源。以空间换时间，推荐的方式。

Python中的顺序表:

	Python中的list和tuple两种类型采用了顺序表的实现技术，具有前面讨论的顺序表的所有性质。

	tuple是不可变类型，即不变的顺序表，因此不支持改变其内部状态的任何操作，而其他方面，则与list的性质类似

	在Python的官方实现中，list就是一种采用分离式技术实现的动态顺序表。

	list实现采用了如下的策略：在建立空表（或者很小的表）时，系统分配一块能容纳8个元素的存储区；
	在执行插入操作（insert或append）时，如果元素存储区满就换一块4倍大的存储区。
	但如果此时的表已经很大（目前的阀值为50000），则改变策略，采用加一倍的方法。
	引入这种改变策略的方式，是为了避免出现过多空闲的存储位置。


链表：

	顺序表的构建需要预先知道数据大小来申请连续的存储空间，而在进行扩充时又需要进行数据的搬迁，
	所以使用起来并不是很灵活。
	
	链表结构可以充分利用计算机内存空间，实现灵活的内存动态管理。

	链表（Linked list）是一种常见的基础数据结构，是一种线性表，但是不像顺序表一样连续存储数据，
	而是在每一个节点（数据存储单元）里存放下一个节点的位置信息（即地址）。



栈(stack)：

	栈(stack):
	
		又可以称为堆栈，是一种容器，可存入数据元素，访问数据，删除数据。特点在于只能允许
		在容器的一端（栈顶top）进行加入数据(push)和输出数据(pop)的运算。
		没有了位置概念，保证任何时候可以访问、删除的元素都是此前最后存入的那个元素，确定
		了一种默认的访问顺序。

		由于栈数据结构只允许在一端进行操作，因而按照后进先出(Last in First Out)的原理运行。


	栈结构实现：

		栈可以用顺序表实现，也可以用链表实现。

		class Stack(object):
			"""栈"""
			def __init__(self):
				self.items = []

			def is_empty(self):
				"""判断是否为空"""
				return self.items == []

			def push(self, item):
				"""加入元素"""
				self.items.append(item)

			def pop(self):
				"""弹出元素"""
				return self.items.pop()

			def peek(self):
				"""返回栈顶元素"""
				return self.items[len(self.items)-1]

			def size(self):
				"""返回栈的大小"""
				return len(self.items)

if __name__ == "__main__":
	stack = Stack()
	stack.push("hello")
	stack.push("world")
	stack.push("itcast")
	print stack.size()
	print stack.peek()
	print stack.pop()
	print stack.pop()
	print stack.pop()




队列：

	队列（queue）是只允许在一端进行插入操作，而在另一端进行删除操作的线性表。

	队列是一种先进先出的(First In First Out)的线性表,简称FIFO。
	允许插入的一端为对尾，允许删除的一端为队头。队列不允许中间部位进行操作
	假设队列是q=(a1,a2,...,an),那么a1就是队头元素，而an是队尾元素。


	队列的实现：

		同栈一样，队列也可以用顺序表或者链表实现。


		class Queue(object):
			"""队列"""
			def __init__(self):
				self.items = []

			def is_empty(self):
				return self.items == []

			def enqueue(self, item):
				"""进队列"""
				self.items.insert(0,item)

			def dequeue(self):
				"""出队列"""
				return self.items.pop()

			def size(self):
				"""返回大小"""
				return len(self.items)

	if __name__ == "__main__":
		q = Queue()
		q.enqueue("hello")
		q.enqueue("world")
		q.enqueue("itcast")
		print q.size()
		print q.dequeue()
		print q.dequeue()
		print q.dequeue()


双端队列：

	双端队列(deque,double-ended queue),是一种具有队列和栈的性质的数据结构

	双端队列中的元素可以从两端弹出，其限定插入和删除操作在表的两端进行，双端
	队列可以在任意一端入队出队。


	class Deque(object):
		"""双端队列"""
		def __init__(self):
			self.items = []

		def is_empty(self):
		"""判断队列是否为空"""
			return self.items == []

		def add_front(self, item):
		"""在队头添加元素"""
			self.items.insert(0,item)

		def add_rear(self, item):
		"""在队尾添加元素"""
			self.items.append(item)

		def remove_front(self):
		"""从队头删除元素"""
			return self.items.pop(0)

		def remove_rear(self):
		"""从队尾删除元素"""
			return self.items.pop()

		def size(self):
		"""返回队列大小"""
			return len(self.items)


	if __name__ == "__main__":
		deque = Deque()
		deque.add_front(1)
		deque.add_front(2)
		deque.add_rear(3)
		deque.add_rear(4)
		print deque.size()
		print deque.remove_front()
		print deque.remove_front()
		print deque.remove_rear()
		print deque.remove_rear()


排序与搜索:

	排序算法（英语：Sorting algorithm）是一种能将一串数据依照特定顺序进行排列的一种算法。

	排序算法的稳定性:

		稳定性：稳定排序算法会让原本有相等键值的纪录维持相对次序。
		也就是如果一个排序算法是稳定的，当有两个相等键值的纪录R和S，且在原本的列表中R出现在S之前，
		在排序过的列表中R也将会是在S之前。

		当相等的元素是无法分辨的，比如像是整数，稳定性并不是一个问题。
		然而，假设以下的数对将要以他们的第一个数字来排序。

		(4, 1)  (3, 1)  (3, 7)（5, 6）
		在这个状况下，有可能产生两种不同的结果，一个是让相等键值的纪录维持相对的次序，而另外一个则没有：

		(3, 1)  (3, 7)  (4, 1)  (5, 6)  （维持次序）
		(3, 7)  (3, 1)  (4, 1)  (5, 6)  （次序被改变）

		不稳定排序算法可能会在相等的键值中改变纪录的相对次序，但是稳定排序算法从来不会如此。

冒泡排序：

	冒泡排序（英语：Bubble Sort）是一种简单的排序算法。它重复地遍历要排序的数列，一次比较两个元素，
	如果他们的顺序错误就把他们交换过来。遍历数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
	这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

	冒泡排序算法的运作如下：
		
		比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
		对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
		针对所有的元素重复以上的步骤，除了最后一个。
		持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

	第一种方式：

		def bubble_sort(alist):
			for j in range(len(alist)-1,0,-1):
				# j表示每次遍历需要比较的次数，是逐渐减小的
			
				for i in range(j):
					if alist[i] > alist[i+1]:
						alist[i], alist[i+1] = alist[i+1], alist[i]

		li = [54,26,93,17,77,31,44,55,20]
		bubble_sort(li)
		print(li)


	第二种方式：

		def bubble_sort(alist):
			for i in range(len(alist)):
				for j in range(i+1,len(alist)):
					if alist[i] > alist[j]:
						alist[i],alist[j] = alist[j],alist[i]

		li = [54,26,93,17,77,44,55,20]
		bubble_sort(li)
		print(li)



	时间复杂度

	最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
	最坏时间复杂度：O(n2)
	稳定性：稳定


选择排序:

	选择排序（Selection sort)是一种简单直观的排序算法。它的工作原理如下。
	首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
	然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
	以此类推，直到所有元素均排序完毕。


	def selection_sort(alist):
		n = len(alist)
		for i in range(n-1):
		
			min_index = i
	
			for j in range(i+1, n):
				if alist[j] < alist[min_index]:
					min_index = j

			if min_index != i:
				alist[i], alist[min_index] = alist[min_index], alist[i]


	
	alist = [54,226,93,17,77,31,44,55,20]
	selection_sort(alist)
	print(alist)
		

	时间复杂度

	最优时间复杂度：O(n2)
	最坏时间复杂度：O(n2)
	稳定性：不稳定（考虑升序每次选择最大的情况）



插入排序:

	插入排序（英语：Insertion Sort）是一种简单直观的排序算法。
	它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
	插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

	def insert_sort(alist):
		# 从第二个位置，即下标为1的元素开始向前插入
		for i in range(1, len(alist)):
		# 从第i个元素开始向前比较，如果小于前一个元素，交换位置
			for j in range(i, 0, -1):
				if alist[j] < alist[j-1]:
					alist[j], alist[j-1] = alist[j-1], alist[j]

	
	alist = [54,26,93,17,77,31,44,55,20]
	insert_sort(alist)
	print(alist)


	最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
	最坏时间复杂度：O(n2)
	稳定性：稳定



快速排序:

	快速排序（英语：Quicksort），又称划分交换排序（partition-exchange sort），
	通过一趟排序将要排序的数据分割成独立的两部分，
	其中一部分的所有数据都比另外一部分的所有数据都要小，
	然后再按此方法对这两部分数据分别进行快速排序，
	整个排序过程可以递归进行，以此达到整个数据变成有序序列。

	步骤为：

	1、从数列中挑出一个元素，称为"基准"（pivot），
	2、重新排序数列，所有元素比基准值小的摆放在基准前面，
		所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
		在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
	3、递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

	递归的最底部情形，是数列的大小是零或一，也就是永远都已经被排序好了。
	虽然一直递归下去，但是这个算法总会结束，因为在每次的迭代（iteration）中，
	它至少会把一个元素摆到它最后的位置去。


	def quick_sort(alist, start, end):
		"""快速排序"""

		递归的退出条件
		if start >= end:
			return

		设定起始元素为要寻找位置的基准元素
		mid = alist[start]

		low为序列左边的由左向右移动的游标
		low = start

		high为序列右边的由右向左移动的游标
		high = end

		while low < high:
			
			如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
			while low < high and alist[high] >= mid:
				high -= 1
			将high指向的元素放到low的位置上
			alist[low] = alist[high]

			如果low与high未重合，low指向的元素比基准元素小，则low向右移动
			while low < high and alist[low] < mid:
				low += 1
			将low指向的元素放到high的位置上
			alist[high] = alist[low]

			退出循环后，low与high重合，此时所指位置为基准元素的正确位置
			将基准元素放到该位置
			alist[low] = mid

		# 对基准元素左边的子序列进行快速排序
		quick_sort(alist, start, low-1)

		# 对基准元素右边的子序列进行快速排序
		quick_sort(alist, low+1, end)


	alist = [54,26,93,17,77,31,44,55,20]
	quick_sort(alist,0,len(alist)-1)
	print(alist)


	时间复杂度

	最优时间复杂度：O(nlogn)
	最坏时间复杂度：O(n2)
	稳定性：不稳定


搜索:

	搜索是在一个项目集合中找到一个特定项目的算法过程。
	搜索通常的答案是真的或假的，因为该项目是否存在。 
	搜索的几种常见方法：顺序查找、二分法查找、二叉树查找、哈希查找	


	二分法查找:

		二分查找又称折半查找，优点是比较次数少，查找速度快，平均性能好
		其缺点是要求待查表为有序表，且插入删除困难。
		因此，折半查找方法适用于不经常变动而查找频繁的有序列表。	

		首先，假设表中元素是按升序排列，将表中间位置记录的关键字与查找关键字比较，
		如果两者相等，则查找成功；否则利用中间位置记录将表分成前、后两个子表，
		如果中间位置记录的关键字大于查找关键字，则进一步查找前一子表，否则进一步查找后一子表。
		重复以上过程，直到找到满足条件的记录，使查找成功，或直到子表不存在为止，此时查找不成功。
	
	二分法查找实现

		1、非递归实现

		def binary_search(alist, item):
			
			first = 0
			last = len(alist)-1
		
			while first<=last:
				
				midpoint = (first + last)/2
				
				if alist[midpoint] == item:
					return True
				
				elif item < alist[midpoint]:
			
					last = midpoint-1
				
				else:
					
					first = midpoint+1
			return False
		
		testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
		print(binary_search(testlist, 3))
		print(binary_search(testlist, 13))


	2、递归实现
		
		bnary_search(alist, item):
			
			if len(alist) == 0:
				return False
			
			else:
				
				midpoint = len(alist)//2
				if alist[midpoint]==item:
					return True
				else:
					
					if item<alist[midpoint]:
						return binary_search(alist[:midpoint],item)
					else:
						return binary_search(alist[midpoint+1:],item)

		testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
		print(binary_search(testlist, 3))
		print(binary_search(testlist, 13))


树与树算法:

	树（tree）是一种抽象数据类型（ADT）或是实作这种抽象数据类型的数据结构，
	用来模拟具有树状结构性质的数据集合。

	它是由n（n>=1）个有限节点组成一个具有层次关系的集合。具有如下特点：

		1、每个节点有零个或多个子节点
		
		2、没有父节点的节点称为根节点

		3、每个非根节点有且只要一个父节点

		4、除了根节点外，每个子节点可以分为多个不相交的子树

	树的术语：

		1、节点的度：一个节点含有的子树的个数称为该节点的度。
		2、树的度：一棵树中，最大的节点的度称为树的度
		3、叶节点或终端节点：度为零的节点
		4、父节点：若一个节点含有子节点，则这个节点称为其子节点的父节点
		5、子节点：一个节点含有的子树的根节点称为该节点的子节点；
		6、兄弟节点：具有相同父节点的节点互称为兄弟节点；
		7、节点的层次：从根开始定义起，根为第1层，根的子节点为第2层，以此类推；
		8、树的高度或深度：树中节点的最大层次；
		9、堂兄弟节点：父节点在同一层的节点互为堂兄弟；
		10、节点的祖先：从根到该节点所经分支上的所有节点；
		11、子孙：以某节点为根的子树中任一节点都称为该节点的子孙。
		12、森林：由m（m>=0）棵互不相交的树的集合称为森林；


	树的种类：

		1、无序树：树中任意节点的子节点之间没有顺序关系，这种树称为无序树，也称为自由树；
		2、有序树：树中任意节点的子节点之间有顺序关系，这种树称为有序树；
			二叉树：每个节点最多含有两个子树的树称为二叉树；
				完全二叉树：对于一颗二叉树，假设其深度为d(d>1)。
							除了第d层外，其它各层的节点数目均已达最大值，
							且第d层所有节点从左向右连续地紧密排列，这样的二叉树被称为完全二叉树，
							其中满二叉树的定义是所有叶节点都在最底层的完全二叉树
				平衡二叉树（AVL树）：当且仅当任何节点的两棵子树的高度差不大于1的二叉树；
				排序二叉树（二叉查找树（英语：Binary Search Tree），也称二叉搜索树、有序二叉树）；
			霍夫曼树（用于信息编码）：带权路径最短的二叉树称为哈夫曼树或最优二叉树；
			B树：一种对读写操作进行优化的自平衡的二叉查找树，能够保持数据有序，拥有多余两个子树。


	树的存储与表示：

		顺序存储：将数据结构存储在固定的数组中，然在遍历速度上有一定的优势，但因所占空间比较大，
				  是非主流二叉树。二叉树通常以链式存储。

		链式存储：可以存储，缺陷：指针域指针个数不定，解决方案：把多叉树，转成二叉树

	常见的一些树的应用场景：

		1.xml，html等，那么编写这些东西的解析器的时候，不可避免用到树
		
		2.路由协议就是使用了树的算法

		3.mysql数据库索引

		4.文件系统的目录结构

		5.所以很多经典的AI算法其实都是树搜索，此外机器学习中的decision tree也是树结构


二叉树：

	二叉树是每个节点最多有两个子树的树结构，通常子树被称作“左子树” 和 “右子树”

	二叉树的性质（特性）：

		性质1、在二叉树的第i层上至多有2^(i-1)个节点(i>0)
		性质2、深度为K的二叉树至多有2^k -1 个节点
		性质3、对于任意一棵二叉树，如果其叶结点数为N0，而度数为2的结点总数为N2，则N0=N2+1;
		性质4、具有n个结点的完全二叉树的深度必为 log2(n+1)
		性质5、对完全二叉树，若从上至下、从左至右编号，则编号为i 的结点，其左孩子编号必为2i，
			   其右孩子编号必为2i＋1；其双亲的编号必为i/2（i＝1 时为根,除外）


	二叉树的遍历:
		
		树的遍历是树的一种重要的运算。所谓遍历是指对树中所有结点的信息的访问，
		即依次对树中每个结点访问一次且仅访问一次，我们把这种对所有节点的访问称为遍历（traversal）。
	
		那么树的两种重要的遍历模式是深度优先遍历和广度优先遍历,深度优先一般用递归，
		广度优先一般用队列。一般情况下能用递归实现的算法大部分也能用堆栈来实现。


		深度优先遍历:

			对于一颗二叉树，深度优先搜索(Depth First Search)是沿着树的深度遍历树的节点，
			尽可能深的搜索树的分支。

			那么深度遍历有重要的三种方法。这三种方式常被用于访问树的节点，
			它们之间的不同在于访问每个节点的次序不同。
			这三种遍历分别叫做先序遍历（preorder），中序遍历（inorder）和后序遍历（postorder）。
			我们来给出它们的详细定义，然后举例看看它们的应用。
		
		先序遍历 在先序遍历中，我们先访问根节点，然后递归使用先序遍历访问左子树，
		再递归使用先序遍历访问右子树

		根节点->左子树->右子树
		

		中序遍历 在中序遍历中，我们递归使用中序遍历访问左子树，然后访问根节点，
		最后再递归使用中序遍历访问右子树
		
		左子树->根节点->右子树

		后序遍历 在后序遍历中，我们先递归使用后序遍历访问左子树和右子树，最后访问根节点
		左子树->右子树->根节点


		广度优先遍历(层次遍历):
			从树的root开始，从上到下从从左到右遍历整个树的节点

		#coding=utf-8

	class Node(object):
   	 	"""节点类"""
   	 	def __init__(self, elem=-1, lchild=None, rchild=None):
       	 		self.elem = elem
        		self.lchild = lchild
			self.rchild = rchild


	class Tree(object):
    	"""树类"""
    		def __init__(self):
        		self.root = Node()
        		self.myQueue = []

    		def add(self, elem):
        	"""为树添加节点"""
        		node = Node(elem)
        		if self.root.elem == -1:  # 如果树是空的，则对根节点赋值
            			self.root = node
            			self.myQueue.append(self.root)
       			 else:
           			treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            			if treeNode.lchild == None:
                			treeNode.lchild = node
                			self.myQueue.append(treeNode.lchild)
           			 else:
               				 treeNode.rchild = node
                			self.myQueue.append(treeNode.rchild)
                			self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。


    		def front_digui(self, root):
        	"""利用递归实现树的先序遍历"""
			if root == None:
			    return
			print root.elem,
			self.front_digui(root.lchild)
			self.front_digui(root.rchild)


		def middle_digui(self, root):
			"""利用递归实现树的中序遍历"""
			if root == None:
			    return
			self.middle_digui(root.lchild)
			print root.elem,
			self.middle_digui(root.rchild)


		def later_digui(self, root):
			"""利用递归实现树的后序遍历"""
			if root == None:
			    return
			self.later_digui(root.lchild)
			self.later_digui(root.rchild)
			print root.elem,


		def front_stack(self, root):
			"""利用堆栈实现树的先序遍历"""
			if root == None:
			    return
			myStack = []
			node = root
			while node or myStack:
			    while node:                     #从根节点开始，一直找它的左子树
				print node.elem,
				myStack.append(node)
				node = node.lchild
			    node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
			    node = node.rchild                  #开始查看它的右子树


		def middle_stack(self, root):
			"""利用堆栈实现树的中序遍历"""
			if root == None:
			    return
			myStack = []
			node = root
			while node or myStack:
			    while node:                     #从根节点开始，一直找它的左子树
				myStack.append(node)
				node = node.lchild
			    node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
			    print node.elem,
			    node = node.rchild                  #开始查看它的右子树


		  def later_stack(self, root):
			"""利用堆栈实现树的后序遍历"""
			if root == None:
			    return
			myStack1 = []
			myStack2 = []
			node = root
			myStack1.append(node)
			while myStack1:                   #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
			    node = myStack1.pop()
			    if node.lchild:
				myStack1.append(node.lchild)
			    if node.rchild:
				myStack1.append(node.rchild)
			    myStack2.append(node)
			while myStack2:                         #将myStack2中的元素出栈，即为后序遍历次序
			    print myStack2.pop().elem,


		  def level_queue(self, root):
			"""利用队列实现树的层次遍历"""
			if root == None:
			    return
			myQueue = []
			node = root
			myQueue.append(node)
			while myQueue:
			    node = myQueue.pop(0)
			    print node.elem,
			    if node.lchild != None:
				myQueue.append(node.lchild)
			    if node.rchild != None:
				myQueue.append(node.rchild)


		if __name__ == '__main__':
		    """主函数"""
		    elems = range(10)           #生成十个数据作为树节点
		    tree = Tree()          #新建一个树对象
		    for elem in elems:                  
			tree.add(elem)           #逐个添加树的节点

		    print '队列实现层次遍历:'
		    tree.level_queue(tree.root)

		    print '\n\n递归实现先序遍历:'
		    tree.front_digui(tree.root)
		    print '\n递归实现中序遍历:' 
		    tree.middle_digui(tree.root)
		    print '\n递归实现后序遍历:'
		    tree.later_digui(tree.root)

		    print '\n\n堆栈实现先序遍历:'
		    tree.front_stack(tree.root)
		    print '\n堆栈实现中序遍历:'
		    tree.middle_stack(tree.root)
		    print '\n堆栈实现后序遍历:'
		    tree.later_stack(tree.root)

	
