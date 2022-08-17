from time import sleep
# A thread is a separate flow of execution
import threading


def countdown():
    global my_timer


# the time that they have which is 10 seconds
my_timer = 10

for x in range(10):
    my_timer = my_timer - 1
    sleep(1)

    print("Out of time")

    countdown_thread = threading.Thread(target=countdown)

    countdown_thread.start()

    while my_timer > 0:
        print("Hello World")
        sleep(1)

    print("Time up")
