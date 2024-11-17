import os

FACTORIO_PATH: str = r"D:\SteamLibrary\steamapps\common\Factorio"
FACTORIO_STEAM_SETTINGS_PATH: str = r"D:\SteamLibrary\steamapps\appmanifest_427520.acf"
FACTORIO_APPDATA_PATH: str = os.path.join(os.getenv('APPDATA'), 'Factorio')

ZANCMOK_PATH: str = os.path.join(os.getenv('APPDATA'), 'Zancmok')
FACTORIO_MANAGER_PATH: str = os.path.join(ZANCMOK_PATH, 'SimpleFactorioManager')
