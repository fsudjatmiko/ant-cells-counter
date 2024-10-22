import pygame
import pygame.gfxdraw
from edge_detection import apply_edge_detection

class GUI:
    def __init__(self, screen):
        self.screen = screen
        self.BACKGROUND_COLOR = (200, 220, 255)
        self.BUTTON_COLOR = (100, 150, 200)
        self.BUTTON_HOVER_COLOR = (80, 130, 180)
        self.TEXT_COLOR = (0, 0, 0)
        self.TITLE_COLOR = (0, 0, 128)
        self.selected_image = None
        self.edge_method = None
        self.processed_image = None
        self.object_count = None
        self.state = "select_image"
        self.image_rects = []
        self.buttons = {
            "canny": pygame.Rect(50, 450, 100, 50),
            "roberts": pygame.Rect(200, 450, 100, 50),
            "retry": pygame.Rect(500, 450, 100, 50),
            "quit": pygame.Rect(650, 450, 100, 50)
        }

    def handle_click(self, pos):
        if self.state == "select_image":
            for rect, image in self.image_rects:
                if rect.collidepoint(pos):
                    self.selected_image = image
                    self.state = "select_method"
                    break
        elif self.state == "select_method":
            if self.buttons["canny"].collidepoint(pos):
                self.edge_method = "canny"
                self.process_image()
            elif self.buttons["roberts"].collidepoint(pos):
                self.edge_method = "roberts"
                self.process_image()
            elif self.buttons["quit"].collidepoint(pos):
                pygame.event.post(pygame.event.Event(pygame.QUIT))
        elif self.state == "show_result":
            if self.buttons["retry"].collidepoint(pos):
                self.reset()
            elif self.buttons["quit"].collidepoint(pos):
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    def render(self, image_loader):
        self.screen.fill(self.BACKGROUND_COLOR)
        
        if self.state == "select_image":
            self.image_rects = image_loader.display_images(self.screen)
            self.draw_text("Select an image", (300, 20), self.TITLE_COLOR, 40)
        elif self.state == "select_method" and self.selected_image:
            self.screen.blit(self.selected_image, (50, 50))
            self.draw_button("canny", "Canny")
            self.draw_button("roberts", "Roberts")
            self.draw_button("quit", "Quit")
            self.draw_text("Select an edge detection method", (250, 20), self.TITLE_COLOR, 40)
        elif self.state == "show_result" and self.processed_image:
            self.screen.blit(self.processed_image, (50, 50))
            self.draw_text(f"Object count: {self.object_count}", (50, 400), self.TEXT_COLOR)
            self.draw_button("retry", "Retry")
            self.draw_button("quit", "Quit")
            self.draw_text("Do you want to retry or quit?", (250, 20), self.TITLE_COLOR, 40)

    def draw_button(self, key, text):
        button = self.buttons[key]
        mouse_pos = pygame.mouse.get_pos()
        color = self.BUTTON_HOVER_COLOR if button.collidepoint(mouse_pos) else self.BUTTON_COLOR
        
        pygame.draw.rect(self.screen, color, button, border_radius=10)
        pygame.gfxdraw.rectangle(self.screen, button, self.TEXT_COLOR)
        
        self.draw_text(text, (button.centerx, button.centery), self.TEXT_COLOR, 24, center=True)

    def draw_text(self, text, pos, color=None, size=36, center=False):
        if color is None:
            color = self.TEXT_COLOR
        font = pygame.font.Font(None, size)
        rendered_text = font.render(text, True, color)
        if center:
            text_rect = rendered_text.get_rect(center=pos)
        else:
            text_rect = rendered_text.get_rect(topleft=pos)
        self.screen.blit(rendered_text, text_rect)
    def process_image(self):
        self.processed_image, self.object_count = apply_edge_detection(self.selected_image, self.edge_method)
        self.state = "show_result"

    def reset(self):
        self.selected_image = None
        self.edge_method = None
        self.processed_image = None
        self.object_count = None
        self.state = "select_image"
