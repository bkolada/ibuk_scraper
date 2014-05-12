__author__ = 'kaef'

import uinput
import time
from pymouse import PyMouse

class Clicker:
    def __init__(self):
        # self.device = uinput.Device([
        #     uinput.ABS_X +  (0, 1920, 0, 0),
        #     uinput.ABS_Y +  (0, 1080, 0, 0),
        #     # uinput.REL_X,
        #     # uinput.REL_Y,
        #     uinput.BTN_LEFT,
        #     uinput.BTN_RIGHT])
        self.m = PyMouse()

    def set_next_button_pos(self, x, y):
        self.next_button_pos = [x, y]

    def set_size_button_pos(self, x, y):
        self.size_button_pos = [x, y]

    def set_blank_page_pos(self, x, y):
        self.blank_page_pos = [x, y]

    def set_vertical_resize_button_pos(self, x, y):
        self.vertical_resize_button_pos = [x, y]

    def click(self, pos):
        print pos
        # self.device.emit(uinput.ABS_X, pos[0], syn=False)
        # self.device.emit(uinput.ABS_Y, pos[1])
        # # self.device.emit_click(uinput.BTN_RIGHT)
        # time.sleep(2)
        # self.device.emit_click(uinput.BTN_LEFT)


        self.m.click(pos[0], pos[1], 1)
        time.sleep(1)

    def click_next_button(self):
        self.click(self.next_button_pos)

    def click_size_button(self):
        self.click(self.size_button_pos)

    def click_blank_page(self):
        self.click(self.blank_page_pos)

    def click_vertical_resize_button_page(self):
        self.click(self.vertical_resize_button_pos)


    def switch_page(self):
        self.click_blank_page()
        self.click_next_button()
        self.click_size_button()
        self.click_vertical_resize_button_page()
        self.click_blank_page()

# findclient: 10526895
# findclient: 10526894
# x:1698 y:417 screen:0 window:10526894
# [kaef@garden ~]$ xdotool getmouselocation
# findclient: 10526895
# findclient: 10526894
# x:1902 y:641 screen:0 window:10526894
# [kaef@garden ~]$ xdotool getmouselocation
# findclient: 10526895
# findclient: 10526894
# x:1898 y:177 screen:0 window:10526894
# [kaef@garden ~]$ xdotool getmouselocation
# findclient: 10526895
# findclient: 10526894
# x:1647 y:184 screen:0 window:10526894
# [kaef@garden ~]$

if __name__ == "__main__":
    i = 3
    c = Clicker()
    c.set_blank_page_pos(1698, 417)
    c.set_next_button_pos(1902, 641)
    c.set_size_button_pos(1898, 177)
    c.set_vertical_resize_button_pos(1647, 184)
    c.switch_page()
