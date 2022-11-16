import os
import signal
from typing_extensions import Self
os.kill(Self.p.pid, signal.CTRL_C_EVENT)