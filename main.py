import pygame
import os
import words as wd

pygame.init()

WIDTH = 1100
HEIGHT =700
letter_width = 50
space_width = 20

x_pos = 100
y_pos = 45

# word_size = letter_width*len(wd.choose) + space_width*(len(word)-1)
Alpha_font = pygame.font.SysFont("comicsans",50)
hangman_img = [pygame.image.load('hangman0.png'),pygame.image.load('hangman1.png'), pygame.image.load('hangman2.png'), pygame.image.load('hangman3.png'), pygame.image.load('hangman4.png'), pygame.image.load('hangman5.png'), pygame.image.load('hangman6.png')]

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x_pos,y_pos)
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Hangman')




def main():
	guessed_letters = []
	run = True
	tries = 0
	word = wd.chooseword()
	word_size = letter_width*len(word) + space_width*(len(word)-1)
	print(word)
	while run and tries != 6:
		alphabet_x = 500
		alphabet_y = 100
		Mouse_x = Mouse_y = 0
		letters = None
		flag = 0
		check = 1 
		letter_x_pos = WIDTH/2 - word_size/2

		win.fill((255,255,0))
		title = Alpha_font.render("HANGMAN",1,(100, 20, 75))
		win.blit(title,(WIDTH/2 - title.get_width()/2, 25,40,40 ))

		# pygame.draw.rect(win,(0,0,0),(500,100,400,350),5)

		event = pygame.event.wait()
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			Mouse_x, Mouse_y = pygame.mouse.get_pos()

		for i in range(65,91):
			if alphabet_x+space_width>900:
				alphabet_x = 500
				alphabet_y+= 70 
			aplhabets = Alpha_font.render(chr(i),1,(100, 20, 50))
			pygame.draw.circle(win,(51, 187, 255),(alphabet_x+25,alphabet_y+25),25)
			win.blit(aplhabets,(alphabet_x+12, alphabet_y+10,40,40 ))
			if chr(i) in guessed_letters:
				pygame.draw.line(win,(255,0,0),(alphabet_x,alphabet_y),(alphabet_x+letter_width,alphabet_y+letter_width),3)
				pygame.draw.line(win,(255,0,0),(alphabet_x+letter_width,alphabet_y),(alphabet_x,alphabet_y+letter_width),3)

			if alphabet_x< Mouse_x <alphabet_x+letter_width and alphabet_y<Mouse_y<alphabet_y+letter_width:
				letters = str(chr(i))
				flag = 1
				Mouse_x = 0
				Mouse_y = 0	
			alphabet_x+=space_width+letter_width

		if letters in guessed_letters:
			flag = 0			
		if flag ==1:
			if not str(letters) in word:
				tries+=1
			guessed_letters.append(letters)		

		for i,pos in enumerate(word):
			pygame.draw.line(win,(161,61,45),(letter_x_pos,600),(letter_x_pos+letter_width,600),3)	
			if pos in guessed_letters:
				lettrs = Alpha_font.render(pos,1,(100, 20, 50))
				win.blit(lettrs,(letter_x_pos+10,555,40,40 ))
			else:
				check = 0
			letter_x_pos+=space_width + letter_width

		if check == 1:
			winner_font = pygame.font.SysFont("comicsans",50)
			won = winner_font.render("You won the game",1,(100, 20, 50))
			win.blit(won,(WIDTH/2 - won.get_width()/2,450,40,40 ))
			run = False				

		win.blit(hangman_img[tries],(100,100))
			
		pygame.display.update()
	if check !=1:	
		winner_font = pygame.font.SysFont("comicsans",50)
		won = winner_font.render("You lost the game",1,(100, 20, 50))
		win.blit(won,(WIDTH/2 - won.get_width()/2,450,40,40 ))	
		letter_x_pos = WIDTH/2 - word_size/2	
		pygame.display.update()	
		pygame.time.delay(3000)
		for i,pos in enumerate(word):
				pygame.draw.line(win,(161,61,45),(letter_x_pos,600),(letter_x_pos+letter_width,600),3)
				if pos in word:
					lettrs = Alpha_font.render(pos,1,(100, 20, 50))
					win.blit(lettrs,(letter_x_pos+10,555,40,40 ))
				else:
					check = 0
				letter_x_pos+=space_width + letter_width
		pygame.display.flip()	
	pygame.time.delay(3000)		

def main_menu():
	def draw_text_middle(text,color,size,win):
		font = pygame.font.SysFont('comicsans',size)
		label = font.render(text,1,color)
		win.blit(label,(WIDTH /2 -(label.get_width()/2),HEIGHT/2 - label.get_height()/2))
	run = True
	while run:
		win.fill((255,255,0))
		draw_text_middle("Press any key to start...",(100, 20, 50),60,win)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				main()
main_menu()	
