from Menu import Menu
import Menus


class App:
    def __init__(self) -> None:
        self.main_menu: Menu = Menu(
            name="Factorio Manager"
        )

        self.load_profile: Menus.LoadProfile = Menus.LoadProfile(
            name="Load Profile"
        )

        self.save_profile: Menus.SaveProfile = Menus.SaveProfile(
            name="Save Profile"
        )

        self.open_folder: Menus.OpenFolder = Menus.OpenFolder(
            name="Open Folder"
        )

        self.reset_appdata: Menus.ResetAppdata = Menus.ResetAppdata(
            name="Reset Appdata"
        )

        self.main_menu.add_option(self.load_profile)
        self.main_menu.add_option(self.save_profile)
        self.main_menu.add_option(self.open_folder)
        self.main_menu.add_option(self.reset_appdata)

        self.main_menu.run()
