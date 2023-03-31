import pygame

class Mario:
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
    
    def move_left(self):
        self.x -= self.speed
    
    def move_right(self):
        self.x += self.speed
    
    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Game:
    def __init__(self, screen_width, screen_height, title):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.title = title
        self.fps=60
        self.reloj=pygame.time.Clock()
        
        # Configuración de la pantalla
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(self.title)
        
        # Cargar imágenes
        self.mario_image = pygame.image.load("mario.png")
        
        # Configuración del personaje de Mario
        self.mario = Mario(50, self.screen_height - 100, 5, self.mario_image)
    
    def run(self):
        # Bucle principal del juego
        running = True
        while running:
            # Eventos del juego
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Movimiento de Mario
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.mario.move_left()
            if keys[pygame.K_RIGHT]:
                self.mario.move_right()
            
            # Dibujar la pantalla
            self.screen.fill((255, 255, 255))
            self.mario.render(self.screen)
            # Establecer la tasa de actualización del juego
            self.reloj.tick(self.fps)
            
            # Mostrar los FPS en la ventana del juego
            pygame.display.set_caption(f"{self.title} - FPS: {int(self.reloj.get_fps())}")
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game(800, 600, "Super Mario")
    game.run()
