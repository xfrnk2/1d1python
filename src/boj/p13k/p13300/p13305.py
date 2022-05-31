def gas_station(n, distances, stations):
    distances = list(map(int, distances.split()))
    stations = list(map(int, stations.split()))

    cost = 0
    j = 0
    for i in range(len(stations)):
        if i == 0:
            while stations[i] <= stations[j] and j < len(stations) - 1:
                j += 1
            for k in range(i, j):
                cost += stations[i] * distances[k]
        if i < j:
            continue
        while stations[i] <= stations[j] and j < len(stations) - 1:
            j += 1
        for k in range(i, j):
            cost += stations[i] * distances[k]
    print(cost)
