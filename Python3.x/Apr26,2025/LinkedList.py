class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self) -> None:
        self.start = None
        self.end = None
        self.temp = None

    def addNode(self) -> None:
        data: int = int(input("enter a number:"))
        node = Node(data)
        if self.start == None:
            self.start = node
            self.end = node
        else:
            self.end.next = node
            self.end = self.end.next
    
    def display(self) -> None:

        self.temp = self.start

        while self.temp!=None:
            print(str(self.temp.data)+ "<-", end = "")
            self.temp = self.temp.next
        
        print("NULL")



if __name__=="__main__":
    linkedlist = Linkedlist()
    linkedlist.addNode()
    linkedlist.addNode()
    linkedlist.addNode()
    linkedlist.addNode()

    linkedlist.display()



