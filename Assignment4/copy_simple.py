import time
import threading
import shutil
source = "/mnt/EAB869F8B869C423/Notebooks/PreIntern/assignments/video_copy/6_AA_SI.mp4"
destination = "/mnt/EAB869F8B869C423/Notebooks/PreIntern/assignments/video_copy/simple_result/"
destination2 = "/mnt/EAB869F8B869C423/Notebooks/PreIntern/assignments/video_copy/seqeunce_result/"
destination3 = "/mnt/EAB869F8B869C423/Notebooks/PreIntern/assignments/video_copy/concurrent_result/"


t1 = threading.Thread(target=shutil.copy,args=(source,destination))
start = time.time()
t1.start()
print("Time taken = ",time.time()-start)

print("---------------------------------")

t2 = threading.Thread(target=shutil.copy,args=(source,destination,destination2,destination3))
start = time.time()
t2.start()
print("Time taken = ",time.time()-start)

