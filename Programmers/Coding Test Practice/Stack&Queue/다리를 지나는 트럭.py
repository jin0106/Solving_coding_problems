bridge_length = int(input())
weight = int(input())
truck_weights = list(map(int, input().split()))

time = 0
trucks_on_the_bridge = [0] * bridge_length
truck_weights.reverse()
while trucks_on_the_bridge:
    time += 1
    trucks_on_the_bridge.pop(0)
    if truck_weights:
        if sum(trucks_on_the_bridge) + truck_weights[-1] <= weight:
            trucks_on_the_bridge.append(truck_weights.pop())
        else:
            trucks_on_the_bridge.append(0)
print(time)