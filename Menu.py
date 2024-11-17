import os
from typing import Self, Optional
from RunState import RunState


class Menu:
    def __init__(self, name: str = "", options: Optional[list[Self]] = None) -> None:
        self.name: str = name
        self.options: list[Self] = options or []

    def add_option(self, option: Self) -> None:
        self.options.append(option)

    def draw(self) -> None:
        os.system('cls')

        print(f"{self.name}:")
        for i, v in enumerate(self.options):
            print(f"[{i + 1:{len(str(len(self.options)))}d}]: {v.name}")

    def run(self) -> RunState:
        self.draw()

        current_selection: str
        while not ((current_selection := input()).isdigit() and int(current_selection) - 1 in range(len(self.options))):
            self.draw()

        option: Self = self.options[int(current_selection) - 1]

        run_state: RunState = option.run()
        while True:
            if run_state is RunState.back:
                self.run()
            elif run_state is RunState.exit:
                return RunState.exit
            elif run_state is RunState.rerun:
                run_state = option.run()
