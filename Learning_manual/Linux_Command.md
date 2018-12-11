
"--------------------------------------------"

                Linux 命令
        
"--------------------------------------------"

 """让进程在后台可靠运行的几种方法"""
 
    1、nohup:
    
      nohup 的用途就是让提交的命令忽略 hangup 信号。
      让我们先来看一下 nohup 的帮助信息：  
      
        NAME
           nohup - run a command immune to hangups, with output to a non-tty
     
            SYNOPSIS
                nohup COMMAND [ARG]...
                nohup OPTION
             
            DESCRIPTION
                 Run COMMAND, ignoring hangup signals.
                 --help display this help and exit
                 --version
                    output version information and exit
      
       只需在要处理的命令前加上 nohup 即可，标准输出和标准错误缺省会被重定向到 nohup.out 文件中。
       一般我们可在结尾加上"&"来将命令同时放入后台运行，也可用">filename 2>&1"来更改缺省的重定向文件名。 
       
      nohup 示例:
        
        # nohup ping www.ibm.com &
    
    2、setsid:
    
        nohup 无疑能通过忽略 HUP 信号来使我们的进程避免中途被中断，
        但如果我们换个角度思考，如果我们的进程不属于接受 HUP 信号的终端的子进程，
        那么自然也就不会受到 HUP 信号的影响了。setsid 就能帮助我们做到这一点。    
        
        setsid 的帮助信息：
        
          NAME
            setsid - run a program in a new session
 
          SYNOPSIS
            setsid program [ arg ... ]
 
          DESCRIPTION
            setsid runs a program in a new session.  
        
          可见 setsid 的使用也是非常方便的，也只需在要处理的命令前加上 setsid 即可。
          
          setsid 示例
            # setsid ping www.ibm.com

    3、&:
    
        这里还有一个关于 subshell 的小技巧。我们知道，
        将一个或多个命名包含在“()”中就能让这些命令在子 shell 中运行中，
        从而扩展出很多有趣的功能，我们现在要讨论的就是其中之一。
        
        当我们将"&"也放入“()”内之后，我们就会发现所提交的作业并不在作业列表中，
        也就是说，是无法通过jobs来查看的。
        让我们来看看为什么这样就能躲过 HUP 信号的影响吧。
    
        subshell 示例:
         
            # (ping www.ibm.com &)
               
            
 """  """ 
 
 
       
         
               
        
        
           