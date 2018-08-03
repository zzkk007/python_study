"-------------------------------------------------------------"

						数据库

"------------------------------------------------------------"

1、数据库:

	数据库，简而言之可视为电子化的文件柜---存储电子文件的处所，用户可以对文件中的数据运行
	新增、截取、更新、删除等操作。

	所谓的"数据库"系以一定方式储存在一起，能予多个用户共享、具有尽可能小的冗余度、与应用程序
	彼此独立的数据集合。

2、数据库管理系统：

	为管理数据库而设计的电脑软件系统，一般具有存储、截取、安全保障、备份等基本功能。
	数据库管理系统可以依据它所支持的数据库模型来做分类，例如：关系式、xml

3、类型：

	关系数据库：是创建在关系模型基础上的数据库，借助于集合代数等数学概念和方法来处理数据库中的数据。
		
		MySQL	
			MariaDB

		ORcal数据库

		PostgreSQL

		Microsoft Access
		等等


	非关系型数据库：是对不同于传统的关系数据库的数据库管理系统的统称。
					两者存在许多显著的不同点，其中最重要的是NoSQL不使用SQL作为查询语言。
					其数据存储可以不需要固定的表格模式，也经常会避免使用SQL的JOIN操作，一般有水平可扩展性的特征。
		
		BigTable
		MongoDB

	键值(key-value)数据库:Key-value数据库是一种以键值对存储数据的一种数据库，
				   类似java中的map。可以将整个数据库理解为一个大的map

		Apache Cassandra(Facebook所用) :高度可扩展
		LeveIDB	(google)
		
		内存型的数据库:
			redis
			memcache
			
			Redis是一个Key-Value存储系统。和Memcached类似，它支持存储的value类型相对更多，
			包括string(字符串)、list(链表)、set(集合)和zset(有序集合)。
			另外redis是一种内存型的数据库，所以可以对外提供很好地读写操作，
			但是同样也暴露出内存占用高，数据持久化不易等问题。


4、数据库模型：

	对象模型
	层次模型（轻量级数据访问协议）
	网状模型（大型数据储存）
	关系模型 :关系模型就是指二维表格模型,因而一个关系型数据库就是由二维表及其之间的联系组成的一个数据组织。
	面向对象模型
	半结构化模型
	平面模型（表格模型，一般在形式上是一个二维数组。如表格模型数据Excel)

5、架构
	
	数据库的架构可以大致区分为三个概括层次：内层、概念层和外层。
	内层：最接近实际存储体，亦即有关数据的实际存储方式。
	外层：最接近用户，即有关个别用户观看数据的方式。
	概念层：介于两者之间的间接层。

6、数据库索引：

	是数据库管理系统中一个排序的数据结构，以协助快速查询，更新数据库表中数据。

7、数据库事务：

	是数据管理系统执行过程中的一个逻辑单位，由一个有限的数据库操作序列构成。

8、数据库范式：

	设计关系数据库时，遵从不同的规范要求，设计出合理的关系型数据库，
	这些不同的规范要求被称为不同的范式，各种范式呈递次规范，越高的范式数据库冗余越小。

	目前关系数据库有六种范式：
	第一范式（1NF） :(列不可再分) 属性不可分,1NF是对属性的原子性约束，要求属性具有原子性，不可再分解
	第二范式（2NF） :(唯一标识)   符合1NF，并且非主属性完全依赖于码。2NF是对记录的惟一性约束，
					              要求记录有惟一标识，即实体的惟一性，更通俗说有主键ID
	第三范式（3NF） :(引用主键)   符合2NF，并且，消除传递依赖。3NF是对字段冗余性的约束，
								  即任何字段不能由其他字段派生出来，它要求字段没有冗余
	巴斯-科德范式(BCNF):符合3NF，并且，主属性不依赖于主属性。
	第四范式		：要求把同一表内的多对多关系删除。
	第五范式（5NF，又称完美范式）:从最终结构重新建立原始结构。

	
		
"-----------------------------------------------------------------------------------"

数据库系统-->数据库(show dadtabases)---->use 库名(切换数据库)--->show tables(一个库中的所有表)。

使用命令对数据库进行操作：

	1、远程连接数据库
		mysql -h 数据库IP -u 账号 -p 密码
	
	2、显示数据库列表
		show databases;

	3、打开数据库,切换数据库
		use mysql;

	4、查看数据库版本
		select version();
		select now(); 显示当前时间
	
	5、创建数据库
		create database 数据库名 charset=utf-8;
	
	6、删除数据库
		drop database 数据库名;

	7、查看当前选择的数据库
		select database();

使用命令对数据库表进行操作：

	1、查看当前数据库中的所有表
		show tables;
	
	2、创建表
		create table 表名(列及类型)
		例如：
		create table students(
			id int auto_increment primary key,
			sname varchar(10) not null
		);

	3、修改表
		alter table 表名 add|change|drop 列名 类型
		如：
		alter table student add birthday datetime;

	4、删除表
		drop table 表名；

	5、查看表结构
		desc 表名；

	6、更改表名称
		rename table 原表名 to 新表名

	7、查看表的创建语句
		show create table 表名;
	
	8、查看连接数,状态
		show processlist; 


数据操作：

	查询：
		
		select *from 表名

	增加：

		全列插入：insert into 表名 values(...)
		缺省插入：insert into 表名(列1,...) values(值1,...)
		同时插入多条数据：insert into 表名 values(...),(...)...;
		或insert into 表名(列1,...) values(值1,...),(值1,...)...;

		主键列是自动增长，但是在全列插入时需要占位，通常使用0，插入成功后以实际数据为准

	修改：

		update 表名 set 列1 = 值1，... where 条件

	删除：

		delete from 表名 where 条件

	
备份与恢复：

	备份：
	
		进入超级管理员:
			sudo -s 

		进入mysql库目录：
			cd /var/lib/mysql

		运行mysqldump命令
			mysqldump –uroot –p 数据库名 > ~/Desktop/备份文件.sql;
			按提示输入mysql的密码

	数据恢复：

		连接数据mysql,创建数据库
		退出链接，执行如下命令：
		mysql -uroot –p 数据库名 < ~/Desktop/备份文件.sql
		根据提示输入mysql密码

"-------------------------------------------------------------------------"

对数据进行操作：

	1、消除重复行
		在select后面列前使用distinct可以消除重复行
		select distinct gender from students;

	2、模糊查询：
		like 
		%表示任意多个任意字符
		_表示一个任意字符

		select * from students where sanme like 'huang%'
		select * from students where sanme lien 'huang_'
		

	3、范围查询

		in 表示在一个非连续的范围内

			查询编号是1或3或8的学生
			select * from student where id in(1,3,8);
		
		between ...and...表示在一个连续的范围内
			
			查询学生是3至8的学生
			select * from student where id between 3 and 8;

	4、空判断

		注意：null 与' '是不同的
		判断is null
		查询没有填写地址的学生
	
		select *from students where hometown is null;

		判非空is not null

		select * from students where hometown is not null;

	5、优先级

		小括号，not，比较运算符，逻辑运算符
		and比or先运算，如果同时出现并希望先算or，需要结合()使用

聚合：为了快速得到统计数据，提供了5个聚合函数
		
	1、count( *)表示计算总行数，括号中写星与列名，结果是相同的
		select count( *) from students;

	2、max(列)表示求此列的最大值
		select max(id) from student where gender = 0;

	3、min(列)表示求此列的最小值
		select min(id) from student where isdelete = 0;

	4、sum(列)表示求此列的和
		select sum(id) from student where gender =1;
	
	5、avg(列)求此列的平均值
		select avg(id) from students where isdelete=0 and gender=0;	


关系：
	
	如下三张表：
	学生表:students、       成绩表:scores、           科目表:subjects
		
		id                    id                            id          
		
		sname                 stuid (学生)                 stitle

		...                   subid (科目)                  ...

							  score (成绩)

	成绩表中，学生列应该存储什么信息？

	答：学生列的数据不是在这里新建的，而应该从学生表引用过来，关系也是一条数据。
		根据范式要求应该存储学生的编号，而不是学生的姓名等其他信息。
		同理，科目表也是关系表，引用科目表中的数据。


		create table scores(
				id int primary key auto_increment,
				stuid int,
				subid int,
				score decimal(5,2),
				foreign key(stuid) references students(id) on delete cascade,
				foreign key(subid) references subjects(id)  on delete cascade
				);

	问：查询每个学生每个科目的分数?
	分析：学生姓名来源于students表，科目名称来源于subjects，分数来源于scores表，
		  怎么将3个表放到一起查询，并将结果显示在同一个结果集中呢？
	答：当查询结果来源于多张表时，需要使用连接查询
	关键：找到表间的关系，当前的关系是
	students表的id---scores表的stuid
	subjects表的id---scores表的subid

	select student.sname,subject.stitle,scores.score from scores 
	inner join students on score.stuid = students.id
	inner join subjects on score.subid = subjects.id

	结论：当需要对有关系的多张表进行查询时，需要使用连接join
	

连接查询:

	连接查询分类如下：
	表A inner join 表B: 表A与表B匹配的行会出现在结果中

	表A left join 表B: 表A与表B匹配的行会出现在结果中，外加表A中独有的数据，未对应的数据使用null填充。

	表A right join 表B: 表A与表B匹配的行会出现在结果中，外加表B独有的数据，为对应的数据使用null填充。

	在查询或条件中推荐使用“表名.列名”的语法
	如果多个表中列名不重复可以省略“表名.”部分
	如果表的名称太长，可以在表名后面使用' as 简写名'或' 简写名'，为表起个临时的简写名称


外键：
	
	外键的作用,主要有两个:
	一个是让数据库自己通过外键来保证数据的完整性和一致性
	一个就是能够增加ER图的可读性

	有些人认为外键的建立会给开发时操作数据库带来很大的麻烦.
	因为数据库有时候会由于没有通过外键的检测而使得开发人员删除,插入操作失败.
	他们觉得这样很麻烦，其实这正式外键在强制你保证数据的完整性和一致性.这是好事儿。

	添加外键的格式:

	alter table students add [CONSTRAINT 外键名] FOREIGN KEY[id](index_col_name, ...)
	REFERENCES  tbl_name (index_col_name, ...)
	[ON DELETE {CASCADE | SET NULL | NO ACTION | RESTRICT}]
	[ON UPDATE {CASCADE | SET NULL | NO ACTION | RESTRICT}]

	说明：
		on delete/on update,用于定义delete,update操作.以下是update,delete操作的各种约束类型:

		CASCADE: 
			级联，外键表中外键字段值会被更新,或所在的列会被删除.
		
		RESTRICT:
			限制，默认值，抛异常.
		
		set null:
			被父面的外键关联字段被update ,delete时,子表的外键列被设置为null.
			而对于insert,子表的外键列输入的值,只能是父表外键关联列已有的值.否则出错.
		
		no aciton:
			什么都不做
		
	外键定义服从下列情况：(前提条件)
		1、所有tables必须是InnoDB型，它们不能是临时表.因为在MySQL中只有InnoDB类型的表才支持外键.

		2、所有要建立外键的字段必须建立索引.

		3、对于非InnoDB表，FOREIGN KEY子句会被忽略掉。

	例子：
		
		DROP TABLE IF EXISTS `user_backups_target`;
		CREATE TABLE `user_backups_target` (
			`id` int(11) NOT NULL auto_increment,
			`target_mail` varchar(70) NOT NULL,
			`company_id` int(11) NOT NULL,
			`domain_id` int(11) NOT NULL,
			`sent` tinyint(1) NOT NULL default '0',
			`inbox` tinyint(1) NOT NULL default '0',
			`operator` varchar(70) NOT NULL,
			`usersinfo_id` bigint(20) NOT NULL,
			`create_time` datetime NOT NULL,
			
			PRIMARY KEY  (`id`),
			KEY `sent` USING HASH (`sent`),
			KEY `inbox` USING HASH (`inbox`)
			) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=gbk;



		DROP TABLE IF EXISTS `user_backups_source`;
		CREATE TABLE `user_backups_source` (
			`id` bigint(20) NOT NULL auto_increment,
			`source_mail` varchar(70) NOT NULL,
			`target_mail_id` int(11) NOT NULL COMMENT '目的邮箱ID',
			`create_time` datetime NOT NULL,
			`usersinfo_id` bigint(20) NOT NULL COMMENT '暂时关联外键做级联删除,等到删除成员功能添加到java再去除此列'
			PRIMARY KEY  (`id`),
			KEY `usersinfoid` (`usersinfo_id`),
			KEY `target_id` (`target_mail_id`),
			KEY `source_mail` USING HASH (`source_mail`),
						
						"外键名"                   "外键"                         "关联的表"     "关联表中的键"
			CONSTRAINT `target_id` FOREIGN KEY (`target_mail_id`) REFERENCES `user_backups_target` (`id`) 
			ON DELETE CASCADE ON UPDATE CASCADE,
			
			CONSTRAINT `usersinfoid` FOREIGN KEY (`usersinfo_id`) REFERENCES `usersinfo-20180615` (`id`) 
			ON DELETE CASCADE ON UPDATE CASCADE
			) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=gbk;


mysql数据库字符串函数：
	
	1、查看字符的ascii码值(str)，str是空串时返回0
		select ascii('a');

	2、查看ascii码值对应的字符串char(数字)
		select char(99)

	3、拼接字符串concat(str1,str2)
		select concat(12,34,'ab')
	
	4、包含字符串个数length(str)
		select length('abc')

	5、截取字符串

		ltrim(str)返回删除了左空格的字符串str
		rtrim(str)返回删除了右空格的字符串str
		trim([方向 remstr from str)返回从某侧删除remstr后的字符串str，
		方向词包括both、leading、trailing，表示两侧、左、右])

		select trim('  bar   ');
		select trim(leading 'x' FROM 'xxxbarxxx');
		select trim(both 'x' FROM 'xxxbarxxx');
		select trim(trailing 'x' FROM 'xxxbarxxx');

	6、返回由n个空格字符组成的一个字符串space(n)
		select space(10);
	
	7、替换字符串replace(str,from_str,to_str)
		select replace('abc123','123','def')
	
	8、大小写转换，函数如下
		lower(str)
		upper(str)
		select lower('aBcD');


mysql数学函数：

	1、求绝对值abs(n)
		select abs(-32);
	
	2、求m除以n的余数mod(m,n),同运算符%
		select mod(10,3);
		select 10%3;
	
	3、地板floor(n)，表示不大于n的最大整数
		select floor(2.3);
	
	4、天花板ceiling(n)，表示不小于n的最大整数
		select ceiling(2.3);

	5、求四舍五入值round(n,d)，n表示原数，d表示小数位置，默认为0
		select round(1.6);

	6、求x的y次幂pow(x,y)
		select pow(2,3);

	7、获取圆周率PI()
		select PI();

	8、随机数rand()，值为0-1.0的浮点数
		select rand();

mysql日期时间函数:

	1、获取子值，语法如下
		year(date)返回date的年份(范围在1000到9999)
		month(date)返回date中的月份数值
		day(date)返回date中的日期数值
		hour(time)返回time的小时数(范围是0到23)
		minute(time)返回time的分钟数(范围是0到59)
		second(time)返回time的秒数(范围是0到59)
	
		select year('2016-12-21');
	
	2、日期计算，使用+-运算符，数字后面的关键字为year、month、day、hour、minute、second

		select '2016-12-21'+interval 1 day;

	3、日期格式化date_format(date,format)，format参数可用的值如下
		
		获取年%Y，返回4位的整数
		*　获取年%y，返回2位的整数
		*　获取月%m，值为1-12的整数
		获取日%d，返回整数
		*　获取时%H，值为0-23的整数
		*　获取时%h，值为1-12的整数
		*　获取分%i，值为0-59的整数
		*　获取秒%s，值为0-59的整数

		select date_format('2016-12-21','%Y %m %d');

	4、当前日期current_date()

		select current_date();

	5、当前时间current_time();
		
		select current_time()

	6、当前日期时间

		select now()

视图：

	对于复杂的查询，在多次使用后，维护是一件非常麻烦的事情
	解决：定义视图
	视图本质上是对查询的一个封装
	定义视图
		
		create view stuscore as 
		select students.*,scores.score from scores
		inner join students on scores.stuid=students.id;

	视图的用途就是查询：

		select * from stuscore;


事务：

	当一个业务逻辑需要多个sql完成时，如果其中某条sql语句出错，则希望整个操作都回退
	使用事务可以完成退回的功能，包证业务逻辑的正确性
	
	事务四大特征(简称ACID)
		原子性(Atomicity):事务中的全部操作在数据库中是不可分割的，要么全部完成，要么均不执行
		一致性(Consistency)：几个并行执行的事务，其执行结果必须与按某一顺序串行执行的结果相一致
		隔离性(Isolation)：事务的执行不受其他事务的干扰，事务执行的中间结果对其他事务必须是透明的
		持久性(Durability)：对于任意已提交事务，系统必须保证该事务对数据库的改变不被丢失，即使数据库出现故障

	要求：表的类型必须是innodb或bdb类型，才可以对此表使用事务

	事务语句
	开启 begin;
	提交 commit;
	回滚 rollback;

	

"-----------------------------------------------------------------------------------------------"

数据库与Python交互：

1、安装mysql模块

	apt-get insatll python-mysql

2、在文件中引入模块

	import Mysqldb

3、Connection 对象:

	用于建立与数据库的连接
	创建对象：调用connect()方法

	conn = connect(参数列表)
		
		参数host：连接的mysql主机IP
		参数port：连接的mysql主机的端口
		参数db：数据库的名称
		参数user:连接用户名
		参数password:连接密码
		参数charset：通信采用的编码方式，默认是'db2312'

	对象的方法：
		close()关闭连接
		commit()事务，所以需要提交才会生效
		rollback()事务，放弃之前的操作
		cursor()返回Cursor对象，用于执行sql语句并获得结果

4、Cursor对象：

	执行sql语句
	创建对象：调用Connection对象的cursor()方法
	cursor1 = conn.cursor()

	对象的方法：
		
		close()关闭
		execute(operation,[,parameters])执行语句，返回受影响的行数
		fetchone() 执行查询语句时，获取查询结果集的第一个行数据，返回一个元组
		next()执行查询语句时，获取当前行的下一行
		fetchall()执行查询时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回
		scroll(value,[,mode])将行指针移动到某个位置
			mode 表示移动的方式
			mode的默认值为reltive，表示基于当前行移动到value,value为正则向下移动，value为负则向上移动。
			mode的值为absolute，表示基于第一条数据的位置，第一条数据的位置为0

	对象属性:
		rowcount只读属性，表示最近一次excute()执行后受影响的行数
		connection获得当前连接对象


"-----------------------------------------------------------------------------------------"


增加、更新、删除


	#encoding=utf-8
	import MySQLdb
	try:
		conn=MySQLdb.connect(host='localhost',port=3306,db='test1',user='root',passwd='mysql',charset='utf8')
	    cs1=conn.cursor()
	    count=cs1.execute("insert into students(sname) values('张良')")
		count=cs1.execute("update students set sname='刘邦' where id=6")
		count=cs1.execute("delete from students where id=6")

		'''
		sname=raw_input("请输入学生姓名：")
		params=[sname]
		count=cs1.execute('insert into students(sname) values(%s)',params)
		'''

		print(count)
		conn.commit()
	    cs1.close()
	    conn.close()
	except Exception,e:
	    print(e.message)


查询数据：

	#encoding=utf8
	import MySQLdb
	try:
		conn=MySQLdb.connect(host='localhost',port=3306,db='test1',user='root',passwd='mysql',charset='utf8')
	    cur=conn.cursor()
	    cur.execute('select * from students where id=7')
		
		"一行"
		result=cur.fetchone()
		"所有"
		result=cur.fetchall()    

		print(result)
		cur.close()
		conn.close()
	except Exception,e:
	    print(e.message)
		

封装：

	观察前面的文件发现，除了sql语句及参数不同，其它语句都是一样的
	创建MysqlHelper.py文件，定义类
	
	#encoding=utf8
	import MySQLdb

	class MysqlHelper():
		def __init__(self,host,port,db,user,passwd,charset='utf8'):
			self.host=host
			self.port=port
			self.db=db
			self.user=user
			self.passwd=passwd
			self.charset=charset

		def connect(self):
	s		elf.conn=MySQLdb.connect(host=self.host,port=self.port,db=self.db,user=self.user,passwd=self.passwd,charset=self.charset)
			self.cursor=self.conn.cursor()

		def close(self):
			self.cursor.close()
			self.conn.close()

		def get_one(self,sql,params=()):
			result=None
			try:
				self.connect()
				self.cursor.execute(sql, params)
				result = self.cursor.fetchone()
				self.close()
			except Exception, e:
				print(e.message)
				return result

		def get_all(self,sql,params=()):
			list=()
			try:
				self.connect()
				self.cursor.execute(sql,params)
				list=self.cursor.fetchall()
				self.close()
			except Exception,e:
				print(e.message)
			return list

		def insert(self,sql,params=()):
			return self.__edit(sql,params)

		def update(self, sql, params=()):
			return self.__edit(sql, params)

		def delete(self, sql, params=()):
			return self.__edit(sql, params)

		def __edit(self,sql,params):
			count=0
			try:
				self.connect()
				count=self.cursor.execute(sql,params)
				self.conn.commit()
				self.close()
		   except Exception,e:
				print e.message
				return count



添加:

	创建testInsertWrap.py文件，使用封装好的帮助类完成插入操作
	#encoding=utf8
	from MysqlHelper import *

	sql='insert into students(sname,gender) values(%s,%s)'
	sname=raw_input("请输入用户名：")
	gender=raw_input("请输入性别，1为男，0为女")
	params=[sname,bool(gender)]
	
	mysqlHelper=MysqlHelper('localhost',3306,'test1','root','mysql')
	count=mysqlHelper.insert(sql,params)
	if count==1:
	    print 'ok'
	else:
		print 'erro'

查询一个

	创建testGetOneWrap.py文件，使用封装好的帮助类完成查询最新一行数据操作
	#encoding=utf8
	from MysqlHelper import *

	sql='select sname,gender from students order by id desc'

	helper=MysqlHelper('localhost',3306,'test1','root','mysql')
	one=helper.get_one(sql)
	print(one)

"--------------------------------------------------------------------------------"

mongo:








"================================================================================="

redis:

NoSQL简介：

	NoSQL,全名为Not Noly SQL，指的是非关系数据库
	随着访问量的上升，网站的数据库性能出现了问题，于是nosql被设计出来
	
	优点:

		高扩展性
		分布式计算
		低成本
		架构的灵活性，半结构化数据
		没有复杂的关系

	缺点：

		没有标准化
		有限的查询功能（到目前为止）
		最终一致时不直观的程序

	分类：

		类型                      部分代表                           特点


		列存储                Hbase、Cassandra、Hypertable      顾名思义，是按列存储数据的。
																最大的特点是方便存储结构化和半结构化数据，
																方便做数据压缩，对针对某一列或
																者某几列的查询有非常大的IO优势。  

		文档存储              MongoDB、CouchDB        文档存储一般类似json的格式存储，存储的内容是文档型的
													  这样也就有机会对某些字段建立索引，实现关系数据某些功能。


		key-value           redis、memcacheDB         可以通过key快速查询到其value，一般来说，存储不管value的格式
													  照单全收。(redis包含了其他功能)
		  存储


		图存储			    Neo4J、FlockDB           图形关系是最佳存储，使用传统关系数据库来解决的话性能低下，
													 而且设计使用不方便。

		对象存储            db4o、versant            通过类似面向对象语言的语法操作数据库，通过对象的方式存储数据


		xml数据库           Berkeley DB XML BaseX    高效的存储XML数据，并支持XML内部查询语法，比如Xpath、XQuery



Redis 

安装：

	1、下载redis 压缩包 wget http://download.redis.io/releases/redis-3.2.8.tar.gz
		官网：https://redis.io/
			
	2、解压：tar xvf redis-3.2.8.tar.gz
				
	3、cd src & make
					
	4、 make完成之后,进行install,默认安装路径为/usr/local/bin下,这里我们把他安装目录放到/usr/local/redis下,
		使用PREFIX指定目录:
		make PREFIX=/usr/local/redis install
		export PATH=/usr/local/redis/bin:/usr/local/mongodb/bin:$PATH:$HOME/bin

	5、make install


起服务：
	
	/usr/local/redis/bin目录下：
	1、./redis-server 

	2、./redis-cli -c -p 端口6379   看看是否连接成功
			
	3、停止redis:  （强行终止redis进程会导致数据丢失，因此应该正确停止redis,发送命令）
		redis-cli SHUTDOWN
		或者使用kill命令结束redis进程，效果同上。


hiredis的安装与使用：

	1、hiredis是Redis数据库的简约C客户端库，是redis官方的C语言客户端，
		支持所有命令（command set），管道（pipelining），时间驱动编程（event driven programming）。

	2、在redis的发行包中的deps目录中就包含hiredis的源码，手动编译安装。

	3、cd  deps/hiredis
		make
		make install

		mkdir /usr/lib/hiredis
		cp libhiredis.so /usr/lib/hiredis //将动态连接库libhiredis.so至/usr/lib/hiredis
		mkdir /usr/include/hiredis
		cp hiredis.h /usr/include/hiredis   //头文件包含#include<hiredis/hiredis.h>	


	4、gcc test.c -lhiredis   //编译链接

	5、编译gcc local_redis.c -lhiredis 
	6、./a.out
		./a.out: error while loading shared libraries: libhiredis.so.0.11: 
		cannot open shared object file: No such file or directory
	
	7、增加共享库：
		如果共享库文件安装到了/usr/local/lib(很多开源的共享库都会安装到该目录下)或其它"非/lib或/usr/lib"目录下, 
		那么在执行ldconfig命令前, 还要把新共享库目录加入到共享库配置文件/etc/ld.so.conf中, 如下:  
		# cat /etc/ld.so.conf
		include ld.so.conf.d/*.conf
		# echo "/usr/local/lib" >> /etc/ld.so.conf
		# ldconfig


	8、redis C语言API简单函数使用介绍：
	
		#include <hiredis/hiredis.h>
		#include "tommail.h"

		//Convert characters to the timestamp
		unsigned long strtotime(char *date) 
		{
			struct tm t;
			unsigned long time;

			sscanf(date,"%d-%d-%d",&t.tm_year,&t.tm_mon,&t.tm_mday);

			t.tm_year-=1900; 
			t.tm_mon-=1; 
			t.tm_mday+=1;
			t.tm_hour=0; 
			t.tm_min=0;
			t.tm_sec=0;
			time=mktime(&t);    //将结构体时间转换成秒数 

			return time;

		}

		//Get the timestamp in the morning
		unsigned long get_timestamp()
		{

			unsigned int tamp;
			time_t now_sec;
			struct tm * now_local;
			char now_date[10+1];
			memset(now_date,0x00,sizeof(now_date));
			time(&now_sec);
			now_local = localtime(&now_sec);
			strftime(now_date,sizeof(now_date),"%Y-%m-%d",now_local);

			tamp = strtotime(now_date);

			return tamp;
		}

		int redis_get_user_info(char *userid)
		{

		    //log_info("The get key[%s] in the redis",userid);
			//记得把ip和端口写在配置文件里,ini.c ini.h md.cf

			char *p;
			int redis_port;
			p = strchr(conf.redis_ip,':');
			if(p)
			{
				*p = '\0';
				redis_port = atoi(p+1);
			}
			else
			{
				redis_port = 6379;
			}


			redisContext *RedisC = redisConnect(conf.redis_ip,redis_port);
			if(RedisC->err)
			{
				redisFree(RedisC);
				log_info("Link the redis ip[%s],port[%d] FAIL!!",conf.redis_ip,redis_port);
				return TOM_ERR;
			}

			char sql[512] = {0};
			memset(sql, 0, sizeof(sql));

			sprintf(sql, "get %s",userid);
			//log_info("[%s] int the redis",sql);

			redisReply* RedisR = (redisReply*)redisCommand(RedisC,sql); 
			if(RedisR->type == REDIS_REPLY_NIL)
			{
				//返回nil对象，说明不存在要访问的数据。
				log_info("There [%s] not int redis",sql);
				freeReplyObject(RedisR);
				redisFree(RedisC);
				return REDIS_NOTDATA;

			}
			if(RedisR->type != REDIS_REPLY_STRING)
			{
				 log_info("Failed to execute sql[%s].\n",sql);
				 freeReplyObject(RedisR);
				 redisFree(RedisC);
				 return TOM_ERR;
			}

			//log_info("The value of [%s] is [%s]",userid,RedisR->str);
			int ret=atoi(RedisR->str);
			freeReplyObject(RedisR);
			redisFree(RedisC);
			return ret;
		}

		//update send_number in the redis
		int redis_incr_user_info(char *userid)
		{

			char *p;
			int  redis_port;
			p = strchr(conf.redis_ip,':');
			if(p)
			{
				p = '\0';
				redis_port = atoi(p+1);
			}
			else
			{
				redis_port = 6379;
			}


			redisContext *RedisC = redisConnect(conf.redis_ip,redis_port);
			if(RedisC->err)
			{
				redisFree(RedisC);
				log_info("Link the redis ip[%s],port[%d] FAIL!!",conf.redis_ip,redis_port);
				return TOM_ERR;
			}

			char sql[512] = {0};
			memset(sql, 0, sizeof(sql));

			sprintf(sql, "incr %s",userid);
			//log_info("[%s] int the redis",sql);

			redisReply* RedisR = (redisReply*)redisCommand(RedisC,sql); 
			if(RedisR->type != REDIS_REPLY_INTEGER)
			{
				 log_info("Failed to execute sql[%s].\n",sql);
				 freeReplyObject(RedisR);
				 redisFree(RedisC);
				 return TOM_ERR;
			}

			freeReplyObject(RedisR);
			redisFree(RedisC);

			return TOM_SUC;
		}

		int redis_set_user_info(char *userid,int value)
		{
			//log_info("The set key[%s],value[%d] in the redis",userid,value);

			char *p;
			int  redis_port;
			p = strchr(conf.redis_ip,':');
			if(p)
			{
				p = '\0';
				redis_port = atoi(p+1);
			}
			else
			{
				redis_port = 6379;
			}


			redisContext *RedisC = redisConnect(conf.redis_ip,redis_port);
			if(RedisC->err)
			{
				redisFree(RedisC);
				log_info("Link the redis ip[%s],port[%d] FAIL!!",conf.redis_ip,redis_port);
				return TOM_ERR;
			}

			char sql[512] = {0};
			memset(sql, 0, sizeof(sql));

			sprintf(sql, "set %s %d",userid,value);
			//log_info("[%s] int the redis",sql);

			redisReply* RedisR = (redisReply*)redisCommand(RedisC,sql); 
			if(NULL == RedisR)
			{
				redisFree(RedisC);
				return TOM_ERR;
			}

			if(!(RedisR->type == REDIS_REPLY_STATUS && strcasecmp(RedisR->str,"OK") == 0))
			{
				log_info("Failed to execute sql[%s].",sql);
				freeReplyObject(RedisR);
				redisFree(RedisC);
				return TOM_ERR;
			}
			freeReplyObject(RedisR);


			//设置到期时间戳
			unsigned long int timestamp;
			timestamp = get_timestamp();
			char timebuff[512] = {0};
			memset(timebuff, 0, sizeof(timebuff));
			sprintf(timebuff, "expireAt %s %ld",userid,timestamp);
			//log_info("set time stamp [%s] int the redis",timebuff);

			redisReply* RedisT = (redisReply*)redisCommand(RedisC,timebuff);
			if(NULL == RedisT)
			{
				redisFree(RedisC);
				return TOM_ERR;
			}


			if(1==RedisT->integer) 
			{
				freeReplyObject(RedisT);
				redisFree(RedisC);
			}
			else
			{
				 log_info("Failed to execute timebuff[%s].",timebuff);
				 freeReplyObject(RedisT);
				 redisFree(RedisC);
				 return TOM_ERR;
			}

			return TOM_SUC;
		}

		int redis_ttl_user_info(char *userid)
		{

			char *p;
			int  redis_port;
			p = strchr(conf.redis_ip,':');
			if(p)
			{
				p = '\0';
				redis_port = atoi(p+1);
			}
			else
			{
				redis_port = 6379;
			}


			redisContext *RedisC = redisConnect(conf.redis_ip,redis_port);
			if(RedisC->err)
			{
				redisFree(RedisC);
				log_info("Link the redis ip[%s],port[%d] FAIL!!",conf.redis_ip,redis_port);
				return TOM_ERR;
			}

			char sql[512] = {0};
			memset(sql, 0, sizeof(sql));

			sprintf(sql, "ttl %s",userid);
			//log_info("[%s] int the redis",sql);

			redisReply* RedisR = (redisReply*)redisCommand(RedisC,sql); 
			if(RedisR->type != REDIS_REPLY_INTEGER)
			{
				 log_info("Failed to execute sql[%s].\n",sql);
				 freeReplyObject(RedisR);
				 redisFree(RedisC);
				 return TOM_ERR;
			}

			int ret = RedisR->integer;
			freeReplyObject(RedisR);

			log_info("ttl userid =%s RedisR->integer =%d",userid,ret);
			if(-1==ret)
			{
				//设置到期时间戳
				unsigned long int timestamp;
				timestamp = get_timestamp();
				char timebuff[512] = {0};
				memset(timebuff, 0, sizeof(timebuff));
				sprintf(timebuff, "expireAt %s %ld",userid,timestamp);
				//log_info("set time stamp [%s] int the redis",timebuff);

				redisReply* RedisT = (redisReply*)redisCommand(RedisC,timebuff);
				if(NULL == RedisT)
				{
					redisFree(RedisC);
					return TOM_ERR;
				}
				if(1==RedisT->integer) 
				{
					freeReplyObject(RedisT);
					redisFree(RedisC);
				}
				else
				{
					 log_info("Failed to execute timebuff[%s].",timebuff);
					freeReplyObject(RedisT);
					redisFree(RedisC);
					return TOM_ERR;
				}
			}
			return TOM_SUC;
		}


"--------------------------------------------------------------------------------------"

redis 数据操作：

	redis 是key-value的数据，所以每个数据都是一个键值对
	键的类型是字符串
	值的类型分为5种：
		字符串string
		哈希hash
		列表list
		集合set
		有序集合zset


键的命令： 使用与所有的值的类型：字符串、hash、列表、集合、有序集合。
	
	查找键，参数支持正则
		KEYS pattern

	判断键是否存在，如果存在返回1，不存在返回0
		EXISTS key [key ...]

	查看键对应的value的类型
		TYPE key

	删除键以及对应的值
		DEL key [key ..]	

	设置过期时间，以秒为单位
	创建时没有设置过期时间则一直存在，知道使用del移除
		EXPIRE key seconds

	查看有效时间，以秒为单位
		TTL key


"--------------------------------------------------------------------------"

redis类型之string:

	string是reids最基本的类型
	最大能存储512MB数据
	string类型是二进制安全的，即可以为任何数据，比如数字、图片、序列化对象等。

	命令：
	
	设置：	

		1、设置键值
			set key value

		2、设置键值及过期时间，以秒为单位
			SETEX key seconds value
	
		3、设置多个键值
			MSET key value  key value ...

	获取：

		1、根据键获取值，如果存在此键返回nil
			GET key

		2、根据多个键获取多个值
			MGET key key ...

	运算：
		
		要求：值是数字

		将key对应的value加1
			INCR key

		将key对应的value加整数
			INCRBY key increment

		将key对应的value减1
			DECR key

		将key对应的value减整数
			DECRBY key decrement

	其他：

		追加值：
			APPEND key value
		
		获取值长度:
			STRLEN key


"--------------------------------------------------------------------------------------"


哈希(Hash)类型:

	Reids 哈希(Hash)类型是字符串key和字符串value之间的映射，所有它十分适合用来表示一个对象信息。
	如我们可以将一个用户对象存储为一个哈希类型，将用户名、年龄、性别等属性各表示一个key-value对。

	哈希在某些应用场景中是一个非常有用存储方式，你可以将数以百万计的对象存储在一个很小的 Redis实例中。
	一个Redis 哈希值可存储232-1(40亿)个key-value对。
	

哈希类型中的设置命令以及使用：
	
	对哈希类型的操作，就是对一个哈希表的操作，对哈希表的设置及取值，就是对哈希表中字段的设置与取值。

	HSET-设置值：

		HSET key field value
		
		设置哈希表key的field字段值为value。如果key不存在，一个新的哈希表会被创建并进行HSET操作。
		如果field字段已经存储，旧值将被覆盖。
		使用HSET命令，每次只能设置一个属性(字段)值，如果需要同时设置多个，可以使用HMSET命令。
	
		复杂度、返回值：
			时间复杂度：O(1)
			返回值：如果field 是哈希表中的一个新字段，并且设置成功，返回1.如果field已存在，且旧值
					已被新值覆盖，则返回0。

		
	HSETNX-字段不存则设置其值，如果存在该操作无效
		
		HSETNX key field value
		
		与HSET命令一样，HSETNX同样会设置哈希表key的field字段值为value。但仅当field不存在才会设置，
		如果field字段已经存在，该操作无效。

		复杂度、返回值：
			时间复杂度：O(1)
			返回值：设置成功，返回1，如果field已存在，则无操作且返回0

	
	HMSET - 设置多个字段及值

		HMSET key field value [field value ...]

		将一个或多个field-value对设置到哈希表key。如果要设置的field已存在，则会覆盖其值。
		如果哈希表不存在，首先会创建再执行HMSET操作。
		
		复杂度、返回值：
		时间复杂度：O(N)，N为field-value对的数量
		返回值：执行成功，返回OK。如果key不是哈希类型，则返回一个错误。
	

	例子：
	127.0.0.1:6379>	HMSET runoobkey name "redis tutorial" likes 20 visitors 23000
	127.0.0.1:6379> HGETALL runoobkey
					1) "name"
					2) "redis tutorial"
					3) "likes"
					4) "20"
					5) "visitors"
					6) "23000"
	127.0.0.1:6379> HGET runoobkey name
					"redis tutorial"
	127.0.0.1:6379>  hset abc f1 v1 
					(integer) 1
	127.0.0.1:6379> hget abc f1
					"v1"
	127.0.0.1:6379> HSETNX abc f1 bd
					(integer) 0
	127.0.0.1:6379> hget abc f1
					"v1"
	127.0.0.1:6379> HMGET runoobkey likes visitors
					1) "20"
					2) "23000"


哈希类型中的获取命令以及使用：
	
	HGET - 获取指定字段值：
		
		HGET key field
	
		返回哈希表key中的field字段的值。
		
		复杂度、返回值：
			时间复杂度：O(1)
			返回值：key存在且field存在则返回其值。否则返回nil。

	HGETALL - 获取所有字段及值
	
		HGETALL key
	
		返回哈希表key中所有的field和其值。
		
		复杂度、返回值：
			时间复杂度：O(N)，N为哈希表的大小
			返回值：以列表形式返回哈希表中的字段和值。若哈希表不存在，否则返回一个空列表。

	HMGET - 返回多个字段值
			
		HMGET key field [field ...]

		返回哈希表key中，一个或多个指定的定段。如果指定的字段在哈希表中不存在，则返回一个nil。
		如果存在，返回field对应的值。

		复杂度、返回值：
			时间复杂度：O(N)，N为指定字段的数量
			返回值：指定字段所关联值的列表。如果指定的key为哈段结构，则返回一个错误
		

	HKEYS -获取所有的属性
		
		HKEYS key

		返回哈希表key中所有的字段。
		
		复杂度、返回值：
			时间复杂度：O(N)，N为哈希表的大小
			返回值：哈希表存在，返回字段列表。哈希表不存在，返回空列表。


	HLEN - 返回字段数量
		
		HLEN key

		返回哈希表key中字段的数量。

		复杂度、返回值：
			时间复杂度：O(1)
			返回值：哈希表存在，返回字段数。哈希表不存在，返回0。


	HVALS - 返回所有字段值

		HVALS key

		返回哈希表key中所有字段的值。
	
		复杂度、返回值：
			时间复杂度：O(N)，N为哈希表的大小
			返回值：哈希表存在，返回字段值的列表。哈希表不存在，返回空列表。

	
	HEXISTS - 判断字段是否存在

		HEXISTS key field

		判断哈希表key中字段field是否存在。

		复杂度、返回值：
			时间复杂度：O(1)
			返回值：哈希表及指定字段存在，返回1。哈希表或指定字段不存在，返回0。

	HDEL - 字段删除
			
		HDEL key field [field ...]
		
		返回哈希表key中一个或多个指定字段，不存在的字段将被忽略。
	
		复杂度、返回值：

			时间复杂度：O(N)，N为要删除的字段数量
			返回值：被成功删除的字段数。


	

哈希类型中的自增命令以及使用：
	如果字段中存储的是数字值，我们可以对其进行加/减法操作。
	
	HINCRBY - 为指定字段值增加
		
		HINCRBY key field increment
		
		为哈希表key中的指定字段field增加一个增量increment。增量也可以为负数，相当于对为指定字段进行减法操作。
		如果哈希表不存在，则会创建一个哈希表，再执行HINCRBY操作。
		如果指定字段field不存在，那么会首先初始化为0，再执行HINCRBY。
		
		如果为非数字值执行HINCRBY操作，则返回一个错误。

		复杂度、返回值：
			时间复杂度：O(1)
			返回值：执行HINCRBY操作后，哈希表key中字段field的值。
		
	
	HINCRBYFLOAT - 为指定字段值增加浮点数
		
		HINCRBYFLOAT key field increment

		为哈希表key中的指定字段field增加一个浮点数增量increment。
		增量也可以为负数，相当于对为指定字段进行减法操作。
		
		如果哈希表不存在，则会创建一个哈希表，再执行HINCRBYFLOAT操作。
		如果指定字段field不存在，那么会首先初始化为0，再执行HINCRBYFLOAT。
		如果为非数字值执行HINCRBYFLOAT操作，则返回一个错误。

		复杂度、返回值：

			时间复杂度：O(1)
			返回值：执行HINCRBYFLOAT操作后，哈希表key中字段field的值。


"------------------------------------------------------------------------------"

Redis value数据类型之列表(List)类型：

1、列表（list）类型：

	Redis的列表（LIST）类型是按照插入顺序排序的字符串链表。该类型和数据结构中的普通链表一样，
	我们可以在其头部(LPUSH)和尾部(RPUSH)添加新的元素。在插入元素时，如果该键不存在，那么将
	创建新列表，如果链表中所有的元素均被移除，那么该键也将会被从数据库中删除。

	一个List中最多可存储2^32-1（40亿）个元素，操作列表元素时，如果是从链表的两头插入或删除元素
	操作效率会非常高。即是列表中已存储了百万条数据，该操作也可以在常量的时间内完成。但是，将
	元素插入列表中间或者删除位于中间的元素，那操作效率非常低。


2、列表类型中的命令及使用:

	在List类型中，有些命令从列表两端进行操作。如：LPUSH、RPUSH等，这些命令操作效率很高。
	而有些需要指定操作位置上，如：LINDEX、LRANGE等，这些命令操作效率较低。


3、创建列表/插入元素:

	LPUSH - 向列表头插入元素
		
		LPUSH key value [value ...]

			将一个或多个值value插入到列表key的头部。
			如果有多个value，那么从左到右依次插入列表。如果列表key不存在，首先会创建一个空列表再执行LPUSH操作。

			复杂度、返回值：
				时间复杂度：O(1)
				返回值：命令执行成功后，列表的长度；如果key存在，但不是List类型，会返回一个错误。


	LPUSHX - 当列表存在则将元素插入表头
		
		LPUSHX key value

			如果列表key存在且是List类型，则将值value插入到列表key的头部。
			如果列表key不存在，则无操作。

			复杂度、返回值：
				时间复杂度：O(1)
				返回值：命令执行成功后，列表的长度；如果key存在，但不是List类型，会返回一个错误


	RPUSH - 将指定元素插入列表末尾
		
		RPUSH key value [value ...]
		
			将指定的一个或多个值，依次插入列表key的末尾。如果列表key不存在，会首先创建一个空列表，再执行RPUSH。

			复杂度、返回值：
				时间复杂度：O(1)
				返回值：执行RPUSH后列表的长度。


	RPUSHX - 当列表存在则将元素插入表尾

		RPUSHX key value

			如果列表key存在且是List类型，则将值value插入到列表key的尾部。
			如果列表key不存在，则无操作。

			复杂度、返回值:
				时间复杂度：O(1)
				返回值：执行RPUSHX后列表的长度。
		

	LINSERT - 将元素插入指定位置
		
		LINSERT key BEFORE|AFTER pivot value

			将元素value插入列表key中pivot元素的之前或之后。
			如果pivot或key不存在则不执行任何操作。如果key不是一个列表类型，则返回一个错误。

			复杂度、返回值：

				时间复杂度：O(N)，N查找pivot所经过元素的数量
				返回值：操作成功，则返回插入操作完成之后，列表的长度；pivot不存在，则返回-1；
						如果key不存在或为空，则返回0。

4、列表取值：

	获取列表中的元素可以使用LPOP和RPOP方法，这两个方法会删除并返回头/尾元素。
	也可以使用LINDEX获取指定位置元素，或使用LRANGE获取指定区间的元素。

	LPOP - 返回列表头元素
		
		LPOP key

			移除返回列表key的头元素。
		
			复杂度、返回值：
				时间复杂度：O(1)
				返回值：列表key中的头元素；如果key不存在，则返回nil
	

	BLPOP - 阻塞并弹出头元素
		
		BLPOP key [key ...] timeout

			BLPOP是LPOP命令的阻塞(blocking)版本，当指定列表中没有任何元素可供弹出的元素时，
			连接将被BLPOP命令阻塞，直到等待超时或有可弹出元素为止。
		
			当指定多个key参数时，会按key的先后顺序依次检查各个列表，并弹出第一个非空列表的头元素。
			timeout参数表示阻塞的时长，如果为0表示可以无限期延长阻塞。

			复杂度、返回值：
				时间复杂度：O(1)
				返回值：如果列表为空，返回一个nil。 否则，返回一个含有两个元素的列表，
						其中：第一个元素是被弹出元素所属的key，第二个元素是被弹出元素的值。

			例子：

				127.0.0.1:6379> BLPOP zzkk timeout 3
							1) "zzkk"
							2) "2"

			
	RPOP - 返回列表尾元素

		RPOP key start stop

			移除并返回列表key的尾元素。
		
			复杂度、返回值：
				时间复杂度：O(1)
				返回值：列表尾元素。当key不存在时，返回nil


	BRPOP - 阻塞并弹出末尾元素

		BRPOP key [key ...] timeout
	
		BRPOP是RPOP命令的阻塞(blocking)版本，当指定列表中没有任何元素可供弹出的元素时，
			连接将被BRPOP命令阻塞，直到等待超时或有可弹出元素为止。
			当指定多个key参数时，会按key的先后顺序依次检查各个列表，并弹出第一个非空列表的末尾元素。
			timeout参数表示阻塞的时长，如果为0表示可以无限期延长阻塞。

		复杂度、返回值：
			时间复杂度：O(1)
			返回值：如果列表为空，返回一个nil。 否则，返回一个含有两个元素的列表，
					其中：第一个元素是被弹出元素所属的key，第二个元素是被弹出元素的值。
		

	LINDEX - 返回指定位置的元素
		
		LINDEX key index

			返回列表key中下标为index的元素。

			index从0开始计数，0表示第一个元素，1表示第二个元素，以次类推。
			也可以使用负数，-1表时倒数第一个元素，-2表时倒数第二个元素，以次类推
			
			复杂度、返回值：
				时间复杂度：O(N)，N为到达下标index所经过元素的数量
				返回值：列表中下标为index的元素；如果key不是列表类型，返回一个错误。
					如果index不在列表有效范围内，返回一个nil。


	LRANGE - 获取指定区间的元素

		LRANGE key start stop

			返回列表key中，以偏移量start和stop指定的区间内的元素。

			LRANGE使用闭区间，即：start和stop索引位的元素都包含在取值范围内(如：LRANGE list 0 10会返回11元素)。
			当start和stop超出有效索引位范围时不会引起错误，如果start大于最大下标值会返回一个空列表；
			如果stop大于最大下标值，会自动设置为最后一位。

			复杂度、返回值：
				时间复杂度：O(S+N)，S为偏移量start，N为指定区间内元素的数量
				返回值：一个包含指定元素的列表


5、列表修改/元素移动:

	Redis 提供了LSET命令，用于修改列表指定位置元素的值。
	除了这个命令外，我们还可以使用RPOPLPUSH将元素从一个列表移动到另一个列表。

	LSET - 设置指定位元素

		LSET key index value
		设置列表key中下标为index的元素值为value。当index超出范围，或对一个空列表进行设置时，会返回一个错误。

		复杂度、返回值：

			时间复杂度：为头/尾元素进行操作时为O(1)；其它情况为O(N)，N列表长度
			返回值：操作成功返回OK，否则返回错误信息。


	RPOPLPUSH - 弹出尾元素，将弹出元素插入另一列表的开头
		
		RPOPLPUSH source destination
	
			RPOPLPUSH命令包含以下两个原子操作：
			将列表source的尾元素弹出，并返回给客户端。
			将source弹出的元素，作为destination列表的头元素插入。
			如果source不存在，返回nil。如果source和destination相同，就会把尾元素移动至开头，这叫做列表的旋转(rotation)操作。

			复杂度、返回值：

			时间复杂度：O(1)
			返回值：被弹出的元素。
			
	
	BRPOPLPUSH - 阻塞并弹出尾元素，将弹出元素插入另一列表的开头
	
		BRPOPLPUSH source destination timeout
		
		BRPOPLPUSH是RPOPLPUSH命令的阻塞版本。当指定的源列表source不为空时，其表现和RPOPLPUSH一样。当source为空时，
			连接将被BRPOP命令阻塞，直到等待超时或有可弹出元素为止。
			timeout参数表示阻塞的时长，如果为0表示可以无限期延长阻塞。

			复杂度、返回值：
				时间复杂度：O(1)
				返回值：如果指定时间内没有任何元素弹出，返回一个nil。 
				否则，返回一个含有两个元素的列表，其中：第一个元素是被弹出元素所属的key，第二个元素是被弹出元素的值。

6、元素删除/列表裁剪

	通过LREM命令可以移除列表中不再需要的元素。而LTRIM可以从指定区间范围裁剪列表。
	
	LREM - 移除元素
		
		LREM key count value
		
			移除指定数量为count的value值。count可能有以下几种情况：
			count >0 : 从表头开始向表尾搜索，移除值为value，数量为 count的元素。
			count < 0 : 从表尾开始向表头搜索，移除值为value，数量为 count绝对值的元素。
			count = 0 : 移除表中所值为value的元素。
			
			复杂度、返回值：
				时间复杂度：O(N)，N列表长度
				返回值：被移除元素的数量。key不存在时，返回0。
	

	LTRIM - 列表裁剪
	
		LTRIM key start stop
			保留列表key中，偏移量start和stop指定的区间内的元素，裁剪其余元素。
			
			LTRIM使用闭区间，即：start和stop索引位的元素都包含在取值范围内(如：LTRIM list 0 10结果是一个包含11元素的列表)。

			复杂度、返回值：
				时间复杂度：O(N)，N移除元素的数量
				返回值：操作成功返回OK，否则返回错误信息。
				
				
"------------------------------------------------------------------------------------------------"






















