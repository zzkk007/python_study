"---------------------------------------------"

				Python Web 学习	

	书本：https://python-web-guide.readthedocs.io/zh/latest/index.html
	作者公众号：PegasusWang


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
