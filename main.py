#!/usr/bin/env python3

#
# Autor   : Wyv3rn
# Version : 0.5.0
#

# Imports
import json
import os

def Help():
    print("""
0. Task Complete get Reward
1. Show Skills
2. Add Skill
3. Edit Skill
4. Delete Skill
exit -> Exit
help -> Help
clear -> clear output
""")

def ReadJson():
# Load Json get Player-Data
    with open('LiveRPG.json', 'r') as f:
        data = json.load(f)
    return data

def WriteJson(data):
    with open('LiveRPG.json' ,'w') as outfile:
        json.dump(data, outfile)

def ClearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def PlayerStats(data):
    # for playerData in data:
    print('\nPlayerlevel : ', data[0]['playerlevel'])
    print('All-Gained-EXP : ', data[0]['expgained'])
    print('Next Level in: ', data[0]['nextLevelIn'])

def PlayerSkills(data):
    i = 0
    for skill in data:
        print('Skill :' , data[i]['Skill'], ' Level: ', data[i]['level'], ' EXP: ' , data[i]['exp'])
        if(i >= len(data) - 1):
           break
        else:
          i += 1

# Interace Level
def LevelUpSkill(data):
   skillName = input("\nEnter SkillName you have Done a Task: ")
   i = 1
   for idx, item in enumerate(data[1:]):
       if(i <= len(data) -1):
           if(item['Skill'] == skillName):
             item['exp'] += 100
             data[0]['expgained'] += 100
             if(item['exp'] >= item['nextLevelIn']):
                item['nextLevelIn'] += 1000
                item['exp'] = 0
                item['level'] += 1
                del data[i]
             if(data[0]['expgained'] >= data[0]['nextLevelIn']):
                   data[0]['playerlevel']  += 1
                   data[0]['nextLevelIn'] += 1500
             data[1:] = item
       else:
         break
       i += 1
   WriteJson(data)
# Skill Json Manipulation Methods
def EditSkill(data):
    i = 1
    skillName = input("\nEnter Skillname to Edit: ")
    for idx, item in enumerate(data[1:]):
      if(i <= len(data) - 1):
         if skillName in item['Skill']:
            newName = input("Enter New Name: ")
            item['Skill'] = newName
            del data[i]
            data = item
      else:
         break
    WriteJson(data)

def DeleteSkill(data):
    i = 0
    skillName = input("\nEnter Skillname to Delete: ")
    for idx , Item in enumerate(data[1:]):
        i += 1
        if(Item['Skill'] == skillName):
             del data[i]
    WriteJson(data)

def AddSkill(data):
    skillName = input("\nEnter New Skillname: ")
    # Check if skill already Exist, if "True" Skip
    data.append({"Skill": skillName, "level": 0, "exp": 0, "nextLevelIn": 1000})
    WriteJson(data)

# Main Method
def Main():
    # Clear Console
    ClearConsole()
    # Load Json get Player-Data
    data = ReadJson()
    # start Screen
    print('Hackers-Live RPG\nBy Wyv3rn')
    print('\nEnter Help for get Options')
    # Main Run
    while True:
        # Print -> Player-Data
        PlayerStats(data)
        # Game Starts Here
        print('\n')
        # Choose Menue Option and Call Method
        choice = input("Choose your Option : ")
        if(choice == '1'):
            ClearConsole()
            PlayerSkills(data[1:])
        elif(choice == '2'):
            ClearConsole()
            AddSkill(data)
        elif(choice == '3'):
            ClearConsole()
            EditSkill(data)
        elif(choice == '4'):
            ClearConsole()
            DeleteSkill(data)
        elif(choice == 'exit'):
            ClearConsole()
            break
        elif(choice == 'help'):
            ClearConsole()
            Help()
        elif(choice == 'clear'):
            ClearConsole()
        elif(choice == '0'):
            ClearConsole()
            LevelUpSkill(data)
        else:
            ClearConsole()
            print('wrong entry , try again')
# Run Main Method then main.py is Called
Main()
