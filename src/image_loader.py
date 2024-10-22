import pygame
import os

class ImageLoader:
    def __init__(self, images_path):
        self.images_path = images_path
        self.images = []
        self.load_images()

    def load_images(self):
        for img_name in os.listdir(self.images_path):
            img_path = os.path.join(self.images_path, img_name)
            image = pygame.image.load(img_path)
            image = pygame.transform.scale(image, (200, 150))
            self.images.append((image, img_name))

    def display_images(self, screen):
        y = 50
        image_rects = []
        for image, name in self.images:
            rect = screen.blit(image, (50, y))
            image_rects.append((rect, image))
            y += image.get_height() + 10
        return image_rects
