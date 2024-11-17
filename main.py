from App import App
import config
import os


def main() -> None:
    setup()
    App()


def setup() -> None:
    current_path: str

    if not os.path.exists(current_path := config.ZANCMOK_PATH):
        os.mkdir(current_path)

    if not os.path.exists(current_path := config.FACTORIO_MANAGER_PATH):
        os.mkdir(current_path)

    if not (os.path.exists(current_path := os.path.join(config.FACTORIO_MANAGER_PATH, 'profiles'))):
        os.mkdir(current_path)


if __name__ == '__main__':
    main()
