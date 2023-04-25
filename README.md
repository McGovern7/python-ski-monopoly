# Python Ski Monopoly

## How the game functions:

### First screen (start screen) - 
- Multiplayer: All players should type in the Server IP and then will get a message if they are connected or not
- Single player: Select the icon you want to play as and the number of computers you want to play against
  - About the computers: The computers will always buy whatever they land on until they run out of money. Once they run
  - out of money they will start selling their utilities, then railroads, then properties if needed

### Second screen (turn screen) - 
- Then each player will roll to see the order that the turn will occur in for the entire game.

### Third screen (board screen) - 
- You will then be sent to the game board and whoever had the largest first roll will play first
- When it is your turn, there will be text that indicates this and a 'ROLL' button will appear (press this or
- press the space bar to roll)
- When you purchase properties you will be able to see them if you press the "Inspect Properties" button
- When you purchase railroads/utilities you will be able to see them if you press the "Other Cards" button

### Fourth screen (property screen) & fifth screen (property screen 2) -
- This screen has all the deed for the properties that you own
- There is also a button to mortgage a property (you will receive back half the price but will get no rent 
- if someone lands on it)
- If you have a monopoly (own all cards of a certain color), you will be able to hit the 'House' button to buy a house
- If you have a house, you will then be able to hit the 'Hotel' button to buy a hotel

### Sixth screen (other card screen) - 
- This screen has the cards for railroads, utilities, and holds your get out of jail free cards
- There is a button to mortgage your railroads and utilities if needed

### Seventh screen (lose screen) - 
- If you end a turn with less than $1 in your bank account, you will see a screen indicating that you lost
- Side note: if a computer loses, you will know because their icon will disappear from the board

### Eighth screen (win screen) - 
- If you are the last player with money in your bank account, you will see a screen indicating that you won!

## Other important info...
### DICE -
- If you roll doubles - you get to roll again
- If you roll doubles for the third time - you go to jail

### How each square functions in this game -
- Go: each time you pass it, $200 will be added to your bank account
- Property:
    - If there is no owner, you will see a pop-up message asking if you would like to buy the property? (you can say yes or no)
    - If the property is already owned, the rent will be subtracted from your bank account and put into the landlord's 
bank account
- Community chest: You will pull a random card with a message and will probably have money added or subtracted from 
your bank account
- Chance: You will pull a random card with a message and might move spaces or gain/lose money
  - *If you move to a new space, you get to interact with the new space
- Tax (Ski wax/Gear upgrade): Either $200 or 10% of your total money (whichever is lower) will be taken from 
your bank account
- Railroad (ski lifts): Same functionality as properties, however if someone owns more than one railroad the rent 
will increase with each one they buy
- Jail: You can be put in jail by a chance/community chest card or by landing on 'Go to jail'
  -  You will see a message telling you that you are in jail (as well as see your piece move to the jail space)
  - You will be asked if you want to pay $50 to get out
  - If you don't pay this, you won't be able to roll for your next turns
  - After you roll three times, you will be forced to pay $50 to get out
  - If you just land on the space, you will be in the 'just visiting' section
- Utility (snow gun/ snow groomer): Same functionality as properties, but the rent is determined by what number you 
rolled to get to that space (rent = 4 times dice roll or rent= 10 times dice roll if you own both)
- Free parking: no money gained or lost


## Sources
- Pygame tutorial 1: https://www.youtube.com/watch?v=FfWpgLFMI7w 
- Screen tutorial: https://www.youtube.com/watch?v=8X2F2_iS4do
- Pygame screen tutorial: https://www.google.com/search?q=how+to+create+different+screens+in+pygame&sxsrf=AJOqlzWyKeUpdmNwj_nGGjanXkqtNZz_8w:1678246634177&source=lnms&tbm=vid&sa=X&ved=2ahUKEwjW0ebzs8v9AhVCF1kFHagnAVwQ_AUoAXoECAEQAw&biw=1308&bih=733&dpr=2#fpstate=ive&vld=cid:1832b6a2,vid:GMBqjxcKogA
- All icons are from: FlatIcon.con -- https://www.flaticon.com/search?word=ski%20resort
