import random

stack = [ ]

def quicksort(left, right):
    a=(left,right)
    stack.append(a)
    print("Call:   ",stack)
    if left<right:
        position = random.randint(left, right)
        quicksort(left, position-1)
        quicksort(position+1, right)
    stack.pop()
    print("Return:   ",stack)

def main( ):
    n = eval(input("Enter length of list: "))
    print("Tracing stack of recursive calls for Quicksort:")
    quicksort(0, n-1)
    

if __name__ == '__main__':
    main( )
    
