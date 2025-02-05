import random
balance = 0
hand = 0
state = "default"

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  global state
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
  global balance
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
    balance = balance - int(chips)
    number = random.randint(1,10)
    secondnumber = random.randint(1,10)
    firsthand = number+secondnumber
    return f"Your hand is {firsthand}"

