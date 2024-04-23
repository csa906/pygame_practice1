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

# 이벤트 루프
running = True
while(running):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

    # screen.fill((0, 0, 255))
    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()