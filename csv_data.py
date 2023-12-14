import csv


# class Package T(N) = O(1), S(N) = O(1)
class Package:
    # __init__() T(N) = O(1), S(N) = O(1)
    def __init__(self, ident, address, city, state, zip_code, del_dead_line, wgt, spec_notes):
        self.id = ident
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code
        self.del_dead_line = del_dead_line
        self.weight = wgt
        self.spec_notes = spec_notes
        self.status = 'At the Hub'
        self.time_delivered = None
        self.assigned_truck = None
        self.time_left_hub = None

    # __str__() T(N) = O(1), S(N) = O(1)
    def __str__(self):  # The __str__() function controls what should be returned when the class object is
        # represented as a string.  Overwrite print(Package) to avoid printing its object memory reference location.  If
        # the __str__() function is not set, the string representation of the object is returned.
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.id, self.address, self.city, self.state, self.zip, self.weight, self.spec_notes, self.status,
            self.assigned_truck, self.time_left_hub, self.del_dead_line, self.time_delivered)
        # %s, %d, and %f are format specifiers or placeholders for formatting strings, decimals, and floats,
        # etc. respectively.  In this case a string is being used, so %s.  Following the complete string "%s, %s, %s,
        # %s, %s, %s, %s, %s", there is a % and ().  The %s is replaced by whatever thing/s I pass to the string
        # within the () after the % symbol.

    # print_pkg_status_at_time() T(N) = O(1), S(N) = O(1)
    def print_pkg_status_at_time(self, user_entered_time):
        if user_entered_time < self.time_left_hub:
            temp_status = 'At the Hub'
            temp_delivery_time = 'Not yet delivered'
        elif user_entered_time >= self.time_delivered:
            temp_status = 'Delivered'
            temp_delivery_time = self.time_delivered
        else:
            temp_status = 'In Route'
            temp_delivery_time = 'Not yet delivered'

        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.id, self.address, self.city, self.state, self.zip, self.weight, self.spec_notes, temp_status,
            self.assigned_truck, self.time_left_hub, self.del_dead_line, temp_delivery_time)


# class Truck T(N) = O(1), S(N) = O(1)
class Truck:

    # __init__() T(N) = O(1), S(N) = O(1)
    def __init__(self, truck_number, pkgs, current_time):
        self.number = truck_number
        self.current_loc = '4001 South 700 East'  # start location is at the hub
        self.packages = pkgs  # list of packages on each truck
        self.current_time = current_time
        self.miles = 0
        self.time_left_hub = current_time
        self.start_time = 0

    # __str__() T(N) = O(1), S(N) = O(1)
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s" % (
            self.current_loc, self.packages, self.current_time, self.miles, self.time_left_hub, self.start_time)

    # has_pkgs_left_to_deliver() T(N) = O(1), S(N) = O(1)
    def has_pkgs_left_to_deliver(self):
        return len(self.packages) > 0

    # remove_package() T(N) = O(1), S(N) = O(1)
    def remove_package(self, pkg_id):
        self.packages.remove(pkg_id)


"""
    def add_package(self, pkg_list, my_hash):
        for i in pkg_list:
            while i < len(pkg_list):
                p = my_hash.lookup(i)
                self.packages.insert(pkg_list)
"""


# load_package_data() T(N) = O(N), S(N) = O(N)
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

            # create package object with that extracted info.
            package = Package(p_id, p_address, p_city, p_state, p_zip, p_del_deadline, p_weight, p_spec_notes)

            # insert the package object into the hash table.
            my_hash.insert(p_id, package)


"""
def get_package_data(my_hash):
    print("Packages from Hashtable:")
    # Fetch data from Hash Table
    for i in range(len(my_hash.table) + 1):  # for i in my_hash.table:
        print("Key: {} and Package: {}".format(i, my_hash.lookup(i + 1)))  # 1 to 11 is sent to
        # myHash.lookup() and printed.
    print('')
"""


# load_distance_array() T(N) = O(N), S(N) = O(N)
def load_distance_array(file_name, distance_array):
    with open(file_name, 'r') as dist:  # r means read
        distance_data = csv.reader(dist, delimiter=',')
        for distance in distance_data:
            distance_array.append(distance)


# load_address_array() T(N) = O(N), S(N) = O(N)
def load_address_array(file_name, address_array):
    with open(file_name, 'r') as addr:
        address_data = csv.reader(addr, delimiter=',')
        for address in address_data:
            address_array.append(address[0])


"""
def address_index_lookup(address, address_array):
    addr = address_array.index(address)
    print('The address array index for', address, 'is: ', addr, end='\n\n')
    return addr
"""