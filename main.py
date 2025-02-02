from card_library.land.mountain import Mountain
from hand import Hand
from deck import Deck
from card_library.weather.smoke import Smoke

def main():
    print("Game started")
    test = Mountain()
    print(test)
    print(test.total_power)
    test2 = Smoke()
    print(test2)
    
    


if __name__ == "__main__":
    main()