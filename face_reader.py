"""
codestellation 2015 woop woop
NOTE: Requires the numpy, cv2, subprocess, and time libraries.
"""

import cv2
import numpy
import subprocess
import time
import serial


class face_reader:
    """
    Object which locates faces in an image, and [actions] based on it.
    """


    def __init__(self):
        self.video_capture = cv2.VideoCapture(-1)
        self.frame_dimensions = (self.video_capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH), self.video_capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
        self.face_finder = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
        self.left_height = None
        self.right_height = None
        self.player = 'aplay'
        # self.ser = serial.Serial('/dev/ttyACM0', 9600)
        # self.usbport =  #get from ls /dev
        # self.ser = serial.Serial(self.usbport,9600,timeout=1)


    def update_face_centers(self):
        """
        writes left_height and right_height based on self.video_capture face params.
        """
        ret, self.frame = self.video_capture.read()
        faces = self.face_finder.detectMultiScale(self.frame, scaleFactor = 1.2, minSize = (20,20))
        self.left_height = None
        self.right_height = None #resetting the two.
        for (x, y, w, h) in faces:
            if x + (w/2) <= self.frame_dimensions[0]/2:
                self.left_height = y+(h/2)
            else:
                self.right_height = y+(h/2)


    def print_face_centers(self):
        self.update_face_centers()
        if self.left_height != None:
            print("Left: \t" + str(self.left_height))
            cv2.circle(self.frame, (int(self.frame_dimensions[0]/4), self.left_height), (20), (0,0,0), -1)
        if self.right_height != None:
            print("Right: \t" + str(self.right_height))
            cv2.circle(self.frame, (int(3*self.frame_dimensions[0]/4), self.right_height), 20, (0,0,0), -1)
        cv2.imshow('frame', self.frame)


    def play_wave(self):
        self.update_face_centers()
        if self.left_height != None:
            tone_to_play = self.map_lh_to_tone()
            cmd = '{} {}'.format(self.player, 'tone_{}.wav'.format(tone_to_play))
            popen = subprocess.Popen(cmd, shell=True)
            # angle = 25*tone_to_play
            # self.move_servo(1, angle)
            # popen.communicate()
            # time.sleep(1)
        if self.right_height != None:
            right_tone_to_play = self.map_rh_to_tone()
            cmd = '{} {}'.format(self.player, 'tone_{}.wav'.format(right_tone_to_play))
            popen = subprocess.Popen(cmd, shell=True)
        cv2.imshow('frame', self.frame)


    def map_lh_to_tone(self):
        sh = self.left_height
        h = self.frame_dimensions[1]
        if sh < h/8:
            return 7
        elif sh < 2*h/8:
            return 6
        elif sh < 3*h/8:
            return 5
        elif sh < 4*h/8:
            return 4
        elif sh < 5*h/8:
            return 3
        elif sh < 6*h/8:
            return 2
        elif sh < 7*h/8:
            return 1
        else:
            return 0


    def map_rh_to_tone(self):
        sh = self.right_height
        h = self.frame_dimensions[1]
        if sh < h/8:
            return 7
        elif sh < 2*h/8:
            return 6
        elif sh < 3*h/8:
            return 5
        elif sh < 4*h/8:
            return 4
        elif sh < 5*h/8:
            return 3
        elif sh < 6*h/8:
            return 2
        elif sh < 7*h/8:
            return 1
        else:
            return 0


    def map_lh_to_servo_position(self):
        h = self.frame_dimensions[1]
        lh = self.left_height
        if lh < (h/5):
            return 1
        elif lh < 2*h/5:
            return 2
        elif lh < 3*h/5:
            return 3
        elif lh < 4*h/5:
            return 4
        elif lh <= h:
            return 5
        else:
            return 0


    def move_servo(self):
        """
        moves servo.
        """
        s_pos_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f'}
        self.update_face_centers()
        s_pos = self.map_lh_to_servo_position()
        self.ser.write(str(chr(ord(s_pos_dict[s_pos]))))


    # def move_servo(self, servo, angle):
    #     if (0 <= angle <= 180):
    #         self.ser.write(chr(255))
    #         self.ser.write(chr(servo))
    #         self.ser.write(chr(angle))
    #     else:
    #         print "something went terribly wrong"

    def release(self):
        self.video_capture.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    fr = face_reader()
    while True:
        # fr.print_face_centers()
        fr.play_wave()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            fr.release()
            break