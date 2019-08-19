# sherlockwatson
Simple zero players game between Sherlock and Watson

Problem statement
Sherlock and Watson just got off a crime case and were really bored. They decided to play a board game which given to them by a former client of theirs. The game is called "The Great Game". The Great Game starts by writing an array that is given on the board. Sherlock and Watson take turns by removing exactly one number from the array, Sherlock takes first turn, obviously.
Following are the rules :-
1. If at any point of the game, removing a number causes the XOR-ALL(bitwise XOR of the entire array) to be 0, the player loses.
2. Bitwise XOR of one number is that number itself.
3. If any player starts their turn with XOR-ALL equal to 0, that player wins.

Assume that both Sherlock and Watson play this game optimally. Given an array, print "Sherlock" if he wins, else print "Watson", without the double quotes.
Input
The first line contains T, the number of test cases.
Each test case contains 2 lines, the first line contains N, the number of elements in the array. The second line contains N space separated integers.
Output
For each test case, print the winner in a new line. If Sherlock wins, print "Sherlock" or if Watson wins, print "Watson".
Constraint
1 ≤ T ≤ 1000
1 ≤ N ≤ 1000
0 ≤ A[i] ≤ 2^16
