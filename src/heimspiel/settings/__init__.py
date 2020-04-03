import os
from .base import *


if os.getenv("IS_PRODUCTION", "") == "True":
    from .prod import *
else:
    from .dev import *
