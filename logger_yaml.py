# install pyyaml
# Successfully installed pyyaml-5.3.1

import logging
import logging.config
import os
import yaml


try:
    os.remove("output/testfile3.log")
except FileNotFoundError:
    pass

with open("config/config.yaml", "r") as f:
    log_cfg = yaml.safe_load(f.read())

logging.config.dictConfig(log_cfg)

logger = logging.getLogger("dev")
logger.setLevel(logging.INFO)

logger.info("This is an info message")
logger.error("This is an error message")
