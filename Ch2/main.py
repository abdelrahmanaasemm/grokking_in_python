def selectionsort(listt):
    for counter in range((len(listt))-1):
        smallindex=counter
        for j in range(counter+1,len(listt)):
            if listt[smallindex]>listt[j]:
                smallindex=j
        listt[counter],listt[smallindex]=listt[smallindex],listt[counter]
    return listt
li=selectionsort([3,4,32,2,99,343,777,22,11,55,77,88])
print(li)













