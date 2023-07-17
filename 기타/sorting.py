# 202055513 김대영 컴퓨터 알고리즘 : Sorting
import random
import sys

def qs(tLi) :
    if len(tLi) <= 1:
        return tLi
    pivot = tLi[len(tLi) // 2]
    lesser_li, equal_li, greater_li = [], [], []
    for num in tLi:
        if num < pivot:
            lesser_li.append(num)
        elif num > pivot:
            greater_li.append(num)
        else:
            equal_li.append(num)
    return qs(lesser_li) + equal_li + qs(greater_li)

def ms(tLi):
    if len(tLi) < 2:
        return tLi

    mid = len(tLi) // 2
    low_li = ms(tLi[:mid])
    high_li = ms(tLi[mid:])
    # Devide

    merged_li = []
    l = h = 0
    while l < len(low_li) and h < len(high_li):
        if low_li[l] < high_li[h]:
            merged_li.append(low_li[l])
            l += 1
        else:
            merged_li.append(high_li[h])
            h += 1
    merged_li += low_li[l:]
    merged_li += high_li[h:]
    # Conquer
    return merged_li

def hs(tLi):
    n = len(tLi)

    for i in range(1, n):
        child = i
        while child != 0:
            parent = (child-1)//2
            if tLi[parent] < tLi[child]:
                tLi[parent], tLi[child] = tLi[child], tLi[parent]
            child = parent 

    for node in range(n-1, -1, -1):
        tLi[0], tLi[node] = tLi[node], tLi[0]
        parent = 0
        child = 1

        while child < node:
            child = parent*2 + 1
            if child < node-1 and tLi[child] < tLi[child+1]:
                child += 1
            if child < node and tLi[parent] < tLi[child]:
                tLi[parent], tLi[child] = tLi[child], tLi[parent]

            parent = child

    return tLi

class Sorting :
    def __init__(self) :
        self.__unsorted_list = []
    
    def print_list(self) :
        for n in self.__unsorted_list :
            sys.stdout.write(str(n))
            sys.stdout.write(' ')
        sys.stdout.write('\n')
        
    def create_list(self) :
        self.__unsorted_list.clear()
        for i in range(0, 10) :
            number = random.randint(1, 100) 
            self.__unsorted_list.append(number) 
        self.print_list()
        
    def bubble_sort(self) :
        sys.stdout.write("---Bubble Sort---\n")
        sys.stdout.write("unsorted list : ")
        self.create_list()
        for i in range(9, 0, -1) :
            for j in range(0, i) :
                if self.__unsorted_list[j] > self.__unsorted_list[j+1] :
                    self.__unsorted_list[j], self.__unsorted_list[j+1] = self.__unsorted_list[j+1], self.__unsorted_list[j]
        sys.stdout.write("sorted list   : ")
        self.print_list()
    
    def insertion_sort(self) :
        sys.stdout.write("---Insertion Sort---\n")
        sys.stdout.write("unsorted list : ")
        self.create_list()
        for i in range(1, 10) :
            for j in range(i, 0, -1) :
                if self.__unsorted_list[j-1] > self.__unsorted_list[j] :
                    self.__unsorted_list[j-1], self.__unsorted_list[j] = self.__unsorted_list[j], self.__unsorted_list[j-1]
                else :
                    break
        sys.stdout.write("sorted list   : ")
        self.print_list()
    
    def selection_sort(self) :
        sys.stdout.write("---Selection Sort---\n")
        sys.stdout.write("unsorted list : ")
        self.create_list()
        for i in range(0, 9) :
            mi = i
            for j in range(i+1, 10) :
                if self.__unsorted_list[mi] > self.__unsorted_list[j] :
                    mi = j
            self.__unsorted_list[i], self.__unsorted_list[mi] = self.__unsorted_list[mi], self.__unsorted_list[i]
        sys.stdout.write("sorted list   : ")
        self.print_list()
        
    def quick_sort(self) :
        sys.stdout.write("---Quick Sort---\n")
        sys.stdout.write("unsorted list : ")
        self.create_list()
        self.__unsorted_list = qs(self.__unsorted_list)
        sys.stdout.write("sorted list   : ")
        self.print_list()
        
    
    def merge_sort(self) :
        sys.stdout.write("---Merge Sort---\n")
        sys.stdout.write("unsorted list : ")
        self.create_list()
        self.__unsorted_list = ms(self.__unsorted_list)
        sys.stdout.write("sorted list   : ")
        self.print_list()
    
    def heap_sort(self) :
        sys.stdout.write("---Heap Sort---\n")
        sys.stdout.write("unsorted list : ")
        self.create_list()
        self.__unsorted_list = hs(self.__unsorted_list)
        sys.stdout.write("sorted list   : ")
        self.print_list()
             
def main() :
    s1 = Sorting()
    s1.bubble_sort()
    s1.insertion_sort()
    s1.selection_sort()
    s1.quick_sort()
    s1.merge_sort()
    s1.heap_sort()
    
if __name__ == "__main__":
    main() 