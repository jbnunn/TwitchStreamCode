from  pycreate2 import Create2

import sys, os, time

# See README on how to find the port
PORT = "/dev/ttyUSB0" # Don't remove the /dev/ portion

# Create a Create2
bot = Create2(PORT)

def main():

    # Start the Create 2
    bot.start()

    # The Create has several modes, Off, Passive, Safe, and Full.
    # Safe: Roomba stops when it detects a cliff, detects a wheel drop, or if on the charger
    # Full: Roomba does not stop when it encounters an event above
    # Passive: Roomba sends sensor data but does not accept changes to sensors or wheels

    # https://cdn-shop.adafruit.com/datasheets/create_2_Open_Interface_Spec.pdf

    bot.safe()

    # directly set the motor speeds ... easier if using a joystick
    bot.drive_direct(5, 5)

    # turn an angle [degrees] at a speed: 45 deg, 100 mm/sec
    bot.turn_angle(45, 100)

    # drive straight for a distance: 5 meters, reverse 100 mm/sec
    bot.drive_distance(5, -100)

    # Tell the Create2 to drive straight forward at a speed of 100 mm/s
    bot.drive_straight(100)
    time.sleep(2)

    # Tell the Create2 to drive straight backward at a speed of 100 mm/s
    bot.drive_straight(-100)
    time.sleep(2)

    # Turn in place
    bot.drive_turn(100, 0)
    time.sleep(2)

    # Turn in place
    bot.drive_turn(-100, 0)
    time.sleep(4)

    # Turn in place
    bot.drive_turn(100, 0)
    time.sleep(2)

    # use the simpler drive direct
    bot.drive_direct(200,-200)  # inputs for motors are +/- 500 max
    time.sleep(2)

    # Stop the bot
    bot.drive_stop()

    # query some sensors
    sensors = bot.get_sensors()  # returns all data
    print(sensors.light_bumper_left)

    # Close the connection
    bot.close()

if __name__ == "__main__":
    try:
        main()
    except serial.serialutil.SerialException:
        print('Serial Exception')
        bot.drive_stop()
        bot.close()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            bot.drive_stop()
            bot.close()
            sys.exit(0)
        except SystemExit:
            bot.drive_stop()
            bot.close()
            os._exit(0)
    
        