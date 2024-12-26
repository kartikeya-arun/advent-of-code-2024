#  Part 1

# import heapq

# leftHeap=[]
# rightHeap=[]

# with open('input.txt','r') as file:
#     lines=file.readlines()
#     freq={}
#     left=[]
#     for line in lines:
#         lineList=list(line.strip().split(' '))
#         heapq.heappush(leftHeap,int(lineList[0]))
#         heapq.heappush(rightHeap,int(lineList[-1]))
#     ans=0
#     while leftHeap:
#         ans+=abs(heapq.heappop(leftHeap)-heapq.heappop(rightHeap))
#     print(ans)

with open('input.txt','r') as file:
    lines=file.readlines()
    freq={}
    left=[]
    for line in lines:
        lineList=list(line.strip().split(' '))
        freq[lineList[-1]]=1+freq.get(lineList[-1], 0)
        left.append(lineList[0])
    ans=0
    for el in left:
        mul=freq.get(el,0)
        ans+=int(el)*mul
    print(ans)