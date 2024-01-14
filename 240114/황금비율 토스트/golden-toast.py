class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.END = Node(-1)
        self.head = self.END
        self.tail = self.END

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head.prev = new_node 
        self.head = new_node
        new_node.prev = None


    def push_back(self, new_data):
        if self.begin() == self.end():
            self.push_front(new_data)
        else:
            new_node = Node(new_data)            
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node
        
    def erase(self, node):
        next_node = node.next

        if node == self.begin():
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None

        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None

        return next_node

    def insert(self, node, new_data):
        if node == self.end():
            self.push_back(new_data)

        elif node == self.begin():
            self.push_front(new_data)

        else:
            new_node = Node(new_data)
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node


    def begin(self):
        return self.head

    def end(self):
        return self.tail


l = DLL()

n, m = map(int, input().split())
breads = str(input())

it = l.begin()

for i in range(n):
    l.insert(it, breads[i])

for j in range(m):
    cmd = input().split()

    if len(cmd) > 1:
        cmd, bread = cmd
    else:
        cmd = cmd[0]

    if cmd == "L":
        if it != l.begin():
            it = it.prev

    if cmd == "R":
        if it != l.end():
            it = it.next

    if cmd == "P":
        l.insert(it, bread)

    if cmd == "D":
        it = l.erase(it)


it = l.begin()
while it != l.end(): # 'd' 'b' 'c'
    print(it.data, end="")   # it가 가리키는 주소에 담긴 데이터 출력
    it = it.next     # 다음 위치로 이동