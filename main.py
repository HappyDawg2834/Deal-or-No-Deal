#December 2021

from random import shuffle
from time import sleep
from os import system
import statistics

system("clear")

playing = "p"
IChosenCase = "hi"
SChosenCase = "hi"
ChosenCase = "hi"
cpick = ""
apick = ""
title = "true"
offer = "false"
lstround = "false"
bank = 0
missingcase = 0
rndcount = 0


cases = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
money = [.01,1,5,10,25,50,75,100,200,300,400,500,750,1000,5000,10000,25000,50000,75000,100000,200000,300000,400000,500000,750000,1000000]
shuffle(money)
usedMoney = []
usedCases = []
moneywon = 0

def moneyMatch(damoney):
  if float(damoney)==.01:
    return ["$ .01","     "]
  elif int(damoney)==1:
    return ["$ 1", "   "]
  elif int(damoney)==5:
    return ["$ 5","   "]
  elif int(damoney)==10:
    return ["$ 10","    "]
  elif int(damoney)==25:
    return ['$ 25',"    "]
  elif int(damoney)==50:
    return ['$ 50',"    "]
  elif int(damoney)==75:
    return  ['$ 75',"    "]
  elif int(damoney)==100:
    return  ['$ 100',"     "]
  elif int(damoney)==200:
    return  ['$ 200',"     "]
  elif int(damoney)==300:
    return  ['$ 300',"     "]
  elif int(damoney)==400:
    return  ['$ 400',"     "]
  elif int(damoney)==500:
    return  ['$ 500',"     "]
  elif int(damoney)==750:
    return  ['$ 750',"     "]
  elif int(damoney)==1000:
    return  ['$ 1,000',"   "]
  elif int(damoney)==5000:
    return  ['$ 5,000',"   "]
  elif int(damoney)==10000:
    return  ['$ 10,000',"   "]
  elif int(damoney)==25000:
    return  ['$ 25,000',"   "]
  elif int(damoney)==50000:
    return  ['$ 50,000',"   "]
  elif int(damoney)==75000:
    return ['$ 75,000',"   "]
  elif int(damoney)==100000:
    return  ['$ 100,000',"   "]
  elif int(damoney)==200000:
    return  ['$ 200,000',"   "]
  elif int(damoney)==300000:
    return  ['$ 300,000',"   "]
  elif int(damoney)==400000:
    return  ['$ 400,000',"   "]
  elif int(damoney)==500000:
    return  ['$ 500,000',"   "]
  elif int(damoney)==750000:
    return  ['$ 750,000',"   "]
  elif int(damoney)==1000000:
    return  ['$ 1,000,000',"   "]


def banker():
  finalstatementforbanker = 0
  anothertotalstankn = []
  numsoftotalsleft = []
  totalstaken = 0
  numofusedCases = 0
  for x in usedCases:
    anothertotalstankn.append(money[x-1])
    totalstaken+=money[x-1]
    numofusedCases +=1
  for x in money:
    if x not in anothertotalstankn:
      numsoftotalsleft.append(x)
  totalsleft = 3418416.01 - totalstaken
  numofcasesleft =  26 - numofusedCases
  avg = totalsleft/numofcasesleft
  median = statistics.median(numsoftotalsleft)
  mstatement1 = median+5000
  mstatement = median
  mstatement = int(mstatement)
  statement = (avg)*.13
  statement = int(statement)
  anavg = (mstatement + statement)/2
  tres = int((mstatement + statement))
  anavgstatement = anavg
  if rndcount<2:
    finalstatementforbanker = mstatement1
  elif 2>rndcount:
    finalstatementforbanker = tres
  else:
    finalstatementforbanker = tres
  return [int(finalstatementforbanker)]

def board():

  cb = ["1","2","3",'4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']

  moneys = ['$ .01','$ 1','$ 5','$ 10','$ 25','$ 50','$ 75','$ 100','$ 200','$ 300','$ 400','$ 500','$ 750','$ 1,000','$ 5,000','$ 10,000','$ 25,000','$ 50,000','$ 75,000','$ 100,000','$ 200,000','$ 300,000','$ 400,000','$ 500,000','$ 750,000','$ 1,000,000']

  if ChosenCase!="hi":
    cb[IChosenCase] = ""
    for ltr in SChosenCase:
      cb[IChosenCase]+=" "
  
  annoyingnum = 0
  while annoyingnum != 26:
    for x in usedCases:
      if str(x) == str(cb[annoyingnum]):
        aa = moneyMatch(money[annoyingnum])
        position = moneys.index(aa[0])
        moneys[position] = aa[1]
        cb[annoyingnum] = ""
        for ltr in str(x):
          cb[annoyingnum]+=" "
    annoyingnum += 1

  print('-------------------------------')
  if title == "true":
    print("       DEAL OR NO DEAL")
  elif title == "false":
    if bank<100:
      print("      * * OFFER: ${:,} * *".format((bank)))
    elif 100<=bank<1000:
      print("     * * OFFER: ${:,} * *".format((bank)))
    elif 1000<=bank<10000:
      print("    * * OFFER: ${:,} * *".format((bank)))
    elif 10000<=bank<100000:
      print("    * * OFFER: ${:,} * *".format((bank)))
    elif 100000<=bank<1000000:
      print("    * * OFFER: ${:,} * *".format((bank)))
    else:
      print("OFFER: ${:,}".format((bank)))
  print('-------------------------------\n[  {:s}   {:s}   {:s}   {:s}   {:s}   {:s}   {:s}  ]\n[  {:s}   {:s}  {:s}  {:s}  {:s}  {:s}  {:s}  ]\n[ {:s}  {:s}  {:s}  {:s}  {:s}  {:s}  {:s}  ]\n[ {:s}  {:s}  {:s}  {:s}  {:s}          ]\n-------------------------------'.format(cb[0],cb[1],cb[2],cb[3],cb[4],cb[5],cb[6],cb[7],cb[8],cb[9],cb[10],cb[11],cb[12],cb[13],cb[14],cb[15],cb[16],cb[17],cb[18],cb[19],cb[20],cb[21],cb[22],cb[23],cb[24],cb[25],))
  print('{:>s}{:>26s}\n{:>s}{:>28s}\n{:>s}{:>28s}\n{:>s}{:>27s}\n{:>s}{:>27s}\n{:>s}{:>27s}\n{:>s}{:>27s}\n{:>s}{:>26s}\n{:>s}{:>26s}\n{:>s}{:>26s}\n{:>s}{:>26s}\n{:>s}{:>26s}\n{:>s}{:>26s}'.format(moneys[0],moneys[13],moneys[1],moneys[14],moneys[2],moneys[15],moneys[3],moneys[16],moneys[4],moneys[17],moneys[5],moneys[18],moneys[6],moneys[19],moneys[7],moneys[20],moneys[8],moneys[21],moneys[9],moneys[22],moneys[10],moneys[23],moneys[11],moneys[24],moneys[12],moneys[25]))
  if ChosenCase != "hi":
    print("-------------------------------")
    if lstround == "false":
      print("   YOU ARE HOLDING CASE #"+SChosenCase+" ")
    if lstround != "false":
      if lstround == "switch":
        print("        YOU HAD #" + SChosenCase + " BUT")
      else:
        pass
      print("      YOU OPENED CASE #"+str(int(missingcase))+" ")
      if bank<100:
        print("          * * ${:,} * *".format((bank)))
      elif 100<=bank<1000:
        print("        * * ${:,} * *".format((bank)))
      elif 1000<=bank<10000:
        print("        * * ${:,} * *".format((bank)))
      elif 10000<=bank<100000:
        print("       * * ${:,} * *".format((bank)))
      elif 100000<=bank<1000000:
        print("       * * ${:,} * *".format((bank)))
      else:
        print("${:,}".format((bank)))

  print("-------------------------------\n")

board()

def caseChecker(acase):
  apick = acase
  while True:
    if apick.isdigit():
      apick = int(apick)
      if 0<apick<27 and apick not in usedCases and apick != ChosenCase:
        return apick
        break
      else:
        apick = input("Please enter a valid case number: ")
        pass
    elif apick == "q":
      return "q"
      break
    else:
      apick = input("Please enter a valid case number: ")
      pass



print("Try to earn the most money!!!\nYou can enter q anytime to quit")
play = input("Would you like to play? ").lower()


while True:
  if play == "y" or play == "yes":
    system("clear")
    board()
    print("Let's get started then!")
    sleep(0.1)
    pickCase = input("To start, enter the case number that you wish to take: ")
    break
  elif play == "q":
    playing = "q"
    break
  else:
    play = input("Please enter y if you change your mind or if you wish to quit enter q: ").lower()

while playing != "q":
  if pickCase.isdigit():
    pickCase = int(pickCase)
    if 0<pickCase<27:
      SChosenCase = str(pickCase)
      IChosenCase = pickCase-1
      ChosenCase = pickCase
      system("clear")
      board()
      break
    else:
      pickCase = input("Please enter a number between 1 and 26: ")
      pass
  elif pickCase == "q":
    playing = "q"
    break
  else:
    pickCase = input("Please enter a number between 1 and 26: ")
    pass
    
if playing != "q":
  firstM = money[IChosenCase]

if playing != "q":
  sleep(1.0)
  cont = input("Are you ready to start opening the other cases? ").lower()
while playing != "q":
  if cont == "y" or cont == "yes":
    system("clear")
    board()
    print("Let's Go!")
    break
  elif cont == "q":
    playing = "q"
    break
  else:
    cont = input("Please enter y when you are ready to continue: ").lower()

darounds = [6,5,4,3,2,1,1,1,1]

for around in darounds:
  count = around
  rndcount+=1
  while playing != "q" and count!=0:
    if playing!="q":
      print("You need to open",count,"cases")
      cpick = input("Please choose a case to open: ")
      cpick = caseChecker(cpick)
      if str(cpick) != "q":
        system("clear")
        board()
        print("You chose case",str(cpick)+"!")
        print("It is worth...")
        sleep(.75)
        lstchangenum = cases.index(cpick)
        lstchange = cases.pop(lstchangenum)
        erasemoneynum = cpick - 1
        erasemoney = money[erasemoneynum]
        usedCases.append(lstchange)
        system("clear")
        board()
        nicemoneyformat = str('{:,}'.format(erasemoney))
        print("Case",str(cpick),"=","$"+nicemoneyformat+"!")
        count -=1
      else:
        playing = "q"
        pass

  if playing != "q":
    banking = banker()
    bank = banking[0]
    bank = (bank)
    title = "false"


  if playing != "q":
    sleep(.75)
    cont = input("Are you ready for your offer? ").lower()
  while playing != "q":
    if cont == "y" or cont == "yes":
      system("clear")
      board()
      break
    elif cont == "q":
      playing = "q"
      break
    else:
      cont = input("Please enter y when you are ready to continue: ").lower()


  if playing != "q":
    sleep(1.0)
    cont = input("Do you wish to take (t) or decline (d): ").lower()
  while playing != "q":
    if cont == "t":
      offer = "true"
      playing = "q"
      moneywon = bank
      system("clear")
      board()
      break
    elif cont == "d":
      system("clear")
      title = "true"
      board()
      print("You have declined the offer!!")
      break
    elif cont == "q":
      playing = "q"
      break
    else:
      cont = input("Please enter t or d: ").lower()

if playing != "q":
  sleep(1.5)
  system("clear")
  board()
  print("You are now on the final round!!")
  print("Remember, you are holding case",ChosenCase)
  lastround = input("Do you wish to open your case (o) or switch cases (s)? ").lower()
  multiplystrat = ChosenCase
  for idk in usedCases:
    multiplystrat*=idk
  missingcase = 403291461126605635584000000/multiplystrat
  int(missingcase)


while playing != "q":
  if lastround == "o":
    system("clear")
    board()
    print("Your case is worth...")
    sleep(3.0)
    system("clear")
    lstround = "true"
    bank = money[IChosenCase]
    moneywon = bank
    board()
    break
  elif lastround == "s":
    system("clear")
    board()
    print("You are swithcing cases...")
    sleep(3.0)
    lstround = "switch"
    bank = money[(int(missingcase-1))]
    moneywon = bank
    system("clear")
    board()
    nicemoneyformat = str('{:,}'.format(moneywon))
    print("Case",str(int(missingcase)),"=","$"+nicemoneyformat+"!")
    break
  else:
    print("Please enter either o or s")
    pass
sadcounts = 0
if playing == "q" and offer == "false":
  system("clear")
  print("I can't believe you quit")
  while sadcounts < 100:
    print(":(   ")
    sleep(.1)
    sadcounts+=1

if playing == "q" and offer == "true":
  nicemoneyformat = str('{:,}'.format(moneywon))
  print("You won:","$"+nicemoneyformat+"!!!")
  sleep(2.0)
  nicemoneyformat = str('{:,}'.format(money[IChosenCase]))
  print("Your original case had $"+nicemoneyformat)
  if bank>money[IChosenCase]:
    print("You made money!!!     :)")
  else:
    print("You did not make money    :(\nHowever, you still did get some money!")

if lstround != "false":
  damissingcase = int(missingcase)
  damissingcase = damissingcase-1
  damissingcase = int(damissingcase)
  if lstround == "true":
    nicemoneyformat = str('{:,}'.format(money[IChosenCase]))
    print("Case #"+SChosenCase+" was worth $"+nicemoneyformat+"!!!")
    sleep(2.0)
    nicemoneyformat = str('{:,}'.format(int(money[damissingcase])))
    print("The other case had $"+ nicemoneyformat)
    if money[damissingcase]<money[IChosenCase]:
      print("You made a good choice!!!     :)")
    else:
      print("You made a bad choice   :(\nHowever, you still did get some money!")
  elif lstround == "switch":
    nicemoneyformat = str('{:,}'.format(int(money[damissingcase])))
    print(str(int(missingcase))+" was worth $"+nicemoneyformat+"!!!")
    sleep(2.0)
    nicemoneyformat = str('{:,}'.format(money[IChosenCase]))
    print("Your original case had $"+ nicemoneyformat)
    if money[damissingcase]>money[IChosenCase]:
      print("You made a good choice!!!     :)")
    else:
      print("You made a bad choice   :(\nHowever, you still did get some money!")

        








