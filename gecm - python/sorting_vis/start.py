import pygame
import sort_vis

pygame.init()
width, height = (1030, 530)
screen = pygame.display.set_mode((width, height))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (30, 30, 30)
FONT = pygame.font.Font("freesansbold.ttf", 50)


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def loop():
    clock = pygame.time.Clock()
    bubble = pygame.Rect(10, 10, 500, 250)
    selection = pygame.Rect(520, 10, 500, 250)
    insertion = pygame.Rect(10, 270, 500, 250)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if bubble.collidepoint(event.pos):
                        # Run bubble sort
                        sort_vis.run('bubble')
                    if selection.collidepoint(event.pos):
                        # Run selection sort
                        sort_vis.run('selection')
                    if insertion.collidepoint(event.pos):
                        # Run insertion sort
                        sort_vis.run('insertion')

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, bubble)
        pygame.draw.rect(screen, WHITE, selection)
        pygame.draw.rect(screen, WHITE, insertion)

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("BUBBLE", smallText)
        textRect.center = (bubble.center)
        screen.blit(textSurf, textRect)

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("SELECTION", smallText)
        textRect.center = (selection.center)
        screen.blit(textSurf, textRect)

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("INSERTION", smallText)
        textRect.center = (insertion.center)
        screen.blit(textSurf, textRect)

        pygame.display.update()

        clock.tick(30)


loop()
pygame.quit()
