from typing import override
import config
from Menu import Menu
from RunState import RunState
import os
import shutil
import stat


class SaveProfile(Menu):
    @staticmethod
    def set_writable_recursive(path: str) -> None:
        for root, directories, files in os.walk(path):
            for directory in directories:
                os.chmod(os.path.join(root, directory), stat.S_IWUSR | stat.S_IREAD | stat.S_IWRITE | stat.S_IEXEC)
            for file in files:
                os.chmod(os.path.join(root, file), stat.S_IWUSR | stat.S_IREAD | stat.S_IWRITE)

    @override
    def run(self) -> RunState:
        os.system('cls')

        print(f"{self.name}:")

        profile_name: str = input("Insert profile name: ")

        new_profile_path: str = os.path.join(config.FACTORIO_MANAGER_PATH, 'profiles', profile_name)

        print("Started saving, don't close the program!")

        if os.path.exists(new_profile_path):
            print("Deleting Old Profile!")
            shutil.rmtree(new_profile_path)

        os.mkdir(new_profile_path)
        os.chmod(new_profile_path, stat.S_IWUSR | stat.S_IREAD | stat.S_IWRITE | stat.S_IEXEC)
        print("Copying Steam Files!")
        shutil.copytree(config.FACTORIO_PATH, os.path.join(new_profile_path, 'steam'))
        SaveProfile.set_writable_recursive(os.path.join(new_profile_path, 'steam'))
        print("Copying Appdata Files!")
        shutil.copytree(config.FACTORIO_APPDATA_PATH, os.path.join(new_profile_path, 'appdata'))
        SaveProfile.set_writable_recursive(os.path.join(new_profile_path, 'appdata'))
        print("Copying Steam Settings!")
        shutil.copy(config.FACTORIO_STEAM_SETTINGS_PATH, new_profile_path)
        print("Finished!")
        input("Press enter to continue: ")

        return RunState.back
