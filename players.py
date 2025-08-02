'''
Create a class Player with below attributes:

playerId - int
playerName - String
runs - int
playerType - String
matchType - String

write constructor as required. 

Create class Solution with main method. 

Implement two static methods - 
findPlayerWithLowestRuns and 
findPlayerByMatchType in Solution class.

findPlayerWithLowestRuns method:
This method will take array of Player 
objects and a String value as input 
parameters.
The method will return the least runs 
of the Player from array of Player 
objects for the given player type.
(String parameter passed). If no Player 
with the above condition are present in 
array of Player objects,
then the method should return 0.

findPlayerByMatchType method:
This method will take array of Player 
objects and String value as input parameters 
and return the array of Player objects
belonging to the match type passed as 
input parameter in Descending order of 
playerId.
If no Player with the above condition are 
present in the array of Player objects, 
then the method should return null.

Note : No two Players will have the same 
playerId and runs.
All the searches should be case insensitive.

The above mentioned static methods should 
be called from the main method. 

For findPlayerWithLowestRuns  method - The 
main method should print the returned runs 
as it is
if the returned value is greater than 0 or 
it should print "No such player".

Eg: 25
where 25 is the lowest runs of the Player.

For findPlayerByMatchType method - The main 
method should print the playerId from the 
returned Player array for each
Player if the returned value is not null. 
If the returned value is null then it should 
print "No Player with given matchType".


Eg:
13
11
where 13 and 11 are the playerId's.

Before calling these static methods in 
main, use Scanner object to read the values 
of four Player
objects referring attributes in the above 
mentioned attribute sequence. 
Next, read the value of two String parameter 
for capturing player type and match Type.
'''

class Player:
    def __init__(self, playerId, playerName, runs, playerType, matchType):
        self.playerId= playerId
        self.playerName= playerName
        self.runs= runs
        self.playerType= playerType
        self.matchType= matchType

class Solution:
    @staticmethod
    def findPlayerWithLowestRuns( players, input_playerType):
        runs_list=[]

        for player in players:
            if player.playerType.lower()== input_playerType.lower():

                runs_list.append(player.runs)

        


        if runs_list==[]:
            print ("No Such Player")
        else:
            print(min(runs_list))
        

    @staticmethod
    def findPlayerByMatchType(players, input_matchType):
        player_list=[]

        for player in players:
            if player.matchType.lower()== input_matchType.lower():
                player_list.append(player)

        player_list.sort(key=lambda player:player.playerId, reverse=True)

        # print(f"This is sorted list: {sorted_player_list}")

        if player_list==[]:
            print("No Player with given matchType")
        else:
            for i in player_list:
                print(i.playerId)
        

n=4

players_obj=[]

for i in range(n):
    playerId= int(input())
    playerName= input()
    runs= int(input())
    playerType= input()
    matchType=input()

    players_obj.append(Player(playerId, playerName, runs, playerType, matchType))

input_playerType= input()
input_matchType= input()

Solution.findPlayerWithLowestRuns(players_obj, input_playerType)
Solution.findPlayerByMatchType(players_obj, input_matchType)

'''
Consider below sample input and output:

Input1:
11
Sachin
100
International
One day
12
Shewag
133
International
Test
13
Varun
78
State
Test
14
Ashwin
67
State
One day
State
One day

Output:
67
14
11


Input2:
11
Sachin
100
International
One day
12
Shewag
133
International
Test
13
Varun
78
State
Test
14
Ashwin
67
State
One day
District
T20


Output:
No such player
No Player with given matchType
'''
    
