#Define the base class player
class player:
  def play(self):
    print("The player is playing cricket.")
#Define the derived class Batsman
class Batsman(player):
  def play(self):
    print("The Batsman is batting.")
#Define the derived class Bowler classes
class Bowler(player):
  def play(self):
    print("The Bowler is bowling.")
#create objects of batsman and bowler classes
batsman=Batsman()
bowler=Bowler()
#call the play()method for each object
batsman.play()
bowler.play()
