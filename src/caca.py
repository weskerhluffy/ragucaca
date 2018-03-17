'''
# Sample code to perform I/O:
 
name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT
 
# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
 
 # XXX: https://www.hackerearth.com/practice/algorithms/sorting/heap-sort/practice-problems/algorithm/raghu-vs-sayan/
 
# Write your code here
from itertools import accumulate
from math import floor
from bisect import bisect_right
 
def parent_idx(n):
    return (n - 1) >> 1
 
def left_child_idx(n):
    return (n << 1) + 1
 
def right_child_idx(n):
    return left_child_idx(n) + 1
 
def swap(a, i, j):
    a[i], a[j] = a[j], a[i]
 
def heapify(a, idx, hsize):
    while idx < hsize:
        lc_idx = left_child_idx(idx)
        rc_idx = right_child_idx(idx)
        
        i = idx
        if lc_idx < hsize and a[lc_idx] >= a[i]:
            i = lc_idx
        if rc_idx < hsize and a[rc_idx] >= a[i]:
            i = rc_idx
        
        if i == idx:
            break
        
        swap(a, i, idx)
        idx = i
          
def valida_heap(a, ini):
    for i in range(ini, len(a)):
        assert left_child_idx(i) > len(a) - 1 or a[i] >= a[left_child_idx(i)] , "fallo i {} {} hi {} {} ".format(i, a[i], left_child_idx(i), a[left_child_idx(i)])
        assert right_child_idx(i) > len(a) - 1 or a[i] >= a[right_child_idx(i)], "fallo i {} {} hd {} {} ".format(i, a[i], right_child_idx(i), a[right_child_idx(i)])
def build_heap(a):
    hsize = len(a)
    for i in range(floor(hsize / 2 - 1), -1, -1):
        heapify(a, i, hsize)
#        valida_heap(a, i)
    
def hsort(a):
    hsize = len(a)
    build_heap(a)
    for i in range(hsize):
        swap(a, 0, hsize - i - 1)
        heapify(a, 0, hsize - i - 1)
 
def bsearchi(a, i, j, n):
    if i == j:
        if n >= a[i]:
            return i
        else:
            return max(0, i - 1)
    mid = i + ((j - i) >> 1)
    if n < a[mid]:
        return bsearchi(a, i, max(i, mid - 1), n)
    else:
        if n > a[mid]:
            return bsearchi(a, min(mid + 1, j), j, n)
        else:
            return mid
 
def heapsort( aList ):
  # convert aList to heap
  length = len( aList ) - 1
  leastParent = length // 2
  for i in range ( leastParent, -1, -1 ):
    moveDown( aList, i, length )
 
  # flatten heap into sorted array
  for i in range ( length, 0, -1 ):
    if aList[0] > aList[i]:
      swap( aList, 0, i )
      moveDown( aList, 0, i - 1 )
 
 
def moveDown( aList, first, last ):
  largest = 2 * first + 1
  while largest <= last:
    # right child exists and is larger than left child
    if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
      largest += 1
 
    # right child is larger than parent
    if aList[largest] > aList[first]:
      swap( aList, largest, first )
      # move down to largest child
      first = largest;
      largest = 2 * first + 1
    else:
      return # force exit
 
 
            
def bsearch(a, n):
    return bsearchi(a, 0, len(a) - 1, n)
 
def accumular(a):
    for i in range(1, len(a)):
        a[i] += a[i - 1]
 
def solve(dishes, rlimit, slimit):
#    tmp = list(sorted(dishes))
# muy lento el heapsort , el sorting de python si pasa, es una mamada
    hsort(dishes)
#    assert dishes == tmp, "{} {}".format(dishes, tmp)
#    tmp = list(accumulate(dishes))
    accumular(dishes)
#    assert dishes == tmp, "{} {}".format(dishes, tmp)
    dishes = [0] + dishes
#    rdishes = dishes[bsearch(dishes, rlimit)]
#    sdishes = dishes[bsearch(dishes, slimit)]
    rdishes = dishes[max(bisect_right(dishes, rlimit)-1,0)]
    sdishes = dishes[max(bisect_right(dishes, slimit)-1,0)]
 
    if rdishes > sdishes:
        return "Raghu Won"
    else:
        if sdishes > rdishes:
            return "Sayan Won"
        else:
            return "Tie"
 
t = int(input())
for _ in range(t):
    a, b, n = map(int, input().strip().split(" "))
    d = list(map(int, input().strip().split(" ")))
    print(solve(d, a, b))