#!/usr/bin/env python
# -*- coding: UTF-8

from threading import Thread
from time import sleep

class Clock(Thread):
       def __init__(self, time):
              Thread.__init__(self)
              self.time = time

       def run(self):
             for i in range(1,self.time):
                    print i
                    sleep(1)#dorme 1 segundo.
#c = Clock(30)
#c.start()
