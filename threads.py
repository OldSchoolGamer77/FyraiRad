from threading import Thread
from net import Net
class NetThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.net = Net()
