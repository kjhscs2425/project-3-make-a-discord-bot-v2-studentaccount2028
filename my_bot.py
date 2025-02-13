import random
balance = 0
hand = 0
state = "default"
firsthand = 0

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  global state
  global firsthand
  print(state)
  if "hi" in user_message:
    return True
  if "easter" in user_message:
    return True
  elif "dirt" in user_message:
    return True
  elif "hi" in user_message:
    return True
  elif "help" in user_message:
    return True
  elif "earn" in user_message:
    return True
  elif "m" in user_message:
    return True
  elif "h" in user_message:
    return True
  elif "s" in user_message:
    return True
  elif "b" in user_message:
    return True
  elif state == "waiting for number":
    print('responding to waiting for number')
    return True
  elif state == "first hand":
    print('responding to first hand')
    return True
  elif state == "second hand":
    return True
  else:
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  global firsthand
  global balance
  global state
  if "easter" in user_message:
    return f"""hmmmm. It seams you have found a golden easter egg! Have a good day ~ the easter egg is worth noting haha."""
  elif "dirt" in user_message:
    return f"""dirt ~ black soil that can be worth more than you think. Type "excavate" to find a suprise hidden within the dirt."""
  elif "hi" in user_message:
    return f"""Hello User! My name is Ko and I'm a discord bot. You can play a game where you try to win cool stuff from mystery boxes with virtual currency you earn from doing different tasks. Type "help" to get instructions."""
  elif "help" in user_message:
    return f"""1. "m" mines blocks to find diamonds, gold, and copper. Every time you press m you will have a 1% chance of hitting diamond, 5% chance of hitting gold, and 15% chance of hitting copper. The rest is dirt. 
2.                 "h" will have you open a mystery box. Since it is a mystery, you will see what you get!
3.                  "b" will make you play blackjack, a classic card game!"""
  elif "earn_tester" in user_message:
    balance += 1
    return f"{balance}"
  elif "m" in user_message:
    number = random.randint(1,100)
    if number == 1:
      balance += 1000
      return f"diamondss!! {balance}"
    elif 2 <= number <= 10:
      balance += 200
      return f"goldddd!! {balance}"
    elif 11 <= number <= 25:
      balance += 50
      return f"copper!! {balance}"
    else:
      balance += 1
      return f"dirt. {balance}"
  elif "h" in user_message:
    balance = balance - 50
    number = random.randint(1,100)
    if number == 1:
      balance += 10000
      return f"Wild Card! You have struck a bag of diamonds! You have got 10 dimamonds (10k)! {balance}"
    elif number == 2:
      balance = balance - 10000
      return f"LAVA! You have hit lava. You have lost 100000 dollars (100 diamonds)! {balance}"
    elif 3 <= number <= 53:
      balance += 0
      return f"Nothing. You hit nothing. Tough. {balance}"
    else:
      balance += 1000
      return f"Common money bag! You have earned 1000 dollars (1 diamond!) {balance}"
  elif "b" in user_message:
    state = "waiting for number"
    return "how much would you like to put into the pot"
  elif state == "waiting for number":
    print("hi")
    chips = user_message
    balance = balance - int(chips)
    number = random.randint(1,10)
    secondnumber = random.randint(1,10)
    print(f"{number=}")
    print(f"{secondnumber=}")
    state = "first hand"
    firsthand = number+secondnumber
    return f"Your hand is {firsthand} - push z to continue or lose all chips."
  elif state == "first hand":
    state = "second hand"
    return("It is now your choice, would you like to hit or stay. Press q for hit and s for stay")
  elif state == "second hand":
    if user_message == "q":
      thridnumber = random.randint(1,10)
      secondhand = firsthand+thridnumber
      print(thridnumber)
      if secondhand > 21:
        state = "bust"
        return (f"Bust you have lost! Your losing hand was {secondhand}")
      if secondhand == 21:
        state = "playerwin"
        return ("You have won! You have hit 21!")
      if secondhand < 21:
        state = "second hand"
        return (f"Lucky Ducky! Your final hand is {secondhand}. The dealer will now play.")
      if user_message == "s":
       state = "dealer play"
       return("The dealer will now play.")
     
      


  elif "dirt" in user_message:
    return"dirt ~ black soil that can be worth more than you think. Type excavate to find a suprise hidden within the dirt."
  elif "excavate" in user_message:
    balance = balance - 10000
    return f"LAVA! You have hit lava. You have lost 100000 dollars (100 diamonds)! Your balance is now {balance}"
  elif "chocolate latte" in user_message:
    balance = balance - 500
    return f"I don't like chocolate...minus 500 dollars. Your balance is now {balance}"
  elif "balance" in user_message:
    return f"Your balance is currently {balance}."
  elif "vanilla latte" in user_message:
    balance = balance + 250
    return f"I love vanilla! Plus 250 dollars. Your balance is now {balance}"