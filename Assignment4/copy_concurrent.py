
def copy_sequence():
    start = time.time()
    with open("6_AA_SI.mp4","rb") as source,open("sequence_result/res.mp4","wb") as destination:
        destination.write(source.read())

    with open("6_AA_SI.mp4","rb") as source,open("sequence_result/res2.mp4","wb") as destination:
        destination.write(source.read())

    with open("6_AA_SI.mp4","rb") as source,open("sequence_result/res3.mp4","wb") as destination:
        destination.write(source.read())


    print("Time taken = ",time.time()-start)

def copy_concurrent():
    start = time.time()
    with open("6_AA_SI.mp4","rb") as source,open("concurrent_result/res.mp4","wb") as destination1, \
    open("concurrent_result/res2.mp4","wb") as destination2,\
    open("concurrent_result/res3.mp4","wb") as destination3:
        destination1.write(source.read())
        destination2.write(source.read())
        destination3.write(source.read())

    print("Time taken = ",time.time()-start)

