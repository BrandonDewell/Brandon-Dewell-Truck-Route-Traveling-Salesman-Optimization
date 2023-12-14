# Brandon Dewell, Student ID: 001478703
import datetime
import algos
import hash_table
import csv_data

# create a hash table.
my_hash = hash_table.ChainingHashTable()

# load package data into hash table.
csv_data.load_package_data('packages.csv', my_hash)

# loading arrays.
distance_array = []
csv_data.load_distance_array('distances.csv', distance_array)
address_array = []
csv_data.load_address_array('addresses.csv', address_array)

# assign packages to trucks.
t1_pkgs = [1, 29, 30, 31, 34, 37, 40, 13, 14, 15, 16, 19, 20, 21, 38, 5]
t3_pkgs = [6, 25, 26]
t2_pkgs = [28, 32, 9, 3, 18, 36, 38, 2, 4, 7, 8, 10, 11, 12, 17, 22]

# time of day the work starts.
start_time = '08:00:00'
h, m, s = start_time.split(':')
time_object_1 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

# create truck objects.
truck1 = csv_data.Truck(1, t1_pkgs, time_object_1)
truck3 = csv_data.Truck(3, t3_pkgs, time_object_1)
truck2 = csv_data.Truck(2, t2_pkgs, time_object_1)

# adjust truck3 start time.
time_object_3 = datetime.timedelta(hours=int(1), minutes=int(5), seconds=int(1))
truck3.current_time = truck3.current_time + time_object_3
truck3.time_left_hub = truck3.current_time

# adjust truck2 start time.
time_object_2 = datetime.timedelta(hours=int(2), minutes=int(20), seconds=int(1))
truck2.current_time = truck2.current_time + time_object_2
truck2.time_left_hub = truck2.current_time

# deliver packages.
truck1_first_load_dist, go_to_hub_dist_t1 = algos.deliver_pkgs(truck1, address_array, distance_array, my_hash)
truck3_dist, go_to_hub_dist_t3 = algos.deliver_pkgs(truck3, address_array, distance_array, my_hash)
truck2_dist, go_to_hub_dist_t2 = algos.deliver_pkgs(truck2, address_array, distance_array, my_hash)

# reload truck 1 with the rest of the packages that are left at the hub.
t1_reload_pkgs = [23, 24, 27, 33, 35, 39]
truck4 = csv_data.Truck(1, t1_reload_pkgs, truck1.current_time)
truck1 = truck4
truck1_reload_dist, go_to_hub_dist_t1_reload = algos.deliver_pkgs(truck1, address_array, distance_array, my_hash)


# user interface.  T(N) = O(N^2), S(N) = O(N^2)
if __name__ == '__main__':
    keep_running = True

    # loop until user is satisfied and wants to exit.
    while keep_running:
        print("\nWelcome to WGUPS")
        print("\nOptions:")
        print("1. Package delivery status")
        print("2. Get total truck mileage")
        print("3. Exit the Program")
        option = input("Enter an option (1,2 or 3): ")
        if option == "1":
            print('')
            bad_value_input = True
            while bad_value_input:
                try:
                    user_time = input('At what time do you want the package data (ex. 09:15:00)?')
                    print('')
                    h, m, s = user_time.split(':')
                    time_object = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    if '00:00:00' < user_time <= '24:00:00':
                        print(
                            'Package data at', time_object, ':\n'
                            'Package ID #, Delivery address, city, state, zipcode, Package weight, Package special '
                            'notes, Package delivery status, Truck # assigned to package, '
                            'Time the package left the hub, Delivery deadline, Time of package delivery')
                        for i in range(1, 41):
                            print(my_hash.lookup(i).print_pkg_status_at_time(time_object))
                        print('')
                    else:
                        print('Incorrect entry.')
                        print('Please enter a value > 00:00:00 and < 24:00:00')
                        print('')
                        continue
                    bad_value_input = False
                except ValueError:
                    print('Incorrect entry.')
                    print('Please only use numbers in the format hh:mm:ss')
                    print('')
                    print('')
        elif option == "2":
            print('')
            print('Truck #1\'s total distance travelled is: ', truck1_first_load_dist +
                  truck1_reload_dist, 'miles.')
            print('Truck #2\'s total distance travelled is: ', truck2_dist, 'miles.')
            print('Truck #3\'s total distance travelled is: ', truck3_dist, 'miles.')
            print('The total distance travelled by all three trucks is',
                  truck1_first_load_dist + truck1_reload_dist + truck2_dist
                  + truck3_dist, 'miles.')
            print('')
        elif option == "3":
            print('')
            print('Thanks for using WGUPS!  Goodbye.')
            print('')
            keep_running = False
        else:
            print('')
            print("Wrong option, please try again!")
