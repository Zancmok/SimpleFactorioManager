from typing import override
import config
from Menu import Menu
from RunState import RunState
from .SaveProfile import SaveProfile
import os
import shutil
import stat


class LoadProfile(Menu):
    @override
    def run(self) -> RunState:
        self.options: list[Menu] = []

        for profile in os.listdir(os.path.join(config.FACTORIO_MANAGER_PATH, 'profiles')):
            self.options.append(Menu(
                name=profile
            ))

        self.draw()

        current_selection: str
        while not ((current_selection := input()).isdigit() and int(current_selection) - 1 in range(len(self.options))):
            self.draw()

        current_selection = self.options[int(current_selection) - 1].name

        print("Started loading, dont close the program!")

        print("Unloading Current Appdata!")
        SaveProfile.set_writable_recursive(config.FACTORIO_APPDATA_PATH)
        shutil.rmtree(config.FACTORIO_APPDATA_PATH)
        print("Loading New Appdata!")
        shutil.copytree(os.path.join(config.FACTORIO_MANAGER_PATH, 'profiles', current_selection, 'appdata'), config.FACTORIO_APPDATA_PATH)

        print("Unloading Current Steam Files!")
        SaveProfile.set_writable_recursive(config.FACTORIO_PATH)
        shutil.rmtree(config.FACTORIO_PATH)
        print("Loading New Steam Files!")
        shutil.copytree(os.path.join(config.FACTORIO_MANAGER_PATH, 'profiles', current_selection, 'steam'), config.FACTORIO_PATH)

        print("Unloading Current Steam Settings!")
        os.chmod(config.FACTORIO_STEAM_SETTINGS_PATH, stat.S_IWUSR | stat.S_IREAD | stat.S_IWRITE | stat.S_IEXEC)
        os.remove(config.FACTORIO_STEAM_SETTINGS_PATH)
        print("Loading New Steam Settings!")
        shutil.copy(os.path.join(config.FACTORIO_MANAGER_PATH, 'profiles', current_selection, 'appmanifest_427520.acf'), config.FACTORIO_STEAM_SETTINGS_PATH)

        print("Finished!")
        input("Press Enter to continue: ")

        return RunState.back
