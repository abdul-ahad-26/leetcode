class MyCircularQueue:

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):

        if (self.tail + 1) % self.k == self.head:
            return "The circular queue is full\n"

        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data

        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    def dequeue(self):
        if self.head == -1:
            print("The circular queue is empty")

        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printQueue(self):
        if self.head == -1:
            print("No element in the circular queue")

        elif self.tail >= self.head:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end="")
                print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end="")

            for i in range(0, self.tail + 1):
                print(self.queue[i], end="")
                print()


class Solution:
    def timeRequiredToBuy(self, tickets, k):
        # Storing values

        time = 0
        n = len(tickets)
        turn = 0
        # Buying process
        while tickets[k] > 0:
            for i in range(n):

                if tickets[i] > 0:
                    tickets[i] = tickets[i] - 1
                    time += 1
                    if tickets[k] == 0:
                        return time


s1 = Solution()
print(s1.timeRequiredToBuy([5,1,1,1], 0))


# k=2
# n=3
# time=0
# while True:
#     target_index=(k-time)%n
#     print("Target_index : ", target)
#     if(time==6):
#         print("target_index is bought all ticket, Time taken: ",time)
#         break
#     time+=1
