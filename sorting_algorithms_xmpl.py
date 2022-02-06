import random
import time

def measure(func):
    def inner(*args,**kwargs):
        t1 = time.time()
        result = func(*args,**kwargs)
        t2 = time.time()
        print(func.__name__,f'execution time: {round(t2-t1,5)}s')
        return result
    return inner



def fill(data:list, size:int, m_num:int)->None:
    for i in range(size):
        data.append(random.randint(0,m_num))


def merge(a,b) -> list:
    if not isinstance(a,list):
        a = [a]
    if not isinstance(b,list):
        b = [b]

    res = []
    while len(a) != 0 and len(b) != 0:
        if(a[0] < b[0]):
            res.append(a[0])
            del a[0]
        else:
            res.append(b[0])
            del b[0]
    if len(a) != 0:
        for x in a:
            res.append(x)
        del a
    if len(b) != 0:
        for x in b:
            res.append(x)
        del b
    return res

@measure
def mergeSort(tosort:list) -> list:
    if(len(tosort)==0):
        return list
    else:
        return _mergeSort(tosort)

def _mergeSort(tosort:list) -> list:
    if(len(tosort)>1):
        _tosort = []
        for idx in range(0,len(tosort),2):
            if idx+1 > len(tosort)-1:
                break
            _tosort.append(merge(tosort[idx],tosort[idx+1]))
        if(len(tosort)%2 != 0):
            _tosort.append(tosort.pop())
        del tosort
        return _mergeSort(_tosort)
    else:
        return tosort[0]

@measure
def quickSort(tosort:list) ->list:
    return _quickSort(tosort)
    
def _quickSort(tosort:list) ->list:
    L = []
    E = [tosort.pop()]
    G = []
    for val in tosort:
        if val <= E[0] :
            L.append(val)
        else:
            G.append(val)
    if len(L) > 1 and len(G) > 1 :
        return _quickSort(L) + E + _quickSort(G)
    if len(L) > 1:
        return _quickSort(L) + E + G
    if len(G) > 1:
        return L + E + _quickSort(G)
    else:
        return L + E + G

@measure
def bubbleSort(data:list)->None:
    sorted = False
    idx = 1
    while not sorted:
        sorted = True
        for i in range(len(data)-idx):
            if data[i] > data[i+1]:
                sorted = False
                tmp = data[i]
                data[i] = data[i+1]
                data[i+1] = tmp
        idx += 1

@measure
def radixSort(data:list, base:int) -> None:
    buffer = []
    for i in range(base):
        buffer.append([])
    sorted = False
    indx = 0
    while not sorted:
        sorted = True
        for i in range(len(data)):
            digit = data[i]%base**(indx+1)//base**indx
            if (digit != 0):
                sorted = False
                buffer[digit].append(data[i])
            else:
                buffer[0].append(data[i])
        indx += 1
        index = 0
        for i in range(base):
            while len(buffer[i]) != 0:
                content = buffer[i][0]
                buffer[i].remove(content)
                data[index] = content
                index += 1


data1 = []
data2 = []
data3 = []
data4 = []
length = 10000
fill(data1,length,length)
fill(data2,length,length)
fill(data3,length,length)
fill(data4,length,length)
bubbleSort(data1)
radixSort(data2,10)
data3 = mergeSort(data3)
data4 = quickSort(data4)
# print(data1)
# print(data2)
# print(data3)
# print(data4)
