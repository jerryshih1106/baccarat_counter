import multiprocessing
from multiprocessing import Process

def do_in_multiprocess(func, arg_list:list):
    mp_context = multiprocessing.get_context('spawn')
    p = mp_context.Process(target=func, args=arg_list)
    p.start()

def do_mp(func, workers:int = 8, args:list = []):
    with multiprocessing.Pool(processes=workers) as pool:
        multiprocessing_output = pool.map(
            func,
            args,
        )
    return multiprocessing_output