import random
import time

print("---------------------------------------------------------------------------------------------------")
print("           Random1000    Reverse1000   Random10000    Reverse10000    Random100000    Reverse100000")
print("---------------------------------------------------------------------------------------------------")

#힙정렬
def heapSort(unsorted_list):
  parent_node = (int)((len(unsorted_list) - 2) / 2)
  
  for parent in range(parent_node, -1, -1):
      build_max_heap(unsorted_list, parent, len(unsorted_list) - 1)
      
  for sorted_num in range(len(unsorted_list) - 1, 0, -1):
      unsorted_list[sorted_num], unsorted_list[0] =\
          unsorted_list[0], unsorted_list[sorted_num]
      build_max_heap(unsorted_list, 0, sorted_num - 1)
  return unsorted_list

def build_max_heap(maxheap_list, parent, end):
  child = parent * 2 + 1
    
  while child <= end:
      if child + 1 <= end and maxheap_list[child] < maxheap_list[child + 1]:
          child += 1
        
      if maxheap_list[parent] < maxheap_list[child]:
          maxheap_list[parent], maxheap_list[child] =\
              maxheap_list[child], maxheap_list[parent]
          parent = child
          child = parent * 2 + 1
      else:
          break

#라이브러리(표준 라이브러리가 제공하는 정렬 알고리즘)
def library(a):
  a.sort()
  return a

#Random1000
n1 = [random.randint(1, 1000) for _ in range(1000)]
start_vect=time.time()
heapSort(n1)
hsn1 = (time.time() - start_vect)
start_vect=time.time()
library(n1)
lbn1 = (time.time() - start_vect)

#Reverse1000
n2 = []
for i in range(1000):
  n2.append(i+1)
n2.reverse()
start_vect=time.time()
heapSort(n2)
hsn2 = (time.time() - start_vect)
start_vect=time.time()
library(n2)
lbn2 = (time.time() - start_vect)

#Random10000
n3 = [random.randint(1, 10000) for _ in range(10000)]
start_vect=time.time()
heapSort(n3)
hsn3 = (time.time() - start_vect)
start_vect=time.time()
library(n3)
lbn3 = (time.time() - start_vect)

#Reverse10000
n4 = []
for i in range(1000):
  n4.append(i+1)
n4.reverse()
start_vect=time.time()
heapSort(n4)
hsn4 = (time.time() - start_vect)
start_vect=time.time()
library(n4)
lbn4 = (time.time() - start_vect)

#Random100000
n5 = [random.randint(1, 100000) for _ in range(100000)]
start_vect=time.time()
heapSort(n5)
hsn5 = (time.time() - start_vect)
start_vect=time.time()
library(n5)
lbn5 = (time.time() - start_vect)

#Reverse100000
n6 = []
for i in range(100000):
  n6.append(i+1)
n6.reverse()
start_vect=time.time()
heapSort(n6)
hsn6 = (time.time() - start_vect)
start_vect=time.time()
library(n6)
lbn6 = (time.time() - start_vect)

print("Heap       %f      %f      %f       %f        %f        %f"%(hsn1, hsn2, hsn3, hsn4, hsn5, hsn6))
print("Library    %f      %f      %f       %f        %f        %f"%(lbn1, lbn2, lbn3, lbn4, lbn5, lbn6))

print("---------------------------------------------------------------------------------------------------")
