import csv


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

    def __str__(self):  # overwrite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self.id, self.address, self.city, self.state, self.zip, self.del_dead_line, self.weight, self.spec_notes)


class Truck:
    def __int__(self, current_loc, pkgs):
        self.current_location = current_loc
        self.packages = pkgs
        """
        TODO
        info from judy's meeting on 10/3/23
        time truck left
        truck total miles
        time object built in to python
        datetime
        time delta
        """

    def __str__(self):  # overwrite print(Truck) to avoid printing object reference.
        return "%s, %s" % (
            self.current_location, self.packages)


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


def get_package_data(my_hash):
    print("Packages from Hashtable:")
    # Fetch data from Hash Table
    for i in range(len(my_hash.table) + 1):  # for i in my_hash.table:
        print("Key: {} and Package: {}".format(i, my_hash.lookup(i + 1)))  # 1 to 11 is sent to
        # myHash.lookup() and printed.
    print('')


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
    student ID # 001478703
"""


def load_distance_array(file_name, distance_array):
    with open(file_name, 'r') as dist:  # r means read
        distance_data = csv.reader(dist, delimiter=',')
        for distance in distance_data:
            # print(distance)
            distance_array.append(distance)


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


# def distance_between(address1, address2):
