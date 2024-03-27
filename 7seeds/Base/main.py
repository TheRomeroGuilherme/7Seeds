import pygame
from Personagem import Protagonista

# inicializando o Pygame e criando uma janela
pygame.init()
display = pygame.display.set_mode([840,480])
pygame.display.set_caption("7 Seeds")

#Sprite da para colocar em grupos para facilitar a desenhar os personagens, monstros e terrenos etc...


#objects
objectWGroup = pygame.sprite.Group()
protagonista = Protagonista(objectWGroup)


#musicas
pygame.mixer.music.load("data/Loop_Minstrel_Dance.wav")
pygame.mixer.music.play(-1) #(-1) para rodar infinitamente, (0) para rodar uma vez, (1 2 3....) vai repetir a música X tantas vezes

#Efeitos sonoros
Walk = pygame.mixer.Sound("data/SnowWalk.ogg")

# ataque = pygame.mixer.Sound("data") # Fazer um som ou achar um som de ataque

gamaLoop = True
isPressingW = False

if __name__ == "__main__":

    while gamaLoop:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gamaLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    Walk.play()
                if event.key == pygame.K_s:
                    Walk.play()
                if event.key == pygame.K_d:
                    Walk.play()
                if event.key == pygame.K_a:
                    Walk.play()

            #elif event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_SPACE:
            #        ataque.play()
        #Update logic:
        objectWGroup.update()
        #Draw:
        display.fill([15, 26, 128])
        objectWGroup.draw(display)
        pygame.display.update()