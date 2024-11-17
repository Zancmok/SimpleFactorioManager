import os
from typing import override
import config
from Menu import Menu
from RunState import RunState
from .SaveProfile import SaveProfile
import shutil


class ResetAppdata(Menu):
    @staticmethod
    def reset_appdata() -> None:
        print("Removing AppData!")
        SaveProfile.set_writable_recursive(config.FACTORIO_APPDATA_PATH)
        shutil.rmtree(config.FACTORIO_APPDATA_PATH)

    @override
    def run(self) -> RunState:
        os.system('cls')
        print(f"{self.name}:")

        print("You sure you want to delete your files(y/n)?: ")
        confirmation: str
        while (confirmation := input()) not in ('y', 'n'):
            pass

        if confirmation == 'n':
            return RunState.back

        try:
            ResetAppdata.reset_appdata()
        except:
            pass

        return RunState.back
