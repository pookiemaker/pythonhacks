# works 90% of the way... 

import multiprocessing as mp
import time



def f(x):
    test = f.e.is_set()
    time.sleep(x)
    f.q.put('Doing: ' + str(x)+ ' :' + str(test))
    if x == 1:
        f.e.set()
        print('f(x): event : ', f.e.is_set())
    return x*x

def f_init(q, e):
    f.q = q
    f.e = e

def main():
    jobs = range(1,6)

    m = mp.Manager()  # setup event 
    e = m.Event()
    e.clear()

    q = mp.Queue()
    p = mp.Pool(None, f_init, [q,e])
    results = p.imap_unordered(f, jobs)
    p.close()

    print('before:',e.is_set())
    e.wait(3)
    print('after:',e.is_set())
    p.terminate()
    p.join()



    for i in range(q.qsize()):
        print q.get()
        print results.next()

if __name__ == '__main__':
    main()

