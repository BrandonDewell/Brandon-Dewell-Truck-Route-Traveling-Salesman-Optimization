import datetime


# finds the distance between two addresses.
# distance_between() T(N) = O(1), S(N) = O(1)
def distance_between(address1, address2, address_array, distance_array):
    addr1 = address_array.index(address1)
    addr2 = address_array.index(address2)
    if distance_array[addr1][addr2] == '':  # if the distance is blank due to being on the upper right side empty
        # side of the distance array, return the distance array with the input addresses reversed.
        return distance_array[addr2][addr1]
    else:
        return distance_array[addr1][addr2]


# finds the smallest distance to the next address from the current address by iterating through a list of distances.
# min_distance_from() T(N) = O(N), S(N) = O(N)
def min_distance_from(from_address, truck, address_array, distance_array, my_hash):
    next_addr = 0
    next_id = 0
    min_dist = 100

    for i in range(len(truck.packages)):
        address2 = my_hash.lookup(truck.packages[i]).address
        dist = float(distance_between(from_address, address2, address_array, distance_array))

        if dist < min_dist:
            min_dist = dist
            next_addr = address2
            next_id = truck.packages[i]

    return next_addr, next_id, min_dist  # all the min distance address package info is returned.


# deliver_pkgs() T(N) = O(N), S(N) = O(N)
def deliver_pkgs(truck, address_array, distance_array, my_hash):
    total_distance = 0
    from_address = truck.current_loc

    # change all the packages on the truck to show their status is out for delivery.
    for i in range(len(truck.packages)):
        my_hash.lookup(truck.packages[i]).status = 'In Route'

    # keep looping while the truck has packages on it.
    while truck.has_pkgs_left_to_deliver():
        from_address = truck.current_loc
        pkg_addr, pkg_id, dist = min_distance_from(truck.current_loc, truck, address_array, distance_array, my_hash)

        # the closest package address gets its package object's info updated.
        pkg_object = my_hash.lookup(pkg_id)
        pkg_object.time_delivered = truck.current_time
        pkg_object.assigned_truck = truck.number
        pkg_object.time_left_hub = truck.time_left_hub
        pkg_object.status = "Delivered"

        # update the truck's info.
        truck.remove_package(pkg_id)
        truck.current_loc = pkg_object.address
        truck.current_time = truck.current_time + datetime.timedelta(hours=(dist / 18))

        # timestamp the package delivery.
        pkg_object.time_delivered = truck.current_time

        # keep track of total distance travelled.
        total_distance += dist

    # truck returns to hub and its info and total distance are updated.
    go_to_hub_dist = float(distance_between(truck.current_loc, from_address, address_array, distance_array))
    total_distance += go_to_hub_dist
    truck.current_loc = '4001 South 700 East'
    truck.current_time = truck.current_time + datetime.timedelta(hours=(go_to_hub_dist / 18))
    return total_distance, go_to_hub_dist
