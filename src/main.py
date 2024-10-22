import pygame
from gui import GUI
from image_loader import ImageLoader

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Edge Detection GUI")
    image_loader = ImageLoader("images")
    gui = GUI(screen)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gui.handle_click(event.pos)

        screen.fill(gui.BACKGROUND_COLOR) 
        gui.render(image_loader)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
