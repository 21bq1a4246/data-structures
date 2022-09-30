n=int(input("enter no.of elements to insert"))
l=[]
for i in range(0,n):
    ele=int(input("enter the elements:"))
    l.append(ele)
print(l)
low=int(input("enter low value:"))
high=int(input("enter high value:"))
key=int(input())
def binary_search(l,low,high,key):
    while low<=high:
        mid=(low+high)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:
            high=high-1
        else:
            low=low+1
    return -1
print("value of mid is",binary_search(l,low,high,key))