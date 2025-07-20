from pathlib import Path
from typing import Final

from environs import Env

ABS_PATH: Final[Path] = Path(__file__).resolve().parent.parent.parent

env = Env()
env.read_env(ABS_PATH / ".env")
