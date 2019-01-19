import evdev
import select
import glob
# print(device)

class barcode:
    def __init__(self):
        input_event=glob.glob("/dev/input/event0") #assume you know where is yout barcode input
        #print(evdev.InputDevice(input_event)) #to check your barcode

    def read(self):
        result = ""
        done = 0
        while done < 2:
            r, w, x = select.select([self.device.fd], [], [])
            for event in self.device.read():
                if event.type == evdev.ecodes.EV_KEY:
                    if event.value == 0:
                        if int(event.code) == 69:
                            done += 1
                            break;
                        my_val = evdev.ecodes.KEY[event.code][4:]
                        if( my_val == 'ENTER' ):
                            # print()
                            result += ''
                        elif( my_val.isdigit() ):
                            result += str(my_val)
                            # print(my_val, end = '')
        return result
        