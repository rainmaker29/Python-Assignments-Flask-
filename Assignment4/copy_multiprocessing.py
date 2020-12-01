import multiprocessing
import shutil

from copy_simple import source,destination,destination2,destination3

orgs = [source]
dests = [destination,destination2,destination3] 
num_cores = multiprocessing.cpu_count()
p = multiprocessing.Pool(num_cores)
operations =  [(x,y) for x in orgs for y in dests]
p.starmap(shutil.copy, operations)
p.close()
p.join()
