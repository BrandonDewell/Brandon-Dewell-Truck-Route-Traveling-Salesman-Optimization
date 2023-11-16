import datetime


def distance_between(address1, address2, address_array, distance_array):
    addr1 = address_array.index(address1)
    addr2 = address_array.index(address2)
    if distance_array[addr1][addr2] == '':  # if the distance is blank due to being on the upper right side of the
        # distance array, return the distance array with the input addresses reversed.
        return distance_array[addr2][addr1]
    else:
        return distance_array[addr1][addr2]


def min_distance_from(from_address, truck, address_array, distance_array, my_hash):
    next_addr = 0
    next_id = 0
    min_dist = 100

    for i in range(len(truck.packages)):
        # address2 = truck[i + 1]
        address2 = my_hash.lookup(truck.packages[i]).address
        # print(address2)
        dist = float(distance_between(from_address, address2, address_array, distance_array))

        if dist < min_dist:
            min_dist = dist
            next_addr = address2
            next_id = truck.packages[i]

    return next_addr, next_id, min_dist  # all the min distance address package info is returned.


def deliver_pkgs(truck, address_array, distance_array, my_hash):
    #  while the truck has more packages
    total_distance = 0
    # pkg_object = None
    from_address = truck.current_loc
    for i in range(len(truck.packages)):
        my_hash.lookup(truck.packages[i]).status = 'In Route'
        # to show packages status is being updated right before heading out, uncomment next line.
        # print('Package #', truck.packages[i], '\'s status changed to: ', my_hash.lookup(truck.packages[i]).status)

    while truck.has_pkgs_left_to_deliver():  # AKA while this statement is true...
        # while len(truck.packages) > 0:
        from_address = truck.current_loc
        pkg_addr, pkg_id, dist = min_distance_from(truck.current_loc, truck, address_array, distance_array, my_hash)
        # the function normally returns the info as items in a list and here it instead assigns them to variables.
        pkg_object = my_hash.lookup(pkg_id)
        # pkg_object.status = 'In Route'
        # pkg_object.time_delivered = None
        pkg_object.time_delivered = truck.current_time
        pkg_object.assigned_truck = truck.number
        pkg_object.time_left_hub = truck.time_left_hub
        pkg_object.status = "Delivered"
        # print('Package #', pkg_id, '\'s status: ', pkg_object.status)
        truck.remove_package(pkg_id)
        truck.current_loc = pkg_object.address
        truck.current_time = truck.current_time + datetime.timedelta(hours=(dist / 18))
        pkg_object.time_delivered = truck.current_time
        # total_distance = total_distance + dist
        total_distance += dist

        """
        print('Truck #', truck.number, 'The distance between', from_address, 'and', truck.current_loc, 'is: ',
              dist, 'miles. Truck #', truck.number, '\'s total distance travelled is:', total_distance, 'miles.')
        print('Package #', pkg_id, '\'s status: ', pkg_object.status, 'at', pkg_object.time_delivered)
        """

        """
        for i in range(1, 41):
            print('Evidence status is changing per delivered package', my_hash.lookup(i))
        """

    """
    go_to_hub_dist = 0
    for i in range(1, 41):
        p = my_hash.lookup(i)
        if p.status == 'At the Hub.':  # a check if there are undelivered packages left, otherwise no need to return
            # to hub.
    """
    go_to_hub_dist = float(distance_between(truck.current_loc, from_address, address_array, distance_array))
    truck.current_loc = '4001 South 700 East'
    truck.current_time = truck.current_time + datetime.timedelta(hours=(go_to_hub_dist / 18))
    total_distance += go_to_hub_dist
    # print('The truck is back at the hub at:', truck.current_loc, 'at', truck.current_time)
    return total_distance, go_to_hub_dist


"""
def truck_load_pkgs(truck, start_time, address_array, distance_array, my_hash):
    unvisited_pkg_list = []
    visited_pkg_list = []
    total_miles = 0

    for pkg in truck.packages:
        # for i in my_hash.lookup(truck.packages.id):
        # unvisited_pkg_list.append(pkg)
        unvisited_pkg_list.append(pkg)
    # print(unvisited_pkg_list)
    print('The unvisited package list contains: ', unvisited_pkg_list)

    next_truck_pkg = min_distance_from(address_array[0], truck, address_array, distance_array, my_hash)
    print('')
    print('The next package to be delivered is', next_truck_pkg)
    next_addr = next_truck_pkg[0]
    next_id = next_truck_pkg[1]
    min_dist = next_truck_pkg[2]

    print('The minimum distance from', address_array[0], 'to', next_addr, 'that has the package id #', next_id,
          'is', min_dist, 'miles.')
    total_miles = total_miles + min_dist
    print('The total miles calculated so far is: ', total_miles, end='\n\n')
    visited_pkg_list.append(address_array[0])
    print('The visited package list includes: ', visited_pkg_list)
    print('The unvisited package list includes: ', unvisited_pkg_list)

    from_addr = next_addr
    for i in range(len(unvisited_pkg_list)):
        next_truck_pkg = min_distance_from(from_addr, truck, address_array, distance_array, my_hash)
        print('')
        print('The next package to be delivered is', next_truck_pkg)
        from_addr = next_truck_pkg[0]
        next_id = next_truck_pkg[1]
        min_dist = next_truck_pkg[2]

        print('The minimum distance from', next_addr, 'to', next_addr, 'that has the package id #', next_id,
              'is', min_dist, 'miles.')
        total_miles = total_miles + min_dist
        print('The total min_dist calculated so far is: ', total_miles, 'min_dist.', end='\n\n')
        visited_pkg_list.append(from_addr)
        print('The visited package list includes: ', visited_pkg_list)
        unvisited_pkg_list.remove(next_id)


        # if address_array[i] != '4001 South 700 East':
            # unvisited_pkg_list.pop(0)  # wrong because it removes package #1, but I need to remove hub address
            # unvisited_pkg_list.remove(next_truck_pkg[1])


    # visited_addr = []


"""

"""
def min_distance_from(from_address, truck_packages_array):
    min_dist = 100
    next_addr = 0
    next_id = 0

    for i in range(len(truck_packages_array.packages)):
        # a2 = truck_packages_array[i + 1]
        a2 = truck_packages_array.current_location
        dist = distance_between(from_address, a2, 'addresses.csv', 'distances.csv')
        if dist < min_dist:
            min_dist = dist
            next_addr = a2
            next_id = truck_packages_array

    return next_addr, next_id, min_dist
"""

""" for i in truck_packages_array:
        # print(i)
        dist = distance_between(from_address, truck_packages_array[i], 'addresses.csv', 'distances.csv')
        print(dist)
"""

"""
    min_dist = 100

    # dist = distance_between(from_address, truck_packages_array[i], 'addresses.csv', 'distances.csv') while
    # distance_between(from_address, truck_packages_array[i], 'addresses.csv', 'distances.csv') < min_dist and
    # distance_between(from_address, truck_packages_array[i], 'addresses.csv', 'distances.csv') != 0:
    for i in truck_packages_array:
        d = distance_between(from_address, truck_packages_array[i], 'addresses.csv', 'distances.csv')
        # small = min(d)
        # print(small)
        if d < min_dist and d != 0:
            min_dist = d
        print(min_dist)
    # distance_between(from_address, address2)
"""
