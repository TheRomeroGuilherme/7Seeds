import pygame

class Protagonista(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)

        self.image = pygame.image.load("data/personagem.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)
    def update(self, *args):
        #logica
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_w]:
            self.rect.y -= 1
            print("Segurando W")

        if Keys[pygame.K_d]:
            self.rect.x += 1
            print("Segurando D")

        if Keys[pygame.K_s]:
            self.rect.y += 1
            print("Segurando S")

        if Keys[pygame.K_a]:
            self.rect.x -= 1
            print("Segurando A")