from enum import Enum


class RunState(Enum):
    rerun: str = "rerun"
    exit: str = "exit"
    back: str = "back"
