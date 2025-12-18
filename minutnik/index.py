import pygame
import sys

pygame.init() 
font = pygame.font.SysFont("Comic Sans MS", 24)
alarm=False
alarm_sound = pygame.mixer.Sound("low-pitch-alarm-buzzer-451576 (1).mp3")
czas = 0
okno = pygame.display.set_mode((600, 800))
okno_text_rect = pygame.Rect(150, 125, 300, 50)

def odswiezanie(czas_text):
    okno.fill((0, 0, 0)) 
    
    
    pygame.draw.rect(okno, (50, 50, 50), okno_text_rect)
    
    czas_font = font.render(f"Czas: {czas_text}", True, (255, 255, 255))
    
    
    okno.blit(czas_font, (160, 130))
    
    pygame.display.update()

def odliczanie(czas_startowy):
    aktualny_czas = czas_startowy
    while aktualny_czas > 0:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        aktualny_czas -= 1
        odswiezanie(str(aktualny_czas))
        pygame.time.delay(1000)
    alarm=True
    while alarm==True:
        alarm_sound.play(-1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.quit()
                        sys.exit()
   
                


while True:
    odswiezanie(str(czas))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                odliczanie(czas)
            if event.key == pygame.K_UP: 
                czas += 1
            if event.key == pygame.K_DOWN:
                czas -= 1
                if czas < 0: czas = 0
            



                
