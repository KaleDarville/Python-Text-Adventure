from random import randint
from colorama import Fore, Back, Style, init
import time, os, sys
from typeSim import clearScreen

init(autoreset=True)
tutorial = input("TUTORIAL?: "+Fore.CYAN)

if "es" in tutorial or "y" in tutorial:
  print(Fore.MAGENTA+"\n[Your objective is to survive, level up, and eventually defeat your enemy.]\n\n[Most level stats cap at level 5.]\n\n[After defeating each threat, you level up, and if you play correctly, get some gold out of it.]\n\n[Gold can be used to upgrade your weapon and buy various buffs.]\n\n[You have to defeat a threat before you run out of HP or it's game over.]\n\n[Every lost attempt causes your enemy to level up and you to lose HP.]\n\n[If your enemy gets to level 5, you are forced to challenge them immediatly.]\n\n[When you get to player level 5, you can challenge your enemy for the final battle.]\n\n[Good luck!]\n")
else:
  pass

player = input(Fore.RESET+"\nState the name of your adventurer: \n   "+Fore.CYAN)
enemy = input(Fore.RESET+"\nState the name of your enemy: \n   "+Fore.CYAN)
weapon = input(Fore.RESET+"\nState your weapon of choice: \n   "+Fore.CYAN)
playerLevel = 1
enemyLevel = 1
weaponLevel = 1
maxHealth = 100
hp = 100
goldMultiplier = 1
gold = 0

if weapon == "":
  weapon = "weapon"
if player == "":
  player = "Player"
if enemy == "":
  enemy = "Enemy"

print(Fore.RESET+"\n\n-Type "+Fore.LIGHTGREEN_EX+"'STATS'"+Fore.RESET+" after 'Next >>>' to see your statistics- (Next >>> "+Fore.LIGHTGREEN_EX+"STATS)"+Fore.RESET)

print("\n   You grab your " + weapon + " and set off across the vast landscape to face your powerful opponent " + enemy + " with only the clothes on your back and only enough food to last a few weeks. After walking for awhile, you come to your first threat...\n\n")

for loop1 in range(1):
  subLoop = 1

  while hp > 0:
    stats = input(Fore.RESET+"Next >>> "+Fore.LIGHTGREEN_EX)

    if stats == "STATS":
      print(Fore.LIGHTGREEN_EX+"\n[" + player + ": Level " + str(playerLevel) + "]\n\n[" + enemy + ": Level " + str(enemyLevel) + "]\n\n[" + weapon + ": Level " + str(weaponLevel) + "]\n\n[Max Health: " + str(maxHealth) + "]\n\n[HP: " + str(hp) + "]\n\n[Gold Multiplier: " + str(goldMultiplier) + "x]\n\n[Gold: " + str(gold) + "]\n")


    if hp <= 50:
      print(Fore.RED+"\n-Final attempt!-\n")

    goblins = randint(1,30)

    if subLoop > 1:
      move = "run"
    else:
      move = "none"

    if goblins == 1:
      goblinText = " goblin at a camp. It doesn't "
    elif "un" in move and goblins > 1:
      goblinText = " goblins at the camp when you return. They still don't "
    elif "un" in move and goblins == 1:
      goblinText = " goblin at the camp when you return. It still doesn't "
    else:
      goblinText = " goblins at a camp. They don't "

    print("\nYou see " +Fore.CYAN+ str(goblins) +Fore.RESET+ goblinText + "notice you...\n")

    move = input("Do you run or fight?\n   "+Fore.CYAN)

    subLoop += 1
    
    if "un" in move:
      print(Fore.RESET+"\nYou run away for the night and return in the morning.\n\n")
    elif goblins >= 25 and "ight" in move:
      print(Fore.RESET+"\nThe hordes of goblins overwhelm you instantly.")
      enemyLevel += 1
      hp -= 50
      print(Fore.RED+"\n(" + enemy + ": Level Up)")
      print(Fore.RED+"(HP - 50)")
      print(Style.BRIGHT+Fore.RED+"\n\n-TRY AGAIN-\n\n"+Style.RESET_ALL) # LOSE (>=25, fight, hp -50)

    elif goblins > 15 and goblins < 25 and "ight" in move:
      print(Fore.RESET+"\nYou almost manage to come out alive, but there are just too many goblins and they kill you.")
      enemyLevel += 1
      hp -= 50
      print(Fore.RED+"\n(" + enemy + ": Level Up)")
      print(Fore.RED+"(HP - 50)")
      print(Style.BRIGHT+Fore.RED+"\n\n-TRY AGAIN-\n\n"+Style.RESET_ALL) # LOSE (15>25, fight, -50 hp)

    elif goblins <= 15 and "ight" in move:
      print(Fore.RESET+"\nYou triumph over the goblins and steal all their food and money. The day is won!")
      gold += 500
      playerLevel += 1
      hp -= 25
      print(Fore.LIGHTGREEN_EX+"\n(" + player + ": Level Up)")
      print(Fore.RED+"(HP - 25)")
      print(Style.BRIGHT+Fore.LIGHTYELLOW_EX+"(Gold + 500)\n\n"+Style.RESET_ALL)
      stats = input(Fore.RESET+"Next >>> ") # WIN (<=15, fight, +50 g, lvl2, -25 hp)

      if stats == "STATS":
        print(Fore.LIGHTGREEN_EX+"\n[" + player + ": Level " + str(playerLevel) + "]\n\n[" + enemy + ": Level " + str(enemyLevel) + "]\n\n[" + weapon + ": Level " + str(weaponLevel) + "]\n\n[Max Health: " + str(maxHealth) + "]\n\n[HP: " + str(hp) + "]\n\n[Gold Multiplier: " + str(goldMultiplier) + "x]\n\n[Gold: " + str(gold) + "]\n")
      break

    else:
      print(Fore.RESET+"\n-Type "+Fore.CYAN+"'run'"+Fore.RESET+" or "+Fore.CYAN+"'fight'"+Fore.RESET+", not "+Fore.CYAN+"'" + move + "'"+Fore.RESET+"-\n\n")

  while hp <= 0:
    print(Fore.RED+"\n-GAME OVER-\n")
    time.sleep(3)
    clearScreen()

  print("\n   Delerious from travelling for five whole days, you find yourself face to face with your own reflection. A window! You've made it to a small village, with a few shops and vedors here and there.")

vendorLoop = 1

while vendorLoop == 1:
  stats = input(Fore.RESET+"\n\nNext >>> ")

  if stats == "STATS":
    print(Fore.LIGHTGREEN+"\n[" + player + ": Level " + str(playerLevel) + "]\n\n[" + enemy + ": Level " + str(enemyLevel) + "]\n\n[" + weapon + ": Level " + str(weaponLevel) + "]\n\n[Max Health: " + str(maxHealth) + "]\n\n[HP: " + str(hp) + "]\n\n[Gold Multiplier: " + str(goldMultiplier) + "x]\n\n[Gold: " + str(gold) + "]\n")
  
  print("\nAt which vendor would you like to shop?\n")
  print(Fore.MAGENTA+"[Blacksmith]")
  print(Fore.MAGENTA+"[Wizard]")
  print(Fore.MAGENTA+"[Doctor]")
  print(Fore.MAGENTA+"[Banker]")
  print(Fore.LIGHTGREEN_EX+"[STATS]")
  vendor = input(Fore.RESET+"[Leave]\n\n  "+Fore.CYAN)

  if "lacksmith" in vendor: # B L A C K S M I T H
    blacksmithLoop = 1
    upgradeLoop = 1

    while blacksmithLoop == 1:
      if upgradeLoop == 1:
        upgradePrice = 30

      if weaponLevel < 5:
        blacksmith = input(Fore.MAGENTA+"\n[Upgrade " + str(weapon) + "] "+Style.BRIGHT+Fore.LIGHTYELLOW_EX+"(" + str(upgradePrice) + " gold" + ")\n"+Style.RESET_ALL+Fore.MAGENTA+"[Choose new/rename weapon] "+Style.BRIGHT+Fore.LIGHTYELLOW_EX+"(0 gold)\n"+Style.RESET_ALL+Fore.RESET+"[Choose another vendor]\n\n   "+Fore.CYAN)
      elif weaponLevel >= 5:
        blacksmith = input(Fore.MAGENTA+"\n[Upgrade " + str(weapon) + "] "+Fore.LIGHTGREEN_EX+"(Max Level Reached)\n"+Fore.MAGENTA+"[Choose new/rename weapon] "+Style.BRIGHT+Fore.LIGHTYELLOW_EX+"(0 gold)\n"+Style.RESET_ALL+Fore.RESET+"[Choose another vendor]\n\n   "+Fore.CYAN)

      if "pgrade" in blacksmith and gold >= upgradePrice and weaponLevel < 5: # UPGRADE WEAPON
        if gold < upgradePrice:
          print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"\n-Not enough gold-"+Style.RESET_ALL)
          break
        upgradePrice += 20
        upgradeLoop += 1
        weaponLevel += 1
        if weaponLevel < 5:
          print(Fore.RESET+"\nYour " + str(weapon) + " is now level " + str(weaponLevel) + "! "+Fore.LIGHTYELLOW_EX+Style.BRIGHT+"(Next upgrade: " + str(upgradePrice) + " gold)"+Style.RESET_ALL)
        if weaponLevel >= 5:
          print(Fore.RESET+"\nYour " + str(weapon) + " is level 5! "+Fore.LIGHTGREEN_EX+"(Max Level Reached)\n")
        elif weaponLevel < 5:
          gold -= upgradePrice
          print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"\n(Gold - " + str(upgradePrice - 20) + ")\n"+Style.RESET_ALL)
      elif "pgrade" in blacksmith and weaponLevel >= 5:
        print(Fore.LIGHTGREEN_EX+"\n-Max Level Reached-\n")
      elif "ew" in blacksmith or "ename" in blacksmith: # RENAME WEAPON
        weapon = input(Fore.RESET+"\nState the name of your new weapon: \n   "+Fore.CYAN)
        print(Fore.RESET+"\n-Weapon renamed-\n")
      elif "nother" in blacksmith: # NEW VENDOR
        break
      else:
        print(Fore.RESET+"\n-Type '"+Fore.CYAN+"upgrade"+Fore.RESET+"' or '"+Fore.CYAN+"new"+Fore.RESET+"'/'"+Fore.CYAN+"rename"+Fore.RESET+"', not "+Fore.CYAN+"'" + blacksmith + "'-\n")

  elif "izard" in vendor: # W I Z A R D
    wizardLoop = 1
    while wizardLoop == 1:
      if enemyLevel > 1:
        wizard = input(Fore.RESET+"\n[Drain power from " + enemy + "] "+Style.BRIGHT+Fore.LIGHTYELLOW_EX+"(15 gold)\n"+Style.RESET_ALL+"[Nickname enemy] (0 gold)\n[Choose another vendor]\n\n   ")
      elif enemyLevel <= 1:
        wizard = input("\n[Drain power from " + enemy + "] (Minimum Level Reached)\n[Nickname enemy] (0 gold)\n[Choose another vendor]\n\n   ")

      if "rain" in wizard and gold >= 15 and enemyLevel > 1: # LOWER ENEMY LEVEL
        if gold < 15:
          print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"\n-Not enough gold-")
          break
        enemyLevel -= 1
        if enemyLevel > 5:
          print(enemy + " has been reduced to level 1. (Minimum Level Reached)")
        elif enemyLevel <= 1:
          print(enemy + " has been reduced to level " + str(enemyLevel) + ".")
        gold -= 15
        print("\n(Gold - 15)\n")
      elif "rain" in wizard and enemyLevel <= 1:
        print("\n-Minimum Level Reached-\n")
      elif "ickname" in wizard: # RENAME ENEMY
        enemy = input("\nState the name of your enemy: \n   ")
        print("\n-Enemy renamed-\n")
      elif "nother" in wizard: # NEW VENDOR
        break
      else:
        print(Fore.RESET+"\n-Type 'drain' or 'nickname', not '" + wizard + "'-\n")
  
  elif "octor" in vendor: # D O C T O R
    doctorLoop = 1
    while doctorLoop == 1:
      healPrice = int((maxHealth - hp)/3)
      if hp < maxHealth and maxHealth < 200:
        doctor = input("\n[Heal (HP + " + str(maxHealth-hp) + ")] (" + str(int(healPrice)) + " gold)\n[Increase max health] (20 gold)\n[Change name] (0 gold)\n[Choose another vendor]\n\n   ")
      elif hp >= maxHealth and maxHealth < 200:
        doctor = input("\n[Heal] (Fully Healed)\n[Increase max health] (20 gold)\n[Change name] (0 gold)\n[Choose another vendor]\n\n   ")
      elif hp < maxHealth and maxHealth >= 200:
        doctor = input("\n[Heal (HP + " + str(maxHealth-hp) + ")] (" + str(int(healPrice)) + " gold)\n[Increase max health] (Max Health Reached)\n[Change name] (0 gold)\n[Choose another vendor]\n\n   ")
      elif hp >= maxHealth and maxHealth >= 200:
        doctor = input("\n[Heal] (Fully Healed)\n[Increase max health] (Max Health Reached)\n[Change name] (0 gold)\n[Choose another vendor]\n\n   ")
      if "eal" in doctor and 'th' not in doctor and gold >= healPrice and hp < maxHealth: # HEAL
        if gold < healPrice:
          print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"\n-Not enough gold-")
          break
        gold -= int(healPrice)
        print("\nYou have been fully healed to " + str(maxHealth) + " HP.")
        print("\n(Gold - " + str(int(healPrice)) + ")\n")
        hp += (maxHealth-hp)
      elif "eal" in doctor and 'th' not in doctor and hp >= maxHealth:
        print("\n-You are already at full health-\n")
      elif "max" in doctor and gold >= 20 and maxHealth < 200 or "health" in doctor and gold >= 20 and maxHealth < 200: # MAX HEALTH
        if gold < 20:
          print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"\n-Not enough gold-")
          break
        maxHealth += 25
        gold -= 20
        print("\nYour maximum health has been increased to " + str(maxHealth) + "!\n")
        print("(Gold - 20)\n")
      elif "max" in doctor and maxHealth >= 200 or "health" in doctor and maxHealth >= 200:
        print("\n-Max Health Reached-\n")
      elif "ame" in doctor: # RENAME PLAYER
        player = input("\nState the new name of your adventurer: \n   ")
        print("\n-Player renamed-\n")
      elif "nother" in doctor: # NEW VENDOR
        break
      else:
        print(Fore.RESET+"\n-Type 'heal', 'max'/'health', 'name', or 'another', not '" + doctor + "'-\n")
  
  elif "anker" in vendor: # B A N K E R
    bankerLoop = 1
    multiplierLoop = 1
    while bankerLoop == 1:
      if multiplierLoop == 1:
        multiplierPrice = 40

      if goldMultiplier < 3:
        banker = input("\n[Increase gold pickup] (" + str(multiplierPrice) + " gold)\n[Choose another vendor]\n\n   ")
      if goldMultiplier >= 3:
        banker = input("\n[Increase gold pickup] (Max Level Reached)\n[Choose another vendor]\n\n   ")

      if "old" in banker and goldMultiplier < 3.0 or "ickup" in banker and goldMultiplier < 3.0: # GOLD MULTIPLIER
        if gold < multiplierPrice:
          print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"\n-Not enough gold-")
          break
        goldMultiplier += .5
        gold -= multiplierPrice
        multiplierPrice += 25
        multiplierLoop += 1
        print("\nGold multiplier increased to " + str(goldMultiplier) + "x! (Next upgrade: " + str(multiplierPrice) + " gold)")
        print("\n(Gold - " + str(multiplierPrice - 25) + ")\n")
      elif "old" in banker and goldMultiplier >= 3.0 or "ickup" in banker and goldMultiplier >= 3.0:
        print("\n-Max Multiplier Reached-\n")
      elif "nother" in banker: # NEW VENDOR
        break
      else:
        print(Fore.RESET+"-Type "+Fore.CYAN+"'gold'/'pickup'"+Fore.RESET+" or "+Fore.RESET+"'another'"+Fore.RESET+", not '" + banker + "'"+Fore.RESET+"-\n")
  elif "STATS" in vendor:
    print(Fore.LIGHTGREEN_EX+"\n[" + player + ": Level " + str(playerLevel) + "]\n\n[" + enemy + ": Level " + str(enemyLevel) + "]\n\n[" + weapon + ": Level " + str(weaponLevel) + "]\n\n[Max Health: " + str(maxHealth) + "]\n\n[HP: " + str(hp) + "]\n\n[Gold Multiplier: " + str(goldMultiplier) + "x]\n\n[Gold: " + str(gold) + "]\n")
    break
  elif "eave" in vendor:
    stats = input(Fore.RESET+"\n\nNext >>> ")

    if stats == "STATS":
      print(Fore.LIGHTGREEN_EX+"\n[" + player + ": Level " + str(playerLevel) + "]\n\n[" + enemy + ": Level " + str(enemyLevel) + "]\n\n[" + weapon + ": Level " + str(weaponLevel) + "]\n\n[Max Health: " + str(maxHealth) + "]\n\n[HP: " + str(hp) + "]\n\n[Gold Multiplier: " + str(goldMultiplier) + "x]\n\n[Gold: " + str(gold) + "]\n")
    vendorLoop += 1
    break
  else: 
    print(Fore.RESET+"\n-Type '"+Fore.CYAN+"blacksmith"+Fore.RESET+"', '"+Fore.CYAN+"wizard"+Fore.RESET+"', '"+Fore.CYAN+"doctor"+Fore.RESET+"', '"+Fore.CYAN+"banker"+Fore.RESET+"', or '"+Fore.CYAN+"leave"+Fore.RESET+"', not '"+Fore.CYAN + vendor + Fore.RESET+"'-")

print("\n-Type 'SHOP' after 'Next >>>' to go back to the village- (Next >>> SHOP)\n")