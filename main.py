from cards_repository.lands.mountain import Mountain
from hand import Hand
from deck import Deck

def main():
  print("Game started")
  test = Mountain()
  print(test)
  print(test.total_power)
  
  


if __name__ == "__main__":
  main()