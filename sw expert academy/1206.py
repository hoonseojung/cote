for test_case in range(1, 11):
    result = 0
    building_num = int(input())
    buildings = list(map(int, input().split()))
    for i in range(2, building_num-2):
        dif_max = max(buildings[i-1], buildings[i-2], buildings[i+1], buildings[i+2])
        if buildings[i] > dif_max:
            result += (buildings[i] - dif_max)
 
    print("#{} {}".format(test_case, result))