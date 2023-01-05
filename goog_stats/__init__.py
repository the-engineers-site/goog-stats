import os


class Stats(object):
    ERRORED, DISABLED_ENV, DISABLED, UNSET, ENABLED = range(5)

    @property
    def enabled(self):
        return self.status in (Stats.UNSET, Stats.ENABLED)

    @property
    def enable_able(self):
        return self.status not in (Stats.ERRORED, Stats.ENABLED)

    @property
    def disable_able(self):
        return self.status not in (Stats.ERRORED, Stats.DISABLED)

    @property
    def recording(self):
        return self.status in (Stats.UNSET, Stats.ENABLED)

    @property
    def sending(self):
        return self.status is Stats.ENABLED

    def __init__(self) -> None:
        print(os.path)

    def enable_stat(self):
        self.enabled = True

    def disable_stat(self):
        self.enabled = False

    def is_enabled(self):
        return self.enabled

    @enabled.setter
    def enabled(self, value: bool):
        self.enabled = value
