"""File to define River class"""

__author__ = "730485079"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

class River:
    
    day: int
    fish: list[Fish]
    bears: list[Bear]


    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        new_list_fish: list[Fish] = []
        new_list_bear: list[Bear] = []

        for fish in self.fish:
            if fish.age <= 3:
                new_list_fish.append(fish)
        for bears in self.bears:
            if bears.age <= 5:
                new_list_bear.append(bears)

        self.fish = new_list_fish
        self.bears = new_list_bear
        return None
        
    def bears_eating(self):
        for bears in self.bears:
            if len(self.fish) >= 5:
                bears.eat(1)
                self.remove_fish(1)
                bears.eat(1)
                self.remove_fish(1)
                bears.eat(1)
                self.remove_fish(1)
        return None
    
    def check_hunger(self):
        new_list_bear: list[Bear] = []
        for bears in self.bears:
            if bears.hunger_score >= 0:
                new_list_bear.append(bears)
        self.bears = new_list_bear
        return None
        
    def repopulate_fish(self):
        nmberofpairs: int = 0
        if len(self.fish) >= 2:
            nmberofpairs = len(self.fish)//2 
            nmberofpairs = nmberofpairs * 4
            for i in range(0, nmberofpairs):
                self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        nmberofpairs: int = 0
        if len(self.bears) >= 2:
            nmberofpairs = len(self.bears)//2 
            for i in range(0, nmberofpairs):
                self.bears.append(Bear())
        return None
    
    def view_river(self):
        fish_pop = len(self.fish)
        bear_pop = len(self.bears)
        day = self.day
        print(f"~~~ Day {day}: ~~~")
        print(f"Fish population: {(fish_pop)}")
        print(f"Bear population: {bear_pop}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
    
    def remove_fish(self, amount: int) -> None:
        idx: int = 0
        while idx < amount:
            self.fish.pop(0)
            idx += 1
