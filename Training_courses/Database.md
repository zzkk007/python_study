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

	

	






