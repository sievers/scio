import numpy
import os

def append(arr,fname,overwrite=False):
    asdf='abc'
    assert(type(fname)==type(asdf))
    asdf=numpy.zeros(2)
    assert(type(arr)==type(asdf))
    if overwrite:
        os.system('rm  ' + fname)
        
    if (os.path.isfile(fname)):
        f=open(fname,'a')
        arr.tofile(f)
        f.close()
    else:
        print 'creating ' + fname
        f=open(fname,'w')
        sz=arr.shape
        myvec=numpy.zeros(len(sz)+2,dtype='int32')
        myvec[0]=len(sz)
        for i in range(len(sz)):
            myvec[i+1]=sz[i]
        myvec[-1]=dtype2int(arr)
        #print myvec
        #print sz
        #print type(myvec)
        myvec.tofile(f)
        arr.tofile(f)
        f.close()

def read(fname):
    f=open(fname)
    ndim=numpy.fromfile(f,'int32',1)
    sz=numpy.fromfile(f,'int32',ndim)
    mytype=numpy.fromfile(f,'int32',1)
    vec=numpy.fromfile(f,dtype=int2dtype(mytype))
    nmat=vec.size/numpy.product(sz)
    new_sz=numpy.zeros(sz.size+1,dtype='int32')
    new_sz[0]=nmat
    new_sz[1:]=sz


    mat=numpy.reshape(vec,new_sz)
                      
    return mat

def int2dtype(myint):
    if (myint==8):
        return 'float64'
    if (myint==4):
        return 'float32'
    if (myint==-4):
        return 'int32'
    if (myint==-8):
        return 'int64'
    
    
def dtype2int(dtype_str):
    
    if (type(dtype_str)!=numpy.dtype):
        dtype_str=dtype_str.dtype

    aa=numpy.zeros(1,dtype='float64')
    if (dtype_str==aa.dtype):
        return 8

    aa=numpy.zeros(1,dtype='float32')
    if (dtype_str==aa.dtype):
        return 4
    

    aa=numpy.zeros(1,dtype='int32')
    if (dtype_str==aa.dtype):
        return -4
    
    aa=numpy.zeros(1,dtype='int64')
    if (dtype_str==aa.dtype):
        return -8
    
    print 'unknown dtype'
    return 0

