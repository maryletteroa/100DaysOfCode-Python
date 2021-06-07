ascii = """    ___ __ 
   (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: .lcf/
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~
"""
print(ascii)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

answ = input("left or right? ").lower()
if answ == "left":
  answ = input("swim or wait? ").lower()
  if answ == "wait":
    answ = input("which door: red, blue, yellow? ").lower()
    if answ == "red":
      print("You were burned by fire.")
      print("Game Over.")
    elif answ == "blue":
      print("You were eaten by beasts.")
      print("Game Over.")
    elif answ == "yellow":
      print("You Win!")
    else:
      print("Game Over.")
  else:
    print("You were attacked by trout.")
    print("Game Over.")
else:
  print("You fell into a hole.")
  print("Game Over.")