from words import word


run = True
tries = 0
guessed_letters = []


live_one = [["_","_","_","_ "," "],
			["|"," "," "," |"," "],
			["|"," "," ","  "," "],
			["|"," "," ","  "," "],
			["|"," "," ","  "," "],
			["|"," "," ","  "," "],
			["|"," "," ","  "," "],]

live_two = [["_","_","_","_ "," "],
			["|"," "," "," |"," "],
			["|"," "," "," O"," "],
			["|"," "," ","  "," "],
			["|"," "," ","  "," "],
			["|"," "," ","  "," "],
			["|"," "," ","  "," "],]
live_three =[["_","_","_","_ "," "],
			["|"," "," "," |"," "],
			["|"," "," "," O"," "],
			["|"," "," "," |"," "],
			["|"," "," "," |"," "],
			["|"," "," ","  "," "],
			["|"," "," ","  "," "],]

live_four = [["_","_","_","_ "," "],
			["|"," "," "," |"," "],
			["|"," "," "," O"," "],
			["|"," "," "," |\\",""],
			["|"," "," "," |"," "],
			["|"," "," ","  "," "],
			["|"," "," ","  "," "],]

live_five = [["_","_","_","_ "," "],
			["|"," "," "," |"," "],
			["|"," "," "," O"," "],
			["|"," ",""," /|\\",""],
			["|"," "," "," |"," "],
			["|"," "," ","  "," "],
			["|"," "," ","  "," "],]

live_six =  [["_","_","_","_ "," "],
			["|"," "," "," |"," "],
			["|"," "," "," O"," "],
			["|"," ",""," /|\\",""],
			["|"," "," "," |"," "],
			["|"," "," ","  \\"," "],
			["|"," "," ","   |"," "],]

live_sev =  [["_","_","_","_ "," "],
			["|"," "," "," |"," "],
			["|"," "," "," O"," "],
			["|"," ",""," /|\\",""],
			["|"," "," "," |"," "],
			["|"," "," ","/ \\"," "],
			["|"," "," ","|  |"," "],]

lives = [live_one,live_two,live_three,live_four,live_five,live_six,live_sev]
def live(count):
	for i in lives[count]:
		for j in i:
			print(j,end = " ")
		print("\n")	


live(0)
print("_ "*len(word))
while run and tries<6:	
	flag = 1
	print("\nguess the word")    
	letters = input().upper()
	if letters in guessed_letters:
		print("\nletter already guessed")
		letters = input().upper()
	else:	
		if len(letters) == 1 and letters in word:
				print("\nguess was correct\n")
		elif len(letters) > 1:
			if letters == word:
				print("\nYou won the game")
				break
			else:
				tries+=1
		else: 
			tries +=1
		guessed_letters.append(letters)		
		live(tries)
	for i,pos in enumerate(word):
		if pos in guessed_letters:
			print(pos+" " ,end="")
		else:
			flag = 0
			print("_ ",end = "")	
	if flag == 1 or letters == 1:
		print("\nYou won the game")
		run = False

if tries==6:
	print("\nYou Lost")
	print("\nword was: ",word)	
    
