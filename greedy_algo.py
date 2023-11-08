
def greedy_algorithm_shortest_distances(from_address, truck, address_array, distance_array, my_hash):
    pass


"""
    def min_distance_from(from_address, truck, address_array, distance_array, my_hash):
        min_dist = 100
        next_addr = 0
        next_id = 0

        for i in range(len(truck.packages)):
            # address2 = truck[i + 1]
            address2 = my_hash.lookup(truck.packages[i]).address
            # print(address2)
            dist = float(distance_between(from_address, address2, address_array, distance_array))
            print('The distance between', from_address, 'and', address2, 'is: ', dist, 'miles.')
            if dist < min_dist:
                min_dist = dist
                next_addr = address2
                next_id = truck.packages[i + 1]

        return next_addr, next_id, min_dist
    unvisited_addr = []

    visited_addr = []
"""
