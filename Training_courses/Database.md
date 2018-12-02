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
	
"---------------------------------------------------------------------------------------------------------------"

索引：

	使用索引很简单，只要能写创建表的语句，就肯定能写创建索引的语句，要知道这个世界上是不存在不会创建表的服务器端程序员的。
	然而， 会使用索引是一回事， 而深入理解索引原理又能恰到好处使用索引又是另一回事，
	这完全是两个天差地别的境界（我自己也还没有达到这层境界）。很大一部份程序员对索引的了解仅限于到“加索引能使查询变快”这个概念为止。

	为什么要给表加上主键？

	为什么加索引后会使查询变快？

	为什么加索引后会使写入、修改、删除变慢？

	什么情况下要同时在两个字段上建索引？

	这些问题他们可能不一定能说出答案。知道这些问题的答案有什么好处呢？如果开发的应用使用的数据库表中只有1万条数据，
	那么了解与不了解真的没有差别， 然而， 如果开发的应用有几百上千万甚至亿级别的数据，那么不深入了解索引的原理，
	写出来程序就根本跑不动，就好比如果给货车装个轿车的引擎，这货车还能拉的动货吗？

	接下来就讲解一下上面提出的几个问题，希望对阅读者有帮助。

	网上很多讲解索引的文章对索引的描述是这样的「索引就像书的目录， 通过书的目录就准确的定位到了书籍具体的内容」，
	这句话描述的非常正确， 但就像脱了裤子放屁，说了跟没说一样，通过目录查找书的内容自然是要比一页一页的翻书找来的快，
	同样使用的索引的人难到会不知道，通过索引定位到数据比直接一条一条的查询来的快，不然他们为什么要建索引。

	想要理解索引原理必须清楚一种数据结构「平衡树」(非二叉)，也就是b tree或者 b+ tree，
	重要的事情说三遍：“平衡树，平衡树，平衡树”。
	当然， 有的数据库也使用哈希桶作用索引的数据结构 ， 然而， 主流的RDBMS都是把平衡树当做数据表默认的索引数据结构的。
	
1、聚集索引 ：

	我们平时建表的时候都会为表加上主键， 在某些关系数据库中， 如果建表时不指定主键，数据库会拒绝建表的语句执行。
	事实上， 一个加了主键的表，并不能被称之为「表」。一个没加主键的表，它的数据无序的放置在磁盘存储器上，
	一行一行的排列的很整齐， 跟我认知中的「表」很接近。
	如果给表上了主键，那么表在磁盘上的存储结构就由整齐排列的结构转变成了树状结构，也就是上面说的「平衡树」结构，
	换句话说，就是整个表就变成了一个索引。
	
	没错， 再说一遍， 整个表变成了一个索引，也就是所谓的「聚集索引」。
	这就是为什么一个表只能有一个主键， 一个表只能有一个「聚集索引」，因为主键的作用就是把「表」的数据格式转换成「索引（平衡树）」的格式放置。
	
	其中树的所有结点（底部除外）的数据都是由主键字段中的数据构成，也就是通常我们指定主键的id字段。最下面部分是真正表中的数据。
	
	 假如我们执行一个SQL语句：
		select * from table where id = 1256;
	首先根据索引定位到1256这个值所在的叶结点，然后再通过叶结点取到id等于1256的数据行。
	这里不讲解平衡树的运行细节， 但是从上图能看出，树一共有三层， 从根节点至叶节点只需要经过三次查找就能得到结果。

	假如一张表有一亿条数据 ，需要查找其中某一条数据，按照常规逻辑， 一条一条的去匹配的话， 最坏的情况下需要匹配一亿次才能得到结果，
	用大O标记法就是O(n)最坏时间复杂度，这是无法接受的，而且这一亿条数据显然不能一次性读入内存供程序使用，
	因此， 这一亿次匹配在不经缓存优化的情况下就是一亿次IO开销，以现在磁盘的IO能力和CPU的运算能力， 有可能需要几个月才能得出结果 。
	如果把这张表转换成平衡树结构（一棵非常茂盛和节点非常多的树），假设这棵树有10层，那么只需要10次IO开销就能查找到所需要的数据，
	速度以指数级别提升，用大O标记法就是O(log n)，n是记录总树，底数是树的分叉数，结果就是树的层次数。
	换言之，查找次数是以树的分叉数为底，记录总数的对数。
	用程序来表示就是Math.Log(100000000,10)，100000000是记录数，10是树的分叉数（真实环境下分叉数远不止10）， 
	结果就是查找次数，这里的结果从亿降到了个位数。因此，利用索引会使数据库查询有惊人的性能提升。
	
	然而， 事物都是有两面的， 索引能让数据库查询数据的速度上升， 而使写入数据的速度下降，原因很简单的，
	因为平衡树这个结构必须一直维持在一个正确的状态， 增删改数据都会改变平衡树各节点中的索引数据内容，破坏树结构，
	因此，在每次数据改变时， DBMS必须去重新梳理树（索引）的结构以确保它的正确，这会带来不小的性能开销，
	也就是为什么索引会给查询以外的操作带来副作用的原因。

2、非聚集索引， 也就是我们平时经常提起和使用的常规索引：

	非聚集索引和聚集索引一样， 同样是采用平衡树作为索引的数据结构。索引树结构中各节点的值来自于表中的索引字段，
	假如给user表的name字段加上索引 ， 那么索引就是由name字段中的值构成，在数据改变时， DBMS需要一直维护索引结构的正确性。
	如果给表中多个字段加上索引 ， 那么就会出现多个独立的索引结构，每个索引（非聚集索引）互相之间不存在关联。 
	如下图
			
	每次给字段建一个新索引， 字段中的数据就会被复制一份出来， 用于生成索引。 因此， 给表添加索引，会增加表的体积， 占用磁盘存储空间。
	
	非聚集索引和聚集索引的区别在于， 通过聚集索引可以查到需要查找的数据， 而通过非聚集索引可以查到记录对应的主键值 ，
	再使用主键的值通过聚集索引查找到需要的数据。
	
	不管以任何方式查询表， 最终都会利用主键通过聚集索引来定位到数据， 聚集索引（主键）是通往真实数据所在的唯一路径。


3、覆盖索引：
	
	有一种例外可以不使用聚集索引就能查询出所需要的数据， 这种非主流的方法 称之为「覆盖索引」查询， 
	也就是平时所说的复合索引或者多字段索引查询。 文章上面的内容已经指出， 当为字段建立索引以后，
	字段中的内容会被同步到索引之中， 如果为一个索引指定两个字段， 那么这个两个字段的内容都会被同步至索引之中。

	先看下面这个SQL语句

	//建立索引

	create index index_birthday on user_info(birthday);

	//查询生日在1991年11月1日出生用户的用户名

	select user_name from user_info where birthday = '1991-11-1'

	这句SQL语句的执行过程如下

	首先，通过非聚集索引index_birthday查找birthday等于1991-11-1的所有记录的主键ID值

	然后，通过得到的主键ID值执行聚集索引查找，找到主键ID值对就的真实数据（数据行）存储的位置

	最后， 从得到的真实数据中取得user_name字段的值返回， 也就是取得最终的结果

	我们把birthday字段上的索引改成双字段的覆盖索引

	create index index_birthday_and_user_name on user_info(birthday, user_name);

	这句SQL语句的执行过程就会变为

	通过非聚集索引index_birthday_and_user_name查找birthday等于1991-11-1的叶节点的内容，
	然而， 叶节点中除了有user_name表主键ID的值以外， user_name字段的值也在里面， 
	因此不需要通过主键ID值的查找数据行的真实所在， 直接取得叶节点中user_name的值返回即可。 
	通过这种覆盖索引直接查找的方式， 可以省略不使用覆盖索引查找的后面两个步骤， 大大的提高了查询性能，

	数据库索引的大致工作原理就是像文中所述， 然而细节方面可能会略有偏差，这但并不会对概念阐述的结果产生影响 。
	
	https://www.cnblogs.com/aspwebchh/p/6652855.html
	
4、什么情况下适合创建索引

	a、经常查询的字段，即在WHERE字句中出现的字段
	
	b、在分组的字段，即在GROUP BY 字句中的字段
	
	c、存在依赖关系的子表和父表之间的联合查询，即主键和外键字段。
	
	d、设置唯一完整性约束的字段。

	什么情况下不适合创建索引：
	
	在查询中很少被使用的字段，拥有许多重复的字段。
	
	CREATE INDEX 索引名
		ON 表名 （属性名【长度】【ASC|DESC】）


"----------------------------------------------------------------------------------------------------------"
视图：

	视图的特点：

	视图的列可以来自不同的表，是表的抽象和在逻辑意义上建立的新关系。
	视图是由基本表（实表）产生的表（虚表）
	视图的建立和删除不影响基本表
	对视图内容的更新（添加、删除、修改）直接影响基本表。
	当视图来自多个基本表时，不允许添加和删除数据。

	创建视图：
	
		create view view_name  AS 查询语句
		
		视图的功能实际上就是封装了复杂的查询语句。
		
	查看视图：
	
		show tables  不仅会显示表的名字，还会显示视图的名字。
		
	删除视图：
		DROP view view_name
		
	修改视图：
	
		ALTER　view viewname as 查询语句
		
"----------------------------------------------------"

触发器：
	
		触发器（TRIGGER）是MySQL的数据对象之一，该对象和
		编程语言中的函数非常类似，都需要声明、执行等。
		
		但是触发器的执行不是由程序调用，也不是手工启动，而是
		有事件来触发、激活从而实现执行。
		
	1、创建触发器：
	
		在MySQL中创建触发器通过SQL语句，CREATE TRIGGER来实现，
		其语法：
			
				CREATE TRIGGER trigger_name
				trigger_time
				trigger_event 
				ON table_name
				FOR EACH ROW
				trigger_stmt 
				
				trigger_name：标识触发器名称，用户自行指定；
				trigger_time：标识触发时机，取值为 BEFORE 或 AFTER；
				trigger_event：标识触发事件，取值为 INSERT、UPDATE 或 DELETE；
				tbl_name：标识建立触发器的表名，即在哪张表上建立触发器；
				trigger_stmt：触发器程序体，可以是一句SQL语句，或者用 BEGIN 和 END 包含的多条语句。
		
		由此可见，可以建立6种触发器，即：BEFORE INSERT、BEFORE UPDATE、BEFORE DELETE、AFTER INSERT、AFTER UPDATE、AFTER DELETE。
		另外有一个限制是不能同时在一个表上建立2个相同类型的触发器，
		因此在一个表上最多建立6个触发器。		
					
		例子：
		
			CREATE TRIGGER tri_diarytime
			BEFORE INSERT
			ON t_dept FOR EACH ROW
				INSERT INTO t_diary VALUES(NULL,'t_dept',now())
			创建一个触发器tri_diarytime,当向部分表中插入任意
			一条记录时，就会在插入操作之前向表t_diary中插入当前时间。
		
		创建包含多执行语句的触发器：
		
			create trigger trigger_name
				BEFORE|AFTER trigger_EVENT
					ON TABLE_NAME FOR EACH ROW
						BEGIN
						trigger_stmt
						END
			在BEGIN END 两个关键字之间是要执行的多个执行语句的内容，
			执行语句用分号隔开。
			在MySQL软件中，一般情况下";"符号作为语句的结束符号，可是
			在创建触发器的时候，需要用到";"符号作为执行的结束符号。
			为了解决这个问题，可以使用关键字DELMITER语句，例如：
			"DELIMITER$$",可以实现将结束语句设置成"$$"	
			
			DELIMITER $$
			CREATE TRIGGER tri_diarytime2
				AFTER INSERT
					ON t_dept FOR　EACH ROW
						BEGIN
							INSERT INTO t_diary VALUES(NULL,'t_dept',new());
							INSERT INTO t_diary VALUES(NULL,'t_dept',new());
						END
						$$
				DELIMITER;
				
		查看触发器：
			SHOW TRIGGERS ;
			
		删除触发器：
			DROP TRIGGER grigger_name
			

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



Python 与 ORM 框架

ORM框架：

	ORM全程：Object Relational Mapping翻译过来就是对象关系映射，简单来说，ORM将数据库
	中的表与面向对象语言中的类建立了一种对应关系。这样我们要操作数据库，数据库中的表
	或者表中的一条记录，就可以直接通过操作类或者类实例来完成。

ORM与SQLAlcheny简介：

	SQLAlchemy是python社区最知名的ORM工具之一，为高效和高性能的数据库访问设计，实现了
	完整的企业级持久模型。

	1、先装SQLAlchemy:

		pip install sqlalchemy

	2、链接数据库：

		from sqlalchemy import create_engine

		engine = create_engine('mysql+mysqldb://root@localhost:3306/blog')

		print(engine)

		在上面的程序中我们默认运行在3306端口的MySQL中的blog数据库。

		如果打印出Engine(mysql+mysqldb://root@localhost:3306/blog)说明我们已经链接成功了。


	3、描述表结构：
	
		要使用ORM，我们需要将数据表的结构用ORM的语言描述出来。SQLAlchemy提供了一套Declarative
		系统来完成这个任务，我们以创建一个user表为例，看看它是怎么用SQLAchemy的语言来描述的：

		from sqlalchemy import create_engine
		from sqlalchemy.ext.declarative import declarative_base
		from sqlalchemy import Column,String,Integer

		engine = create_engine('mysql+mysqldb://root@localhost:3306/blog?charset=utf8')

		Base = declarative()

		class User(Base):

			__tablename__ = 'users'

			id = Column(Integer,primary_key=True)
			
			username = Column(String(64),nullable=False,index=True)
			
			password = Column(String(64),nullable=False)

			email = Column(String(64),nullable=False,index=True)

			def __repr__(self):
				return '%s(%r)'%(self.__class__.__name__,self.username)

		在User类中，用__tablename__指定在MySQL中表的名字，我们创建了三个基本字段，
		类中的每一个Column代表数据中的一列，在Column中，指定该列的一些配置，第一个字段
		代表类的数据类型。上面我们使用了String、Integer，其他常用的还包括：Text、Boolean
		SmallInteger、DateTime。

		nullable = False代表此列不可以为空，index=True表示在该列创建索引，
		另外定义__repr__是为了方便调试，你可以不定义，也可以定义更详细。

	4、关系定义：

		一对多关系：
		
		对于一个对于一个普通的博客应用来说，用户和文章显然是一个一对多的关系，
		一篇文章属于一个用户，一个用户可以写很多篇文章，那么他们之间的关系可以这样定义：

		class User(Base):
		
			__tablename__ = 'users'
			
			
			id = Column(Integer,primary_key=True)
			username = Column(String(64), nullable=False, index=True)
			password = Column(String(64), nullable=False)
			email = Column(String(64), nullable=False, index=True)
			articles = relationship('Article')

		class Article(Base):

			__tablename__ = 'articles'

			id = Column(Integer, primary_key=True)
			title = Column(String(255), nullable=False, index=True)
			content = Column(Text)
			user_id = Column(Integer, ForeignKey('users.id'))
			author = relationship('User')
			
			def __repr__(self):
				return '%s(%r)' % (self.__class__.__name__, self.title)

		表articles中有一个外键指向users表中的主键id,而在User中使用SQLAlchemy提供了relationship
		描述关系，而用户与文章的关系是双向的，所有两张表中都定义了relationship。

		SQLAlchemy 提供了 backref 让我们可以只需要定义一个关系：
	
			articles = relationship('Article',backref='author')
		添加了这个可以不用在Article中定义relationship了。

		
		一对一关系：
		
		在User中我们只定义了几个必须的字段，但通常用户还需要其他信息，但这些信息可能不是必须
		填写的，我们可以放到另外一张UserInfo表中，这样User和表Userinfo就形成了一对一的关系。

		class User(Base):
			
			__tablename__ = 'users'

			id = Column(Integer, primary_key=True)
			username = Column(String(64), nullable=False, index=True)
			password = Column(String(64), nullable=False)
			email = Column(String(64), nullable=False, index=True)
			articles = relationship('Article', backref='author')
			userinfo = relationship('UserInfo', backref='user', uselist=False)
			
			def __repr__(self):
				return '%s(%r)' % (self.__class__.__name__, self.username)

		class UserInfo(Base):

			__tablename__ = 'userinfos'

			id = Column(Integer, primary_key=True)
			name = Column(String(64))
			qq = Column(String(11))
			phone = Column(String(11))
			link = Column(String(64))
			user_id = Column(Integer, ForeignKey('users.id'))

		定义方法和一对多相同，只是需要添加 userlist=False 。

		
		映射到数据:

			表已经描述好了，在文件末尾使用下面的命令在我们连接的数据库中创建对应的表：
			if __name__ == '__main__':
			    Base.metadata.create_all(engine)
	

	5、CURD
		
		当你想打电话给朋友时，你是否得用手机拨通他的号码才能建立一个会话？同样的，你想和MySQL
		交谈也得先通过SQLAlchemy建立一个会话：

		from sqlalchemy.orm import sessionmaker

		Session = sessionmaker(bin=engine)
		session = Session()

		你可以把sessionmaker想象成一个手机，engine当做MySQL的号码，拨通这个"号码"创建了一个Session类，
		下面我梦通过这个类的实例与Mysql交谈了。

		在python的世界中，Faker是用来生产虚假数据的库，安装它

		pill install faker

		结合Faker库创建一些测试数据：

		faker = Factory.create()
		
		Session = sessionmaker(bind = engine)

		session = Session()

		faker_users = [User(
			username=faker.name(),
			password=faker.word(),
			email=faker.email(),)for i in range(10)]
	
		ADD到数据库：

			session.add_all(faker_users)
			session.commit()

			使用 SQLAlchemy 往数据库中添加数据，我们只需要创建相关类的实例，
			调用 session.add() 添加一个，或者 session.add_all() 一次添加多个， 
			最后 session.commit() 就可以了。



		QUERY数据库：
			
			如果我们知道用户 id，就可以用 get 方法,filter_by 用于按某一个字段过滤，
			而 filter 可以让我们按多个字段过滤，all 则是获取所有。获取某一字段值可以直接类的属性获取：

			a = session.query(user).get(10)
			b = session.query(User).all()

		Update数据库：

			a = session.query(User).get(10)
			a.user = 'My test blog post'
			session.add(a)
			session.commit()

		Delete数据库：

			a = session.query(User).get(10)
			session.delete(a)
			session.commit（）

		删除直接调用 delete 删除获取到的对象，提交 session 即可。


	完整代码:

		# coding: utf-8

		import random
		from faker import Factory

		from sqlalchemy import create_engine, Table
		from sqlalchemy.ext.declarative import declarative_base
		from sqlalchemy import ForeignKey
		from sqlalchemy import Column, String, Integer, Text
		from sqlalchemy.orm import sessionmaker, relationship


		engine = create_engine('mysql+mysqldb://root@localhost:3306/blog?charset=utf8')
		Base = declarative_base()
	
	
		class User(Base):
		
		    __tablename__ = 'users'
			
			id = Column(Integer, primary_key=True)
			username = Column(String(64), nullable=False, index=True)
			password = Column(String(64), nullable=False)
			email = Column(String(64), nullable=False, index=True)
			articles = relationship('Article', backref='author')
		    userinfo = relationship('UserInfo', backref='user', uselist=False)
			
			def __repr__(self):
				return '%s(%r)' % (self.__class__.__name__, self.username)
							
							
		class UserInfo(Base):
								
			 __tablename__ = 'userinfos'
									
			id = Column(Integer, primary_key=True)
			name = Column(String(64))
			qq = Column(String(11))
			phone = Column(String(11))
			link = Column(String(64))
			user_id = Column(Integer, ForeignKey('users.id'))
	
	
		class Article(Base):
		
		    __tablename__ = 'articles'
			
			id = Column(Integer, primary_key=True)
			title = Column(String(255), nullable=False, index=True)
			content = Column(Text)
			user_id = Column(Integer, ForeignKey('users.id'))
			cate_id = Column(Integer, ForeignKey('categories.id'))
		    tags = relationship('Tag', secondary='article_tag', backref='articles')
			
			def __repr__(self):
				return '%s(%r)' % (self.__class__.__name__, self.title)
							
							
		class Category(Base):
								
			__tablename__ = 'categories'
									
			id = Column(Integer, primary_key=True)
			name = Column(String(64), nullable=False, index=True)
			articles = relationship('Article', backref='category')
	
			def __repr__(self):
				return '%s(%r)' % (self.__class__.__name__, self.name)
					
					
		article_tag = Table(
			'article_tag', Base.metadata,
			Column('article_id', Integer, ForeignKey('articles.id')),
			Column('tag_id', Integer, ForeignKey('tags.id'))
			)
					
					
		class Tag(Base):
						
			__tablename__ = 'tags'
							
			id = Column(Integer, primary_key=True)
			name = Column(String(64), nullable=False, index=True)
	
			def __repr__(self):
				return '%s(%r)' % (self.__class__.__name__, self.name)
					
					
		if __name__ == '__main__':
			Base.metadata.create_all(engine)
	
			faker = Factory.create()
			Session = sessionmaker(bind=engine)
			session = Session()
	
			faker_users = [User(
				username=faker.name(),
				password=faker.word(),
				email=faker.email(),
				) for i in range(10)]
		    session.add_all(faker_users)
	
			faker_categories = [Category(name=faker.word()) for i in range(5)]
			session.add_all(faker_categories)

			faker_tags= [Tag(name=faker.word()) for i in range(20)]
		    session.add_all(faker_tags)
	
			for i in range(100):
		        article = Article(
				title=faker.sentence(),
				content=' '.join(faker.sentences(nb=random.randint(10, 20))),
				author=random.choice(faker_users),
				category=random.choice(faker_categories))
			
			for tag in random.sample(faker_tags, random.randint(2, 5)):
				article.tags.append(tag)
			session.add(article)
																		 
		session.commit()


SQLObject 连接数据库:
	
	1、安装：

		pip install -U SQLObject
		or
		easy_install -U SQLObject

	2、

		


"======================================================================"

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
	
	
	键的命令:
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

Redis 数据类型之集合(Set)类型:

	无序集合、元素为string类型、元素具有唯一性，不重复。

	Redis中的集合（Set）类型类似于List类型,Set类型可以认为是没有排序的字符串集合，和List类型一样
	我们可以对集合类型进行元素的添加、删除或判断元素是否存在等操作。

	set类型操作的时间复杂度为O(1),其中最大元素数量为2^23-1,与List类型不同的是，Set集合不允许出现重复
	的元素，如果多次添加相同元素，Set中将仅保留改元素中的一个。

	和List类型相比，Set类型有一个重要的特性，可以完成多个集合的聚合技术操作。
	如：SUNION、SUNIONSTORE、SDIFFSTORE.


集合类型中的命令及使用：

1、元素添加、成员判断

	SADD - 添加元素

		SADD key member member

		将一个或多个元素member添加到集合key中，如果要添加的元素在集合中已经存储，则忽略。
		如果集合key不存在，那么包含元素member的集合会被创建。

		返回值：
			被添加到集合中的信元素的数量，不包括被忽略的元素，如果key不是集合类型，将返回一个错误。
	
	SCARD - 集合元素数

		SCARD key

		返回集合key中的元素的数量

		返回值：
			集合中的元素数；集合不存在，返回0


	SMEMBERS - 返回集合中成员

		SMEMBERS key

		返回集合key中所有的成员，如果key不存在，会被当做空集合

	SISMEMBER - 判断元素是否是集合成员

		SISMEMBER key number

		判断元素member是否是集合key的成员
		
		返回值：
		
			如果memmber是集合成员，返回1，如果不是集合成员或集合不存在，返回0


2、获取集合元素、元素删除：
	
	集合类型中并不能明确返回指定的成员，但可以通过SPOP 或SRANDMEMBER随机
	返回一个或多个元素成员。SREM命令可以移除集合中指定的元素，SMOVE可以将
	元素从一个集合迁移至另一个集合。

	SPOP - 随机返回并移除一个元素

		SPOP key

			随机移除并返集合key中的一个元素

			返回值：
				被移除的元素，如果key不存在或集合为空，返回nil

	
	SRANDMEMBER - 随机返回一个或多个元素(没有删除)

		SRANDMEMBER key [count]

			如果参数count 未提供，则随机返回集合key中的一个元素，count元素提供时，按下面规则返回：

			count 小于集合元素总是，则随机返回数量为count的元素，如大于则返回全部元素
			如果count为负数，则返回一个数量为其绝对值的元素

			返回一个元素或数量为count的集合，集合为空则返回nil


	SREM - 移除指定的元素

		SREM key member [member ...]

			移除集合key中指定的一个或多个元素member，如果member不存在会被忽略

			返回值：被移除的元素数量；key不是集合类型，返回一个错误

	SMOVE - 将元素从集合移至另一个集合

		SMOVE source destination member

			将元素member从source移至集合destination

			返回值：成功返回1，否则返回0


3、集合间的操作：

	集合类型中还提供了集合键的操作的命令，这些操作有：差集、交集、并集命令有返回知道的集合元素或
	将操作结果存储至一个新的集合。

	SDIFF - 返回一或过个集合的差集

		SDIFF key [key ...]

			返回差集成员列表

	SDIFFSTORE - 将一或多个集合的差集保存至另一集合

		SDIFFSTORE destination key [key ...]
			
			该命令不是直接返回，而是将差集存储到另一个集合destination中，如果destination已存在，则
			将其覆盖。

			返回值：结果差集成员数量


	SINTER - 将一或多个集合的交集保存至另一集合

		SINTER key [key ...]

			返回一个或多个指定集合的交集，如果key不存在，会视为空集合，返回结果集也为空。

			返回值：交集成员列表
			
		
	SINTERSTORE - 将一或多个集合的交集存储到新集合

		SINTERSTORE destination key [key ...]

			该命令类似于SINTER，但它不会返回成员列表，而是将结果集存储至一个新的集合destination中。

			返回值：结果集中的成员数量。

	
	SUNION - 返回集合的并集

		SUNION key [key ...]

		返回一个或多个集合的并集；如果key不存在，会被视为空集合。

		返回值：并集成员列表。

	SUNIONSTORE - 将集合的并集插入新集合

		SUNIONSTORE destination key [key ...]

			此命令类似于SUNION，但它不会直接返回集合的交集，而是将结果插入一个新的集合destination
			如果destination已存在，则将其覆盖。

			返回值：并集元素数量。


"---------------------------------------------------------------------------"
	
Redis 数据类型之有序集合(Sorted Set):

	sorted set 有序集合、元素为string类型，元素具有唯一性，不重复。
	每个元素都会关联一个duble类型的score，表示权重，通过权重将元素从小到大排序
	score 是Redis对集合元素排序的一个权重依据，虽然集合元素不可重复，但score是可重复的。

	Redis 的有序集合类型操作效率非常高，是其它同类数据库所难以实现。
	在有序集合中添加、删除或更新一个元素的操作速度都非常快，其时间复杂度为集合中成员数量的对数。
	由于有序集合中的成员在集合中的位置是有序的，所以即使是操作集合中部的成员也会非常高效。


1、有序集合添加、修改元素：

	有序集合使用ZADD 命令向已经有的有序集合添加新元素、或创建新的有序集合。score是有序集合排序是的
	权重依据，对于已经存在的元素，可以使用ZINCRBY命令修改元素的权重值。

	ZADD key score member [[score member] [score member] ...]

		将一个或多个元素及其score 值添加到有序集合key中，如果某个元素member已经存在，更新score值
		并将其重新插入合适的位置

		score 可以是整数或双精度浮点数。

		key不存在，则创建一个新的有序集合并插入指定元素，key存在但不是有序集合返回错误。

		返回值：被成功添加的新元素的数量。


	ZINCRBY - 增加元素权重

		ZINCRBY key increment member

			为有序集合key的元素memebr的score增加值increment,如果increment为负数，用于减小元素的score值。

			返回值：member新的score值；当key不是有序集合返回一个错误

	
2、有序集合查询

	查询有序集合时，可以查询其某一个或多个元素的。
	查询一个元素，可以通过ZRANK命令查询元素的排名，或使ZSCORE命令查询元素的权重。
	而查询多个元素，可以按正序/倒叙、下标区间/权重区间查询元素。

	ZCARD - 返回集合基数

		ZCARD key 
		
			返回值：有序集合key的基数，当集合不存在时，返回0


	ZRANK - 返回指定元素的排名
		
		ZRANK key member

			返回有序集合key的元素member排名，元素成员按score值递增，
			相同score值的成员按字典排序。元素排名从0开始计数。

			返回值：元素member的排名；如果key不是有序集合，返回nil

	ZSCORE - 返回指定元素的权重

		ZSCORE key meber

			返回有序集合key中，member的score值

			返回值：指定元素的score值，如果元素不存在或key不存在，返回nil

	ZCOUNT - 返回集合两个权重间的元素数

		ZCOUNT key min max 

			返回有序集合key，socre值在min和max之间的元素数

			返回值：有序集合key的基数，当集合不存在时，返回0

	
	ZRANGE - 返回指定区间内的元素

		ZRANGE key start stop 
		
			返回有序集合key指定区间内的元素。元素成员按score值递增，相同score值的成员按字典排序。
			start和stop都是从0开始。当使用负数时，表示从集合的末尾开始计数。

			返回值：指定区间内的成员列表

	
3、有序集合删除：

	ZREM - 移除元素

	ZREM key member [member ...]
		
		移除有序集合key中一个或多个元素member的排名，不存在的成员忽略

		返回值：被成功移除的元素数量，如果key不是有序集合，返回错误

	

"--------------------------------------------------------------------------------------"

reids 高级

主要讨论发布订阅模块、主从配置两个知识点。


1、redis 发布订阅：

	Redis 通过PUBLISH 、SUBSCRIBE等命令实现了订阅与发布模式，这个功能提供了两种信息机制，
	分别是订阅/发布到频道和订阅/发布到模式

	发布者不是计划发送信息给特定的接受者（订阅者），而是发布的信息分到不同的频道，
	不需要知道什么样的订阅者订阅
	订阅者对一个或多个频道感兴趣，只需接收感兴趣的消息，不需要知道什么样的发布者的
	发布者和订阅者的解耦合可以带来更大的扩展性和更加动态的网络拓扑
	客户端发到频道的消息，将会被推送到所有订阅次频道的客户端
	客户端不需要主动去获取消息，只需要订阅频道，这个频道的内容就会被推送过来。
	
2、消息的格式：

	推送消息的格式包含三部分

	part1:消息类型、包含三种类型

		subscribe,表示订阅成功
		unsubscribe,表示取消订阅成功
		message，表示其它终端发布消息

	如果第一部分的值为subscribe，则第二部分是频道，第三部分是现在订阅频道的数量

	如果第一部分的是为unsubscribe,则第二部分是频道，第三部分是现在订阅频道的数量
		如果为0则表示当前没有订阅任何频道，当在Pub/Sub以外状态，客户端可以发出任何redis命令。

	如果第一部分的值为message，则第二部分是来源频道的名称，第三部分是消息内容。



3、命令：

	订阅：

		SUBSCRIBE 频道名称 [频道名称 ...]
	
	取消订阅，如果不写参数，表示取消所有订阅

		UNSUBSCRIBE 频道名称 [频道名称]

	发布：

		PUBLISH 频道 消息


4、例子：

	订阅频道名为 redisChat:

	127.0.0.1:6379> SUBSCRIBE redisChat
	Reading messages... (press Ctrl-C to quit)
	1) "subscribe"
	2) "redisChat"
	3) (integer) 1
	1) "message"
	2) "redisChat"
	3) "Learn reids by ruboo.com"
	1) "message"
	2) "redisChat"
	3) "Learn reids"
	
	我们先重新开启个 redis 客户端，然后在同一个频道 redisChat 发布两次消息，
	订阅者就能接收到消息

	127.0.0.1:6379> PUBLISH redisChat "Learn reids by ruboo.com"
	(integer) 1
	127.0.0.1:6379>  PUBLISH redisChat "Learn reids"
	(integer) 1



"-------------------------------------------------------------------------"

redis基本配置：

	在源文件下/home/zhangkun/software/redis-3.2.9/redis.conf中
	
	绑定地址：如果需要远程访问，可将此行注释:
		bind 127.0.0.1

	端口，默认为6379:
		port 6379

	是否以守护进程运行:
		如果以守护进程运行，则不会在命令行阻塞，类似于服务
		如果以非守护进程运行，则当前终端被阻塞，无法使用
		推荐改为yes，以守护进程运行

		daemonize no|yes

	数据文件:

		dbfilename dump.rdb

	数据文件存储路径:
		
		dir的默认值为./，表示当前目录
		推荐改为：dir /var/lib/redis

使用配置文件方式启动:

	一般配置文件都放在/etc/目录下
		cp /home/zhangkun/software/redis-3.2.9/redis.conf /etc/redis/

	推荐指定配置文件启动:
		redis-server /etc/redis/redis.conf

	停止redis服务:
		ps ajx|grep redis
		sudo kill -9 redis的进程id


redis 主从配置：

	一个master可以拥有多个slave,一个slave又可以拥有多个slave,如此下去，形成了一个多级服务器集群架构。

	比如：将ip为192.168.1.10的机器作为主服务器，将ip为192.168.1.11的机器作为从服务器


	设置主服务器的配置：
		bind 192.168.1.10

	设置从服务器的配置：
	注意：在slaveof 后写主机ip，再写端口，而且端口必须写：

		bind 192.168.1.11
		slaveof 192.168.1.10 6379

	在master和slave分别执行info命令，查看输出信息
	在master上写数据
		set hello world

	在slave上读数据
		get hello


Redis 数据备份与恢复:

	Redis SAVE 命令用于创建当前数据库的备份。

		redis 127.0.0.1:6379> SAVE 
		OK
	该命令将在 redis 安装目录中创建dump.rdb文件。/usr/local/redis/bin中

	
	恢复数据：

		如果需要恢复数据，只需将备份文件 (dump.rdb) 移动到 redis 安装目录并启动服务即可。
		获取 redis 目录可以使用 CONFIG 命令

		redis 127.0.0.1:6379> CONFIG GET dir
		1) "dir"
		2) "/usr/local/redis/bin"


"------------------------------------------------------------------------------------------"

Python Reids:

1、redis连接

	redis 提供了两个类Redis 和 StrictRedis 用于实现Redis的命令。
	StrictRedis用于实现大部分的官方的命令，并使用官方的语法和命令
	Redis是StrictRedis的子类，用于向后兼容旧版本的redis-py

	redis 连接实例是线程安全的，可以直接将redis连接实例设置为一个全局变量，直接使用。
	如果需要另一个Redis实例（or Redis数据库）时，就需要重新创建redis连接实例来获取一个新的连接。
	同理，python的redis没有实现select命令。


2、安装：

	联网安装
		sudo pip install redis

	使用源码安装
		unzip redis-py-master.zip
		cd redis-py-master
		sudo python setup.py install


3、交互代码

	引入模块：

		import redis
	
	连接：

		try:
			r = redis.StrictRedis(host='localhost',6379)
		except Exception as e:
			print(e.message)

	方式1：根据数据类型的不同，调用相应的方法，完成读写

		r.set('name','hello')
		r.get('name')

	连接池：

		reids 使用Connection pool 来管理对一个redis server的所有连接，避免每次连接，释放连接的开销
		默认，每个Redis实例都会维护一个自己的连接池，可以直接建立一个链接池，然后作为参数Redis，
		这样就可以实现多个Redis实例共享一个连接池。

		import redis
		pool = redis.ConnectionPool(host='0.0.0.0', port=6379)
		r = redis.Redis(connection_pool=pool)
		r.set('age', '16')
		print(r.get('age'))

		# 使用 StrictRedis 连接池
		import redis
		pool = redis.ConnectionPool(host='47.92.114.20', port=6379)
		r = redis.StrictRedis(connection_pool=pool)
		r.set('age', '16')
		print(r.get('age'))
		# 结果
		b'16'


封装：

	连接redis服务器部分是一致的
	这里讲string类型的读写进行封装

	import redis
	
	

"--------------------------------------------------------------------------"

Mongodb:

MongoDB 简介
		
	1、是一个基于分布式，文件存储的NoSQL数据库
	2、由c++语言编写，运行稳定，性能高
	3、旨在为WEB应用提供可扩展的高性能数据存储解决方案


MongoDB 特点：

	模式自由：可以把不同结构的文档存储在同一个数据库里

	面向集合的存储：适合存储JSON风格文件的形式

	完整的索引支持：对任何属性可索引

	复制和高可用性：支持服务器之间的数据复制，支持主-从模式及服务器之间相互复制。
					复制的主要目的是提供冗余及自动故障转移

	自动分片：支持云级别的伸缩性：自动分片功能支持水平的数据库集群，可动态添加额外的机器。

	丰富的查询：支持丰富的查询表达式，查询指令使用JSON形式的标记，可轻易查询文档中的内嵌的对象及数组

	快速的更新：查询优化器会分析查询表达式，并生成一个高效的查询计划

	高效的传统存储方案：支持二进制数据及大型对象(如照片和图片)



基本操作：

	MongoDB 将数据存储为一个文档，数据结构由键值(key=>value)对组成

	MongoDB 文档类似于JSON对象，字段值可以包含其他文档、数组、文档数组

	安装数据库管理mongodb环境

	完成数据库、集合的管理

	数据的增加、修改、删除、查询


	名词：

	SQL术语/概念            MongoDB术语/概念            解释说明

	  database                database                  数据库

	  table                   collection                数据库表/集合

	  row                     document                  数据记录行/文档

	  column                  field                     数据字段/域

	  index                   index                     索引

	  table joins                                       表连接，MongoDB不支持

	  primary key             primary key               主键，MongoDB自动将_id字段设置为主键


	MongoDB中的三元素： 数据库、集合、文档

		1、集合就是关系数据库中的表
		
			集合类似于关系数据库中的表，储存多个文档，结构不固定，如果可以存储如下文档在一个集合中
			{'name':'guojing','gender':'男'}
			{'name':'huanggrong','age'"18"}
			{'book':'shuihuzhuan','heros':'108'}


		2、文档对应着关系数据库中的行
	
			文档，就是一个对象，有键值对构成，是json的扩展Bson形式。
			{'name':'guojing','gender':'男'}
	
		3、数据库：是一个集合的物理容器，一个数据库中可以包含多个文档
			一个服务器通常有多个数据库。


安装MongoDB：

	1、下载mongodb的版本，注意两点：

		根据业界规则，偶数为稳定版，如1.6X,奇数为开发版，如1.7X

		32bit的MongoBD最大只能存储2G的数据，64bit的没有限制。

		到官网下载合适版本：https://www.mongodb.com/download-center#community
		https://www.mongodb.org/dl/linux/x86_64
		wget http://fastdl.mongodb.org/linux/mongodb-linux-x86_64-debian71-3.5.6.tgz	

	2、检查是否安装过mongodb：

		rpm -qa|grep mongodb
		service mongodb status
		mongodb: unrecognized service

	3、添加用户和用户组：
		
		groupadd mongodb
		useradd mongodb -g mongodb

	4、解压：

		tar -zxvf mongodb-linux-x86_64-debian81-4.0.1.tgz

		移动到/usr/local/目录下：
			mv -r mongodb-linux-x86_64-debian81-4.0.1/ /usr/local/mongodb

		将bin目录下的可执行文件添加到PATH路径中：

		export PATH=/usr/local/mongodb/bin:$PAHT

	5、建立数据和日志的文件夹：

		MongoDB的数据库存储在data目录的db目录下，但是这个目录在安装过程中不会自动创建，
		所以需要你收到创建data目录，并在data目录中创建db目录。

		mkdir /usr/local/mongodb/data
		mkdir /usr/local/mongodb/logs

		以下实例中我们将data目录创建于根目录下(/)。
		注意：/data/db 是 MongoDB 默认的启动的数据库路径(--dbpath)。


	6、启动：
		/usr/local/mongodb/bin/mongod --dbpath=/usr/local/mongodb/data/ --port=27017 
		--logpath=/usr/local/mongodb/logs/mongodb.log --fork


	7、启动MongoDB后台管理 Shell

		如果你需要进入MongoDB后台管理，需要先打开mongodb安装目录下的bin目录，然后执行mongo命令文件。

		MongoDB shell 是Mongodb自带的交互式javascript shell，用来对Mongodb进行操作管理和交互式环境。
		当你进入mongoDB后台后，它默认会链接到 test 文档（数据库）：

			$ cd /usr/local/mongodb/bin
			$ ./mongo
			MongoDB shell version: 3.0.6
			connecting to: test
			Welcome to the MongoDB shell.
	
			由于它是一个JavaScript shell，您可以运行一些简单的算术运算:


	8、使用配置文件启动方式：

	添加配置文件：
		/usr/local/mongodb/mongodb.conf 

		添加以下设置

		port=27017 #端口号
		dbpath=/usr/local/mongodb/data/   #数据库路径
		logpath=/usr/local/mongodb/logs/mongodb.log #日志输出文件路径
		pidfilepath=/usr/local/mongodb/mongo.pid
		fork=true #设置后台运行
		logappend=true #日志输出方式
		shardsvr=true
		directoryperdb=true
		#auth=true  #开启认证


	启动MongoDb
		使用config命令指定配置文件的路径
		[root@localhost ~] cd /usr/local/mongodb/bin/
		[root@localhost bin]./mongod --config /usr/local/mongodb/mongodb.conf 
	

	9、Mongodb GUI：robomongo，解压后在bin目录下找到运行程序


Mongodb数据库操作：

	/usr/local/mongodb/bin/mongo

	1、查看当前数据库名称：
		
		>db
		test
		当你进入mongoDB后台后，它默认会链接到 test 文档（数据库）：
		
	2、查看所有数据库名称
	   列出所有在物理上存在的数据库
		
		>show dbs
		admin  0.000GB
		local  0.000GB

	3、切换数据库
	   如果数据库不存在，则指向数据库，但不创建，直到插入数据或创建集合时数据库才被创建

	   >use 数据库名称

	   默认的数据库为test，如果你没有创建新的数据库，集合将存放在test数据库中


	4、删除当前指向的数据库
	   如果数据库不存在，则什么也不做

	   db.dropDatabase()


Mongodb集合操作：

	1、语法：
		
		集合创建:

			db.createCollection(name,options)
			
				name是要创建的集合的名称
				options是一个文档，用于指定集合的配置
				选项参数是可选的，所以只需要指定集合的名称
				以下是可以使用的选项列表：

			例1：不限制集合大小

				db.createCollection("stu")

			例2：限制集合大小，后面学会插入语句后可以查看效果

				参数capped:默认值是false表示不设置上限，值为true表示设置上限
				参数size:当capped值为true时，需要指定此参数，表示上限大小，
						 当文件达到上限时，会将之前的数据覆盖，单位为字节。

				db.createCollection("sub",{capped:true,size:10})

		查看当前数据库的集合：

			show collections

		删除集合：

			db.集合名.drop()


数据类型：
	
	下表为Mongodb中常用的几种数据类型：

	ObjectID :文档ID

	String :字符串，最常用，必须是有效的UTF-8

	Boolean:存储一个布尔值，true或false

	Integer:整数可以是32或64，这取决于服务器

	Double:存储浮点值

	Arrays:数组和列表，多个值存储到一个键

	Object:用于嵌入式的文档，即一个值为一个文档

	Null:存储Null值

	Timestamp:时间戳

	Date:存储当前日期或时间的UNIX时间格式


	ObjectID:

		每个文档都有一个属性，为_id，保证每个文档的唯一性
		可以自己去设置_id插入文档
		如果没有提供，那么MongoDB为每个文档提供了一个独特的_id，类型为objectID
		ObjectID是一个12字节的十六进制数
			前4个字节为当前时间戳
			接下来3个字节为机器ID
			接下来的2个字节中Mongodb的服务进程id
			最后3个字节是简单的增量值。


Mongodb文档操作：			

	1、创建

		db.集合名称.insert(document)

		插入文档时，如果不指定_id参数，Mongodb会为文档分配一个唯一的Objectid

		例1：
				db.stu.insert({name:'gj',gender:1})

		例2:
				s1={_id :'20160101',name:'hr'}
				s1.gender=0
				db.stu.insert(s1)

	
	2、查询

		db.集合名字.find()



	3、更新

		db.集合名称.update(
			
			<query>,
			<update>,
			{multi:<boolean>})


		参数query:查询条件，类似sql语句update中where部分

		参数update：更新操作，类似sql语句update中set部分

		参数multi：可选，默认是false，表示只更新找到的第一条记录，
				   值为True表示把满足条件的文档全部更新。

		例子：
			db.stu.update({name:'hr'},{name:'mnc'})

		指定属性更新，通过操作符$set,这里是只修改name这个属性，如果不加$set,则会把整条语句替换掉。
		
			db.stu.insert({name:'hr',gender:0})
			db.sut.update({name:'hr'},{$set:{name:'hys'}})

		修改多条匹配到的数据

			db.stu.update({},($set:{gender:0},{multi:true}))

	4、保存(这个和insert没有什么区别吧)

		db.集合名称.save(document)
		
		如果文档的_id已经存在则修改，如果文档的_id不存在则添加

		db.stu.save({_id:'20160102','name':'yk',gender:1})


	5、删除

		db.集合名称.remove(
				<query>,
				{
					justOne:<boolean>
				})

		参数query:可选，删除文档的条件
		参数justOne:可选，如果设为True或1，则只删除一条，默认为false，表示删除多条。

		例子：只删除一条
			
			db.stu.remove({gender:0},{justOne:true})

		删除全部：
			
			db.stu.remove({})


	6、关于size的示例

		创建集合：

		db.createCollection('sub',{capped:true,size:10})	

		插入第一条数据库查询

			db.sub.insert({title:'linux',count:10})
			db.sub.find()

		插入第二条数据查询
			
			db.sub.insert({title:'web',count:15})
			db.sub.find()

		插入第三条数据查询
			
			db.sub.insert({title:'sql',count:18})
			db.sub.find()

		插入第四条数据库查询

			db.sub.insert({title:'django',count:12})
			db.sub.find()

		插入第五条数据库查询
		db.sub.insert({title:'python',count:14})
		db.sub.find()


Mongodb数据库数据查询:
	
	1、基本查询

		方法find():查询
			
			db.集合名称.find({条件文档})

		方法findOne():查询，只返回第一个

			db.集合名称.findOne({条件文档})

		方法pretty()：将结果格式化

			db.集合名称.find({条件文档}).pretty()


		limit():用于读取指定数量的文档
			
			语法：db.集合名字.find().limit(NUMBER)

			参数NUMBER表示要获取文件的条数
			如果没有指定参数则显示集合中所有的文档

			例子：查询2条学生信息
			db.stu.find().limit(2)

		skip():用于跳过指定数量的文档
			
			语法：db.集合名称.find().skip(NUMBER)

			参数NUMber表示跳过的记录条数，默认值是0

			例子：查询从第3条开始的学生信息

			db.stu.find().skip(2)

		limit()和skip()一起使用，部分先后顺序

			创建数据集:

			for(i=0;i<15;i++){
			db.t1.insert({_id:i})
			}

			查询第5到第8条数据

			db.stu.find().limit(4).skip(5)
			或
			db.stu.find().skip(5).limit(4)


	2、比较运算符：

		等于，默认是等于判断，没有运算符

		小于$lt

		小于或等于$lte

		大于$gt

		大于或等于$gte

		不等于$ne

		例1：查询名称等于'gj'的学生
		
			db.stu.find({name:'gj'})

		例2：查询年龄大于或等于18的学生

			db.stu.find({age:{$get:18}})

	3、逻辑运算符

		查询时可以有多个条件，多个条件之间需要通过逻辑运算符连接

		
		逻辑与：默认是逻辑与的关系
		例3、查询年龄大于或等于18，并且性别为1的学生

			db.stu.find({age:{$get:18},gender:1})

		逻辑或：使用$or
		例4、查询年龄大于18或性别为1的学生

			db.stu.find({$or:[{age:{$gt:18}},{gender:1}}]})

		and和or一起使用
		例5：查询年龄大于18或性别为0的学生，并且学生的姓名为gj
			db.stu.find({$or:[{age:{$gte:18}},{gender:1}],name:'gj'})


	4、范围运算符

		使用"$in","$nin"判断是否在某个范围内
		查询年龄为18,28的学生
		db.stu.find({age:{$in:[18,28]}})

	5、支持正则表达式

		使用//或$regex编写正则表达式
		查询姓黄的学生

		db.stu.find({name:/^黄/})

		db.stu.find({name:{$regex:'^黄'}})


	6、自定义查询

		使用$where后面写一个函数，返回满足条件的数据
		例7：查询年龄大于20的学生

		db.stu.find({$where:function(){return this.age>20}})


投影：

	在查询的返回结果中，只选择必要的字段，而不是选择一个文档的整个字段
	如：一个文档有5个字段，需要显示只有3个，投影其中的3个字段即可
	语法：

	参数为字段与值，值为1表示显示，值为0不显示

	db.集合名称.find({},{字段名称:1,...})

	对于需要显示的字段，设置为1即可，不设即为不显示。
	特殊：对于_id列默认是显示的，如果不显示，需要明确设置为0
	
	例1:
		db.stu.find({},{name:1,gender:1})

	例2：
		db.stu.find({},{_id:0,name:1,gender:1})	


排序：

	方法sort(),用于对结果集进行排序

	语法：

		db.集合名称.find().sort({字段:1,...})
	
		参数为1为升序排序
		参数为-1为降序排序

		例子：根据性别降序，再根据年龄升序

		db.stu.find().sort({gender:-1,age:1})


统计个数：

	方法count()用于统计结果集中文档条数
	语法：
		
		db.集合名称.find({条件}).count()

		也可以为：

		db.集合名称.count({条件})

		1、统计男生的人数
			
			db.stu.find({gender:1}).count()

		2、统计年龄大于20的男生人数

			db.stu.count({age:{$ge:20},gender:1})

消除重复:

	方法distinct()对数据进行去重

	db.集合名称.distinct('去重字段',{条件})
		
		例1、查找年龄大于18的性别(去重)

		db.stu.distinct('gender',{age:{$gt:18}})


Mongodb高级操作：

	Mongodb的高级操作，包括聚合、主从复制、分片、备份与恢复、MR
	完成Python与mongodb的交互

	1、聚合 aggregate

		聚合(aggregate)主要用于计算数据，类似sql中的sum(),avg()

		语法：
			db.集合名称.aggregate([{管道:{表达式}}])


			db.stu.aggregate([]) == db.stu.find()

		管道：管道在Unix和Linux中一般讲当前命令的输出结果作为下一个命令的输入
			ps ajx | grep mongo
		
		在mongodb中，管道具有同样的作用，文档处理完毕后，通过管道进行下一次处理
		
		常用管道：

			$group :将集合中的文档分组，可用于统计结果
				

				将集合中的文档分组，可用于统计结果
				_id表示分组的依据，使用某个字段的格式为'$'字段

				例1：统计男生、女生的总人数

					db.stu.aggregate([{$group:{_id:'$gender',counter:{$sum:1}}}])


				Group by null
				将集合中的所有文档分为一组
				
				例2：求学生总人数，平均年龄

				db.stu.aggregate([
					{$group:
						{
							_id:null,
							counter:{$sum:1},
							avgAge:{$avg:'$age'}
						}
					}			
				])


				透视数据：

				例3：统计学生性别及学生姓名

				db.stu.aggrate([
						{$group:
							{
								_id:'$gender'
								name:{$push:'$name'}
							}
						}
				])

				使用$$ROOT可以将文档内容加入到结果集的数组中，代码如下:

				db.stu.aggregate([
						    {
								$group:
							        {
										_id:'$gender',
										name:{$push:'$$ROOT'}
									}
							}
				])


			$match :过滤数据，只输出符合条件的文档

				用于过滤数据，只符合条件的文档
				
				例1：查询年龄大于20的学生

					db.stu.aggregate([{$match:{age:{$gt:20}}}])

				例2：查询年龄大于20的男生，女生的人数
					
					db.stu.aggregate([
							{$match:{age:{$gt:20}}},
							{$group:{_id:'$gender',counter:{$sum:1}}}])

	
			$project:修改输入文档的结构，如重命名、增加、删除字段、创建计算结果
	
				例1：查询学生的姓名、年龄

					db.stu.aggregate([{$project:{_id:0,name:1,age:1}}])

				例2：查询男生、女生人数，输出人数
					db.stu.aggregate([
							{$group:{id:'$gender',counter:{$sum:1}}},
							{$project:{_id:0,counter:1}}
							])

			$sort:将输入文档排序后输出
				
				将输入文档排序后输出
				例1：查询学生信息，按年龄升序
					b.stu.aggregate([{$sort:{age:1}}])

				例2：查询男生、女生人数，按人数降序

				db.stu.aggregate([
						{$group:{_id:'$gender',counter:{$sum:1}}},
						{$sort:{counter:-1}}
						])

			$limit:限制聚合管道返回的文档数

				例1、查询2条学生信息
				db.stu.aggregate([{$limit:2}])
			
			$skip：跳过指定数量的文档，并返回余下的文档
				
				例2：查询从第3条开始的学生信息
				db.stu.aggregate([{$skip:2}])
				
			
			$unwind:将数组类型的字段进行拆分

				语法1：

					对某字段值进行拆分
					
					db.集合名称.aggregate([{$unwind:'$字段名称'}])

				例子1：
					构造数据：db.t2.insert({_id:1,item:'t-shirt',size:['S','M','L']})
					查询：db.t2.aggregate([{$unwind:'$size'}])

					结果：

						{"_id" : 1, "item" : "t-shirt", "size" : "S" }
						{"_id" : 1, "item" : "t-shirt", "size" : "M" }
						{"_id" : 1, "item" : "t-shirt", "size" : "L" }
				语法2：

					对某字段值进行拆分
					处理空数组、非数组、无字段、null情况

					db.inventory.aggregate([{
						$unwind:{
							path:'$字段名称',
							preserveNullAndEmptyArrays:<boolean>#防止数据丢失
						}
					}])


					例子

					构造数据
					
					db.t3.insert([
							{ "_id" : 1, "item" : "a", "size": [ "S", "M", "L"] },
							{"_id" : 2, "item" : "b", "size" : [ ] },
							{"_id" : 3, "item" : "c", "size": "M" },
							{"_id" : 4, "item" : "d" },
							{ "_id" : 5, "item" : "e", "size" : null })

					使用语法1查询
						db.t3.aggregate([{$unwind:'$size'}])

						查看查询结果，发现对于空数组、无字段、null的文档，都被丢弃了
						问：如何能不丢弃呢？
						答：使用语法2查询
							db.t3.aggregate([{$unwind:{path:'$sizes',preserveNullAndEmptyArrays:true}}])
		表达式:

			处理输入文档并输出

			语法：
				表达式：'$列名'

			常用表达式：

				$sum :计算总和，$sum:1同count表示计数。

				$avg :计算平均值。

				$min :计算最小值。

				$max :计算最大值。

				$push:在结果文档中插入值到一个数组中。

				$first:根据资源文档的排序获取第一个文档数据。

				$last:根据资源文档的排序获取最后一个文档数据。


"-----------------------------------------------------------------------------------"

Mongodb数据库安全：

	为了更安全的访问mongoDB，需要访问者提供用户名和密码，于是需要在mongodb中创建用户
	采用了角色--用户--数据库的安全管理方式

	常用的系统角色如下：

		root：只在admin数据库中可用，超级账号，超级权限

		Read: 允许用户读取指定数据库

		readWrite:允许用户读写指定的数据库

创建超级管理用户：

		use admin
		db.createUser({
			user:'admin',
			pwd:'123',
			roles:[{role:'root',db:'admin'}]
				})

	修改配置文件 mongod.conf
	启动身份认证
	注意：keys and values 之间一定要加空格，否则解析会报错

		security:

			authorization:enabled

	重启服务：

		service  mongod stop
		service  mongod start

	终端连接：

		mongo -u 'admin' -p '123' --authenticationDatabase 'admin'



普通用户管理:

	使用超级管理员登录，然后进入用户管理操作
	查看当前数据库的用户
	
	use test1
	show users
	
	创建普通用户：
		
		db.createUser({
			user:'t1',
			pawd:'123'
			roles:[{
				role:'readWrite',db:'test1'
			}]
			})

	终端连接：

		mongo -u t1 -p 123 --authenticationDatabase test1

	修改用户名：可以修改pwd、roles属性
		
		db.updateUser('t1',{pwd:'456'})
	
"--------------------------------------------------------------------"

复制(副本集)：

	什么是复制：

		复制提供了数据的冗余备份，并在多个服务器上存储数据副本，提高了数据的可用性，并可以保证数据的安全性。
		复制还允许从硬件故障和服务中断中恢复数据


	为什么要复制：

		数据备份
		数据灾难恢复
		读写分离
		高数据可用性
		无宕机维护
		副本集对应程序是透明

	复制的工作原理：

		复制至少需要两个点A、B...
		A是主节点，负责处理客户端请求
		其他都是从节点，负责复制主节点上的数据
		节点常见的搭配方式为：一主一从，一主多从
		主节点记录在其上的所有操作，从节点定期轮询获取这些操作，然后对自己的数据副本执行这些操作
			从而保证从节点和主节点数据一致。
		主节点和从节点进行数据交换保障数据的一致性。

	复制的特点：
		
		N 个节点的集群
		任何节点可作为主节点
		所有写入操作都在主节点上
		自动故障转移
		自动恢复
	
	设置复制节点：

		接下来的操作需要打开多个终端窗口，而且可能会连接多台ubuntu主机，会显得有些乱，建议在xshell中实现
		
		step1:创建数据库目录t1、t2
		在Desktop目录下演示，其它目录也可以，注意权限即可

			mkdir t1
			mkdir t2

		step2:使用如下格式启动mongod,注意replSet的名称是一致的

			mongod --bind_ip 192.168.196.128 --port 27017 --depath ~/Desktop/t1 --replSet rs0
			mongod --bind_ip 192.168.196.128 --port 27018 --dbpath ~/Desktop/t2 --replSet rs0


		step3:连接主服务器，此处设置192.168.196。128:27017为主服务器

			mongo --host 192.168.196.128 --port 27017

		step4:初始化

			rs.initiate()

		step5:查看当前状态

			rs.status()

		step6:添加副本集

			rs.add('192.168.196.128:27018')

		step7:复本集添加成功后，当前状态如下图：
			rs.status()

		step8:连接第二个mongo服务
			mongo --host 192.168.196.128 --port 27018

		step9:向主服务器中插入数据

			use test1
			for(i=0;i<10;i++){
				db.t1.insert({_id:i})}
				db.t1.find()

		step10:在从服务器中插查询
			
			说明：如果在从服务器上进行读操作，需要设置rs.slaveOk()
			rs.slaveOk()
			db.t1.find()

	其他说明:
		
		删除从节点：

		rs.remove('192.168.196.128:27018')
		关闭主服务器后，再重新启动，会发现原来的从服务器变为了从服务器，
		新启动的服务器（原来的从服务器）变为了从服务器
		

Mongodb备份:

	语法：

		mongodump -h  dbhost  -d dbname -o dbdirectory

		-h:服务器地址，也可以指定端口号

		-d:需要备份的数据库名称

		-o:备份数据存放的位置，此目录中存放着备份出来的数据

	例1：
		
		mkdir test1bak

		mongodump -h 192.168.126.198:27017 -d test1 -o ~/Desktop/test1bak


	备份恢复：

	语法：

		mongorestore -h dbhost -d dbname --dir dbdirectory

		-h:服务器地址

		-d:需要恢复的数据库实例

		--dir:备份数据所在位置

	例2：

		mongorestore -h 192.168.196.128:27017 -d test2 --dir ~/Desktop/test1bak/test1


"-----------------------------------------------------------------------------------"

python与mangodb的交互：

	1、安装pymongo


		第一种方式使用pip工具安装：

		python -m pip install pymongo
		python -m pip install pymongo==3.5.1
		python -m pip install --upgrade pymongo

		
		第二种方式：

		用easy_install + 包名

		第三种方式：

			下载安装包，并解压到磁盘下；
			进入到该文件的setup.py 目录下 ，打开cmd，并切换到该目录下；
			先执行 python setup.py build
			然后执行 python setup.py install

	2、引入包pymongo

		import pymongo
		import pymongo from MongoClient

	3、连接Mongodb库

		client = pymongo.MongoClient("localhost",27017)

	4、得到数据库test_database

		db = client.test_database

	5、得到集合stu

		stu = db.test_collection

	6、添加文档到集合中，我们使用insert_one()方法：


		s1 = {
			'name':'gj',
			'age':18}
		
		s1_id = stu.insert_one(s1).inserted_id

	7、查找一个文档

		s2 = stu.find_one()

	8、查找多个文档1

		for cur in std.find():
			print cur

	9、查找多个文档2

		cur = stu.find()
		cur.next()
		cur.next()
		cur.next()

	10、获取文档个数

		print stu.count()
	

