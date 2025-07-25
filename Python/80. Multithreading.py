# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target = my_function)

import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking the {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You talk out the trash")

def get_mail():
    time.sleep(3)
    print("You get the mail")

print("------- by using normal functions -------")
walk_dog("Doney", "Ambati")
take_out_trash()
get_mail()

print("------- by using threading -------")
chore1 = threading.Thread(target=walk_dog, args=("Tinku","Ambati"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are completed")