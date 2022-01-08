import pygame
import sys

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')
pygame.font.init()


def drawGrid():
	screen.fill((128, 128, 128))
	for i in range(1, 3):
		pygame.draw.line(screen, (255, 255, 255), (i * 200, 0), (i * 200, HEIGHT), 6)
		pygame.draw.line(screen, (255, 255, 255), (0, i * 200), (HEIGHT, i * 200), 6)


def drawText(text, color, x, y, size):
	font = pygame.font.SysFont('Comic Sans MS', size)
	box = font.render(text, True, color)
	rect = box.get_rect(topleft = (x, y))
	screen.blit(box, rect)


def checkWin(board):
	# column or row check
	for i in range(3):
		if abs(sum(board[i])) == 3:
			return True
		checkCol = 0
		for j in range(3):
			checkCol += board[j][i]
		if abs(checkCol) == 3:
			return True

	# cross
	if board[0][0] + board[1][1] + board[2][2] == 3 or board[0][0] + board[1][1] + board[2][2] == -3:
		return True
	if board[2][0] + board[1][1] + board[0][2] == 3 or board[2][0] + board[1][1] + board[0][2] == -3:
		return True

	# not win
	return False


def Play1vs1():
	# draw null grid
	drawGrid()

	# vars
	running = True
	clicked = False
	postition = -1
	win = 0
	xPostition = 0
	yPostition = 0
	board = [[0 for x in range(3)] for y in range(3)]
	countTurns = 0 

	# game loop
	while running and countTurns < 9:
		mouse = pygame.mouse.get_pos()

		# event
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				main()
			if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
				if board[mouse[1] // 200][mouse[0] // 200] == 0:
					clicked = True
					postition *= -1
					xPostition = mouse[0] // 200
					yPostition = mouse[1] // 200
					countTurns += 1
			if event.type == pygame.MOUSEBUTTONUP and clicked == True:
				clicked = False

		# check win condition
		if clicked and not checkWin(board):
			if postition == 1:
				drawText('X', (255, 0, 0), xPostition * 200 + 30, yPostition * 200 - 30, 170)
				board[yPostition][xPostition] = 1
			if postition == -1:
				drawText('O', (0, 255, 255), xPostition * 200 + 20, yPostition * 200 - 30, 170)
				board[yPostition][xPostition] = -1

		if checkWin(board):
			if board[yPostition][xPostition] == 1:
				pygame.draw.rect(screen, (255, 255, 0), (150, 200, 300, 150))
				drawText('X win', (0, 0, 0), 180, 190, 100)
				running = False
			if board[yPostition][xPostition] == -1:
				pygame.draw.rect(screen, (255, 255, 0), (150, 200, 300, 150))
				drawText('O win', (0, 0, 0), 170, 190, 100)
				running = False
			win = 1
		# update
		pygame.display.update()
	
	if win == 0: 
		pygame.draw.rect(screen, (255, 255, 0), (150, 200, 300, 150))
		drawText('Draw', (0, 0, 0), 190, 200, 100)
		pygame.display.update()

	pygame.time.delay(1000)
	Play1vs1()

 
def main():
    running = True
    playButton = pygame.Rect(150, 180, 300, 100)
    clicked = False
    screen.fill((128, 128, 128))

    while running:
        mouse = pygame.mouse.get_pos()

        if clicked and playButton.collidepoint(mouse):
                Play1vs1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False

		# title
        drawText('Tic - Tac - Toe', (0, 255, 0), 5, 10, 85)

		# button 1
        pygame.draw.circle(screen, (255, 255, 0), (150, 230), 50)
        pygame.draw.circle(screen, (255, 255, 0), (450, 230), 50)
        pygame.draw.rect(screen, (255, 255, 0), playButton)
        drawText('Play', (0, 0, 0), 190, 170, 80)

        pygame.display.update()
    
if __name__ == '__main__':
    main()
