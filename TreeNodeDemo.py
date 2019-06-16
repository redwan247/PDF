class Node:

    def __init__(self):
        self.children=[]
        self.name=""


    def rename(self,a):
        self.name=a

    def addChildren(self,a):
        self.children = self.children + [a]



def preOrderTraversal(a):
    print(a.name)
    for c in a.children:
        preOrderTraversal(c)

root=Node()
root.rename("Root")

n1 = Node()
n1.rename("N1")

n11 = Node()
n11.rename("N11")
n12 = Node()
n12.rename("N12")
n13 = Node()
n13.rename("N13")
n1.addChildren(n11)
n1.addChildren(n12)
n1.addChildren(n13)


n2 = Node()
n2.rename("N2")

root.addChildren(n1)
root.addChildren(n2)

preOrderTraversal(root)
