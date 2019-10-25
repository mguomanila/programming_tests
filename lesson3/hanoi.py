import time
# tower of hanoi
def hanoi(disc,src,aux,dst):
    #start = time.clock()
    if(disc > 0):
        hanoi(disc-1,src,dst,aux)
        #print('Move disc %s from %s to %s' % (disc,src,dst))
        hanoi(disc-1,aux,src,dst)
    #print('time: %fs' % (time.clock()-start))
