'''
Algorithm

Specific set of instructions that are unambiguous
Instructions not a code solution
Accomplish the same goal every time
Have a defined input and output


'''
l = [1,5,3,6,2345,234,3456,164,723,1398,2,4,5,4,6,2,5,8,4, 45,26,78,93]


def merge_sort(list_, left, right):
    """
    MergeSort Recursive Method
    """
    if len(list_) is 0:
        return
    #Stop condition for the recursion
    if right <= left:
        return
    else:
        mid = (right + left) / 2 #Middle point
        merge_sort(list_, left, mid) #Sort left half
        merge_sort(list_, mid+1, right) #Sort right half
        merge(list_,left, mid, right) #Merge left and right sides

def merge(a, left, mid, right):
    """
    Merge fuction
    """
    #Copy array
    copy_list = []
    i, j = left, mid + 1
    ind = left
    
    while ind < right+1:
        
        #if left array finish merging, copy from right side
        if i > mid:
            copy_list.append(a[j])
            j +=1
        #if right array finish merging, copy from left side
        elif j > right:
            copy_list.append(a[i])
            i +=1
        #Check if right array value is less than left one
        elif a[j] < a[i]:
            copy_list.append(a[j])
            j +=1
        else:
            copy_list.append(a[i])
            i +=1
        ind +=1
        
    ind=0
    for x in (xrange(left,right+1)):
        a[x] = copy_list[ind]
        ind += 1



def merge_sort(list_):
    """
    MergeSort Recursive Method
    """
    if len(list_) is 0:
        return
    #Stop condition for the recursion
    if right <= left:
        return
    else:
        mid = (right + left) / 2 #Middle point
        merge_sort(list_[:mid+1]) #Sort left half
        merge_sort(list_[mid+1:]) #Sort right half
        merge(list_,left, mid, right) #Merge left and right sides

def merge(a, left, mid, right):
    """
    Merge fuction
    """
    #Copy array
    copy_list = []
    i, j = left, mid + 1
    ind = left
    
    while ind < right+1:
        
        #if left array finish merging, copy from right side
        if i > mid:
            copy_list.append(a[j])
            j +=1
        #if right array finish merging, copy from left side
        elif j > right:
            copy_list.append(a[i])
            i +=1
        #Check if right array value is less than left one
        elif a[j] < a[i]:
            copy_list.append(a[j])
            j +=1
        else:
            copy_list.append(a[i])
            i +=1
        ind +=1
        
    ind=0
    for x in (xrange(left,right+1)):
        a[x] = copy_list[ind]
        ind += 1

def CountingSort(l):
    #create key
    temp = []
    for i in xrange(max(l)+1):
        temp.append(0)
    for i in l:
        temp[i] += 1
    del(l)
    l = []
    for i in xrange(len(temp)):
        for j in xrange(temp[i]):
            l.append(i)
    return l
'''
def MergeSort(l):
    #Split list in two
    #Split until list is length <= 1
    #
'''
def QuickSort(l):
    def qsort(l):
        left = []
        right = []
        if len(l) == 1:
            return l
        if len(l) == 0:
            return
        else:
            pivot = l[int(len(l)/2)]
            flag = False
            for i in l:
                if i < pivot:
                    left.append(i)
                elif i > pivot:
                    right.append(i)
                if i == pivot:
                    if flag:
                        left.append(i)
                    else:
                        flag = True
                #print l, left, pivot, right
            return [qsort(left), pivot, qsort(right)]

    def x(l, newL):
        if len(l) ==1:
            newL.append(l[0])
            return
        if len(l) == 0:
            return
        for i in xrange(len(l)):
            if type(l[i]) == list:
                x(l[i], newL)
            else:
                if l[i] != None:
                    newL.append(l[i])
    newList = []
    sortL = qsort(l)
    x(sortL, newList)
    return newList

def QuickSortKey(list, key):
    #Sorting algorithm
    def qsort(l):
        #new list for items to left of pivot
        left = []
        
        #new list for items to right of pivot
        right = []

        #New list for items equal to the pivot
        equal = []

        #Returns if only one item or no items in list
        if len(l) == 1:
            return l
        if len(l) == 0:
            return
        else:
            #The center item is the pivot
            pivot = l[int(len(l)/2)][key]

            #Loops for each element in list
            for i in xrange(len(l)):
                #Checks if the items is the pivot
                if i != int(len(l)/2):
                    #Adds the item to the left or right lists according to if it is smaller or greater than than the pivot
                    if l[i][key] < pivot:
                        left.append(l[i])
                    elif l[i][key] > pivot:
                        right.append(l[i])
                    else:
                        #Adds to left list if equal to pivot
                        equal.append(l[i])
                    #print l, left, pivot, right
            equal.append(pivot)
            #Returns partially-sorted list
            return [qsort(left), equal, qsort(right)]

    #Reformatting algorithm
    def x(l, newL):
        #If there is only one item in the list,
        if len(l) ==1:
            #Add the item to the new list
            newL.append(l[0])
            return

        #Does nothing if no items in list
        if len(l) == 0:
            return

        #Loops for each item in list
        for i in xrange(len(l)):
            #If the item is a list
            if type(l[i]) == list:
                #Runs method again through the inner list
                x(l[i], newL)
            else:
                #If item exists,
                if l[i] != None:
                    #Add the item to the new list
                    newL.append(l[i])

    #Sorts the list using sorting algorithm, creates a new list that holds the sorted list
    sortL = qsort(l, key)

    #New list as the finished product
    newList = []

    #Reformats the list into the new list
    x(sortL, newList)

    #Returns the finished product
    return newList

def InsertionSort(l):
    for i in xrange(1,len(l)):
        index = -1
        for j in xrange(i-1, -1, -1):
            if l[i]>=l[j]:
                index = j+1
                break
        if index == -1:
            index = 0
        l.insert(index, l.pop(i))

def InsertionSortKey(l, key):
    for i in xrange(1,len(l)):
        index = -1
        for j in xrange(i-1, -1, -1):
            if l[i][key]>=l[j][key]:
                index = j+1
                break
        if index == -1:
            index = 0
        l.insert(index, l.pop(i))

def SelectionSort(l):
    for i in xrange(0,len(l)):
        smallest = i
        for j in xrange(i,len(l[i:])+i):
            if l[j] < l[smallest]:
                smallest = j
        #smallest = l[i:].index(min(l[i:]))
        temp = l[i]
        l[i] = l[smallest]
        l[smallest] = temp

def SelectionSortKey(l, key):
    for i in xrange(0,len(l)):
        smallest = i
        for j in xrange(i,len(l[i:])+i):
            if l[j][key] < l[smallest][key]:
                smallest = j
        #smallest = l[i:].index(min(l[i:]))
        temp = l[i]
        l[i] = l[smallest]
        l[smallest] = temp
        
def SelectionSort(l):
    for i in xrange(1, len(l)):
        l.insert(i, l.pop(l.index(min(l[i:]), i)))

def RadixSort(l):
    power = 1
    while(max(l)/pow(10, power-1) != 0):
        rad = []
        for i in xrange(10):
            rad.append([])
        for i in l:
            rad[(i/pow(10, power-1))%10].append(i)
        l = []
        for i in rad:
            for j in i:
                l.append(j)
        power += 1
    return l

def BinarySearch(l, item):
    if len(l) == 0:
        return -1
    if l != QuickSort(l):
        return -1
    mid = len(l)/2
    if l[mid] == item:
        return mid
    elif l[mid] < item:
        temp = BinarySearch(l[mid+1:], item)
        if temp == -1:
            return -1
        else:
            return mid+1+temp
    else:
        temp = BinarySearch(l[:mid], item)
        if temp == -1:
            return -1
        else:
            return temp

def BinarySearchLoop(l, item):
    L = 0
    R = len(l)-1
    m = len(l)/2
    while(l[m] != item):
        #print L, m, R, item
        if m == R or m == L:
            if l[R] == item:
                return R
            if l[L] == item:
                return L
            return -1
        if l[m] < item:
            L = m+1
        else:
            R = m-1
        m = (R+L)/2
    return m


def BinarySearchLoopKey(l, item, key):
    L = 0
    R = len(l)-1
    m = len(l)/2
    while(l[m][key] != item):
        #print L, m, R, item
        if m == R or m == L:
            if l[R][key] == item:
                return R
            if l[L][key] == item:
                return L
            return -1
        if l[m][key] < item:
            L = m+1
        else:
            R = m-1
        m = (R+L)/2
    return m

#BinarySearch([1, 2, 4,5, 8, 10, 14, 25, 30], 30)
