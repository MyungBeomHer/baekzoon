import sys

I = sys.stdin.readline
N = int(input())
G = {}
#G[A][0] = B /G[A][1] = C는 안된다.....
for _ in range(N):
    root,left,right = I().strip().split()
    G[root] = [left,right]

def preorder(now):
    if now != '.':
        print(now,end = '')
        preorder(G[now][0]) #left
        preorder(G[now][1]) #right

def inorder(now):
    if now != '.':
        inorder(G[now][0])
        print(now,end = '')
        inorder(G[now][1])

def postorder(now):
    if now != '.':
        postorder(G[now][0])
        postorder(G[now][1])
        print(now,end = '')

preorder('A')
print()
inorder('A')
print()
postorder('A')