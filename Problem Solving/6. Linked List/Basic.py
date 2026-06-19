class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
if __name__ == "__main__":
    arr = [2,3,4,5]
y = Node(arr[0])
print(y)
print(y.data)

class Node:
    def __init__(self,data):
        self.data = data
a = Node(5)
b = a
b.data = 20
print(a.data)

print("-----Array to Linked List-----")
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
def array_to_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for i in range(1,len(arr)):
        current.next = Node(arr[i])
        current = current.next
    return head
def print_linked_list(head):
    temp = head
    while temp:
        print(temp.data,end=" -> ")
        temp = temp.next
    print("None")
arr = [10,20,30,40,50]
head = array_to_linked_list(arr)
print_linked_list(head)

print("-----Length of the linked list-----")
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
def array_to_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for i in range(1,len(arr)):
        current.next = Node(arr[i])
        current = current.next
    return head
def length_of_linked_list(head):
    count = 0
    temp = head
    while temp:
        count+=1
        temp = temp.next
    return count
arr = [1,2,3,4,5,6,7,8,9]
head = array_to_linked_list(arr)
print("Length:",length_of_linked_list(head))

print("-----Search an linked list-----")
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
def Aarry_to_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for i in range(1,len(arr)):
        current.next = Node(arr[i])
        current = current.next
    return head
def search_a_number(head,a):
    temp = head
    while temp:
        if (temp.data==a):
            return True
        temp = temp.next
    return False
arr = [1,2,34,4,56,6,7]
head = Aarry_to_linked_list(arr)
print(search_a_number(head,37))

print("-----Delete head of the linked list-----")
def delete_head_of_the_linked_list(head):
    if head is None:
        return None 
    return head.next
arr = [1,2,3,4,5]
head = Aarry_to_linked_list(arr)
head = delete_head_of_the_linked_list(head)
print_linked_list(head)


print("-----Delete tail of the linked list-----")
def delete_tail_of_the_head(head):
    if head == None or head.next == None:
        return None
    temp = head
    while temp.next.next != None:
        temp = temp.next
    temp.next = None
    return head
arr = [77,66,55,44,33,22,11]
head = array_to_linked_list(arr)
head = delete_tail_of_the_head(head)
print_linked_list(head)