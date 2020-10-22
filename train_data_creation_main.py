import numpy as np
import os
from grabscreen import grab_screen
from getkeys import key_check
import time
import cv2

file_name = 'training_data_v2.npy'
if os.path.isfile(file_name):
    print('file exist! Loading previous data')
    training_data = list(np.load(file_name))
else:
    print('starting fresh!! creating new data .......................')
    training_data = []


def key_to_output(keys):
    output = [0, 0, 0, 0]
    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    elif 'W' in keys:
        output[1] = 1
    else:
        output[3] = 1

    return output

def main():
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    last_time = time.time()
    while True:

        # the region=(0, 40, 1280, 760) for 720p resolution. or region=(0, 40, 800, 640) for smaller resolution.
        frame = grab_screen(region=(0, 40, 1280, 760))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.resize(frame, (128, 72))
        keys = key_check()
        output = key_to_output(keys)
        training_data.append([frame,output])

        # print('frame took {} sec'.format(time.time() - last_time))
        # last_time = time.time()
        if len(training_data) % 500 == 0:
            print(f'({len(training_data)} training_data has been created.)')
            np.save(file_name, training_data)


        # cv2.imshow('test', frame)
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break
    #    keys = key_check()
    #    output = key_to_output(keys)
    #    training_data.append([frame,output])
    #
    #    if len(training_data) % 500 == 0:
    #        print(len(training_data))
    #        np.save(file_name, training_data)


main()
