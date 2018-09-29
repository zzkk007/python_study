
"-----------------------------------------------------"

		前端开发系统化学习教程

"----------------------------------------------------"

	前端开发系统化学习教程，包括html、css、PC端及移动端布局技巧、
	javascript、jquery、js特效制作、ajax前后台交互等。


HTML:

1、HTML概述和基本结构：

	概述：
	
		HTML是HyperText Mark-up Language的首字母简写，意思是超文本标记语言
		超文本指的是超链接，标记指的是标签，是一种用来制作网页的语言，
		这种语言由一个个的标签组成，用这种语言制作的文件保存的是一个文本文件。
		文件的扩展名为html或htm，一个html文件就是一个网页，HTML文件用编辑器打开
		显示的是文本，可以用文本的方式编辑它，如果用浏览器打开，
		浏览器会按照标签描述内容将文件渲染成网页，
		显示的网页可以从一个网页链接跳转到另外一个网页。

	结构：

		一个html的基本结构如下：

		<!DOCTYPE html>
		<html lang="en">
			<head>            
				<meta charset="UTF-8">
				<title>网页标题</title>
			</head>
			<body>
				网页显示内容
			</body>
		</html>

		第一行是文档声明，第二行“<html>”标签和最后一行“</html>”定义html文档的整体，
		"<html>"标签中的‘lang="en"’定义网页的语言为英文，定义成中文是'lang="zh-CN"',
		不定义也没什么影响，它一般作为分析统计用。
		"<head>"标签和"<body>"标签是它的第一层子元素,
		"<head>"标签里面负责对网页进行一些设置以及定义标题，
		设置包括定义网页的编码格式，外链css样式文件和javascript文件等，
		设置的内容不会显示在网页上，标题的内容会显示在标题栏.
		"<body>"内编写网页上显示的内容。

	HTML文档类型：

		目前常用的两种文档类型是xhtml 1.0和html5

	xhtml 1.0:

		xhtml 1.0 是html5之前的一个常用的版本，目前许多网站仍然使用此版本。
		此版本文档用sublime text创建方法： html:xt + tab
		文档示例：

			<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
				"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
			<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
				<head>
					<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
				    <title> xhtml 1.0 文档类型 </title>
				</head>
				<body>
					
				</body>
			</html>


	html5:

		pc端可以使用xhtml 1.0，也可以使用html5，html5是向下兼容的
		此版本文档用sublime text创建方法： html:5 + tab 或者 ! + tab
		文档示例：

			<!DOCTYPE html>
			<html lang="en">
				<head>
					<meta charset="UTF-8">
				    <title> html5文档类型 </title>
				</head>
				<body>
					
				</body>
			</html>


	两种文档的区别:
		
		1、文档声明和编码声明

		2、html5新增了标签元素以及元素属性

	html文档规范:

		xhtml制定了文档的编写规范，html5可部分遵守，也可全部遵守，看开发要求。

		1、所有的标签必须小写

		2、所有的属性必须用双引号括起来

		3、所有标签必须闭合

		4、img必须要加alt属性(对图片的描述)

	html注释:

		html文档代码中可以插入注释，注释是对代码的说明和解释，
		注释的内容不会显示在页面上，html代码中插入注释的方法是：

		<!-- 这是一段注释  -->

	html标签特点：

		HTML的标签大部分是成对出现的，少量是单个出现的，
		特定标签之间可以相互嵌套，嵌套就是指一个标签里面
		可以包含一个或多个其他标签，包含的标签和父标签
		可以是同类型的，也可以是不同类型的。

		<!-- 成对出现的标签  -->
		<body>......</body>
		<p>......</p>
		<div>......</div>
		<b>......</b>

		<!-- 单个出现的标签  -->
		<br />
		<img src="..." />
		<input type="..." />

		<!-- 标签之间的嵌套  -->
		<p>
		    <span>...</span>
			<a href="...">...</a>
		</p>
		<div>
			<h3>...</h3>
			<div>
				<span>...</span>
				<p>...</p>
			</div>
		</div>


2、html标题：

	通过<h1>、<h2>、<h3>、<h4>、<h5>、<h6>标签可以在网页上定义6种级别的标题。

	6种级别的标题表示文档的6级目录层级关系，
	比如说：<h1>用作主标题(最重要的),其后是<h2>(次重要的)再其次是 <h3>,以此类推。
	搜索引擎会使用标题将网页的结构和内容编制索引，所以网页上使用标题是很重要的。
	
	<h1>这是一级标题</h1>
	<h2>这是二级标题</h2>
	<h3>这是三级标题</h3>

3、html段落、换行与字符实体：

	html段落：

		<p>标签定义一个文本段落，一个段落含有默认的上下间距，
		段落之间会用这种默认间距隔开，代码如下：

		<!DOCTYPE html>
		<html lang="en">
		<head>
		    <meta charset="UTF-8">
			<title>段落</title>
		</head>
		<body>
				<p>HTML是 HyperText Mark-up Language 的首字母简写，意思是超文本标记语言，超
				文本指的是超链接，标记指的是标签，是一种用来制作网页的语言，这种语言由一个个的
				标签组成，用这种语言制作的文件保存的是一个文本文件，文件的扩展名为html或者htm。
				</p>
								
				<p>一个html文件就是一个网页，html文件用编辑器打开显示的是文本，可以用文本的方
				式编辑它，如果用浏览器打开，浏览器会按照标签描述内容将文件渲染成网页，显示的网
				页可以从一个网页链接跳转到另外一个网页。</p>
		</body>
		</html>

	html换行：

		代码中成段的文字，直接在代码中回车换行，在渲染成网页时候不认这种换行，
		如果真想换行，可以在代码的段落中插入<br/>来强制换行，代码如下：

		<p>
		一个html文件就是一个网页，html文件用编辑器打开显示的是文本，可以用<br />
		文本的方式编辑它，如果用浏览器打开，浏览器会按照标签描述内容将文件<br />
		渲染成网页，显示的网页可以从一个网页链接跳转到另外一个网页。
		</p>

	
	html字符实体：

		代码中成段的文字，如果文字间想空多个空格，在代码中空多个空格，
		在渲染成网页时只会显示一个空格，如果想显示多个空格，
		可以使用空格的字符实体,代码如下：
	
		<!--在段落前想缩进两个文字的空格，使用空格的字符实体：&nbsp;-->
		<p>
		&nbsp;&nbsp;一个html文件就是一个网页，html文件用编辑器打开显示的是文本，可以用<br/>
		文本的方式编辑它，如果用浏览器打开，浏览器会按照标签描述内容将文件<br/>
		渲染成网页，显示的网页可以从一个网页链接跳转到另外一个网页。</p>
		

		在网页上显示“<”和“>”会误认为是标签，想在网页上显示“<”和“>”可以使用它们的字符实体，比如：
		<p>
		    3 &lt; 5 <br>
			10 &gt; 5
		</p>

4、html块、含样式的标签：

	html块:

		1、div标签 块元素，表示一块内容，没有具体的语义。
		2、span标签 行内元素，表示一行中的一小段内容，没有具体的语义。

	含样式和语义的标签:

		1、em标签 行内元素，表示语气中的强调词
		2、i标签 行内元素，原本没有语义，w3c强加了语义，表示专业词汇
		3、b标签 行内元素，原本没有语义，w3c强加了语义，表示文档中的关键字或者产品名
		4、strong标签 行内元素，表示非常重要的内容

	语义化的标签:
		
		语义化的标签，就是在布局的时候多使用语义化的标签，
		搜索引擎在爬网的时候能认识这些标签，理解文档的结构，方便网站的收录。
		比如：h1标签是表示标题，p标签是表示段落，ul、li标签是表示列表，
		a标签表示链接，dl、dt、dd表示定义列表等，语义化的标签不多。

5、html图像、绝对路径和相对路径：

	html图像：

		<img>标签可以在网页上插入一张图片，它是独立使用的标签，
		通过"src"属性定义图片的地址，通过"alt"属性定义图片加载失败时显示的文字，
		以及对搜索引擎和盲人读屏软件的支持。

		<img src="images/pic.jpg" alt="产品图片" />

	绝对路径和相对路径:

		像网页上插入图片这种外部文件，需要定义文件的引用地址，
		引用外部文件还包括引用外部样式表，
		javascript等等，引用地址分为绝对地址和相对地址。

		绝对地址：相对于磁盘的位置去定位文件的地址
		相对地址：相对于引用文件本身去定位被引用的文件地址

		绝对地址在整体文件迁移时会因为磁盘和顶层目录的改变而找不到文件，
		相对路径就没有这个问题。相对路径的定义技巧：

6、html链接：

	html链接：

		<a>标签可以在网页上定义一个链接地址，通过src属性定义跳转的地址，
		通过title属性定义鼠标悬停时弹出的提示文字框。

		<a href="#"></a> <!--#表示链接到页面顶部-->
		<a href="http://www.itcast.cn/" title="跳转的传智播客网站">传智播客</a>
		<a href="2.html">测试页面2</a>

	定义页面内滚动跳转:

		页面内定义了"id"或者"name"的元素，可以通过a标签链接到它的页面滚动位置，
		前提是页面要足够高，有滚动条，且元素不能在页面顶部，否则页面不会滚动。

		<a href="#mao1">标题一</a>
		......
		......
		<h3 id="mao1">跳转到的标题</h3>

7、html列表:

	有序列表:

		在网页上定义一个有编号的内容列表可以用<ol>、<li>配合使用来实现代码如下：

		<ol>
		    <li>列表文字一</li>
			<li>列表文字二</li>
			<li>列表文字三</li>
		</ol>

		在网页上生成的列表，每条项目上会按1、2、3编号，有序列表在实际开发中较少使用。

	无序列表:

		在网页上定义一个无编号的内容列表可以用<ul>、<li>配合使用来实现，代码如下：

		<ul>
		    <li>列表文字一</li>
			<li>列表文字二</li>
			<li>列表文字三</li>
		</ul>

		在网页上生成的列表，每条项目上会有一个小图标，这个小图标在不同浏览器上显示效果不同，
		所以一般会用样式去掉默认的小图标，如果需要图标，可以用样式自定义图标，
		从而达到在不同浏览器上显示的效果相同,实际开发中一般用这种列表。

	定义列表:

		定义列表通常用于术语的定义。<dl>标签表示列表的整体。
		<dt>标签定义术语的题目。<dd>标签是术语的解释。
		一个<dl>中可以有多个题目和解释，代码如下：

		<h3>前端三大块</h3>
		<dl>
		    <dt>html</dt>
			<dd>负责页面的结构</dd>

			<dt>css</dt>
			<dd>负责页面的表现</dd>

			<dt>javascript</dt>
			<dd>负责页面的行为</dd>

		</dl>


8、html表格：

	table常用标签：

		1、table标签：声明一个表格
		2、tr标签：定义表格中的一行
		3、td和th标签：定义一行中的一个单元格，td代表普通单元格，th表示表头单元格

	table常用属性：

		1、border 定义表格的边框
		2、cellpadding 定义单元格内内容与边框的距离
		3、cellspacing 定义单元格与单元格之间的距离
		4、align 设置单元格中内容的水平对齐方式,设置值有：left | center | right
		5、valign 设置单元格中内容的垂直对齐方式 top | middle | bottom
		6、colspan 设置单元格水平合并
		7、rowspan 设置单元格垂直合并

	传统布局：

		传统的布局方式就是使用table来做整体页面的布局，布局的技巧归纳为如下几点：

		1、定义表格宽高，将border、cellpadding、cellspacing全部设置为0
		2、单元格里面嵌套表格
		3、单元格中的元素和嵌套的表格用align和valign设置对齐方式
		4、通过属性或者css样式设置单元格中元素的样式

9、html表单：

	表单用于搜集不同类型的用户输入，表单由不同类型的标签组成，
	实现一个特定功能的表单区域（比如：注册），首先应该用<form>标签来定义表单区域整体，
	在此标签中再使用不同的表单控件来实现不同类型的信息输入，
	具体实现及注释可参照以下伪代码：

	<!-- form定义一个表单区域,action属性定义表单数据提交的地址，
	method属性定义提交的方式。   -->
	<form action="http://www..." method="get">
	
	<!-- label标签定义表单控件的文字标注，input类型为text定义了
	一个单行文本输入框  -->
	<p>
	<label>姓名：</label><input type="text" name="username" />
	</p>
	
	<!-- input类型为password定义了一个密码输入框  -->
	<p>
	<label>密码：</label><input type="password" name="password" />
	</p>
	
	<!-- input类型为radio定义了单选框  -->
	<p>
	<label>性别：</label>
	<input type="radio" name="gender" value="0" /> 男
	<input type="radio" name="gender" value="1" /> 女
	</p>
	
	<!-- input类型为checkbox定义了单选框  -->
	<p>
	<label>爱好：</label>
	<input type="checkbox" name="like" value="sing" /> 唱歌
	<input type="checkbox" name="like" value="run" /> 跑步
	<input type="checkbox" name="like" value="swiming" /> 游泳
	</p>
	
	<!-- input类型为file定义上传照片或文件等资源  -->
	<p>
	<label>照片：</label>
	<input type="file" name="person_pic">
	</p>
	
	<!-- textarea定义多行文本输入  -->
	<p>
	<label>个人描述：</label>
	<textarea name="about"></textarea>
	</p>
	
	<!-- select定义下拉列表选择  -->
	<p>
	<label>籍贯：</label>
	<select name="site">
	    <option value="0">北京</option>
		<option value="1">上海</option>
		<option value="2">广州</option>
		<option value="3">深圳</option>
	</select>
	</p>
					
	<!-- input类型为submit定义提交按钮  
		还可以用图片控件代替submit按钮提交，一般会导致提交两次，不建议使用。如：
		<input type="image" src="xxx.gif">
	-->
	
	<p>
	<input type="submit" name="" value="提交">
							  
	<!-- input类型为reset定义重置按钮  -->
	<input type="reset" name="" value="重置">
	</p>
							  
	</form>


10、html内嵌框架：

	html内嵌框架

		<iframe>标签会创建包含另外一个html文件的内联框架（即行内框架），
		src属性来定义另一个html文件的引用地址，frameborder属性定义边框，
		scrolling属性定义是否有滚动条，代码如下：

		<iframe src="http://www..." frameborder="0" scrolling="no"></iframe>
		
	内嵌框架与a标签配合使用:
		
		a标签的target属性可以将链接到的页面直接显示在当前页面的iframe中，代码如下：
		
		<a href="01.html" target="myframe">页面一</a>
		<a href="02.html" target="myframe">页面二</a>
		<a href="03.html" target="myframe">页面三</a>
		<iframe src="01.html" frameborder="0" scrolling="no" name="myframe"></iframe>


"----------------------------------------------------"

CSS:

	为了让网页元素的样式更加丰富，也为了让网页的内容和样式能拆分开，
	CSS由此思想而诞生，CSS是 Cascading Style Sheets 的首字母缩写，意思是层叠样式表。
	有了CSS，html中大部分表现样式的标签就废弃不用了，html只负责文档的结构和内容，
	表现形式完全交给CSS，html文档变得更加简洁。


1、css基本语法及页面引用：

	css 基本语法:

		css的定义方法是：选择器{属性:值;属性:值;属性:值;}

		选择器是将样式和页面元素关联起来的名称，属性是
		希望设置的样式属性每个属性有一个或多个值。代码如下：
		div{width:100px; height:100px; color:red }

	css 页面引入方法:

		1、外联式：通过link标签，链接到外部样式表到页面中。
			<link rel="stylesheet" type="text/css" href="css/main.css">
		
		2、嵌入式：通过style标签，在网页上创建嵌入的样式表。

			<style type="text/css">
				div{
						width:100px; height:100px; color:red }
					     ......
			</style>

		3、内联式：通过标签的style属性，在标签上直接写样式。

			<div style="width:100px; height:100px; color:red ">......</div>

2、css 文本设置:

	常用的应用文本的css样式：

	color 设置文字的颜色，如： color:red;

	font-size 设置文字的大小，如：font-size:12px;

	font-family 设置文字的字体，如：font-family:'微软雅黑';
	
	font-style 设置字体是否倾斜，如：font-style:'normal'; 设置不倾斜，font-style:'italic';设置文字倾斜
	
	font-weight 设置文字是否加粗，如：font-weight:bold; 设置加粗 font-weight:normal 设置不加粗
	
	font 同时设置文字的几个属性，写的顺序有兼容问题，
		 建议按照如下顺序写： font：是否加粗 字号/行高 字体；如： font:normal 12px/36px '微软雅黑';
	
	line-height 设置文字的行高，如：line-height:24px;
	
	text-decoration 设置文字的下划线，如：text-decoration:none; 将文字下划线去掉
	
	text-indent 设置文字首行缩进，如：text-indent:24px; 设置文字首行缩进24px
	
	text-align 设置文字水平对齐方式，如text-align:center 设置文字水平居中


3、css 颜色表示法:

	css颜色值主要有三种表示方法：

	1、颜色名表示，比如：red 红色，gold 金色

	2、rgb表示，比如：rgb(255,0,0)表示红色

	3、16进制数值表示，比如：#ff0000 表示红色，这种可以简写成 #f00


4、css选择器:

	1、标签选择器

		标签选择器，此种选择器影响范围大，建议尽量应用在层级选择器中：

		*{
			margin:0;padding:0}
			div{color:red}   

		<div>....</div>   <!-- 对应以上两条样式 -->
		<div class="box">....</div>   <!-- 对应以上两条样式 -->
	
	2、id选择器：
		
		通过id名来选择元素，元素的id名称不能重复，
		所以一个样式设置项只能对应于页面上一个元素，不能复用，
		id名一般给程序使用，所以不推荐使用id作为选择器。

		#box{color:red} 
			<div id="box">....</div>   <!-- 对应以上一条样式，其它元素不允许应用此样式 -->

	3、类选择器：

		通过类名来选择元素，一个类可应用于多个元素，一个元素上也可以使用多个类，
		应用灵活，可复用，是css中应用最多的一种选择器。

		.red{color:red}
		.big{font-size:20px}
		.mt10{margin-top:10px} 

		<div class="red">....</div>
		<h1 class="red big mt10">....</h1>
		<p class="red mt10">....</p>

	4、层级选择器：

		主要应用在选择父元素下的子元素，或者子元素下面的子元素，
		可与标签元素结合使用，减少命名，同时也可以通过层级，防止命名冲突。
		举例：


		.box span{color:red}
		.box .red{color:pink}
		.red{color:red}

		<div class="box">
		<span>....</span>
	    <a href="#" class="red">....</a>
		</div>
		
		<h3 class="red">....</h3>

	5、组选择器:

		多个选择器，如果有同样的样式设置，可以使用组选择器。
		举例：

		.box1,.box2,.box3{width:100px;height:100px}
		.box1{background:red}
		.box2{background:pink}
		.box2{background:gold}

		<div class="box1">....</div>
		<div class="box2">....</div>
		<div class="box3">....</div>

	6、伪类及伪元素选择器:

		常用的伪类选择器有hover，表示鼠标悬浮在元素上时的状态，伪元素选择器有before和after,
		它们可以通过样式在元素中插入内容。

		.box1:hover{color:red}
		.box2:before{content:'行首文字';}
		.box3:after{content:'行尾文字';}

		<div class="box1">....</div>
		<div class="box2">....</div>
		<div class="box3">....</div>

	7、css元素溢出：

		当子元素的尺寸超过父元素的尺寸时，需要设置父元素显示溢出的子元素的方式，
		设置的方法是通过overflow属性来设置。

		overflow的设置项： 
		1、visible 默认值。内容不会被修剪，会呈现在元素框之外。
		2、hidden 内容会被修剪，并且其余内容是不可见的，此属性还有清除浮动、清除margin-top塌陷的功能。
		3、scroll 内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。
		4、auto 如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。
		5、inherit 规定应该从父元素继承 overflow 属性的值。

	8、块元素、内联元素、内联块元素：

		元素就是标签，布局中常用的有三种标签，块元素、内联元素、内联块元素，
		了解这三种元素的特性，才能熟练的进行页面布局。

		块元素：

			块元素，也可以称为行元素，布局中常用的标签如：
			div、p、ul、li、h1~h6、dl、dt、dd等等都是块元素，它在布局中的行为：

			支持全部的样式
			如果没有设置宽度，默认的宽度为父级宽度100%
			盒子占据一行、即使设置了宽度

		内联元素:

			内联元素，也可以称为行内元素，布局中常用的标签如：
			a、span、em、b、strong、i等等都是内联元素，它们在布局中的行为：

			支持部分样式（不支持宽、高、margin上下、padding上下）
			宽高由内容决定
			盒子并在一行
			代码换行，盒子之间会产生间距
			子元素是内联元素，父元素可以用text-align属性设置子元素水平对齐方式，
			用line-height属性值设置垂直对齐方式

		内联块元素:

			内联块元素，也叫行内块元素，是新增的元素类型，现有元素没有归于此类别的，
			img和input元素的行为类似这种元素，但是也归类于内联元素，
			我们可以用display属性将块元素或者内联元素转化成这种元素。
			它们在布局中表现的行为：			
			
			支持全部样式
			如果没有设置宽高，宽高由内容决定
			盒子并在一行
			代码换行，盒子会产生间距
			子元素是内联块元素，父元素可以用text-align属性设置子元素水平对齐方式，
			用line-height属性值设置子元素垂直对齐方式

		这三种元素，可以通过display属性来相互转化，不过实际开发中，块元素用得比较多，
		所以我们经常把内联元素转化为块元素，少量转化为内联块，而要使用内联元素时，
		直接使用内联元素，而不用块元素转化了。

		display属性
		display属性是用来设置元素的类型及隐藏的，常用的属性有：
		1、none 元素隐藏且不占位置
		2、block 元素以块元素显示
		3、inline 元素以内联元素显示
		4、inline-block 元素以内联块元素显示

	
	9、浮动：

		文档流 
		文档流，是指盒子按照html标签编写的顺序依次从上到下，从左到右排列，块元素占一行，
		行内元素在一行之内从左到右排列，先写的先排列，后写的排在后面，每个盒子都占据自己的位置。

		浮动特性

		1、浮动元素有左浮动(float:left)和右浮动(float:right)两种
		2、浮动的元素会向左或向右浮动，碰到父元素边界、浮动元素、未浮动的元素才停下来
		3、相邻浮动的块元素可以并在一行，超出父级宽度就换行
		4、浮动让行内元素或块元素自动转化为行内块元素
		5、浮动元素后面没有浮动的元素会占据浮动元素的位置，
			没有浮动的元素内的文字会避开浮动的元素，形成文字饶图的效果
		6、父元素内整体浮动的元素无法撑开父元素，需要清除浮动
		7、浮动元素之间没有垂直margin的合并

		清除浮动

		父级上增加属性overflow：hidden
		在最后一个子元素的后面加一个空的div，给它样式属性 clear:both（不推荐）
		使用成熟的清浮动样式类，clearfix
		.clearfix:after,.clearfix:before{content: "";display: table;}
		.clearfix:after{clear:both;}
		.clearfix{zoom:1;}
		清除浮动的使用方法：
		.con2{... overflow:hidden}
		或者
		<div class="con2 clearfix">
	 
	10、定位：

		关于定位 
		我们可以使用css的position属性来设置元素的定位类型，postion的设置项如下：

		relative 生成相对定位元素，元素所占据的文档流的位置不变，元素本身相对文档流的位置进行偏移
		absolute 生成绝对定位元素，元素脱离文档流，不占据文档流的位置，可以理解为漂浮在文档流的上方，
				相对于上一个设置了相对或者绝对或者固定定位的父级元素来进行定位，
				如果找不到，则相对于body元素进行定位。
		fixed 生成固定定位元素，元素脱离文档流，不占据文档流的位置，
				可以理解为漂浮在文档流的上方，相对于浏览器窗口进行定位。
		static 默认值，没有定位，元素出现在正常的文档流中，相当于取消定位属性或者不设置定位属性
		inherit 从父元素继承 position 属性的值
	
		定位元素特性 
		
			绝对定位和固定定位的块元素和行内元素会自动转化为行内块元素

		定位元素层级 
			
			定位元素是浮动的正常的文档流之上的，可以用z-index属性来设置元素的层级

		典型定位布局 
			
			1、固定在顶部的菜单
			2、水平垂直居中的弹框
			3、固定的侧边的工具栏
			4、固定在底部的按钮


	11、background属性：

		属性解释 
		background属性是css中应用比较多，且比较重要的一个属性，
		它是负责给盒子设置背景图片和背景颜色的，background是一个复合属性，它可以分解成如下几个设置项：

		background-color 设置背景颜色
		background-image 设置背景图片地址
		background-repeat 设置背景图片如何重复平铺
		background-position 设置背景图片的位置
		background-attachment 设置背景图片是固定还是随着页面滚动条滚动
		实际应用中，我们可以用background属性将上面所有的设置项放在一起，而且也建议这么做，


	12、CSS盒子模型：

		盒子模型解释：

		元素在页面中显示成一个方块，类似一个盒子，CSS盒子模型就是使用现实中盒子来做比喻，
		帮助我们设置元素对应的样式。

		把元素叫做盒子，设置对应的样式分别为：盒子的边框(border)、
		盒子内的内容和边框之间的间距(padding)、盒子与盒子之间的间距(margin)。



		设置边框 
			设置一边的边框，比如顶部边框，可以按如下设置：

			border-top-color:red;    /* 设置顶部边框颜色为红色 */  
			border-top-width:10px;   /* 设置顶部边框粗细为10px */   
			border-top-style:solid;  /* 设置顶部边框的线性为实线，常用的有：solid(实线)  
			dashed(虚线)  dotted(点线); */
			上面三句可以简写成一句：

			border-top:10px solid red;
			
			设置其它三个边的方法和上面一样，把上面的'top'换成'left'就是设置左边，
			换成'right'就是设置右边，换成'bottom'就是设置底边。

			四个边如果设置一样，可以将四个边的设置合并成一句：

			border:10px solid red;

		设置内间距padding：

			设置盒子四边的内间距，可设置如下：

			padding-top：20px;     /* 设置顶部内间距20px */ 
			padding-left:30px;     /* 设置左边内间距30px */ 
			padding-right:40px;    /* 设置右边内间距40px */ 
			padding-bottom:50px;   /* 设置底部内间距50px */

			上面的设置可以简写如下：

			padding：20px 40px 50px 30px; /* 四个值按照顺时针方向，分别设置的是 上 右 下 左  
											 四个方向的内边距值。 */
			padding后面还可以跟3个值，2个值和1个值，它们分别设置的项目如下：

			padding：20px 40px 50px; /* 设置顶部内边距为20px，左右内边距为40px，底部内边距为50px */ 
			padding：20px 40px; /* 设置上下内边距为20px，左右内边距为40px*/ 
			padding：20px; /* 设置四边内边距为20px */

		设置外间距margin：

			外边距的设置方法和padding的设置方法相同，
			将上面设置项中的'padding'换成'margin'就是外边距设置方法。

		margin相关技巧：

			1、设置元素水平居中： margin:x auto;
			2、margin负值让元素位移及边框合并

		外边距合并：

			外边距合并指的是，当两个垂直外边距相遇时，它们将形成一个外边距。
			合并后的外边距的高度等于两个发生合并的外边距的高度中的较大者。解决方法如下：

			1、使用这种特性
			2、设置一边的外边距，一般设置margin-top
			3、将元素浮动或者定位

		margin-top 塌陷：

			在两个盒子嵌套时候，内部的盒子设置的margin-top会加到外边的盒子上，
			导致内部的盒子margin-top设置失败，解决方法如下：

			1、外部盒子设置一个边框
			2、外部盒子设置 overflow:hidden
			3、使用伪元素类：

			.clearfix:before{content: '';
						display:table;}
		

						

"---------------------------------------------------"

3 Photoshop:

	学习使用Photoshop的基本使用，以及Photoshop中关于切图这一块的知识，
	目的是能熟练使用Photoshop查看UI设计师的设计效果图，
	同时利用Photoshop切图来制作专业html页面。

	1、常用图片格式

		psd:

			psd是photoshop的专用格式，UI设计师使用photoshop设计效果图，
			最后会将psd格式的效果图交付给前端工程师，这种格式是不压缩的，
			而且保留了图层、透明和半透明等图片信息，所以这种图片格式的容量相对来说是很大的，
			前端工程师使用这种格式的效果图来切图制作网页，但是网页中不会使用这个格式的图片，
			它的作用一是保存图片的原始数据，二是方便图片的修改。

		jpg:

			jpg是一种有损压缩格式，压缩效率高，容量相对来说最小，
			网络传输速度快，它不能存为透明背景，在网页中应用最广，
			一般在不需要透明背景的时候就使用这种图片。

		gif:

			gif是一种无损压缩格式的图片，最多只有256种颜色，
			颜色丰富的图片转化为这种格式会颜色失真。它的背景可以是透明的，
			但不能是半透明的，透明背景中的图像，如果边缘轮廓是曲线的，
			会产生锯齿，它还可以保存为动画格式。

		peng:

			png的目的是为了代替gif图片，无损压缩，背景可以是透明或者半透明的，
			透明图像边缘光滑，没有锯齿，网页中需要透明或者半透明背景的图片，首选是png图片。

		webp:

			它是由谷歌于2010年推出的新一代图片格式，在压缩方面比当前jpg格式更优越，
			在质量相同的情况下，WebP格式图像的体积要比jpg格式图像小40%，
			不过这种图片还没有得到广泛的浏览器支持，仅在Chrome和Opera上支持.

		位图和矢量图:

			位图也叫点阵图，是由一个个的方形的像素点排列在一起拼接而成的，位图在放大时，
			图像会失真。上面讲的5种图像都属于位图。

			矢量图和位图组成图像的原理不同，它的图像轮廓是由函数曲线生成的，
			当放大图像时，实际的原理就是将曲线乘以一个倍数，图像可以轻易地放大，
			而且不会出现像素块，图像边缘也不会出现锯齿。

		svg:

			svg是一种矢量二维图形格式，它是基于xml标记语言描述的，可以通过任何文本编辑器创建。
			它的优点是文件容量小，放大不失真，而且背景也可以是透明的。
			目前大量使用这种格式来制作网页图标或者网页地图，由于它是矢量的，
			所以在不同终端屏幕上(pc、手机)都有很好的显示效果。			

		flash:

			flash是一种矢量动画文件格式，曾经在网络上风靡一时，如今已逐渐退出历史舞台，
			原因是它的技术更新跟不上发展，这种格式既可以是静态的图形，还可以是多媒体动画，
			还可以加入用户交互和数据，这是它曾经很流行的原因，这种格式名为swf，flash是对它的统称。

		总结: 
			在网页制作中，如何选择合适的图片格式呢？
			1、网页制作中，如果要使用不透明背景的图片，就使用jpg图片；
			  如果要使用透明或者半透明背景的图片，就使用png图片；
			
			2、制作网页图标时候，如果图标含多种颜色，可以使用gif或png图片；
			   如果图标是单色，而且要求有很好的显示效果，可以使用svg；如果是动画图标，可以使用gif。



"---------------------------------------------------"

前端页面开发流程:


	1、创建页面项目目录

	2、使用Photoshop对效果图切图，切出网页制作中需要的小图片

	3、将装饰类图像合并，制作成雪碧图

	4、结合Photoshop和代码编辑器，参照效果图，进行html和css代码书写，制作页面


"------------------------------------------------"

7 JavaScript

	学习前端脚本语言javascript的基本概念、页面引入方式、获取页面元素
	及操作元素属性的技巧，学习函数的基本定义方法和使用方法。


	1、JavaScript介绍:

		JavaScript是运行在浏览器端的脚本语言，
		JavaScript主要解决的是前端与用户交互的问题。
		包括使用交互和数据交互。

		JavaScript是浏览器解释执行的，前端脚本语言还有JScript(微软、IE独有)

		前端三大块：

			HTML：页面结构
			CSS：页面表现：元素大小、颜色、位置、隐藏或显示、部分动画效果。
			JavaScript: 页面行为：部分动画效果、页面与用户的交互、页面功能。

	2、JavaScript 嵌入页面的方式：

		1 行间事件（主要用于事件）
			
			<input type="button" name="" onclick="alert('ok！');"

		2 页面script标签嵌入：

			<script type="text/javascript">        
			    var a = '你好！';
				alert(a);
			</script>

		3 外部引入：

			<script type="text/javascript" src="js/index.js"></script>

	3、JavaScript 语句与注释：

		1 一条javascript语言应以";"结尾

			<script type="text/javascript">    
			var a = 123;
			var b = 'str';
			function fn(){
				alert(a);
			};
			fn();
			</script>

		2 javascript注释

			<script type="text/javascript">    
			
			// 单行注释
			var a = 123;
			/*  
				多行注释
				1、...
				2、...
			*/
			var b = 'str';
			</script>
	
	4、变量：

		JavaScript 是一种弱类型语言，Javascript的变量类型由它的值来决定。
		定义变量需要用关键字'var'.

		var a = 123;
		var b = 'asd';

		//同时定义多个变量可以用","隔开，公用一个‘var’关键字  
		var c = 45,d='qwe',f='68';
	
		变量类型：

			5种基本数据类型：
			number、string、boolean、undefined、null

			1种复合类型：
			object

		变量、函数、属性、函数参数命名规范：

			1、区分大小写
			2、第一个字符必须是字母、下划线（_）或者美元符号（$）
			3、其他字符可以是字母、下划线、美元符或数字


	5、获取元素方法之一：

		可以使用内置对象document上的getElementById方法来获取页面上
		设置了id属性的元素，获取到的是一个html对象，然后将它赋值给一个变量，
		比如：

		<script type="text/javascript">
		    var oDiv = document.getElementById('div1');
		</script>
				....
		<div id="div1">这是一个div元素</div>

		上面的语句，如果把javascript写在元素的上面，就会出错，
		因为页面上从上往下加载执行的，javascript去页面上获取元素div1的时候，
		元素div1还没有加载，解决方法有两种：
			
		第一种方法：将javascript放到页面最下边：

			....
			<div id="div1">这是一个div元素</div>
			....
			
			<script type="text/javascript">
			var oDiv = document.getElementById('div1');
			</script>
			</body>

		第二种方法：将javascript语句放到window.onload触发的函数里面,
		获取元素的语句会在页面加载完后才执行，就不会出错了。

			<script type="text/javascript">
				window.onload = function(){
				var oDiv = document.getElementById('div1');}
			</script>

			....

			<div id="div1">这是一个div元素</div>""'')
					

	6、操作元素属性：

		获取的页面元素，就可以对页面元素的属性进行操作，属性的操作包括属性的读和写。

		操作属性的方法:

			1、"."操作
			2、"[]"操作

		属性写法：

			html的属性和js里面的属性写法一样
			"class"属性写成"className"
			"style"属性里面的属性，有横杠的改成驼峰式，比如：“font-size”，改成”style.fontSize”

		通过“.”操作属性：

			<script type="text/javascript">
				
				window.onload = function(){

					var oInput = document.getElementById('input1');
					var oA = document.getElementById('link1');
					// 读取属性值
					var val = oInput.value;
					var typ = oInput.type;
					var nam = oInput.name;
					var links = oA.href;
					// 写(设置)属性
					oA.style.color = 'red';
					oA.style.fontSize = val;
				}
			</script>
			......
			<input type="text" name="setsize" id="input1" value="20px">
			<a href="http://www.itcast.cn" id="link1">传智播客</a>

		通过“[ ]”操作属性：

			<script type="text/javascript">
			
			    window.onload = function(){

					var oInput1 = document.getElementById('input1');
					var oInput2 = document.getElementById('input2');
					var oA = document.getElementById('link1');
					// 读取属性
					var val1 = oInput1.value;
					var val2 = oInput2.value;
					// 写(设置)属性
					// oA.style.val1 = val2; 没反应
					oA.style[val1] = val2;        
				}

			</script>
			......
			<input type="text" name="setattr" id="input1" value="fontSize">
			<input type="text" name="setnum" id="input2" value="30px">
			<a href="http://www.itcast.cn" id="link1">传智播客</a>

		innerHTML：

			innerHTML可以读取或者写入标签包裹的内容

			<script type="text/javascript">
				window.onload = function(){

					var oDiv = document.getElementById('div1');
					//读取
					var txt = oDiv.innerHTML;
					alert(txt);
					//写入
					oDiv.innerHTML = '<a href="http://www.itcast.cn">传智播客<a/>';
				}
			</script>
	
			......

			<div id="div1">这是一个div元素</div>

	7、函数：

		函数就是重复执行的代码片。

		函数定义与执行：

			<script type="text/javascript">
			    // 函数定义
				function aa(){
					alert('hello!');
				}
			   // 函数执行
				aa();
			</script>















"------------------------------------------------"

8 JQuery


"-----------------------------------------------"

9 移动端库和框架


"-----------------------------------------------"

10 前端自动化以及优化

"----------------------------------------------"
























