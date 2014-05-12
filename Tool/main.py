__author__ = 'kaef'

import defaults as cfg
from Clicker import Clicker
from ScreenCapture import ScreenCapture

def main():
    import time
    time.sleep(4)
    c = Clicker()
    c.set_blank_page_pos(cfg.blank_page_pos_x,cfg.blank_page_pos_y)
    c.set_next_button_pos(cfg.next_button_pos_x,cfg.next_button_pos_y)
    c.set_size_button_pos(cfg.size_button_pos_x,cfg.size_button_pos_y)
    c.set_vertical_resize_button_pos(cfg.vertical_resize_button_pos_x,cfg.vertical_resize_button_pos_y)
    a = ScreenCapture(cfg.folder)
    a.set_dim(cfg.img_x,cfg.img_y,cfg.img_xx,cfg.img_yy)
    for i in range(cfg.start, cfg.finish):
        a.capture_with_id(i)
        c.switch_page()


if __name__ == "__main__":
    main()