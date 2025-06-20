# Реалізація зв'язаного списку з операціями вставки, видалення, пошуку, реверсу та сортування

# Клас для вузла зв'язаного списку
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Реалізація зв'язаного списку
class LinkedList:
    def __init__(self):
        self.head = None

    # Вставка елемента на початок, в кінець або після певного вузла
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Вставка елемента в кінець списку
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    # Вставка елемента після певного вузла
    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Видалення вузла за значенням
    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    # Пошук вузла за значенням
    def search_element(self, data: int):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    # Друк елементів списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування списку за допомогою злиття (Merge Sort)
    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return

        # Функції для розділення списку
        def split(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return head, mid

        # Функція для злиття двох відсортованих списків
        def merge(l1, l2):
            dummy = Node()
            tail = dummy
            while l1 and l2:
                if l1.data < l2.data:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 or l2
            return dummy.next
        
        # Рекурсивна функція для сортування
        def merge_sort_rec(head):
            if not head or not head.next:
                return head
            left, right = split(head)
            left_sorted = merge_sort_rec(left)
            right_sorted = merge_sort_rec(right)
            return merge(left_sorted, right_sorted)

        self.head = merge_sort_rec(self.head)

    # Злиття двох відсортованих списків
    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node()
        tail = dummy
        p1 = list1.head
        p2 = list2.head

        while p1 and p2:
            if p1.data < p2.data:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next

        tail.next = p1 or p2

        result = LinkedList()
        result.head = dummy.next
        return result


# Тестування
llist = LinkedList()
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_end(20)
llist.insert_at_end(25)

print("\nПочатковий список:")
llist.print_list()

llist.delete_node(10)
print("\nПісля видалення елемента 10:")
llist.print_list()

print("\nРеверс списку:")
llist.reverse_list()
llist.print_list()

print("\nСортування списку:")
llist.merge_sort()
llist.print_list()

print("\nОб'єднання двох відсортованих списків:")
l1 = LinkedList()
l1.insert_at_end(1)
l1.insert_at_end(4)
l1.insert_at_end(6)
print("\nСписок №1:")
l1.print_list()

l2 = LinkedList()
l2.insert_at_end(2)
l2.insert_at_end(3)
l2.insert_at_end(5)
print("\nСписок №2:")
l2.print_list()

merged = LinkedList.merge_sorted_lists(l1, l2)
print("\nОб'єднаний відсортований список:")
merged.print_list()
