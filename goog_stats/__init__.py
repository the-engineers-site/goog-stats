import uuid

import typer
import time
from pathlib import Path
import logging
import json

import goog_stats.consts

LOGGER = logging.getLogger(__name__)


class Stats(object):
    start_time: time
    collection_conf = consts.analytics_config
    working_dir = Path(typer.get_app_dir(consts.APP_NAME))
    config_path = ""

    def __init__(self, tid: str, ul: str = 'en') -> None:
        self.create_working_dir()
        if self.config_path.exists():
            self.__load_config()
        else:
            self.enabled = True
            self.start_time = time.time()
            self.collection_conf[consts.CLIENT_ID] = uuid.uuid4().__str__()
            self.collection_conf[consts.TARGET_ID] = tid
            self.collection_conf[consts.USER_LANG] = ul
            self.write_config()

    def write_config(self):
        with open(self.config_path, 'w') as outfile:
            json.dump(self.collection_conf, outfile)

    def create_working_dir(self):
        self.working_dir.mkdir(parents=True, exist_ok=True)
        self.config_path = Path("{}/{}".format(self.working_dir, consts.CONFIG_FILE_PATH))

    def enable_stat(self):
        status = self.collection_conf[consts.ENABLED]
        if status:
            return
        else:
            self.collection_conf[consts.ENABLED] = True
            self.write_config()
        return

    def disable_stat(self):
        status = self.collection_conf[consts.ENABLED]
        if not status:
            return
        else:
            self.collection_conf[consts.ENABLED] = False
            self.write_config()
        return

    def is_enabled(self):
        return self.collection_conf[consts.ENABLED]

    def __load_config(self):
        self.collection_conf = json.load(open(self.config_path))
