#! python3
# sandwichMaker_2.0.py a script that asks user their sandwich preferences.

import pyinputplus as pyip
import sys
#help(pyip.inputInt)
MM = {
        'bread':{'Wheat': 1.00,
                'White': .75,
                'Sourdough': 1.50
        },
        'protein':{'Chicken': 1.50,
                    'Turkey': 2.00,
                    'Ham': 1.00,
                    'Tofu': 2.00
        },
        'cheese':{'Cheddar': 1.00,
                'Swiss': 1.25,
                'Mozzarella': 1.75,

        },
        'extras':{'Mustard': .25,
                'Lettuce': .50,
                'Tomato': .50,
                'Mayo': .25
        }
}

totalCost = []
qty = 0
qtySame = 0
counter = 0

def addFood(ingredient, options, prices):
    if ingredient != 'bread' and ingredient != 'protein':   #print only if ingredient is optional.
        wantPrt = f'Would you like {ingredient}? '
        if pyip.inputYesNo(prompt=wantPrt) == 'no':
           return None
        if ingredient == 'extras':                  # ask extras individually
            wantIndiv(ingredient, options)
            return None
    if ingredient == 'bread' and counter < qty:     #print only if is new custom sandwich
        print('Ok, now on to the next sandwich.')
    upPrompt = f'What kind of {ingredient} would you like?\n'
    showPrices(options, prices)                                 #print options and prices
    response = pyip.inputMenu(options,prompt=upPrompt, numbered=True)   #Ingredient choice made
    for i in range(len(options)):
        if response != options[i]:
            continue
        if response == options[i]:
            totalCost.append(prices[i])                         # add price to tally
            #MM[newPrompt].get(options[i])

def wantIndiv(ingredient, options):
    for j in range(len(options)):
        indivOpt = f'{options[j]}? '
        if pyip.inputYesNo(prompt=indivOpt) == 'yes':
            totalCost.append(MM[ingredient].get(options[j]))
            print('Total: $'+str(sum(totalCost)))

def showPrices(options, prices):
    display = 0
    for d in range(len(options)):
        if display < len(options[d]):
            display = len(options[d])
    print()
    for p in range(len(prices)):
        print(options[p].ljust(display+2,'_'), end='')
        print('$'+str(prices[p]))
    print()

#DO YOU WANT SANDWICH?
order = pyip.inputYesNo(prompt='Would you like a sandwich? ')
if order  == 'yes':
    qty = pyip.inputInt(prompt='Cool. How many do you want? ',min=1)
    counter = qty
    if qty > 1:
        if pyip.inputYesNo(prompt='Will those be identical with all the same ingredients?') == 'yes':
            qtySame = qty - 1
            qty = 1
elif order  == 'no':
    print('No problem. Maybe next time.\n')
    sys.exit()

#Iterate through Main Menu (MM) options.
for s in range(qty):
    for i, val in enumerate(MM):
        addFood(list(MM.keys())[i], list(MM[val].keys()), list(MM[val].values()))
        print('Total: $'+str(sum(totalCost)))
        counter -= 1

grandTotal = (qty+qtySame)*(sum(totalCost))
print('Ok. Your total comes to: $'+str(grandTotal))





"""
menuList = list(MM)

pBread = 'What kind of bread would you like?\n'
pProtein = 'What kind of protein would you like?\n'
pYesNoCheese = 'Would you like cheese?'
pCheese = 'What kind of cheese would you like?\n'
pMayoYN = 'Mayo?'
pMstrdYN = 'Mustard?'
pLttceYN = 'Lettuce?'
pTmtoYN= 'Tomato?'
pHowMany = 'How many sandwiches do you want?\n'

pList = [pBread,pProtein,pYesNoCheese,pCheese,pMayoYN,pMstrdYN,pLttceYN,pTmtoYN,pHowMany]

qty = 0
numSndwch = 0
hungry = True
moreSndw = True
while hungry:

    #TYPE OF BREAD
    addFood(pList[0], menuList[0:2+1])
    print('Total: $'+str(sum(totalCost)))

    #TYPE OF PROTEIN
    addFood(pList[1], menuList[3:6+1])
    print('Total: $'+str(sum(totalCost)))

    #WANT CHEESE?
    wantThis(pList[2],pList[3],menuList[7:9+1])
    print('Total: $'+str(sum(totalCost)))

    #MAYO/MUSTARD/LETTUCE/TOMATO?
    wantIndiv(pList[4:7+1],menuList[10:13+1])
    #print('Total: $'+str(sum(totalCost)))

    qty += 1
    if qty == numSndwch:
        #hungry = False

    # HOW MANY SANDWICHES?
    if moreSndw == True:
        numSndwch = pyip.inputInt(prompt=pList[-1],min=1)
        if numSndwch == 1:
            hungry = False
        if numSndwch > 1:
            moreSndw = False
            allSame = pyip.inputYesNo(prompt='All the same kind?')
            if allSame == 'yes':
                hungry = False


grandTotal = numSndwch*(sum(totalCost))
print('Ok. Your total comes to: $'+str(grandTotal))
"""
