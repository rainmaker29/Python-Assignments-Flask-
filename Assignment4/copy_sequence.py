import time
start = time.time()
with open("6_AA_SI.mp4","rb") as source,open("sequence_result/res.mp4","wb") as destination:
    destination.write(source.read())

with open("6_AA_SI.mp4","rb") as source,open("sequence_result/res2.mp4","wb") as destination:
    destination.write(source.read())

with open("6_AA_SI.mp4","rb") as source,open("sequence_result/res3.mp4","wb") as destination:
    destination.write(source.read())


print("Time taken = ",time.time()-start)

