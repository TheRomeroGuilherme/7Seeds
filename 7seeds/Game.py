import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Meu Jogo")

# Definir cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Definir a classe do jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self):
        pass

# Criar grupo de sprites e adicionar o jogador
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Loop principal do jogo
running = True
while running:
    # Mantenha o loop funcionando na taxa de quadros correta
    pygame.time.Clock().tick(60)

    # Lidar com eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar
    all_sprites.update()

    # Desenhar
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
sys.exit()
