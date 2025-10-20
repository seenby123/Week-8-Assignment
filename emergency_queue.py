class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

class MinHeap:
    def __init__(self):
        self.data = []

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.data[index].urgency < self.data[parent].urgency:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent
            parent = (index - 1) // 2

    def heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left
        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right
        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            self.heapify_down(smallest)

    def peek(self):
        if self.data:
            return self.data[0]
        return None

    def remove_min(self):
        if not self.data:
            return None
        min_patient = self.data[0]
        last_patient = self.data.pop()
        if self.data:
            self.data[0] = last_patient
            self.heapify_down(0)
        return min_patient

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")


# test
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()

    next_up = heap.peek()
    print("Next up:", next_up.name, next_up.urgency)

    served = heap.remove_min()
    print("Served:", served.name)
    heap.print_heap()
