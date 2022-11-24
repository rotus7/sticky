# coding: utf-8

from random import randint

MAX_LENGTH = 10

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def searchData(self, data):
        cr = self.head

        for i in range(self.length):
            if cr.data == data:
                tgt = i
                return tgt

            cr = cr.next

        return -1

    def push(self, data, node):

        if self.length >= MAX_LENGTH - 1:
            print("Size over...")

            return None

        if node != -1:
            print(str(data) + " is overlapping...")

            return None


        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1

        return self

    def pop(self):
        if self.head == None:
            print("List no data")

            return None

        cr = self.head
        newTail = cr

        while cr.next != None:
            newTail = cr
            cr = cr.next

        self.tail = newTail
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        print(str(cr.data) + " is popped out")

        return cr

    def shift(self):
        if self.head == None:
            return None

        cr = self.head
        self.head = cr.next
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return cr

    def unshift(self, data, node):
        if self.length >= MAX_LENGTH - 1:
            print("Size over...")

            return None

        if node != -1:
            print(str(data) + " is overlapping...")

            return None

        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            self.tail = newNode

        else:
            newNode.next = self.head
            self.head = newNode

        self.length += 1

        return self

    def getNode(self, index):
        if (index < 0) or (index >= self.length):
            return None

        cnt = 0
        cr = self.head

        while cnt != index:
            cr = cr.next
            cnt += 1

        return cr

    def setData(self, index, data):
        tgtNode = self.getNode(index)

        if tgtNode == None:
            return False

        else:
            tgtNode.data = data

            return True

    def insertData(self, index, data):
        if (index < 0) or (index > self.length):
            return False

        elif index == self.length:
            return bool(self.push(data))

        elif index == 0:
            return bool(self.unshift(data))

        else:
            before = self.get(index)
            newNode = Node(data)
            prevNode = self.get(index - 1)
            nextNode = prevNode.next
            prevNode.next = newNode
            newNode.next = nextNode
            print("Node" + str(index) + " Changed " + str(before) + " to " + str(data))

            return True

    def removeNode(self, index):
        if (index < 0) or (index >= self.length):
            print("Not found data...")

            return None

        elif index == (self.length - 1):
            print(str(self.tail.data) + " is removed")

            return self.pop()

        elif index == 0:
            print(str(self.head.data) + " is removed")

            return self.shift()

        else:
            rm = self.getNode(index)
            prevNode = self.getNode(index - 1)
            tgtNode = prevNode.next
            prevNode.next = tgtNode.next
            self.length -= 1
            print(str(rm.data) + " is removed")

            return tgtNode

    def allRemove(self):
        self.head = None
        self.tail = None
        self.length = None

    def printList(self):
        if self.length == 0:
            print("List no data ...")
        else:
            arr = list()
            cr = self.head

            while cr != None:
                arr.append(cr.data)
                cr = cr.next

            print(arr)


def test():
    singlyList = SinglyLinkedList()

    singlyList.push(11, singlyList.searchData(11))
    singlyList.push(22, singlyList.searchData(22))
    singlyList.push(33, singlyList.searchData(33))
    singlyList.push(44, singlyList.searchData(44))
    singlyList.push(55, singlyList.searchData(55))

    singlyList.printList()

    singlyList.removeNode(singlyList.searchData(33))

    singlyList.removeNode(singlyList.searchData(11))

    singlyList.push(66, singlyList.searchData(66))

    singlyList.removeNode(singlyList.searchData(11))

    singlyList.push(66, singlyList.searchData(66))

    singlyList.allRemove()

    singlyList.printList()

def main():
    test()

if __name__ == "__main__":
    main()
