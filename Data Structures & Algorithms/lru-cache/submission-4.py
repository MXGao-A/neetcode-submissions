class Node:
    def __init__(self,key,val):
        self.key=key
        self.value=val
        self.prev=None
        self.next=None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size=0

    def remove_node(self,node):
        node_prev,node_next=node.prev,node.next
        node_prev.next=node_next
        node_next.prev=node_prev

    def put_it_front(self,node):
        old_head=self.head.next
        self.head.next=node
        old_head.prev=node
        node.prev=self.head
        node.next=old_head
        

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        else:
            node=self.cache[key]
            value=node.value
            self.remove_node(node)
            self.put_it_front(node)
            return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self.remove_node(node)
            self.put_it_front(node)
        else:
            node=Node(key,value)
            self.put_it_front(node)
            self.cache[key]=node
            self.size+=1
            if self.size>self.capacity:
                last_used=self.tail.prev
                self.tail.prev=last_used.prev
                last_used.prev.next=self.tail
                del self.cache[last_used.key]
                self.size-=1
                
        
