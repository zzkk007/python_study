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

                    第 五 章 用 Python 实现设计模式
    
"---------------------------------------------------------------------------"

   
   
   
   
   
   
   
   
   
   
   
   
   
   
    

