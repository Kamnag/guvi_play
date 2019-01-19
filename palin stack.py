class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
 
s = Stack()
t = input()
 
for c in t:
    s.push(c)
 
rev = ''
while not s.is_empty():
    rev += s.pop()
 
if t == rev:
    print('YES')
else:
    print('NO')
