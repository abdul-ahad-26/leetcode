def time_required_to_buy(tickets, k):
    time = 0
    for i in range(len(tickets)):
        if i <= k:
            time += min(tickets[i], tickets[k])
        else:
            time += min(tickets[i], tickets[k] - 1)
    return time

print(time_required_to_buy([2, 3, 2], 2))
print(time_required_to_buy([5, 1, 1, 1], 0))