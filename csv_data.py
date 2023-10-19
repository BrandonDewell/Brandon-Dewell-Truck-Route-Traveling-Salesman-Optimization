import csv


# from main import distance_array


class Package:
    def __init__(self, ident, address, city, state, zip_code, del_dead_line, wgt, spec_notes):
        self.id = ident
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code
        self.del_dead_line = del_dead_line
        self.weight = wgt
        self.spec_notes = spec_notes

    def __str__(self):  # The __str__() function controls what should be returned when the class object is
        # represented as a string.  Overwrite print(Package) to avoid printing its object memory reference location.  If
        # the __str__() function is not set, the string representation of the object is returned.
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self.id, self.address, self.city, self.state, self.zip, self.del_dead_line, self.weight, self.spec_notes)
        # %s, %d, and %f are format specifiers or placeholders for formatting strings, decimals, and floats,
        # etc. respectively.  In this case a string is being used, so %s.  Following the complete string "%s, %s, %s,
        # %s, %s, %s, %s, %s", there is a % and ().  The %s is replaced by whatever thing/s I pass to the string
        # within the () after the % symbol.


class Truck:
    def __init__(self, pkgs, current_time):
        self.current_location = '4001 South 700 East'  # start at the hub
        self.packages = pkgs  # list of packages on each truck
        self.current_time = current_time
        self.miles = 0
        self.time_left_hub = 0
        self.start_time = 0

        # TODO
        """
        info from judy's meeting on 10/3/23
        time truck left
        truck total miles
        time object built in to python
        datetime
        time delta
        """


"""
    def __str__(self):  # The __str__() function controls what should be returned when the class object is
        # represented as a string.  Overwrite print(Truck) to avoid printing its object memory reference location.  If
        # the __str__() function is not set, the string representation of the object is returned.
        return "%s, %s, %s, %s, %s" % (
            self.current_location, self.packages, self.miles, self.time_left_hub, self.current_time)
        # %s, %d, and %f are format specifiers or placeholders for formatting strings, decimals, and floats,
        # etc. respectively.  In this case a string is being used, so %s.  Following the complete string "%s, %s, %s,
        # %s, %s", there is a % and ().  The %s is replaced by whatever thing/s I pass to the string
        # within the () after the % symbol.
"""


def load_package_data(file_name, my_hash):
    with open(file_name, newline='') as pack:
        package_data = csv.reader(pack, delimiter=',')
        for package in package_data:
            p_id = int(package[0])
            p_address = package[1]
            p_city = package[2]
            p_state = package[3]
            p_zip = package[4]
            p_del_deadline = package[5]
            p_weight = package[6]
            p_spec_notes = package[7]

            # create package object
            package = Package(p_id, p_address, p_city, p_state, p_zip, p_del_deadline, p_weight, p_spec_notes)

            # insert it into the hash table
            my_hash.insert(p_id, package)
        print('All package data has been inserted into the hash table.', end='\n\n')


def get_package_data(my_hash):
    print("Packages from Hashtable:")
    # Fetch data from Hash Table
    for i in range(len(my_hash.table) + 1):  # for i in my_hash.table:
        print("Key: {} and Package: {}".format(i, my_hash.lookup(i + 1)))  # 1 to 11 is sent to
        # myHash.lookup() and printed.
    print('')


def get_package_info(my_hash, id):
    return id


# def insert_package_data(file_name, my_hash):


"""
def get_distance_data(my_hash, dist1, dist2):
    budget = int(input("? "))
    greedyAlgorithmMinExpenses(budget)
    print("Distance between  from Hashtable:")
    # Fetch data from Hash Table
    for i in range(len(my_hash.table) + 1):  # for i in my_hash.table:
        print("Key: {} and Package: {}".format(i, my_hash.lookup(i + 1)))  # 1 to 11 is sent to myHash.lookup()
        # and printed.
"""

# TODO
"""
def insert_package_data(h):
    myHash.insert()
    https://wgu.webex.com/meet/judy.ligocki
    https://wgu.webex.com/meet/preety.khatri
    student ID # 001478703
"""


def load_distance_array(file_name, distance_array):
    with open(file_name, 'r') as dist:  # r means read
        distance_data = csv.reader(dist, delimiter=',')
        for distance in distance_data:
            # print(distance)
            distance_array.append(distance)
        print('The distance array is loaded.', end='\n\n')


"""
def get_distance_array()
    for x in address_array:
        print(x)
"""


def load_address_array(file_name, address_array):
    with open(file_name, 'r') as addr:
        address_data = csv.reader(addr, delimiter=',')
        for address in address_data:
            # print(address[0])
            address_array.append(address[0])
        print('The address array has been loaded.', end='\n\n')


def address_index_lookup(address, address_array):
    addr = address_array.index(address)
    print('The address array index for', address, 'is: ', addr, end='\n\n')
    return addr


def distance_between(address1, address2, address_array, distance_array):
    addr1 = address_array.index(address1)
    addr2 = address_array.index(address2)
    if distance_array[addr1][addr2] == '':  # if the distance is blank due to being on the upper right side of the
        # distance array, return the distance array with the input addresses reversed.
        return distance_array[addr2][addr1]
    else:
        return distance_array[addr1][addr2]


def min_distance_from(from_address, truck):
    min_dist = 100
    next_addr = 0
    next_id = 0

    for i in range(len(truck.packages)):
        # address2 = truck[i + 1]
        address2 = truck.current_location
        dist = distance_between(from_address, address2, 'addresses.csv', 'distances.csv')
        if dist < min_dist:
            min_dist = dist
            next_addr = address2
            next_id = truck

    return next_addr, next_id, min_dist


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
