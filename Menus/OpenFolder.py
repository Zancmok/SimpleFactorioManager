from typing import override
from Menu import Menu
from RunState import RunState
import os
import config


class OpenFolder(Menu):
    @override
    def run(self) -> RunState:
        os.system(f'start {config.FACTORIO_MANAGER_PATH}')

        return RunState.back
