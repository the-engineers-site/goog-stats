import os
import time


class Stats(object):
    enabled: bool = False
    start_time: time

    def __init__(self) -> None:
        print("starting stats collector")
        self.start_time = time.time()

    def enable_stat(self):
        self.enabled = True
        return

    def disable_stat(self):
        self.enabled = False

    def is_enabled(self):
        return self.enabled
