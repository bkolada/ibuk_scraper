import pyscreenshot as ImageGrab


class ScreenCapture:
    def __init__(self, path):
        self.set_folder_path(path)

    def set_folder_path(self, path):
        self.folder = path


    def set_dim(self, x, y, xx, yy):
        self.x = x
        self.y = y
        self.xx = xx
        self.yy = yy

    def capture_with_id(self, id=0):
        im = ImageGrab.grab(bbox=(self.x, self.y, self.xx, self.yy))
        im.save(self.folder + "%d.png" % id)


if __name__ == "__main__":
    a = ScreenCapture("/home/kaef/")
    a.set_dim(100, 100, 500, 500)
    a.capture_with_id(100)
    import time

    time.sleep(1)