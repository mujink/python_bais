def solution(bridge_length, weight, truck_weights):
    count = 0
    bridge = [0 for i in range(bridge_length)]
    overbridge = []
    truck_num = len(truck_weights)
    while len(overbridge) != truck_num:
        if len(truck_weights) != 0:
            tmp = sum(bridge) + truck_weights[0]
        if tmp <= weight:
            if len(truck_weights) != 0:
                bridge.append(truck_weights[0])
                del truck_weights[0]
            else:
                bridge.append(0)
                
            if bridge[0] == 0:
                del bridge[0]
                count += 1
            else:
                overbridge.append(bridge[0])
                del bridge[0]
                count += 1
        else:
            if bridge[0] == 0:
                bridge.append(0)
                del bridge[0]
                count += 1
            else:
                overbridge.append(bridge[0])
                del bridge[0]
                if len(truck_weights) != 0:
                    tmp = sum(bridge) + truck_weights[0]

                if tmp <= weight:
                    bridge.append(truck_weights[0])
                    del truck_weights[0]
                else:
                    bridge.append(0)
                count += 1 
    answer = count
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
# 8
# bridge_length = 100
# weight = 100
# truck_weights = [10]
# 101
# bridge_length = 100
# weight = 100
# truck_weights = [10,10,10,10,10,10,10,10,10,10]

a = solution(bridge_length, weight, truck_weights)
print(a)