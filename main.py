from cards_repository.land.mountain import Mountain
from hand import Hand
from deck import Deck
from cards_repository.weather.smoke import Smoke

def main():
  print("Game started")
  test = Mountain()
  print(test)
  print(test.total_power)
  test2 = Smoke()
  
  


if __name__ == "__main__":
  main()