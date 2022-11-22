# coding: utf-8

from os import system

class Node():
    def __init__(self, data):
        self.data = data

        self.next = None


class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, data):
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

        print("Pop out is" + str(cr.data))

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

    def unshift(self, data):
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
            newNode = Node(data)
            backNode = self.get(index - 1)
            frontNode = backNode.next
            backNode.next = newNode
            newNode.next = frontNode

            return True

    def removeNode(self, index):
        if (index < 0) or (index >= self.length):
            return None

        elif index == (self.length - 1):
            return self.pop()

        elif index == 0:
            return self.shift()

        else:
            backNode = self.get(index - 1)
            tgtNode = backNode.next
            backNode.next = tgtNode.next
            self.length -= 1

            return tgtNode

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



def main():
    singlyList = SinglyLinkedList()
    while True:
        system('cls')
        singlyList.printList()
        print("")
        print("Push node        >> (1)")
        print("Pop node         >> (2)")
        print("Shift node       >> (3)")
        print("UnShift node     >> (4)")
        print("Set data         >> (5)")
        print("Insert data      >> (6)")
        print("Remove node      >> (7)")
        print("Exit program     >> (0)")
        sel = int(input(">> "))

        if sel == 1:
            num = int(input("Enter push number : >> "))
            singlyList.push(num)

        elif sel == 2:
            singlyList.pop()

        elif sel == 3:
            singlyList.shift()

        elif sel == 4:
            num = int(input("Enter UnShift number : >>"))
            singlyList.unshift(num)

        elif sel == 5:
            num1 = int(input("Enter select node number : >> "))
            num1 -= 1
            num2 = int(input("Enter set number : >> "))
            singlyList.setData(num1, num2)

        elif sel == 6:
            num1 = int(input("Enter select node number : >> "))
            num1 -= 1
            num2 = int(input("Enter insert number : >> "))
            singlyList.insertData(num1, num2)

        elif sel == 7:
            num = int(input("Enter remove node number : >> "))
            num -= 1
            singlyList.removeNode(num)

        else:
            break

if __name__ == "__main__":
    main()
