import pygame

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\최상규\\Desktop\\Python\\python1\\pygame_basic1\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\최상규\\Desktop\\Python\\python1\\pygame_basic1\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
character_x_pos = (screen_width - character_width) / 2 # 캐릭터 가로 위치
character_y_pos = screen_height- character_height # 캐릭터 세로 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True
while(running):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT): # 창 닫히는 이벤트
            running = False

        if(event.type == pygame.KEYDOWN): # 키 누르는 이벤트
            if(event.key == pygame.K_LEFT): # 캐릭터 왼쪽 이동
                to_x -= 5
            elif(event.key == pygame.K_RIGHT): 
                to_x += 5
            elif(event.key == pygame.K_UP):
                to_y -= 5
            elif(event.key == pygame.K_DOWN):
                to_y += 5

        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                to_x = 0
            elif(event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                to_y = 0
        
    character_x_pos += to_x
    character_y_pos += to_y

    # 가로 경계값 처리
    if(character_x_pos < 0):
        character_x_pos = 0
    elif(character_x_pos > screen_width - character_width):
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if(character_y_pos < 0):
        character_y_pos = 0
    elif(character_y_pos > screen_height - character_height):
        character_y_pos = screen_height - character_height
    

    # screen.fill((0, 0, 255))
    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()