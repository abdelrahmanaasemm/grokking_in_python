def main():
    listt= [1,3,33,332,334,545,646,657,878,998]
    index=  binarysearch(listt,545)
    print(index)
def binarysearch(listt,item):
    low=0
    high= (len(listt)) - 1
    while low<=high :
        mid = int((low + high) / 2)
        if item==listt[mid]:
            return mid
        elif item >listt[mid]:
            low = mid +1
        elif item <listt[mid]:
            high=mid-1

    return -1


















main()