"---------------------------------------------"
	
	本篇是学习 python-web-guide 学习笔记
	书本：https://python-web-guide.readthedocs.io/zh/latest/index.html

"---------------------------------------------"
		
		第一章:    入门基础





"---------------------------------------------"

		第二章:     编码之前碎碎念(工程实践)



"---------------------------------------------"

		第三章:    小白的踩坑记录


"--------------------------------------------"

		第四章:    开发和编程工具

1、vim 工具集成python IDE:

	a. 通过vim --version 命令查看vim版本是否支持python

		debian:~$ vim --version
		VIM - Vi IMproved 7.3 (2010 Aug 15, compiled Feb 10 2013 02:28:47)
		Included patches: 1-547
		Modified by pkg-vim-maintainers@lists.alioth.debian.org
		Compiled by jamessan@debian.org
		Huge version without GUI.  Features included (+) or not (-):
			+arabic +autocmd -balloon_eval -browse ++builtin_terms +byte_offset +cindent 
			-clientserver -clipboard +cmdline_compl +cmdline_hist +cmdline_info +comments 
			+conceal +cryptv +cscope +cursorbind +cursorshape +dialog_con +diff +digraphs 
			-dnd -ebcdic +emacs_tags +eval +ex_extra +extra_search +farsi +file_in_path 
			+find_in_path +float +folding -footer +fork() +gettext -hangul_input +iconv 
			+insert_expand +jumplist +keymap +langmap +libcall +linebreak +lispindent 
			+listcmds +localmap -lua +menu +mksession +modify_fname +mouse -mouseshape 
			+mouse_dec +mouse_gpm -mouse_jsbterm +mouse_netterm -mouse_sysmouse 
			+mouse_xterm +mouse_urxvt +multi_byte +multi_lang -mzscheme +netbeans_intg 
			+path_extra -perl +persistent_undo +postscript +printer +profile -python 
			-python3 +quickfix +reltime +rightleft -ruby +scrollbind +signs +smartindent 
			-sniff +startuptime +statusline -sun_workshop +syntax +tag_binary 
			+tag_old_static -tag_any_white -tcl +terminfo +termresponse +textobjects +title
			-toolbar +user_commands +vertsplit +virtualedit +visual +visualextra +viminfo 
			+vreplace +wildignore +wildmenu +windows +writebackup -X11 -xfontset -xim -xsmp
			-xterm_clipboard -xterm_save 
		    system vimrc file: "$VIM/vimrc"
		      user vimrc file: "$HOME/.vimrc"
		       user exrc file: "$HOME/.exrc"
		   fall-back for $VIM: "/usr/share/vim"
			Compilation: gcc -c -I. -Iproto -DHAVE_CONFIG_H     
			 -g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat 
			 -Werror=format-security -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1      
			 Linking: gcc   -Wl,-z,relro -Wl,--as-needed -o vim       
			 -lm -ltinfo -lnsl  -lselinux -lacl -lattr -lgpm

		你要确保已经满足以下两点要求：
	
			Vim编辑版本应该大于7.3。
			支持Python语言。在所选编辑器的功能中，确保你看到了+python。
		
		debian$vim --version|grep python
			
			+path_extra -perl +persistent_undo +postscript +printer +profile -python 
			-python3 +quickfix +reltime +rightleft -ruby +scrollbind +signs +smartindent

			如果前面是 + 代表支持，- 代表不支持

	b. 重新安装下载最新vim 源码(确保安装get)：

		下载:
			
			git clone https://github.com/vim/vim.git ~/.
			cd  vim
		
		安装依赖包：
			apt-get install python-dev
			apt-get install python3-dev
			apt-get install libncurses5-dev  

		设置配置文件：

			./configure --with-features=huge --enable-python3interp --enable-pythoninterp 
			--with-python-config-dir=/usr/lib/python2.7/config-x86_64-linux-gnu/ 
			--enable-rubyinterp --enable-luainterp --enable-perlinterp 
			--with-python3-config-dir=/usr/lib/python3.5/config-3.5m-x86_64-linux-gnu/ 
			--enable-multibyte --enable-cscope --prefix=/usr/local/vim/

			配置说明:
			--with-features=huge：支持最大特性
			--enable-rubyinterp：打开对ruby编写的插件的支持
			--enable-pythoninterp：打开对python编写的插件的支持
			--enable-python3interp：打开对python3编写的插件的支持
			--enable-luainterp：打开对lua编写的插件的支持
			--enable-perlinterp：打开对perl编写的插件的支持
			--enable-multibyte：打开多字节支持，可以在Vim中输入中文
			--enable-cscope：打开对cscope的支持
			--with-python-config-dir=/usr/lib/python2.7/config-x86_64-linux-gnu/ 指定python 路径
			--with-python-config-dir=/usr/lib/python3.5/config-3.5m-x86_64-linux-gnu/ 指定python3路径
			--prefix=/usr/local/vim：指定将要安装到的路径(自行创建)
		
		安装：

			make
			make install

		设置软件连接：

			ln -s  /usr/local/vim/bin/vim  /usr/bin/vim
		
	c. 查看设置：

		debian:$# vim --version|grep python
		+comments          +libcall           +python/dyn        +viminfo
		+conceal           +linebreak         +python3/dyn       +vreplace

2、配置vimrc:

	vim的所有配置都是在 ~/.vimrc 这个文件中完成。默认是没有的需要自己新建：

		cd ~
		touch .vimrc
		vim .vimrc

	基本配置：

		set shortmess=atI " 启动的时候不显示那个援助乌干达儿童的提示 "
		set lines=40 columns=155 " 设定窗口大小"
		set nu " 显示行号"
		syntax on " 语法高亮"
		syntax enable
		set ruler " 显示标尺"
		set showcmd " 输入的命令显示出来，看的清楚些"
		set statusline=%F%m%r%h%w\ [FORMAT=%{&ff}]\ [TYPE=%Y]\ 
		[POS=%l,%v][%p%%]\ %{strftime(\"%d/%m/%y\ -\ %H:%M\")} "状态行显示的内容"
		
		set guifont=Courier_New:h10:cANSI " 设置字体"
		if version >= 603
		set helplang=cn
		set encoding=utf-8
		endif
				
		colorscheme desert  
		autocmd InsertLeave * se nocul " 用浅色高亮当前行 "
		autocmd InsertEnter * se cul   " 用浅色高亮当前行"
				
		"代码补全 "
		set completeopt=preview,menu 
		" 在处理未保存或只读文件的时候，弹出确认"
		set confirm
		" 自动缩进"
		set autoindent
		set cindent
		" Tab键的宽度"
		set tabstop=4
		" 统一缩进为4"
		set softtabstop=4
		set shiftwidth=4
		" 不要用空格代替制表符"
		set noexpandtab
		" 在行和段开始处使用制表符"
		set smarttab
		" 历史记录数"
		set history=1000
		" 侦测文件类型"
		filetype on
		" 载入文件类型插件"
		filetype plugin on
		" 为特定文件类型载入相关缩进文件"
		filetype indent on
		"保存全局变量"
		set viminfo+=!
		" 带有如下符号的单词不要被换行分割"
		set iskeyword+=_,$,@,%,#,-
		" 字符间插入的像素行数目"
		set linespace=0
		" 增强模式中的命令行自动完成操作"
		set wildmenu
		" 使回格键（backspace）正常处理indent, eol, start等"
		set backspace=2
		" 允许backspace和光标键跨越行边界"
		set whichwrap+=<,>,h,l
		" 可以在buffer的任何地方使用鼠标（类似office中在工作区双击鼠标定位）"
		set mouse=a
		set selection=exclusive
		set selectmode=mouse,key
		" 通过使用: commands命令，告诉我们文件的哪一行被改变过"
		set report=0
		" 在被分割的窗口间显示空白，便于阅读"
		set fillchars=vert:\ ,stl:\ ,stlnc:\
		" 高亮显示匹配的括号"
		 set showmatch
		" 匹配括号高亮的时间（单位是十分之一秒）"
		set matchtime=1
		" 光标移动到buffer的顶部和底部时保持3行距离"
		set scrolloff=3
		" 为C程序提供自动缩进"
		set smartindent

		"自动补全"
		:inoremap ( ()<ESC>i
		:inoremap ) <c-r>=ClosePair(')')<CR>
		:inoremap {{<CR>}<ESC>O
		:inoremap } <c-r>=ClosePair('}')<CR>
		:inoremap [ []<ESC>i
		:inoremap ] <c-r>=ClosePair(']')<CR>
		:inoremap " ""<ESC>i                      //"""
		:inoremap ' ''<ESC>i                      //'''
		function! ClosePair(char)
		if getline('.')[col('.') - 1] == a:char
		return "\<Right>"
		else
		return a:char
		endif
		endfunction
		filetype plugin indent on 
		"打开文件类型检测, 加了这句才可以用智能补全"
		set completeopt=longest,menu
		set cursorline 

	配置插件:

		vim插件中最主要的就是vundle了，vundle用来管理vim的其它插件.

		1、Vundle:

			Vundle 是 Vim bundle 的简称,使用git来管理vim插件，有了它，安装其它插件就方便很多。

			项目地址https://github.com/VundleVim/Vundle.vim。

			首先下载源码：
				git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

			如果~/.vim/bundle目录不存在，则新建目录：
				
				cd ~
				mkdir .vim
				cd .vim
				mkdir bundle
			
			然后将下列配置放在.vimrc文件的开头：

				set nocompatible              " be iMproved, required"
				filetype off                  " required"
				 
				" set the runtime path to include Vundle and initialize"
				set rtp+=~/.vim/bundle/Vundle.vim
				call vundle#begin()
	 
				" let Vundle manage Vundle, required"
				Plugin 'VundleVim/Vundle.vim'
	 
				" All of your Plugins must be added before the following line"
				call vundle#end()            " required "
				filetype plugin indent on    " required "


			如果想下载某个插件，比如自动缩进indentpython.vim插件，需要将:
				Plugin 'vim-scripts/indentpython.vim'

			置于call vundle#begin()和call vundle#end()之间，保存配置后在vim中执行
				:PluginInstall

			即可以自动下载indentpython.vim插件了。
			当看到命令行出现Done!就代表所有插件安装完成啦！

			bundle可以管理下载几种不同的插件,方式如下：
				github上的插件
				Plugin 'tpope/vim-fugitive'
				来自于http://vim-scripts.org/vim/scripts.html的插件
				Plugin 'L9'
				非github上的git插件
				Plugin 'git://git.wincent.com/command-t.git'
				本地插件
				Plugin 'file:///home/gmarik/path/to/plugin'
				" The sparkup vim script is in a subdirectory of this repo called vim."
				" Pass the path to set the runtimepath properly. "
				" Plugin 'rstacruz/sparkup', {'rtp': 'vim/'} "
				有旧插件的情况下，下载新的插件并重命名以避免冲突
				Plugin 'ascenator/L9', {'name': 'newL9'}

			其它常用的命令：

				:PluginList       - lists configured plugins
				:PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
				:PluginSearch foo - searches for foo; append `!` to refresh local cache
				:PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal

			所有通过Vundle 下载的插件都会下载到：~/.vim/bundle 目录下。

		2、YouCompleteMe：

			非常好用的自动补全插件，就是比较重。
			官网地址：http://valloric.github.io/YouCompleteMe/
			github地址：https://github.com/Valloric/YouCompleteMe
			YouCompleteMe安装后还需要手动编译，然后再在.vimrc中配置。
			
			在debian、ubuntu中使用，首先准备一些工具：

				sudo apt-get install build-essential cmake

			使用vundle安装：

				在.vimrc中添加配置，:PluginInstall 命令进行下载
					Plugin 'Valloric/YouCompleteMe'
				
				在下载完成之后：
					cd ~/.vim/bundle/YouCompleteMe
					./install.py --clang-completer
					参数 --clang-completer是为了加上C系列语言的自动补全，也可以不加：

				复制一下默认配置文件到用户主目录：
					cp third_party/ycmd/examples/.ycm_extra_conf.py ~/
	
				
			在.vimrc中进行一下配置：
				
				let g:ycm_min_num_of_chars_for_completion = 2  "开始补全的字符数"
				let g:ycm_python_binary_path = 'python'  "jedi模块所在python解释器路径"
				let g:ycm_seed_identifiers_with_syntax = 1  "开启使用语言的一些关键字查询"
				let g:ycm_autoclose_preview_window_after_completion=1 "补全后自动关闭预览窗口"

			代码跳转：

				nnoremap <leader>jd :YcmCompleter GoToDefinitionElseDeclaration<CR>

			开关YCM：

				let g:ycm_auto_trigger = 0   "turn off"
				let g:ycm_auto_trigger = 1   "turn on"

		3、支持vim8的补全插件:

			YouCompleteMe实际上是使用jedi-vim来补全python代码的，
			如果觉得YCM实在太重，可以使用支持vim8的maralla/completor.vim来补全代码：
		
			下载：
			
				Plugin 'maralla/completor.vim'
			
			下载jedi： 
				
				pip install jedi
			
			配置：

				let g:completor_python_binary = '/path/to/python/with/jedi/installed'

			设置起来比YCM简单很多了。

		4、自动缩进插件:

			写python代码，自动缩进是必须的，可以使用indentpython.vim插件：

				Plugin 'vim-scripts/indentpython.vim'

		5、语法检查:

			安装syntastic插件，每次保存文件时Vim都会检查代码的语法：
			
				Plugin 'vim-syntastic/syntastic'

			添加flake8代码风格检查：
				
				Plugin 'nvie/vim-flake8'

		6、配色方案:

			solarized配色方案已经流行很久了，github地址https://github.com/altercation/vim-colors-solarized。

			手动下载：

				$ cd ~/.vim/bundle
				$ git clone git://github.com/altercation/vim-colors-solarized.git
				$ mv vim-colors-solarized ~/.vim/bundle/

			或者vundle下载：
				Plugin 'altercation/vim-colors-solarized'

			solarized有dark和light两种配色，配置：

				syntax enable
				set background=light or dark
				colorscheme solarized

			也可以根据gui模式和终端模式进行切换：

				if has('gui_running')
				    set background=light
				else
					set background=dark
				endif

		7、nerdtree:

			给vim添加一个树形目录，地址https://github.com/scrooloose/nerdtree。

			下载：

				Plugin 'scrooloose/nerdtree'
			
			添加开关树形目录的快捷键：

				map <C-n> :NERDTreeToggle<CR>

				Ctrl+n就可以开启目录了。

			设置忽略.pyc文件：

				let NERDTreeIgnore=['\~$', '\.pyc$', '\.swp$']

			为nerdtree添加git支持：

				Plugin 'Xuyuanp/nerdtree-git-plugin'

			如果你想用tab键：

				Plugin 'jistr/vim-nerdtree-tabs'

		8、indentLine:

			缩进指示线，地址https://github.com/Yggdroot/indentLine。

			安装：
				Plugin 'Yggdroot/indentLine'
			
				设置：

					let g:indentLine_char='┆'
					let g:indentLine_enabled = 1

			python是靠代码缩进来判断代码块的，缩进指示线还是很方便的。

		9、vim-autopep8:

			自动格式化工具，安装后运行:Autopep8就可以自动依照pep8的标准自动格式化代码。

			地址https://github.com/Yggdroot/indentLine。

			首先安装autopep8：

				$ pip install autopep8
				Plugin 'tell-k/vim-autopep8'

			可以设置快捷键F8代替:Autopep8：

				autocmd FileType python noremap <buffer> <F8> :call Autopep8()<CR>

		10、auto-pairs:

			自动补全括号和引号等，地址https://github.com/jiangmiao/auto-pairs。

			Plugin 'jiangmiao/auto-pairs'

		11、ctrlp.vim:

			搜索插件，在vim normal模式下，按下ctrl+p，然后输入你要寻找的文件就行了。
			地址https://github.com/kien/ctrlp.vim。
			Plugin 'kien/ctrlp.vim'

		12、ag.vim:

			搜索引擎使用了the_silver_searcher

				apt-get install silversearcher-ag
				or
				brew install the_silver_searcher
			
			插件
				Plugin 'rking/ag.vim'
	
			使用
				:Ag [options] {pattern} [{directory}]

		13、vim-fugitive：

			git集成插件，可以在vim中运行git命令，https://github.com/tpope/vim-fugitive。

			Plugin 'tpope/vim-fugitive'	
    
    
"--------------------------------------------"

            第五章  Write Idiom Python 
    
"""Python 支持链式比较"""

    # bad
    a = 5
    
    if a > 1 and a < 7:
        pass
    # good
    
    if 1 < a < 7:
        pass
    

"""Python 交换变量"""

    # bad
    
    x = 10
    y = 5
    temp = x
    x = y
    y = temp
    
    # good
    x = 10
    y = 5
    x, y = y, 5

"""Python 中替代三目运算符"""

    # bad
    
    a = 10
    b = 5
    if a > b:
        c = a
    else:
        c = b
    
    # good
    
    c = a if a > b else b


"""拼接字符列表时，用join方法实现"""


"""格式化字符时多使用format函数"""

    # bad

    name = "tony"
    age = 100
    
    str = "my name : " + name + "my age :" + str(age)
    
    str1 = "my name : %s my age :%d" % (name, age)
    
    # good
    
    str2 = "my name :{} my age:{}".format(name, age)

"""使用列表或者字典comprehension"""

    # bad
    
    mylist = range(20)
    odd_list = []
    for e in mylist:
        if e % 2 == 1:
            odd_list.append(e)
    
    # good
    
    ood_list = [e for e in mylist if e % 2 == 1]

    # bad
    
    user_list = [{'name': 'lucy', 'email': "lucy@tom.com"}, {'name': "lily", 'email': 'llily@tom.com'}]
    user_email = {}
    for user in user_list:
        if 'email' in user:
            user_email[user['name']] = user['email']
            # {'lucy': 'lucy@tom.com', 'lily': 'llily@tom.com'}
    
    # good
    
    {user['name']: user['email'] for user in user_list if 'email' in user}


"""条件判断时，避免直接和True、False、None 进行比较（==）"""

    # bad
    
    if == []:
        pass
     
    # good
    
    if 1:
        pass
        
    # bad
    
    if something == None:
    
    # good, None 是单例对象
    
    if something is None:
    
"""使用 enumerate 代表 for 循环中的 index 变量访问"""

    # bad
    
    my_container = ['lily', 'lucy', 'tom']
    
    index = 0
    
    for element in my_container:
        print '{} {}'.format(index,element)
        index += 1
        
    # good
    
    for index, element in enumerate(my_container):
        print "%d %s" % (index, element)
        
""避免使用可变（mutable）变量作为函数参数的默认初始化值""""

    # bad
    
    def function(l = []):
        l.append(1)
        return l
        
    print(function())
    print(function())
    print(function())
    
    # print
    
    [1]
    [1, 1]
    [1, 1, 1]
    
    #good, 使用None作为可变对象的占位符
    
    def function(l = None):
        if l is None:
            l = []
        l.append()
        return l
        
"""一切皆对象"""
    
    # bad
    
    def print_addition_table():
        for x in range(1, 3):
            for y in range(1, 3):
                print(str(x + y) + '\n')
                
    def print_subtraction_table():
        for x in range(1, 3):
            for y in range(1, 3):
                print(str(x - y) + '\n')
                
    def print_multiplication_table():
        for x in range(1, 3):
            for y in range(1, 3):
                print(str(x * y) + '\n')

    def print_division_table():
        for x in range(1, 3):
            for y in range(1, 3):
                print(str(x / y) + '\n')
    
    print_additon_table()
    print_subtraction_table()
    print_multiplication_table()
    print_division_table()
    
    # good, python 一切皆是对象，可以函数作为参数，类似技巧可以简化代码
    
    import operator as op
    
    def print_table(operator):
        for x in range(1, 3):
            for y in range(1, 3):
                print(str(operator(x, y)) + '\n')
    
    for operator in (op.add, op.sub, op.mul, op.div):
        print_table(operator)
        
        
    # operator模块:
        
        operator模块是python中内置的操作符函数接口, 它定义了一些算术和比较内置操作的
        函数，operator模块是用c实现的，所以执行起来比Python代码快。
        
        比较操作符:
            
           from operator import *
            a = 1
            b = 5
            for func in (lt, le, eq, ne, ge, gt):
                print func(a,b)
                
            lt  <
            le  <=
            eq  ==
            ne  !=
            ge  >=
            gt  >
       
        算术操作:
            add   +
            sub   -
            mul   *
            div   /
            floordiv  整除除法
            pow   指数
            truediv(a,b) 浮点数除法
                               
        位操作： 
            
            and_  按位与
            or_(c,d) 按位或
            xor(c,d) 异或
            invert 取反
            lshift(c,d) 左移位
            rshift(d,c) 右移位
                   
"""防御式编程 EAFP vs LBYL"""

    EAFP : easier to ask forgiveness than permission
    EAFP : 可以理解成一切按正常的逻辑编码，不用管可能出现错误，等出了错误再说。
    
    LBYL : look before you leap
    LBYL : 就是尽可能每写一行代码，都要提前考虑下当前的前置条件是否成立。
    
    # LBYL
    def getPersonInfo(person):
        if person == None:
            print("person must be not null")
        pirnt(person.info)

    # EAFP
    
    def getPersonInfo(person):
        try:
            print(person.info)
        except NameErrorL
            print("person must be not null!")
    
    其实用EAFP风格的代码最大的好处是代码逻辑清晰，
    而LBYL会导致本来两句话说清楚的事，往往因为穿插了很多条件检查的语句使代码逻辑变得混乱。
    Python社区更提倡EAFP形式的。另外还有一个原因，在高并发场景下， 
    if条件如果是个表达式，会造成一致性问题，这个时候必须用EAFP形式。
    
"""用dict 对象完成 switch...case... 的功能"""

    # bad
    
    def apply_operation(left_operand, right_operand, operator):
        if operator == '+':
            return left_operand + right_operand
        elif operator == '-':
            return left_operand - right_operand
        elif operator == '*':
            return left_operand * right_operand
        elif operator == '/':
            return left_operand / right_operand
    
    # good
    
    def apply_operation(left_operand, right_operand, operator):
        import operator as op
        operator_mapper = {'+': op.add, '-': op.sub, '*': op.mil, '/': op.truediv}
        return operator_mapper[operator](left_operand, right_operand)
             
"""访问tuple的数据项时，可以用 namedtuple 代替 index 的方式访问"""

    # bad 
    
    rows = [('lily', 20, 2000), ('lucy', 19, 2500)]
    for row in rows:
        print('{1} age is {2}, salary is {3} ').format(row[0], row[1], row[2])
        
    # good
    
    from collections import namedtuple
    Employee = namedtuple('Employee', 'name, age, salary')
    for row in rows:
        employee = Employee._make(row)
        print('{1} age is {2}, salary is {3} ').format(employee.name, employee.age, employee.salary)
    
    # collections.nametuple:
        
        namedtuple是继承自tuple的子类。
        namedtuple创建一个和tuple类似的对象，而且对象拥有可访问的属性。
        
        看下面列子:
        
            form collections import namedtuple
           
            # 定义一个namedtuple类型 User, 并包含name, sex 和 age 属性
            User = namedtuple('User',['name', 'sex', 'age'])
            
            # 创建一个User 对象
            user = User(name = 'kongxx', 'male', 21)
            
            # 也可以通过一个list创建一个User对象，这里注意需要使用"_make"方法
            user = User._make(['kongxx', 'male', 21])
         
            # 获取用户的属性
            print(user.name)
            print(user.sex)
            print(user.age)

            # 修改对象属性，注意要使用"_replace"方法
            user = user._replace(age=22)
            print(user)
            # User(name='user1', sex='male', age=21)

            # 将User对象转换成字典，注意要使用"_asdict"
            print(user._asdict())
            # OrderedDict([('name', 'kongxx'), ('sex', 'male'), ('age', 22)])

"""用 isinstance 来判断对象的类型 """
 
    因为在python中定义变量时，不用像其他静态语言，如java, 要指定其变量数据类型。
    但这并不意味着python中没有数据类型，每个对象有不同的数据类型，一个变量只有
    在运行的时候根据引用的对象，才会确定其数据类型。
    比如，下面代码计算一个对象的长度值，如果是序列数据类型（str, list, dcit, set）
    直接调用len方法，如果是True, False, None 则返回1， 如果是数值的，则返回int值。
    
    # bad
    
    def get_size(some_object):
        try:
            return len(some_object)
        except TypeError:
            if some_object in (True, False, None):
                return 1
        else:
            return int(some_object)
            
    # good
    
    def get_size(some_object):
        if isinstance(some_object,(list, dict, str, tuple)):
            return len(some_object)
        elif isinstance(some_object, (bool, type(None))):
            return 1
        elif isinstance(some_object, (int, float)):
            return int(some_object)

"""用 with 管理操作资源的上下文环境"""
    
    在一个比较典型的场景中， 如数据库操作， 我们操作connection 时一般要正常
    关闭连接，而不管是正常退出还是异常退出。如下：
    
    # bad
  
    class Connection(object):
    def execute(self, sql):
        raise Exception('ohoh, exception!')
        
    def close(self):
        print('closed the Connection')
        
    try:
        conn = Connection() 
        conn.execute('select *from t_users')    
    finally:
        conn.close()
        
    # good
    
    class Connection(object):
    def execute(self, sql):
        raise Exception('ohoh, exception!')
    def close(self):
        print('closed the Connection')
    def __enter__(self):
        return self
    def __exit__(self, errorType, errorValue, error):
        self.close()
    
    with Connection() as conn:
        conn.excute('select *from t_users') 
        
        
"""使用 generator 返回耗费内存的对象"""       

    # bad
    
    def f():
        # ...
        return biglist
    
    # good
    
    def f():
        # ...
        for i in biglist:
            yield i
       
                        
""" 30个python小技巧 """

    1、拆箱
        
        >>> a, b, c = 1, 2, 3
        >>> a, b, c
        (1, 2, 3)
        
        >>> a, b, c = (2*i + 1 for i in range(3))
        >>> a, b, c
        (1, 3, 5)
        
        >>> a, (b, c), d = [1, (2, 3), 4]
        >>> a, b, c, d
        (1, 2, 3, 4)
    
    2、拆箱变量交换
        
        >>> a, b = 1, 2
        >>> a, b = b, a
        >>> a, b 
        (2, 1)
     
    3、 扩展拆箱(只兼容python3)
    
        >>> a, *b, c = [1, 2, 3, 4]
        >>> a
        1
        >>> b
        [2, 3, 4]
        >>> c
        5
        
    5、 负数索引
    
        >>> a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        >>> a[-1]
        10
        >>> a[-11]
        0
    
    6、切割列表
        
        >>> a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        >>> a[2:8]
        [2, 3, 4, 5, 6, 7]
        
    7、负数索引切割列表
    
        >>> a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        >>> a[-4:-2]
        [7, 8]
        >>> a[-4:-1]
        [7, 8, 9]
        
        >>> a[-4:-2:-1]
        []
        >>> a[-4:-7:-1]
        [7, 6, 5]
        
        >>> a[-4:2:-1]
        [7, 6, 5, 4, 3]
        
        >>> a[-4:-8:-2]
        [7, 5]
    
    8、 列表切割赋值
    
        >>> a = [1, 2, 3, 4, 5] 
        >>> a[2:3] = [0, 0]
        [1, 2, 0, 0, 4, 5]
        
        >>> a[1:1] = [8, 9]
        >>> a
        [1, 8, 9, 2, 0, 0, 4, 5]
        
        >>> a[1:-1] = []
        [1, 5]
    
    9、命名列表切割方式
        
        Python slice() 函数:
            
            描述：
                 slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。
            语法:
                slice 语法：
                class slice(stop)
                class slice(start, stop[, step])
                参数说明：
                start -- 起始位置
                stop -- 结束位置
                step -- 间距
            
            返回值：
                
                返回一个切片对象。
             
            例子：
                
                >>>myslice = slice(5)    # 设置截取5个元素的切片
                >>> myslice
                slice(None, 5, None)
                >>> arr = range(10)
                >>> arr
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                >>> arr[myslice]         # 截取 5 个元素
                [0, 1, 2, 3, 4]
                   
        
    
        >>> a = [0, 1, 2, 3, 4, 5]
        >>> LASTTHREE = slice(-3, None) 
        slice(-3, None, None)
        >>> a[slice]
        [3, 4, 5]
     
    10、 列表以及迭代器的压缩和解压缩
    
        python zip()函数：
        
            描述：
            
            zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
            然后返回由这些元组组成的列表。
            
            如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，
            利用 * 号操作符，可以将元组解压为列表。   
            
            语法：
            
                zip 语法：
                zip([iterable, ...])
                参数说明：
                iterabl -- 一个或多个迭代器;
                返回值
                返回元组列表。
            
            实例：
                以下实例展示了 zip 的使用方法：
                >>>a = [1,2,3]
                >>> b = [4,5,6]
                >>> c = [4,5,6,7,8]
                >>> zipped = zip(a,b)     # 打包为元组的列表
                [(1, 4), (2, 5), (3, 6)]
                >>> zip(a,c)              # 元素个数与最短的列表一致
                [(1, 4), (2, 5), (3, 6)]
            
                >>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
                [(1, 2, 3), (4, 5, 6)]    
                
    
        >>> a = [1, 2, 3]
        >>> b = ['a', 'b', 'c']
        >>> z = zip(a, b)
        >>> z
        [(1, 'a'), (2, 'b'), (3, 'c')]
        
        >>> zip(*z)
        [(1, 2, 3),('a', 'b', 'c')]
        
    11、列表相邻元素压缩器
    
        >>> a = [1, 2, 3, 4, 5, 6]
        >>> zip(*([iter(a)] * 2))
        [(1, 2), (3, 4), (5, 6)]
        
        >>> group_adjacent = lambda a, k : zip(*([iter(a)] * k))
        >>> group_adjacent(a, 3)
        [(1, 2, 3), (4, 5, 6)]
        
        >>> group_adjacent(a, 2)
        [(1, 2), (3, 4), (5, 6)]
        
        >>> group_adjacent(a, 1)    
        [(1,), (2,), (3,), (4,), (5,), (6,)]
        
        >>> group_adjacent(a, 6)
        [(1, 2, 3, 4, 5, 6)]
        
           
        >>> a[::2]
        [1, 3, 5]
        >>> a[1::2]
        [2, 4, 6]
        >>> zip(a[::2],[1::2])
        [(1, 2), (3, 4), (5, 6)]
        
        >>> zip(a[::3], a[1::3], a[2::3])
        [(1, 2, 3), (4, 5, 6)]
        
        
        >>> group_adjacent = lambda a, k : zip(*(a[i:k] for i in range(k)))
        >>> group_adjacent(a, 3)
        [(1, 2, 3), (4, 5, 6)]
        >>> group_adjacent(a, 2)
        [(1, 2), (3, 4), (5, 6)]
        
        >>> list(a[i::1] for i in range(1))
        [[1, 2, 3, 4, 5, 6]]
        >>> group_adjacent(a, 1)
        [(1,), (2,), (3,), (4,), (5,), (6,)]
        
        >>> list(a[i::6] for i in range(6)) 
        [[1], [2], [3], [4], [5], [6]]
        >>> group_adjacent(a, 6)
        [(1, 2, 3, 4, 5, 6)]
        
        
    12、在列表中用压缩器和迭代器滑动取值窗口
    
        >>> def n_grams(a, n):
                z = [iter(a[i:]) for i in range(n)]
                return zip(*z)
        
        >>> a[0:]
        [1, 2, 3, 4, 5, 6]
        >>> a[1:]
        [2, 3, 4, 5, 6]
        >>> a[2:]
        [3, 4, 5, 6]
        >>> a[3:]
        [4, 5, 6]
    
        >>> a = [1, 2, 3, 4, 5, 6]
        >>> n_grams(a, 3)
        [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
        
        >>> n_grams(a, 2)
        [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
        
        >>> n_grams(a, 4)
        [(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)]
        
        
    13、用压缩器反转字典:
    
        >>> m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        >>> m.items()
        [('a', 1), ('c', 3), ('b', 2), ('d', 4)]
        >>> m.keys()
        ['a', 'c', 'b', 'd']
        >>> m.values()
        [1, 3, 2, 4]
        
        >>> zip(m.values(), m.keys())
        [(1, 'a'), (3, 'c'), (2, 'b'), (4, 'd')]
        >>> dict(zip(m.values(), m.keys()))
        {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    
    14、列表展开:
    
        >>> a = [[1, 2], [3, 4], [5, 6]]
        >>> import itertools
        >>> list(itertools.chain.from_iterable(a))
        
        >>> sum(a, [])
        [1, 2, 3, 4, 5, 6]
        
        
        >>> [l for l in a]
        [[1, 2], [3, 4], [5, 6]]
        >>> [x for l in a for x in l]
        [1, 2, 3, 4, 5, 6]
        
        >>> a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
        >>> [x for l1 in a for l2 in l1 for x in l2]
        [1, 2, 3, 4, 5, 6, 7, 8]
        
        >>> a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
        >>> flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
        >>> flatten(a)
        [1, 2, 3, 4, 5, 6, 7, 8]
    
    15、生成器表达式:
        
        >>> g = (x ** 2 for x in range(10))
        >>> next(g)
        0
        >>> next(g)
        1
        >>> next(g)
        4
        >>> next(g)
        9
        
        >>> sum(x ** 3 for x in range(10))
        2025
        >>> sum(x ** 3 for x in xrange(10) if x % 3 == 1)
        408
    
    16、字典推导:
        
        >>> m = {x: x ** 2 for x in range(5)}
        >>> m
        {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
        
        >>> m = {x: 'A' + str(x) for x in range(10)}
        {0: 'A0', 1: 'A1', 2: 'A2', 3: 'A3', 4: 'A4', 5: 'A5', 6: 'A6', 7: 'A7', 8: 'A8', 9: 'A9'}
        
    17、用字典推导反转字典:
    
        >>> m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        >>> {v: k for k, v in m.items()}
        {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
        
    18、命名元组:
        
        import collections
        >>> Point = collections.namedtuple('Point', ['x', 'y'])
        >>> p = Point(x = 1.0, y = 2.0)
        >>> p.x
        1.0
        >>> p.y
        2.0
        
    19、继承命名元组:
        
        >>> class Point(collections.namedtuple('PointBase', ['x', 'y'])):
            __slots__ = ()
            def __add__(self, other):
                return Point(x = self.x + other.x , y = self.y + other.y)
        
        >>> p = Point(x = 1.0, y = 2.0)
        >>> q = Point(x = 2.0, y = 3.0)
        >>> p + q
        PointBase(x=3.0, y=5.0)
        
        
    20、操作集合：
        
        >>> A = {1, 2, 3, 3}
        >>> A
        set([1, 2, 3, 4])
        
        >>> B = {3, 4, 5, 6, 7}
        >>> B
        set([3, 4, 5, 6, 7])
        
        >>> A = {1, 2, 3, 4}

        >>> A | B
        set([1, 2, 3, 4, 5, 6, 7])
        >>> 
        >>> A & B
        set([3, 4])
        >>> 
        >>> A - B
        set([1, 2])
        >>> 
        >>> B - A
        set([5, 6, 7])
        >>> 
        >>> A ^ B
        set([1, 2, 5, 6, 7])
        >>> 
        >>> 
        >>> (A ^ B) == ((A - B) | (B - A))
        True
    
    
    21、操作多重集合:
        
        >>> A = collections.Counter([1, 2, 2])
        >>> B = collections.Counter([2, 2, 3])
        >>> 
        >>> A
        Counter({2: 2, 1: 1})
        >>> B
        Counter({2: 2, 3: 1})
        >>> 
        >>> A | B
        Counter({2: 2, 1: 1, 3: 1})
        >>> 
        >>> A & B
        Counter({2: 2})
        >>> 
        >>> 
        >>> A + B
        Counter({2: 4, 1: 1, 3: 1})
        >>> A - B
        Counter({1: 1})
    
    22、 统计在可迭代器中最常出现的元素:
        
        collections模块自Python 2.4版本开始被引入，包含了dict、set、list、tuple以外的一些特殊的容器类型，
        分别是：
            OrderedDict类：排序字典，是字典的子类。引入自2.7。
            namedtuple()函数：命名元组，是一个工厂函数。引入自2.6。
            Counter类：为hashable对象计数，是字典的子类。引入自2.7。
            deque：双向队列。引入自2.4。
            defaultdict：使用工厂函数创建字典，使不用考虑缺失的字典键。引入自2.5。
        
            Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，
            其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。
            
            Counter类的创建:
                >>> c = Counter()  # 创建一个空的Counter类
                >>> c = Counter('gallahad')  # 从一个可iterable对象（list、tuple、dict、字符串等）创建
                >>> c = Counter({'a': 4, 'b': 2})  # 从一个字典对象创建
                >>> c = Counter(a=4, b=2)  # 从一组键值对创建
            
            计数值的访问与缺失的键:
                当所访问的键不存在时，返回0，而不是KeyError；否则返回它的计数。    
                    >>> c = Counter("abcdefgab")
                    >>> c["a"]
                    2
                    >>> c["c"]
                    1
                    >>> c["h"]
                    0

        >>> A = collections.Counter([1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7])
        >>> A
        Counter({3: 4, 1: 2, 2: 2, 4: 1, 5: 1, 6: 1, 7: 1})
        >>> A.most_common(1)
        [(3, 4)]
        >>> A.most_common(3)
        [(3, 4), (1, 2), (2, 2)]        
    
    23、两端都可操作的队列:
    
        >>> Q = collections.deque()
        >>> Q.append(1)
        >>> Q.append(1)
        >>> Q
        deque([1])    
        >>> Q.appendleft(2)
        >>> Q
        deque([2, 1])
        >>> 
        >>> Q.extend([3, 4])
        >>> Q
        deque([2, 1, 3, 4])
        >>> 
        >>> Q.extendleft([5, 6])
        >>> Q
        deque([6, 5, 2, 1, 3, 4])
        >>> 
        >>> Q.pop()
        4
        >>> Q.popleft()
        6
        >>> 
        >>> Q.popleft()
        5
        
        # rotate(n), 向左移动n位
        >>> Q
        deque([3, 2, 1])
        >>> Q.rotate(2)
        >>> Q
        deque([2, 1, 3])
        >>> Q.rotate(1)
        >>> Q
        deque([3, 2, 1])
        >>> Q.rotate(2)
        >>> Q
        deque([2, 1, 3])
          
        # - 往右移动
        >>> Q.rotate(-3)
        >>> Q
        deque([2, 1, 3])
        >>> Q.rotate(-1)
        >>> Q
        deque([1, 3, 2])
    
    24、有最大长度的双端队列:
    
        >>> last_three = collections.deque(maxlen = 3)
        >>> for i in range(10):
        ...     last_three.append(i)
        ...     print ', '.join(str(x) for x in last_three)
        ... 
        0
        0, 1
        0, 1, 2
        1, 2, 3
        2, 3, 4
        3, 4, 5
        4, 5, 6
        5, 6, 7
        6, 7, 8
        7, 8, 9
    
    25、可排序词典:
    
        >>> m = dict((str(x),x) for x in range(10))
        {'1': 1, '0': 0, '3': 3, '2': 2, '5': 5, '4': 4, '7': 7, '6': 6, '9': 9, '8': 8}
        >>> print ', '.join(m.keys())
        1, 0, 3, 2, 5, 4, 7, 6, 9, 8
        >>> m = collections.OrderedDict((str(x), x) for x in range(10))
        >>> m
        OrderedDict([('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9)])
        >>> 
        >>> print ', '.join(m.keys())
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        >>> 
        >>> m = collections.OrderedDict((str(x), x) for x in range(10, 0, -1))
        >>> m
        OrderedDict([('10', 10), ('9', 9), ('8', 8), ('7', 7), ('6', 6), ('5', 5), ('4', 4), ('3', 3), ('2', 2), ('1', 1)])
        >>> print ', '.join(m.keys())                               
        10, 9, 8, 7, 6, 5, 4, 3, 2, 1
        
    26、默认词典：

        >>> m = dict()
        >>> m['a']
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        KeyError: 'a'
        >>> 
        >>> m = collections.defaultdict(int)
        >>> m['a']
        0
        >>> m['b']
        0
        >>> 
        >>> m = collections.defaultdict(str)
        >>> m['a']
        ''
        >>> 
        >>> m['b'] += 'a'
        >>> 
        >>> m['a']
        ''
        >>> 
        >>> m['b']
        'a'
        >>> 
        >>> m = collections.defaultdict(lambda: '[default value]') 
        >>> m['a']
        '[default value]'
        >>> 
        >>> m['b']
        '[default value]'
    
    27、默认字典的简单树状表达:
    
        >>> import json
        >>> tree = lambda: collections.defaultdict(tree)
        >>> root = tree()
        >>> root['menu']['id'] = 'file'
        >>> root['menu']['value'] = 'File'
        >>> root['menu']['menuitems']['new']['value'] = 'New'
        >>> root['menu']['menuitems']['new']['onclick'] = 'new();'
        >>> root['menu']['menuitems']['open']['value'] = 'Open'
        >>> root['menu']['menuitems']['open']['onclick'] = 'open();'
        >>> root['menu']['menuitems']['close']['value'] = 'Close'
        >>> root['menu']['menuitems']['close']['onclick'] = 'close();'
        >>> print json.dumps(root, sort_keys=True, indent=4, separators=(',', ': '))
        {
            "menu": {
                "id": "file",
                "menuitems": {
                    "close": {
                        "onclick": "close();",
                        "value": "Close"
                    },
                    "new": {
                        "onclick": "new();",
                        "value": "New"
                    },
                    "open": {
                        "onclick": "open();",
                        "value": "Open"
                    }
                },
                "value": "File"
            }
        }           
    
    28、对象到唯一计数的映射:
    
        >>> import itertools, collections
        >>> value_to_numeric_map = collections.defaultdict(itertools.count().next)
        >>> value_to_numeric_map['a'] 
        0
        >>> value_to_numeric_map['b']
        1
        >>> value_to_numeric_map['c']
        2
        >>> value_to_numeric_map['d']
        3
        >>> value_to_numeric_map['e']
        4
        >>> value_to_numeric_map['h']
        5
        >>> value_to_numeric_map['e']
        4
    
    29、最大和最小的几个列表元素：
        
        xrange() 函数用法与 range 完全相同，所不同的是生成的不是一个数组，而是一个生成器。
        
        
        >>> import random
        >>> import heapq
        >>> a = [random.randint(0, 100) for __ in xrange(100)]
        >>> a
        [20, 66, 47, 33, 86, 100, 99, 35, 3, 55, 44, 47, 49, 81, 42, 100, 70, 47, 52, 51, 
        5, 15, 33, 63, 78, 97, 7, 19, 69, 53, 65, 18, 16, 95, 86, 2, 79, 26, 33, 25, 18, 
        2, 20, 26, 84, 48, 72, 15, 18, 93, 21, 11, 40, 2, 82, 79, 28, 41, 60, 44, 23, 
        24, 97, 50, 59, 70, 21, 36, 3, 77, 0, 52, 77, 13, 16, 47, 18, 65, 54, 90, 31, 
        49, 6, 81, 99, 57, 5, 22, 94, 83, 48, 72, 56, 86, 26, 1, 40, 62, 18, 11]
        
        这个模块(build-in)实现了一个堆的数据结构，完美的解决了Top-K问题(前几名问题)，
        以后解决Top-K问题的时候，直接把这个模块拿来用就可以了
        注意，默认的heap是一个小顶堆！
        
        heapq.heappush(heap, item) 把item添加到heap中（heap是一个列表）
        heapq.heappop(heap) 把堆顶元素弹出，返回的就是堆顶
        heapq.heappushpop(heap, item) 先把item加入到堆中，然后再pop，比heappush()再heappop()要快得多
        heapq.heapreplace(heap, item) 先pop，然后再把item加入到堆中，比heappop()再heappush()要快得多
        heapq.heapify(x) 将列表x进行堆调整，默认的是小顶堆
        heapq.merge(*iterables) 将多个列表合并，并进行堆调整，返回的是合并后的列表的迭代器
        heapq.nlargest(n, iterable, key=None) 返回最大的n个元素（Top-K问题）
        heapq.nsmallest(n, iterable, key=None) 返回最小的n个元素（Top-K问题）

        >>> heapq.nsmallest(5, a) 
        [0, 1, 2, 2, 2]
        >>> 
        >>> 
        >>> heapq.nlargest(5, a)
        [100, 100, 99, 99, 97]
        
    30、 两个列表的笛卡尔积:
    
        >>> import itertools
        >>> for p in itertools.product([1, 2, 3], [4, 5]):
        ...     print(p)
        ... 
        (1, 4)
        (1, 5)
        (2, 4)
        (2, 5)
        (3, 4)
        (3, 5)
        >>> 
        >>> for p in itertools.product([0, 1], repeat=4):
        ...     print ''.join(str(x) for x in p)
        ... 
        0000
        0001
        0010
        0011
        0100
        0101
        0110
        0111
        1000
        1001
        1010
        1011
        1100
        1101
        1110
        1111
    
    31、列表组合和列表元素替代组合:
    
        >>> for c in itertools.combinations([1, 2, 3, 4, 5], 2):
        ...     print ''.join(str(x) for x in c)
        ... 
        123
        124
        125
        134
        135
        145
        234
        235
        245
        345
    
        >>> for c in itertools.combinations_with_replacement([1, 2, 3], 2):
        ...     print ''.join(str(x) for x in c)
        ...
        11
        12
        13
        22
        23
        33
    
    32、列表元素排列组合:
        
        >>> for p in itertools.permutations([1, 2, 3, 4]):
        ...     print ''.join(str(x) for x in p)
        ... 
        1234
        1243
        1324
        1342
        1423
        1432
        2134
        2143
        2314
        2341
        2413
        2431
        3124
        3142
        3214
        3241
        3412
        3421
        4123
        4132
        4213
        4231
        4312
        4321
        >>>   
    
    33、可链接迭代器:

        >>> a = [1, 2, 3, 4]
        >>> for p in itertools.chain(itertools.combinations(a, 2), itertools.combinations(a, 3)):
        ...     print p
        ...
        (1, 2)
        (1, 3)
        (1, 4)
        (2, 3)
        (2, 4)
        (3, 4)
        (1, 2, 3)
        (1, 2, 4)
        (1, 3, 4)
        (2, 3, 4)
        >>> for subset in itertools.chain.from_iterable(itertools.combinations(a, n) for n in range(len(a) + 1))
        ...     print subset
        ...
        ()
        (1,)
        (2,)
        (3,)
        (4,)
        (1, 2)
        (1, 3)
        (1, 4)
        (2, 3)
        (2, 4)
        (3, 4)
        (1, 2, 3)
        (1, 2, 4)
        (1, 3, 4)
        (2, 3, 4)
        (1, 2, 3, 4)                  
    
    34、根据文件指定列类聚：
        
        >>> import itertools
        >>> with open('contactlenses.csv', 'r') as infile:
        ...     data = [line.strip().split(',') for line in infile]
        ...
        >>> data = data[1:]
        >>> def print_data(rows):
        ...     print '\n'.join('\t'.join('{: <16}'.format(s) for s in row) for row in rows)
        ...
        
"""Python程序员的10个常见错误"""
    
    Python是一门解释性的，面向对象的，并具有动态语义的高级编程语言。
    它高级的内置数据结构，结合其动态类型和动态绑定的特性，使得它在快速应用程序开发。
    
    1、在函数参数中乱用表达式作为默认值:
        
        Python 允许给某个参数设置默认值以使该参数成为一个可选参数。
        尽管这是这门语言很棒的一个功能，但是这当这个默认值是可变对象（mutable）时，那就有些麻烦了。
        
        >>> def foo(bar = []):
            bar.append("baz")
            return bar
            
        >>> foo()
        ["baz"]
        >>> foo()
        ["baz", "baz"]
        >>> foor()
        ["baz", "baz", "baz"]
        
        
        >>> def foo(bar = None):
            if bar is None:
                bar = []
            bar.append('baz')
            return bar
        
        >>> foo()
        ["baz"] 
        >>> foo()
        ["baz"]
        
    2、不正确的使用类变量
    
        看下面的例子：
        
        >>> class A(object):
            x = 1
        
        >>> class B(A):
            pass
            
        >>> class C(A)
        
        >>>print A.x, B.x, C.x
        1 1 1
        
        看起来没有问题。 
        
        >>> B.x = 2
        >>> print A.x, B.x, C.x
        1 2 1
        >>> A.x = 3
        >>> 
        >>> print A.x, B.x, C.x
        3 2 3
        
        在python里，类的变量通常在内部被当做字典来处理并遵循通常所说的方法解析顺序。
        因此在上面的代码中，因为属性x在类C中找不到，因此它会往上去它的基类中查找。
        换句话说，C没有它自己独立于A的属性x。因此对C.x的引用实际上是对A.x的引用。
    
    3、 在异常处理时错误的使用参数
    
        >>> try:
        ...     l = ['a', 'b']
        ...     int(l[2])
        ... except ValueError, IndexError:
        ...     pass
        ... 
        Traceback (most recent call last):
          File "<stdin>", line 3, in <module>
        IndexError: list index out of range
        
        这里的问题在于except语句不会像这样去接受一系列的异常。
        并且，在Python 2.x里面，语法except Exception, e是用来将异常和这个可选的参数绑定起来（即这里的e），
        以用来在后面查看的。因此，在上面的代码中，IndexError异常不会被except语句捕捉到；
        而最终ValueError这个异常被绑定在了一个叫做IndexError的参数上。
        
        在except语句中捕捉多个异常的正确做法是将所有想要捕捉的异常放在一个元组（tuple）里并作为第一个参数给except语句。
        并且，为移植性考虑，使用as关键字，因为Python 2和Python 3都支持这样的语法，例如：
        
        >>> try:
        ...     l = ['a', 'b']
        ...     int(l[2])
        ... except (ValueError, IndexError) as e:
        ...     pass
        ... 
        >>> 
    
    4、误解Python作用域的规则:
    
        Python 的作用域解析是基于LEGB(Local(本地), Enclosing(封闭), Clobal(全局)， Built-in(内置))
        的规则进行操作的。这看起来很直观，但是一些细微之处很容易出错。
        
        >>> x = 10
        >>> def foo():
                x += 1
                print x
        >>> foo()
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "<stdin>", line 2, in foo
        UnboundLocalError: local variable 'x' referenced before assignment
        
       
        # 闭包的问题 
        >>> def func():
        ...     x = 10
        ...     def foo():
        ...             x += 1
        ...             print(x)
        ... 
        >>> foo()
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "<stdin>", line 2, in foo
        UnboundLocalError: local variable 'x' referenced before assignment
        
        
        
        这是因为，在一个作用域里面给一个变量赋值的时候，
        Python自动认为这个变量是这个作用域的本地变量，并屏蔽作用域外的同名的变量。       
    
    5、 在遍历列表的同时又在修改这个列表:
        
        >>> odd = lambda x : bool(x % 2)
        >>> numbers = [n for n in range(10)]
        >>> for i in range(len(numbers)):
        ...     if odd(numbers[i]):
        ...         del numbers[i]  # 这不对的：在遍历列表时删掉列表的元素。
        ...
        Traceback (most recent call last):
              File "<stdin>", line 2, in <module>
        IndexError: list index out of range
        
        遍历一个列表或者数组的同时又删除里面的元素，对任何有经验的软件开发人员来说这是个很明显的错误。
        但是像上面的例子那样明显的错误，即使有经验的程序员也可能不经意间在更加复杂的程序中不小心犯错。

        所幸，Python集成了一些优雅的编程范式，如果使用得当，可以写出相当简化和精简的代码。
        一个附加的好处是更简单的代码更不容易遇到这种“不小心在遍历列表时删掉列表元素”的bug。
        例如列表推导式（list comprehensions）就提供了这样的范式。
        再者，列表推导式在避免这样的问题上特别有用，接下来这个对上面的代码的重新实现就相当完美：
      
        >>> odd = lambda x : bool(x % 2)
        >>> numbers = [n for n in range(10)]
        >>> numbers[:] = [n for n in numbers if not odd(n)]  # 啊，这多优美
        >>> numbers
        [0, 2, 4, 6, 8] 
    
    6、搞不清楚在闭包（closures）中Python是怎样绑定变量的:
    
       >>> def create_multipliers():
        ...     return [lambda x : j * x for j in range(5)]
        ... 
        >>> for multiplier in create_multipliers():
        ...     print multiplier(2)
        ... 
        8
        8
        8
        8
        8      
        
        这是由于Python的后期绑定（late binding）机制导致的，
        这是指在闭包中使用的变量的值，是在内层函数被调用的时候
        查找的，因此在上面的代码中，当任一返回函数被调用的时候
        i 的值是在它被调用时的周围作用域查找（那时候，循环已经结束了
        所以，i 已经被赋予了它最终的值 4）
       
        解决的办法比较巧妙：

        >>> def create_multipliers():
        ...     return [lambda x, i=i : i * x for i in range(5)]
        ...
        >>> for multiplier in create_multipliers():
        ...     print multiplier(2)
        ...
        0
        2
        4
        6
        8 
        
        这下对了！这里利用了默认参数去产生匿名函数以达到期望的效果。
        有人会说这很优美，有人会说这很微妙，也有人会觉得反感。
        但是如果你是一名Python程序员，重要的是能理解任何的情况。     
    
    7、循环加载模块:
    
        假设你有两个文件，a.py和b.py，在这两个文件中互相加载对方，例如：
        
        在a.py中:

            import b
            def f():
                return b.x
            print f() 
        
        在b.py中:
            import a
            x = 1
            def g():
                print a.f()
        
        首先，我们试着加载a.py：
        >>> import a
        1
        
        没有问题。也许让人吃惊，毕竟有个感觉应该是问题的循环加载在这儿。
        事实上在Python中仅仅是表面上的出现循环加载并不是什么问题。
        如果一个模块以及被加载了，Python不会傻到再去重新加载一遍。
        但是，当每个模块都想要互相访问定义在对方里的函数或者变量时，问题就来了。 
        
        让我们再回到之前的例子，当我们加载a.py时，它再加载b.py不会有问题，因为在加载b.py时，
        它并不需要访问a.py的任何东西，而在b.py中唯一的引用就是调用a.f()。
        但是这个调用是在函数g()中完成的，并且a.py或者b.py中没有人调用g()，所以这会儿心情还是美丽的。  
     
        但是当我们试图加载b.py时（之前没有加载a.py），会发生什么呢：
        
        >>> import b
        Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
              File "b.py", line 1, in <module>
            import a
              File "a.py", line 6, in <module>
            print f()
              File "a.py", line 4, in f
            return b.x
        AttributeError: 'module' object has no attribute 'x'
        
        解决的方案可以做一点细微的改动。改一下b.py，使得它在g()里面加载a.py：
        x = 1
        def g():
            import a	# 只有当g()被调用的时候才加载
            print a.f()
            
        这会儿当我们加载b.py的时候，一切安好：
        >>> import b
        >>> b.g()
        1	# 第一次输出，因为模块a在最后调用了‘print f()’
        1	# 第二次输出，这是我们调用g()
    
    
    8、与Python标准库模块命名冲突:
        
        Python的一个优秀的地方在于它提供了丰富的库模块。
        但是这样的结果是，如果你不下意识的避免，很容易你会遇到你自己的模块的名字与
        某个随Python附带的标准库的名字冲突的情况 
    
    9、不能区分Python 2和Python 3:
    
        看下面这个文件foo.py：

        import sys
         
        def bar(i):
            if i == 1:
                raise KeyError(1)
            if i == 2:
                raise ValueError(2)
         
        def bad():
            e = None
            try:
                bar(int(sys.argv[1]))
            except KeyError as e:
                print('key error')
            except ValueError as e:
                print('value error')
            print(e) 
        bad() 
        
        在Python 2里，运行起来没有问题：
        $ python foo.py 1
        key error
        1
        $ python foo.py 2
        value error
        2
        
        但是如果拿到Python 3         
        $ python3 foo.py 1
        key error
        Traceback (most recent call last):
          File &quot;foo.py&quot;, line 19, in &lt;module&gt;
            bad()
          File &quot;foo.py&quot;, line 17, in bad
            print(e)
        UnboundLocalError: local variable
        
        "问题"在于，在Python 3里，在except块的作用域以外，异常对象（exception object）是不能被访问的。
        (原因在于，如果不这样的话，Python会在内存的堆栈里保持一个引用链直到Python的垃圾处理
        将这些引用从内存中清除掉。)
        
        避免这样的问题可以这样做：保持在execpt块作用域以外对异常对象的引用，这样是可以访问的。
        import sys
         
        def bar(i):
            if i == 1:
                raise KeyError(1)
            if i == 2:
                raise ValueError(2)
         
        def good():
            exception = None
            try:
                bar(int(sys.argv[1]))
            except KeyError as e:
                exception = e
                print('key error')
            except ValueError as e:
                exception = e
                print('value error')
            print(exception)
         
        good()
    
    
    10、错误的使用__del__方法：
   
        假设有一个文件mod.py中这样使用：
        
        import foo
        class Bar(object):
                ...
            def __del__(self):
                foo.cleanup(self.myhandle)         
        
        然后试图在another_mod.py里这样：
        import mod
        mybar = mod.Bar()
        那么你会得到一个恶心的AttributeError异常。
        
        这是因为（参考这里），当解释器关闭时，模块所有的全局变量会被置为空（None）。
        结果便如上例所示，当__del__被调用时，名字foo已经被置为空了。
        
        使用atexit.register()可以解决这个问题。
        如此，当你的程序结束的时候（退出的时候），你的注册的处理程序会在解释器关闭之前处理。
        
        import foo
        import atexit
         
        def cleanup(handle):
            foo.cleanup(handle)
         
        class Bar(object):
            def __init__(self):
                ...
                atexit.register(cleanup, self.myhandle)

"---------------------------------------------------------------------------"

                    第 六 章 用 Python 实现基本的数据结构和算法 

""" 01 ADT（Abstract Data Type）抽象数据类型，定义数据和其操作"""
    
    什么是抽象数据类型:
    
        抽象数据类型(ADT)的含义是指一个数学模型以及定义在此数学模型上的一组操作。
        即把数据类型和数据类型上的运算捆在一起，进行封装。
        引入抽象数据类型的目的是把数据类型的表示和数据类型上运算的实现与
        这些数据类型和运算在程序中的引用隔开，使它们相互独立。
        
        最常用的数据运算有五种：
            插入
            删除
            修改
            查找
            排序
         
    下边代码是一个简单的示例，如果实现一个简单的 Bag 类，先定义具有的操作
    然后我们再用类的 magic method 来实现这些方法，迭代器的实现：
               
        class Bag(object):
        
            """
            constructor  构造函数
            size
            contains
            append
            remove
            iter
            """
        
            def __init__(self):
                self._items = list()
        
            def __le__(self):
                return len(self._items)
        
            def __contains__(self, item):
        
                return item in self._items
        
            def add(self, item):
                self._items.append(item)
        
            def remove(self, item):
                assert item in self._items, 'item must in the bag'
                return self._items.remove(item)
        
            def __iter__(self):
                return _BagIterator(self._items)
        
        class _BagIterator(object):
        
            """
                注意这里实现了迭代器类
            """
        
            def __init__(self, seq):
                self._bag_items = seq
                self._cur_item = 0
        
            def __iter__(self):
                return self
        
            def __next__(self):
                if self._cur_item < len(self._bag_items):
                    item = self._bag_items[self._cur_item]
                    self._cur_item +=  1
                    return item
                else:
                    raise StopIteration
        
        if __name__ == '__main__':
        
            b = Bag()
            b.add(1)
            b.add(2)
            b.add(3)
            b.add(4)
            b.add(5)
        
            # for 使用 __iter__ 构建，用 __next__ 迭代
        
            for i in b:
                print(i)
        
            # for 语句等价于
            """   
                i = b.__iter__()
                while True:
                    try:
                        item = i.__next__()
                        print(item)
                    except StopIteration:
                        break
            """

""" 02 array VS list"""

    array : 
        
        定长， 操作有限
        
        python 3.5 中引入了 array 类， 可以用 import array 直接导入。    
    
    list :
        
        会预先分配内存，操作丰富，但是耗费内存。
        
        扩充的两种策略:
            每次扩充增加固定数目的存储位置，如每次扩充增加10个元素位置，这种策略可称为线性增长。
            特点：节省空间，但是扩充操作频繁，操作次数多。
        
            每次扩充容量加倍，如每次扩充增加一倍存储空间。
            特点：减少了扩充操作的执行次数，但可能会浪费空间资源。以空间换时间，推荐的方式。
                
        list.append: 如果之前没有分配够内存，会重新开辟新区域，然后复制之前的数据，复杂度退化 O(1)
        list.insert: 会移动被插入区域后所有元素,O(n)
        list.pop: pop不同位置需要的复杂度不同pop()是O(1)复杂度,pop(0)首位O(n)复杂度
        list[]: slice操作copy数据（预留空间）到另一个list
        
    来实现一个array的ADT:   
     
     """
     模块ctypes是Python内建的用于调用动态链接库函数的功能模块，
     一定程度上可以用于Python与其他语言的混合编程。
     由于编写动态链接库，使用C/C++是最常见的方式，
     故ctypes最常用于Python与C/C++混合编程之中。
     
     魔方方法： __getitem__, __setitem__
     
        class DictDemo:
            def __init__(self,key,value):
                self.dict = {}
                self.dict[key] = value
            def __getitem__(self,key):
                return self.dict[key]
            def __setitem__(self,key,value):
                self.dict[key] = value
        
        dictDemo = DictDemo('key0','value0')
        print(dictDemo['key0']) #value0
        dictDemo['key1'] = 'value1'
        print(dictDemo['key1']) #value1
     
     上面的对象就相当于自己创建了一个内建类型相似的字典，当实例中有类似字典的操作的时候
     
     实例dictDemo["key0"]就类似上面的的操作，
     则会自动调用类中定义的方法__getitem__，输出在该方法返回的值
    
     再看看dictDemo["key1"] = "value1"，就是字典的操作，
     会自动调用类中定义的方法__setitem__，来设置相应的值
        
     """
        import ctypes

        class Array(object):
        
            def __init__(self, size):
                assert size > 0, 'array size must be > 0 '
        
                self._size = size
                PyArrayType = ctypes.py_object * size
                self._elements = PyArrayType()
                self.clear(None)
        
            def __len__(self):
                return self._size
        
            def __getitem__(self, index):
        
                assert index >= 0 and index < len(self), 'out of range'
                return  self._elements[index]
        
            def __setitem__(self, index, value):
        
                assert index >= 0 and index < len(self), 'out of range'
                self._elements[index] = value
        
            def clear(self, value):
                """ 设置每个元素为 value"""
        
                for i in range(len(self)):
                    self._elements[i] = value
        
            def __iter__(self):
                return _ArrayIterator(self._elements)
        
        class _ArrayIterator(object):
        
            def __init__(self, items):
        
                self._items = items
                self._idx = 0
        
            def __iter__(self):
                return self
        
            def __next__(self):
                if self._idx < len(self._items):
                    val = self._items[self._idx]
                    self._idx += 1
                    return val
                else:
                    raise StopIteration
        
        if __name__ == '__main__':
        
            a = Array(10)
            a[0] = 1
            a[1] = 2
            a[2] = 3
            a[3] = 4
            a[4] = 5
            a[5] = 6
        
            print(a[5])
        
            for i in a:
                print(i)
            
            """
                结果如下：
                
                6
                1
                2
                3
                4
                5
                6
                None
                None
                None
                None
               
            """                   
    
    Two-Demensional Arrays (二维数组):
    
        class Aarray2D(object):

    """
        要实现的方法
        Array2D(nrows, ncols) : constructor

        numRows()
        numCols()
        clear(value)
        getitem(i, j)
        setitem(i, j, value)
        
        @property成为属性函数，可以对属性赋值时做必要的检查，并保证代码的清晰短小，
        主要有2个作用：
            将方法转换为只读
            重新实现一个属性的设置和读取方法,可做边界判定

        """
        def __init__(self, numrows, numclos):
            self._the_rows = Array(numrows)
    
            for i in range(numrows):
                self._the_rows[i] = Array(numclos)
    
        @property
        def numRows(self):
            return len(self._the_rows)
    
        @property
        def numCols(self):
            return len(self._the_rows[0])
    
        def clear(self, value):
            for row in self._the_rows:
                row.clear(value)
    
        def __getitem__(self, ndx_tuple):
            assert len(ndx_tuple) == 2
            
            row, col = ndx_tuple[0], ndx_tuple[1]
            assert (row >= 0 and row < self.numRows and col >= 0 and col < self.numCols)
    
        def __setitem__(self, ndx_tuple, value):
    
            assert len(ndx_tuple) == 2
            row , col = ndx_tuple[0], ndx_tuple[1]
            assert (row >= 0 and row < self.numRows and col>= 0 and col < self.numCols)
    
            the_1d_array = self._the_rows[row]
            the_1d_array[col] = value
        
 
 """03 Sets and Maps"""           
    
    除了 list 之外，最常用的应该是 Python 内置的 set 和 dict 了。
    
    1、set ADT:
    
    A set is a container that stores a collection of unique values over
    a given comparable domain in which the stored values have no particular ordering.
    
    内置函数 set()
    
        set() 函数创建一个无序不重复元素集，可以进行关系测试，删除重复数据，
        还可以计算交集、差集、并集等。
        
        set 语法：
            class set([iterable])
        参数说明：
            iterable ---可迭代对象
        返回值：  
            返回新的集合对象      
        
        set 中常用的一些方法：
        
            1、创建集合，要创建一个集合对象，向内置的set函数传递一个序列或其他的可迭代的对象：

                x = set('abcde')
                y = set('bdxyz')
            
                print(x)
                    set(['a', 'c', 'b', 'e', 'd'])
        
            2、集合添加的方法，分别是 add 和 update 删除 remove
            
                add方法：要把传入的元素作为一个整体添加到集合中
	
                x.add('python')
                    set(['a', 'c', 'b', 'e', 'd', 'python'])
                
                update方法：把要传入的元素拆开，作为一个个体传入到集合中：
                
                    x.update('xyz')
                        set(['a', 'c', 'b', 'e', 'd', 'python', 'y', 'x', 'z'])
                
                删除方法：remove()
                
                    x.remove('python')
                        set(['a', 'c', 'b', 'e', 'd', 'y', 'x', 'z'])
            
            3、 集合通过表达式操作符支持一般的数学集合运算。
                   注意，不能在一般序列上应用这些表达式，必须通过序列创建集合后才能使用。
                
                   python 符号          含义
                
                      -                差集      x - y		set(['a', 'c', 'e'])
                
                      &                交集      x & y      set(['y', 'x', 'b', 'd', 'z'])
                        
                      |                并集      x | y      set(['a', 'c', 'b', 'e', 'd', 'y', 'x', 'z'])
                
                   in,not in            成员关系 'a' in x    True
                
                     ==,!=           等于，不等于  x!=y      True
                
                     >,<              大于，小于   x>y       True         
        
        
        下面的类中，不能实现迭代。
        
        class Set(object):
        """
            使用 list 实现 set ADT
            Set()
            length()
            contains(element)
            add(element)
            remove(element)
    
            isSubsetOf(setB)
            union(setB)
            intersect(setB)
            difference(setB)
            iterator
    
        """
    
            def __init__(self):
                self._theElements = list()
        
            def __len__(self):
                return len(self._theElements)
        
            def __contains__(self, item):
                return item in self._theElements
        
            def add(self, item):
                if item not in self._theElements:
                    self._theElements.append(item)
        
            def print(self):
                for i in self._theElements:
                    print('{0}'.format(i))
        
            def remove(self, item):
                assert item in self._theElements, "The element must be set"
        
            def __eq__(self, setB):
                if len(self._theElements) != len(setB):
                    return False
                else:
                    return self.isSubsetof(setB)
        
            def isSubsetof(self, setB):
        
                for item in self._theElements:
                    if item not in setB:
                        return False
                    else:
                        return True
        
            def union(self, setB):
        
                newSet = Set()
                newSet._theElements.extend(self._theElements)
        
                for item in setB:
                    if item not in self._theElements:
                        newSet._theElements.append(item)
                return newSet
            
            def __iter__(self):
                
                return _SetIterator(self._theElements)
    

        class _SetIterator(object):
        
            def __init__(self, items):
                self._items = items
                self._idx = 0
        
            def __iter__(self):
                return self
        
            def __next__(self):
                if self._idx < len(self._items):
                    val = self._items[self._idx]
                    self._idx += 1
                    return val
                else:
                    raise StopIteration
        
        if __name__ == '__main__':
        
            setA = Set()
            for i in range(10):
                setA.add(i)
        
            setA.print()
            
            for i in setA:
                print(i)
        
            print('-----------------')
        
            setB = set('iloveyou')
        
            setC = setA.union(setB)
        
            setC.print()
    
    2、Maps or Dict: 键值对,python内部采用hash实现:
    
        映射是存储数据记录集的一个容器，存储的每条记录都与一个唯一 key 关联。
        
        Map ADT:
        
            Map(): 创建一个空映射。
            length(): 返回映像中的 key/value 对个数。
            contains(key): 判断该 key 是否在映射中
            add(key, value); 若该键值对未存在于映射中，添加; 若已存在即更新该 key 对应的值;添加后返回 True，更新后返回 False。
            remove(key): 删除键值对，不存在时抛出异常。
            valueOf(key): 返回该 key 关联的数据记录。
            iterator(): 返回迭代器用于遍历映射中的键。
        
        基于 List 的实现:
            
        两种实现方法： 
            1. 分别用一个 List 存储 key，另一个 List 存储 value，并维护这两个 List 的关联性。 
            2. 只用一个 List 来存储 key/value 对。
            
        下面的实现代码使用了方法 2：
         
            # Implementation of Map ADT using a single list.
            class _MapEntry:
                def __init__(self, key, val):
                    self.key = key
                    self.value = val
            
            class Map:
                def __init__(self):
                    self._entryList = list()
            
                def __len__(self):
                    return len(self._entryList)
            
                # Helper method used to find the index position of a category. If the
                # key is not found, None is returned.
                def _findPosition(self, key):
                    for e, ndx in enumerate(self._entryList):
                        if e.key == key:
                            return ndx
                    return None
            
                def __contains__(self, key):
                    ndx = self._findPosition(key)
                    return ndx is not None
            
                # Adds a new entry to the map if the key does exist. Otherwise, the
                # new value replaces the current value associated with the key.
                def add(self, key, val):
                    ndx = self._findPosition(self, key)
                    if ndx is not None:
                        self._entryList[ndx].value = val
                        return False
                    else:
                        self._entryList.append(_MapEntry( key, val) )
                        return True
            
                def valueOf(self, key):
                    ndx = self._findPosition(self, key)
                    assert ndx is not None, "Invalid map key."
                    return self._entryList[ndx].value
            
                def remove(self, key):
                    ndx = self._findPosition(self, key)
                    assert ndx is not None, "Invalid map key."
                    self._entryList.pop(ndx)
            
                def keyArray(self):
                    keys = list()
                    for e in self._entryList:
                        keys.append(e.key)
                    return keys
            
                def __iter__(self):
                    return _MapGenerator(self._entryList)
            
                __setitem__ = add
                __getitem__ = valueOf
            
            def _MapGenerator(entryList):
                for e in entryList:
                    yield e   
                          
""04 Searching and Sorting """
    
    排序和查找是最基础和频繁的操作，python内置了in操作符和bisect二分操作模块实现查找，
    内置了sorted方法来实现排序操作。
    二分和快排也是面试中经常考到的，本章讲的是基本的排序和查找。
    
    1、冒泡排序:
    
        冒泡排序(Bubble Sort) 是一种简单的排序算法，它重复地遍历的数列
        一次比较两个元素，如果他们顺序错误就把他们交换过来，遍历数列的
        工作是重复地进行，直到没有再续约交换的，也就是排序完成。
        这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。
        
        冒泡排序算法的运作如下：

            比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
            对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
            针对所有的元素重复以上的步骤，除了最后一个。
            持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
        
        def bubble_sort(alist):
            # 产生每次需要遍历的次数
            for i in range(len(alist)-1, 0, -1):
                # 遍历
                for j in range(i):
                    if alist[j] > alist[j + 1]:
                        alist[j], alist[j + 1]  = alist[j + 1] , alist[j]

        if __name__ == '__main__':
            source_list = [1, 54, 22, 67, 43, 78, 12, 9, 12]
            bubble_sort(source_list)
            print(source_list)
    
        时间复杂度: 
            最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
            最坏时间复杂度：O(n^2)
            稳定性：稳定
            
    2、选择排序:
    
        选择排序(Selection sort) 是一种简单直观的排序算法，它的工作原理如下：
        首先是在未排序的序列中找到最小(大)的元素，存放到排序序列的起始位置。
        然后，再从未排序的序列中继续寻找最小(大)元素，然后放到已排序序列的末尾。
        依次类推，直到所有元素排序完毕。
        
        选择排序的主要优点与数据移动有关。如果某个元素位于正确的最终位置上，则它不会被移动。
        选择排序每次交换一对元素，它们当中至少有一个将被移到其最终位置上，
        因此对n个元素的表进行排序总共进行至多n-1次交换。
        在所有的完全依靠交换去移动元素的排序方法中，选择排序属于非常好的一种。
        
        def selection_sort(alist):

            for i in range(len(alist)-1):
                min_index = i
                for j in range(i + 1, len(alist)):
                    if alist[min_index] > alist[j]:
                        min_index = j
                
                if min_index != i:
                    alist[min_index], alist[i] = alist[i], alist[min_index]
        
        if __name__ == '__main__':    
            source_list = [1, 54, 22, 67, 43, 78, 12, 9, 12]
            selection_sort(source_list)
            print(source_list)
        
        
        
        时间复杂度

            最优时间复杂度：O(n2)
            最坏时间复杂度：O(n2)
            稳定性：不稳定（考虑升序每次选择最大的情况）
    
    3、插入排序:
    
        插入排序（Insertion Sort） 是一种简单直观的排序算法， 它的工作原理是通过
        构建有序序列，对于未排序数据，在已排序的序列中从后向前扫描，找到相应位置
        并插入，插入排序在实现上，在从后向前扫描的过程中，需要反复的把已经排序元素
        逐步往后移动，为最新的元素提供插入空间。
        
        def insert_sort(alist):
            # 从第二个位置，即下标为 1 的元素开始向前插入
            for i in range(1, len(alist)):
                # 从第 i 个元素开始向前比较, 如果小于前一个元素，交换位置
                for j in range(i, 0 , -1):
                    if alist[j] < alist[j - 1]:
                        alist[j], alist[j - 1] = alist[j - 1], alist[j]
                    
        if __name__ == '__main__':    
            source_list = [1, 54, 22, 67, 43, 78, 12, 9, 12]
            insert_sort(source_list)
            print(source_list)
        
        
        时间复杂度

            最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
            最坏时间复杂度：O(n2)
            稳定性：稳定
    
    4、快速排序:
        
        快速排序（Quick sort）, 又称划分交换排序 (partition-exchange sort)
        通过一趟排序将要排序的数据分割成独立的两部分， 其中一部分的所有数据都比
        另一部分小，然后再按照此方法对这部分数据分别进行快速排序，整个排序过程
        可以递归进行，以此到的整个数据变成又序序列。
        
        步骤为：
        
            (1) 从数列中挑出一个元素，称为"基准"（pivot）
            
            (2) 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准大的摆在
                基准后面（相同数据可以放到任意一边）。在这个分区结束之后，该基准就处于
                数列的中间位置，这个称为分区(partition)操作。
            (3) 递归地(recursive) 把小于基准元素的子数列和大于基准的子数列排序。
        
        递归的最底部情形, 是数列的大小是零或一，也就是永远都已经被排序好了。
        虽然一直递归下去，但是这个算法总会结束，因为在每次的迭代（iteration）中，
        它至少会把一个元素摆到它最后的位置去。
        
        
            def quick_sort(alist, start, end):

                if start  >= end:
                    return
                mid = alist[start]
                low = start
                high = end
            
                while low < high:
                    while low < high and alist[high] >= mid:
                        high -= 1
                    alist[low] = alist[high]
                    while low < high and alist[low] < mid:
                        low += 1
                    alist[high] = alist[low]
                
                alist[low] = mid
                
                quick_sort(alist, 0, low - 1)
                quick_sort(alist, low + 1, end)
            
            if __name__ == "__main__":

                source_list = [32, 543, 324, 34, 7, 90, 30, 14, 53, 99, 333]        
                quick_sort(source_list, 0 , len(source_list)-1)
                print(source_list)
        
        时间复杂度：
        
            最优时间复杂度：O(nlogn)
            最坏时间复杂度：O(n^2)
            稳定性：不稳定    
                
    
    
    5、希尔排序:
    
        希尔排序(Shell Sort) 是插入排序的一种，也称缩小增量排序，是直接插入排序算法的
        一种更高效的改进版本。希尔排序是非稳定排序算法，该方法因 DL.Shell 于1959年提出
        而得名，希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序;
        随着增量逐渐减少，每组包含的关键词越来越多，当增量减至 1 时，整个文件恰好被分成
        一组，算法便终止。
        
        希尔排序过程:
            
            希尔排序的基本思想是：将数组列在一个表中并对列分别进行插入排序，重复这过程，
            不过每次用更长的列（步长更长了，列数更少了）来进行。最后整个表就只有一列了。
            将数组转换至表是为了更好地理解这算法，算法本身还是使用数组进行排序。
            
            例如，假设有这样一组数[ 13 14 94 33 82 25 59 94 65 23 45 27 73 25 39 10 ]，
            如果我们以步长为5开始进行排序，我们可以通过将这列表放在有5列的表中来更好地描述算法，
            这样他们就应该看起来是这样(竖着的元素是步长组成)：       
                
                13 14 94 33 82
                25 59 94 65 23
                45 27 73 25 39
                10
            
            然后我们对每列进行排序：

                10 14 73 25 23
                13 27 94 33 39
                25 59 94 65 82
                45
            
            将上述四行数字，依序接在一起时我们得到：[ 10 14 73 25 23 13 27 94 33 39 25 59 94 65 82 45 ]。
            这时10已经移至正确位置了，然后再以3为步长进行排序： 
             
                10 14 73
                25 23 13
                27 94 33
                39 25 59
                94 65 82
                45
            
            排序之后变为：
                
                10 14 13
                25 23 33
                27 25 59
                39 65 73
                45 94 82
                94
                
            最后以1步长进行排序（此时就是简单的插入排序了）
            
        def shell_sort(alist):
            n = len(alist)
            # 初始步长
            gap = n // 2
            while gap > 0:
                # 按步长进行插入排序
                for i in range(gap, n):
                    j = i
                    # 插入排序
                    while j>=gap and alist[j-gap] > alist[j]:
                        alist[j-gap], alist[j] = alist[j], alist[j-gap]
                        j -= gap
                # 得到新的步长
                gap = gap // 2 
                
        if __name__ == "__main__":
            alist = [54,26,93,17,77,31,44,55,20]
            shell_sort(alist)
            print(alist)        
        
        最优时间复杂度：根据步长序列的不同而不同
            最坏时间复杂度：O(n2)
            稳定想：不稳定      
        
    6、 二分法查找：
    
        # 非递归实现
        
        def binary_search(alist, item):

            first = 0
            last = len(alist) - 1
        
            while first <= last:
                midpoint = (first + last)//2
        
                if alist[midpoint] == item:
                    return True
                elif item < alist[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
            return False   
        
        if __name__ == "__main__":
            testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
            print(binary_search(testlist, 3))
            print(binary_search(testlist, 13))
        
        # 递归实现
        
        def binary_search_dg(alist, item):
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
        
        if __name__ == "__main__":
            testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
            print(binary_search(testlist, 3))
            print(binary_search(testlist, 13))
        
        
        
        
""" 05 Linked Structure"""
    
    list是最常用的数据结构，但是list在中间增减元素的时候效率会很低，
    这时候linked list会更适合，缺点就是获取元素的平均时间复杂度变成了O(n)       
    
    链表的实现：
    
        class SingleLinkList(object):
        
            def __init__(self):
                self._head = None
        
            def is_empty(self):
                return self._head is None
        
            def length(self):
        
                cur = self._head
                count = 0
                while cur is not None:
                    count += 1
                    cur = cur.next
                return count
        
            def travel(self):
                cur = self._head
        
                while cur is not None:
                    print('{0}'.format(cur.item))
                    cur = cur.next
        
            def add(self, item):
        
                node = SingleNode(item)
        
                node.next = self._head
                self._head = node
        
            def append(self, item):
        
                node = SingleNode(item)
        
                if self.is_empty():
                    self._head = node
        
                else:
        
                    cur = self._head
        
                    while cur.next is not None:
                        cur = cur.next
                    cur.next = node
        
            def inset(self, post, item):
        
                """ 指定位置添加元素 """
        
                # 若指定位置 post 为第一个元素之前，则执行头部插入
        
                if post <= 0:
                    self.add(item)
        
                elif post > self.length() - 1:
                    self.append(item)
        
                else:
                    node = SingleNode(item)
                    count = 0
        
                    # pre 用来指向指定位置 post 的前一个位置 post - 1, 初始从头节点移动到指定位置
                    pre = self._head
                    while count < post - 1:
                        count += 1
                        pre = pre.next
        
                    node.next = pre.next
                    pre.next = node
        
            def remove(self, item):
        
                cur = self._head
                pre = None
        
                while cur is not None:
        
                    if cur.item == item:
        
                        # 链表第一个节点就是要删除的节点
                        if not pre:
                            self._head = cur.next
                        else:
                            pre.next = cur.next
                        break
                    else:
                        pre = cur
                        cur = cur.next
            
            # 反转
            def reversal(self):
                pre, cur = None, self._head
                
                # 一定要明白链表的特性，cur.next 是一个指针，
                # cur.next 等于谁，cur 的下一项就是谁。
            
                while cur is not None:
                    cur.next, pre , cur = pre, cur, cur.next
                return pre
            
            # 相邻两个节点交换
            def swapPairs(self):
        
                pre, pre.next = self, self._head
        
                while pre.next and pre.next.next:
                    a = pre.next
                    b = a.next
        
                    pre.next, b.next, a.next = b, a, b.next
        
                    pre = a
                return self.next
    
    时间复杂度：
        
        操作            时间复杂度
        访问元素	        O(n)	
        在头部插入/删除	O(1)	
        在尾部插入/删除	O(n)	
        在中间插入/删除	O(n)


""" 06 Stacks """

    栈是计算机里用的较多的数据结构，栈是一种后进先出数据结构，
    由于栈数据结构只允许在一端进行操作，因而按照后进先出（LIFO, Last In First Out）的原理运作。
    可以理解为往一个桶里放盘子，先放进去的会被压在地下，拿盘子的时候，后放的会被先拿出来。
    
    1、用 列表实现数据结构
    
        栈的操作

            Stack() 创建一个新的空栈
            push(item) 添加一个新的元素item到栈顶
            pop() 弹出栈顶元素
            peek() 返回栈顶元素
            is_empty() 判断栈是否为空
            size() 返回栈的元素个数   
        
        
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
    
       
    2、第二种实现方式（linked list）：
    
        使用list实现很简单，但是如果涉及大量push操作，list的空间不够时复杂度退化到O(n)
        而linked list可以保证最坏情况下仍是O(1) 
        
            class Stack:
            
                def __init__(self):
                    self._top = None    # top节点, _StackNode or None
                    self._size = 0    # int
            
                def isEmpty(self):
                    return self._top is None
            
                def __len__(self):
                    return self._size
            
                def peek(self):
                    assert not self.isEmpty()
                    return self._top.item
            
                def pop(self):
                    assert not self.isEmpty()
                    node = self._top
                    self.top = self._top.next
                    self._size -= 1
                    return node.item
            
                def _push(self, item):
                    self._top = _StackNode(item, self._top)
                    self._size += 1
            
            
            class _StackNode:
                def __init__(self, item, link):
                    self.item = item
                    self.next = link
            
            if __name__ == "__main__":
                stack = Stack()
                stack.push(1)
                stack.push(2)
                stack.push(3)
                stack.push(4)
            
                print(stack.peek())
                print(stack.isEmpty())
                print(stack.pop())
                print(stack.pop())
                print(stack.pop())        
                
""" 07 Queues 队列"""
    
    队列（queue）是只允许在一端进行插入操作，而在另一端进行删除操作的线性表。
    队列是一种先进先出的（First In First Out）的线性表，简称FIFO。
    队列也是经常使用的数据结构，比如发送消息等，celery可以使用redis提供的list实现消息队列。 
    本章我们用list和linked list来实现队列和优先级队列。   
    
    1、用列表实现的队列
        
        Queue() 创建一个空的队列
        enqueue(item) 往队列中添加一个item元素
        dequeue() 从队列头部删除一个元素
        is_empty() 判断一个队列是否为空
        size() 返回队列的大小
        
        
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
    
    2、linked list 实现
        
        class Queue_list(object):
            """ Queue ADT, linked list 实现。为了改进环型数组有最大数量的限制，改用
            带有头尾节点的linked list实现。
            """
            def __init__(self):
                self._qhead = None
                self._qtail = None
                self._qcount = 0
        
            def isEmpty(self):
                return self._qhead is None
        
            def __len__(self):
                return self._count
        
            def enqueue(self, item):
                node = _QueueNode(item)    # 创建新的节点并用尾节点指向他
                
                if self.isEmpty():
                    self._qhead = node
                else:
                    self._qtail.next = node
                self._qtail = node
                self._qcount += 1
        
            def dequeue(self):
                assert not self.isEmpty(), 'Can not dequeue from an empty queue'
                node = self._qhead
                if self._qhead is self._qtail:
                    self._qtail = None
                self._qhead = self._qhead.next    # 前移头节点
                self._qcount -= 1
                return node.item
        
        class _QueueNode(object):
            def __init__(self, item):
                self.item = item
                self.next = None




"""08 高级链表 """

    1、循环链表:
      
        常见操作：
        
        is_empty() 判断链表是否为空
        length() 返回链表的长度
        travel() 遍历
        add(item) 在头部添加一个节点
        append(item) 在尾部添加一个节点
        insert(pos, item) 在指定位置pos添加节点
        remove(item) 删除一个节点
        search(item) 查找节点是否存在
    
        实现：
        
        class Node(object):
            """节点"""
            def __init__(self, item):
                self.item = item
                self.next = None
        
        
        class SinCycLinkedlist(object):
            """单向循环链表"""
            def __init__(self):
                self._head = None
        
            def is_empty(self):
                """判断链表是否为空"""
                return self._head == None
        
            def length(self):
                """返回链表的长度"""
                # 如果链表为空，返回长度0
                if self.is_empty():
                    return 0
                count = 1
                cur = self._head
                while cur.next != self._head:
                    count += 1
                    cur = cur.next
                return count
        
            def travel(self):
                """遍历链表"""
                if self.is_empty():
                    return
                cur = self._head
                print cur.item,
                while cur.next != self._head:
                    cur = cur.next
                    print cur.item,
                print ""
        
        
            def add(self, item):
                """头部添加节点"""
                node = Node(item)
                if self.is_empty():
                    self._head = node
                    node.next = self._head
                else:
                    #添加的节点指向_head
                    node.next = self._head
                    # 移到链表尾部，将尾部节点的next指向node
                    cur = self._head
                    while cur.next != self._head:
                        cur = cur.next
                    cur.next = node
                    #_head指向添加node的
                    self._head = node
        
            def append(self, item):
                """尾部添加节点"""
                node = Node(item)
                if self.is_empty():
                    self._head = node
                    node.next = self._head
                else:
                    # 移到链表尾部
                    cur = self._head
                    while cur.next != self._head:
                        cur = cur.next
                    # 将尾节点指向node
                    cur.next = node
                    # 将node指向头节点_head
                    node.next = self._head
        
            def insert(self, pos, item):
                """在指定位置添加节点"""
                if pos <= 0:
                    self.add(item)
                elif pos > (self.length()-1):
                    self.append(item)
                else:
                    node = Node(item)
                    cur = self._head
                    count = 0
                    # 移动到指定位置的前一个位置
                    while count < (pos-1):
                        count += 1
                        cur = cur.next
                    node.next = cur.next
                    cur.next = node
        
            def remove(self, item):
                """删除一个节点"""
                # 若链表为空，则直接返回
                if self.is_empty():
                    return
                # 将cur指向头节点
                cur = self._head
                pre = None
                # 若头节点的元素就是要查找的元素item
                if cur.item == item:
                    # 如果链表不止一个节点
                    if cur.next != self._head:
                        # 先找到尾节点，将尾节点的next指向第二个节点
                        while cur.next != self._head:
                            cur = cur.next
                        # cur指向了尾节点
                        cur.next = self._head.next
                        self._head = self._head.next
                    else:
                        # 链表只有一个节点
                        self._head = None
                else:
                    pre = self._head
                    # 第一个节点不是要删除的
                    while cur.next != self._head:
                        # 找到了要删除的元素
                        if cur.item == item:
                            # 删除
                            pre.next = cur.next
                            return
                        else:
                            pre = cur
                            cur = cur.next
                    # cur 指向尾节点
                    if cur.item == item:
                        # 尾部删除
                        pre.next = cur.next
        
            def search(self, item):
                """查找节点是否存在"""
                if self.is_empty():
                    return False
                cur = self._head
                if cur.item == item:
                    return True
                while cur.next != self._head:
                    cur = cur.next
                    if cur.item == item:
                        return True
                return False
        
        if __name__ == "__main__":
            ll = SinCycLinkedlist()
            ll.add(1)
            ll.add(2)
            ll.append(3)
            ll.insert(2, 4)
            ll.insert(4, 5)
            ll.insert(0, 6)
            print "length:",ll.length()
            ll.travel()
            print ll.search(3)
            print ll.search(7)
            ll.remove(1)
            print "length:",ll.length()
            ll.travel() 
                
    2、双链表:
        
        一种更复杂的链表是“双向链表”或“双面链表”。
        每个节点有两个链接：一个指向前一个节点，当此节点为第一个节点时，指向空值；
        而另一个指向下一个节点，当此节点为最后一个节点时，指向空值。
        
        操作：
            
            is_empty() 链表是否为空
            length() 链表长度
            travel() 遍历链表
            add(item) 链表头部添加
            append(item) 链表尾部添加
            insert(pos, item) 指定位置添加
            remove(item) 删除节点
            search(item) 查找节点是否存在
        
        实现：          
        
        class Node(object):
            """双向链表节点"""
            def __init__(self, item):
                self.item = item
                self.next = None
                self.prev = None
        
        
        class DLinkList(object):
            """双向链表"""
            def __init__(self):
                self._head = None
        
            def is_empty(self):
                """判断链表是否为空"""
                return self._head == None
        
            def length(self):
                """返回链表的长度"""
                cur = self._head
                count = 0
                while cur != None:
                    count += 1
                    cur = cur.next
                return count
        
            def travel(self):
                """遍历链表"""
                cur = self._head
                while cur != None:
                    print cur.item,
                    cur = cur.next
                print ""
        
            def add(self, item):
                """头部插入元素"""
                node = Node(item)
                if self.is_empty():
                    # 如果是空链表，将_head指向node
                    self._head = node
                else:
                    # 将node的next指向_head的头节点
                    node.next = self._head
                    # 将_head的头节点的prev指向node
                    self._head.prev = node
                    # 将_head 指向node
                    self._head = node
        
            def append(self, item):
                """尾部插入元素"""
                node = Node(item)
                if self.is_empty():
                    # 如果是空链表，将_head指向node
                    self._head = node
                else:
                    # 移动到链表尾部
                    cur = self._head
                    while cur.next != None:
                        cur = cur.next
                    # 将尾节点cur的next指向node
                    cur.next = node
                    # 将node的prev指向cur
                    node.prev = cur
        
        
        
            def search(self, item):
                """查找元素是否存在"""
                cur = self._head
                while cur != None:
                    if cur.item == item:
                        return True
                    cur = cur.next
                return False
                
            def insert(self, pos, item):
                """在指定位置添加节点"""
                if pos <= 0:
                    self.add(item)
                elif pos > (self.length()-1):
                    self.append(item)
                else:
                    node = Node(item)
                    cur = self._head
                    count = 0
                    # 移动到指定位置的前一个位置
                    while count < (pos-1):
                        count += 1
                        cur = cur.next
                    # 将node的prev指向cur
                    node.prev = cur
                    # 将node的next指向cur的下一个节点
                    node.next = cur.next
                    # 将cur的下一个节点的prev指向node
                    cur.next.prev = node
                    # 将cur的next指向node
                    cur.next = node
             
            def remove(self, item):
               """删除元素"""
                if self.is_empty():
                    return
                else:
                    cur = self._head
                    if cur.item == item:
                        # 如果首节点的元素即是要删除的元素
                        if cur.next == None:
                            # 如果链表只有这一个节点
                            self._head = None
                        else:
                            # 将第二个节点的prev设置为None
                            cur.next.prev = None
                            # 将_head指向第二个节点
                            self._head = cur.next
                        return
                    while cur != None:
                        if cur.item == item:
                            # 将cur的前一个节点的next指向cur的后一个节点
                            cur.prev.next = cur.next
                            # 将cur的后一个节点的prev指向cur的前一个节点
                            cur.next.prev = cur.prev
                            break
                        cur = cur.next   
                        
                        
"""09 Recursion """        

    递归是把一个大的问题分解成更小的问题，然后再解决更小、更琐碎的部分，从而解决问题的过程。                    
    
    1、递归函数，调用自己的函数，看一个简单的递归函数，倒序打印一个数
    
       def printRev(n):
            if n > 0:
                print(n)
                print(printRev(n - 1))
       
       
       if __name__ == "__main__":

            printRev(3)    
            
       打印结果：
                3
                2
                1
                None
                None
                None
       
       def printRev(n):
            if n > 0:
                print(printRev(n - 1))
                #之所以最小的先打印是因为函数一直递归到n==1时候的最深栈，此时不再
                # 递归，开始执行print语句，这时候n==1，之后每跳出一层栈，打印更大的值
                print(n)
       if __name__ == "__main__": 
            printRev(3)
            
       打印结果：
                None
                1
                None
                2
                None
                3 
                
"""10 Hash Tables 哈希表，散列表"""

    基于比较的搜索（线性搜索、有序数组的二分搜索）最好的时间复杂度只能达到 O(logn)
    利用 Hash 可以实现 O(1) 查找，Python 内置dict 实现就是 hash, 你会发现 dict 的
    key 必须实现了 __hash__ 和 __eq__ 方法。
 
    Hash: Hash是将搜索键映射到有限范围的数组索引的过程，目的是提供对键的直接访问。
    
    has 方法有一个 hash 函数来计算一个 hash 值， 作为数组下标， 放到该下标对应的槽中。
    当不同 key 根据 hash 函数计算得到的下标相同时， 就出现了冲突。 解决冲突的方式有很多，
    比如让比如让每个槽成为链表，每次冲突以后放到该槽链表的尾部，但是查询时间就会退化，不再是O(1)。
    还有一种探查方式，当key的槽冲突时候，就会根据一种计算方式去寻找下一个空的槽存放，
    探查方式有线性探查，二次方探查法等，cpython解释器使用的是二次方探查法。
    还有一个问题就是当python使用的槽数量大于预分配的2/3时候，会重新分配内存并拷贝以前的数据，
    所以有时候dict的add操作代价还是比较高的，牺牲空间但是可以始终保证O(1)的查询效率。
    如果有大量的数据，建议还是使用bloomfilter或者redis提供的HyperLogLog。
    
    用 python 实现一个类似的 hash 结构
    
            import ctypes

            class Array:  # 第二章曾经定义过的ADT，这里当做HashMap的槽数组使用
                def __init__(self, size):
                    assert size > 0, 'array size must be > 0'
                    self._size = size
                    PyArrayType = ctypes.py_object * size
                    self._elements = PyArrayType()
                    self.clear(None)
            
                def __len__(self):
                    return self._size
            
                def __getitem__(self, index):
                    assert index >= 0 and index < len(self), 'out of range'
                    return self._elements[index]
            
                def __setitem__(self, index, value):
                    assert index >= 0 and index < len(self), 'out of range'
                    self._elements[index] = value
            
                def clear(self, value):
                    """ 设置每个元素为value """
                    for i in range(len(self)):
                        self._elements[i] = value
            
                def __iter__(self):
                    return _ArrayIterator(self._elements)
            
            
            class _ArrayIterator:
                def __init__(self, items):
                    self._items = items
                    self._idx = 0
            
                def __iter__(self):
                    return self
            
                def __next__(self):
                    if self._idx < len(self._items):
                        val = self._items[self._idx]
                        self._idx += 1
                        return val
                    else:
                        raise StopIteration
            
            
            class HashMap:
                """ HashMap ADT实现，类似于python内置的dict
                一个槽有三种状态：
                1.从未使用 HashMap.UNUSED。此槽没有被使用和冲突过，查找时只要找到UNUSEd就不用再继续探查了
                2.使用过但是remove了，此时是 HashMap.EMPTY，该探查点后边的元素扔可能是有key
                3.槽正在使用 _MapEntry节点
                """
            
                class _MapEntry:    # 槽里存储的数据
                    def __init__(self, key, value):
                        self.key = key
                        self.value = value
            
                UNUSED = None    # 没被使用过的槽，作为该类变量的一个单例，下边都是is 判断
                EMPTY = _MapEntry(None, None)     # 使用过但是被删除的槽
            
                def __init__(self):
                    self._table = Array(7)    # 初始化7个槽
                    self._count = 0
                    # 超过2/3空间被使用就重新分配，load factor = 2/3
                    self._maxCount = len(self._table) - len(self._table) // 3
            
                def __len__(self):
                    return self._count
            
                def __contains__(self, key):
                    slot = self._findSlot(key, False)
                    return slot is not None
            
                def add(self, key, value):
                    if key in self:    # 覆盖原有value
                        slot = self._findSlot(key, False)
                        self._table[slot].value = value
                        return False
                    else:
                        slot = self._findSlot(key, True)
                        self._table[slot] = HashMap._MapEntry(key, value)
                        self._count += 1
                        if self._count == self._maxCount:    # 超过2/3使用就rehash
                            self._rehash()
                        return True
            
                def valueOf(self, key):
                    slot = self._findSlot(key, False)
                    assert slot is not None, 'Invalid map key'
                    return self._table[slot].value
            
                def remove(self, key):
                    """ remove操作把槽置为EMPTY"""
                    assert key in self, 'Key error %s' % key
                    slot = self._findSlot(key, forInsert=False)
                    value = self._table[slot].value
                    self._count -= 1
                    self._table[slot] = HashMap.EMPTY
                    return value
            
                def __iter__(self):
                    return _HashMapIteraotr(self._table)
            
                def _slot_can_insert(self, slot):
                    return (self._table[slot] is HashMap.EMPTY or
                            self._table[slot] is HashMap.UNUSED)
            
                def _findSlot(self, key, forInsert=False):
                    """ 
                    Args:
                        forInsert (bool): if the search is for an insertion
                    Returns:
                        slot or None
                    """
                    slot = self._hash1(key)
                    step = self._hash2(key)
                    _len = len(self._table)
            
                    if not forInsert:    # 查找是否存在key
                        while self._table[slot] is not HashMap.UNUSED:
                            # 如果一个槽是UNUSED，直接跳出
                            if self._table[slot] is HashMap.EMPTY:
                                slot = (slot + step) % _len
                                continue
                            elif self._table[slot].key == key:
                                return slot
                            slot = (slot + step) % _len
                        return None
            
                    else:    # 为了插入key
                        while not self._slot_can_insert(slot):    # 循环直到找到一个可以插入的槽
                            slot = (slot + step) % _len
                        return slot
            
                def _rehash(self):    # 当前使用槽数量大于2/3时候重新创建新的table
                    origTable = self._table
                    newSize = len(self._table) * 2 + 1    # 原来的2*n+1倍
                    self._table = Array(newSize)
            
                    self._count = 0
                    self._maxCount = newSize - newSize // 3
            
                    # 将原来的key value添加到新的table
                    for entry in origTable:
                        if entry is not HashMap.UNUSED and entry is not HashMap.EMPTY:
                            slot = self._findSlot(entry.key, True)
                            self._table[slot] = entry
                            self._count += 1
            
                def _hash1(self, key):
                    """ 计算key的hash值"""
                    return abs(hash(key)) % len(self._table)
            
                def _hash2(self, key):
                    """ key冲突时候用来计算新槽的位置"""
                    return 1 + abs(hash(key)) % (len(self._table)-2)
            
            
            class _HashMapIteraotr:
                def __init__(self, array):
                    self._array = array
                    self._idx = 0
            
                def __iter__(self):
                    return self
            
                def __next__(self):
                    if self._idx < len(self._array):
                        if self._array[self._idx] is not None and self._array[self._idx].key is not None:
                            key = self._array[self._idx].key
                            self._idx += 1
                            return key
                        else:
                            self._idx += 1
                    else:
                        raise StopIteration
            
            
            def print_h(h):
                for idx, i in enumerate(h):
                    print(idx, i)
                print('\n')
            
            
            if __name__ == "__main__":
            
                def test_HashMap():
                    """ 一些简单的单元测试，不过测试用例覆盖不是很全面 """
                    h = HashMap()
                    assert len(h) == 0
                    h.add('a', 'a')
                    assert h.valueOf('a') == 'a'
                    assert len(h) == 1
                
                    a_v = h.remove('a')
                    assert a_v == 'a'
                    assert len(h) == 0
                
                    h.add('a', 'a')
                    h.add('b', 'b')
                    assert len(h) == 2
                    assert h.valueOf('b') == 'b'
                    b_v = h.remove('b')
                    assert b_v == 'b'
                    assert len(h) == 1
                    h.remove('a')
                    assert len(h) == 0
                
                    n = 10
                    for i in range(n):
                        h.add(str(i), i)
                    assert len(h) == n
                    print_h(h)
                    for i in range(n):
                        assert str(i) in h
                    for i in range(n):
                        h.remove(str(i))
                    assert len(h) == 0 
        
        
""" Binary Tree 二叉树 """

    数（tree） 是一种抽象的数据类型(ADT)，或是实作这种抽象数据类型的数据结构，用来模拟
    具有树状结构性质的数据集合。 它是由 n(n >= 1) 个有限节点组成一个具有层次关系的集合。
    
    它具有如下特点：
    
        每个节点有零个或多个子节点
        没有父节点的节点是根节点
        每个非根节点有且只有一个父节点
        除了根节点外，每个子节点可以分为多个不相交的子树。
    
    树的术语：
    
        节点的度：一个节点含有的子树的个数称为该节点的度
        树的度：一颗树中， 最大的节点的度称为树的度
        叶节点或终端节点：度为零的节点。
        父亲节点或父节点：若一个节点含有子节点，则这个节点称为其子节点的父节点；
        孩子节点或子节点：一个节点含有的子树的根节点称为该节点的子节点；  
        兄弟节点：具有相同父节点的节点互称为兄弟节点；
        节点的层次：从根开始定义起，根为第1层，根的子节点为第2层，以此类推；    
        树的高度或深度：树中节点的最大层次；
        堂兄弟节点：父节点在同一层的节点互为堂兄弟；
        节点的祖先：从根到该节点所经分支上的所有节点；
        子孙：以某节点为根的子树中任一节点都称为该节点的子孙。
        森林：由m（m>=0）棵互不相交的树的集合称为森林；      
        
    树的种类：
        
        无序树：树中任意节点的子节点之间没有顺序关系，这种树称为无序树，也称为自由树；
        有序树：树中任意节点的子节点之间有顺序关系，这种树称为有序树；
        二叉树：每个节点最多含有两个子树的树称为二叉树；
        完全二叉树：对于一颗二叉树，假设其深度为d(d>1)。除了第d层外，其它各层的节点数目均已达最大值，且第d层所有节点从左向右连续地紧密排列，这样的二叉树被称为完全二叉树，其中满二叉树的定义是所有叶节点都在最底层的完全二叉树;
        平衡二叉树（AVL树）：当且仅当任何节点的两棵子树的高度差不大于1的二叉树；
        排序二叉树（二叉查找树（英语：Binary Search Tree），也称二叉搜索树、有序二叉树）；
        霍夫曼树（用于信息编码）：带权路径最短的二叉树称为哈夫曼树或最优二叉树；
        B树：一种对读写操作进行优化的自平衡的二叉查找树，能够保持数据有序，拥有多余两个子树。
    
    二叉树:
        
        二叉树是每个节点最多有两个子树的树结构。通常子树被称作“左子树”（left subtree）和“右子树”（right subtree）
        
        二叉树的性质(特性)--> 这个和 棋盘的性质是一样的。
            
            性质1：在二叉树的第 i 层上至多有 2^(i - 1) 个节点(i > 0)
            性质2：深度为k的二叉树至多有 2^k - 1 个节点 （k > 0）
            性质3：对于任意一颗二叉树，如果其叶节点数为 N0, 而度数为2的节点总数为 N2, 则 N0 = N2 + 1(根节点)
            性质4：具有 n 个节点是完全二叉树的深度必须为 log2(n + 1)
            性质5：对完全二叉树，若从上至下、从左至右编号，则编号为i 的结点，
                  其左孩子编号必为2i，其右孩子编号必为2i＋1；其双亲的编号必为i/2（i＝1 时为根,除外）
    
    二叉树的实现（使用列表）:
           
        # 通过使用Node类中定义三个属性，分别为elem本身的值，还有lchild左孩子和rchild右孩子
        
        class Node_Tree(object):

            def __init__(self, elem = -1, lchild = None, rchild = None):
                self.elem = elem
                self.lchild = lchild
                self.rchild = rchild    
        
        # 树的创建,创建一个树的类，并给一个root根节点，一开始为空，随后添加节点
        
        class Tree(object):
            """树类"""
            def __init__(self, root=None):
                self.root = root
        
            def add(self, elem):
                """为树添加节点"""
                node = Node(elem)
                #如果树是空的，则对根节点赋值
                if self.root == None:
                    self.root = node
                else:
                    queue = []
                    queue.append(self.root)
                    #对已有的节点进行层次遍历
                    while queue:
                        #弹出队列的第一个元素
                        cur = queue.pop(0)
                        if cur.lchild == None:
                            cur.lchild = node
                            return
                        elif cur.rchild == None:
                            cur.rchild = node
                            return
                        else:
                            #如果左右子树都不为空，加入队列继续判断
                            queue.append(cur.lchild)
                            queue.append(cur.rchild)
    # 先序遍历 在先序遍历中，我们先访问根节点，
    # 然后递归使用先序遍历访问左子树，再递归使用先序遍历访问右子树                    
                   
           #根节点->左子树->右子树
           def preorder(self, root):
                """递归实现先序遍历"""
                if root == None:
                    return
                print root.elem
                self.preorder(root.lchild)
                self.preorder(root.rchild)           
           
           # 左子树->根节点->右子树
           # 中序遍历 在中序遍历中，我们递归使用中序遍历访问左子树，
           # 然后访问根节点，最后再递归使用中序遍历访问右子树
           def inorder(self, root):
              """递归实现中序遍历"""
              if root == None:
                  return
              self.inorder(root.lchild)
              print root.elem
              self.inorder(root.rchild) 
            
           # 左子树->右子树->根节点
           # 后序遍历 在后序遍历中，我们先递归使用后序遍历访问左子树和右子树，最后访问根节点
           def postorder(self, root):
              """递归实现后续遍历"""
              if root == None:
                  return
              self.postorder(root.lchild)
              self.postorder(root.rchild)
              print root.elem
              
        if __name__ == '__main__':   
                T = Tree()
                T.add(1)
                T.add(2)
                T.add(3)
                T.preorder(T.root)   
              
         
        
        
        
    
        
         
       
                           
                
       
    
       
          
        
                
            
               
           
        
        
               
       
    
    
    
    







"---------------------------------------------------------------------------"   










   
   
   
   
   
   
   
    

