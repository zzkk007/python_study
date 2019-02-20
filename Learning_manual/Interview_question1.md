
1、Python 下多线程的限制以及多进程中传递参数的方式？

    python多线程有个全局解释器锁（global interpreter lock），
    这个锁的意思是任一时间只能有一个线程使用解释器，跟单cpu跑多个程序一个意思，
    大家都是轮着用的，这叫“并发”，不是“并行”。    
    
    多进程间共享数据，可以使用 multiprocessing.Value 和 multiprocessing.Array
    
2、    