import pygame

win = pygame.display.set_mode((1030, 530))

# initial position
x = 40
y = 40

# width of each bar
width = 40


def run(method):
    height = [200, 50, 130, 90, 250, 61, 110,
              88, 33, 80, 70, 159, 180, 20,
              100, 89, 69, 4, 220, 16, 15]
    run = True
    pygame.init()
    if method == 'bubble':
        pygame.display.set_caption("Bubble sort")
    elif method == 'insertion':
        pygame.display.set_caption("Insertion sort")
    else:
        pygame.display.set_caption("Selection sort")

    # infinite loop
    while run:
        execute = False
        pygame.time.delay(10)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if keys[pygame.K_SPACE]:
            execute = True
        if execute == False:
            win.fill((0, 0, 0))
            show(height)
            pygame.display.update()
        else:
            if method == 'bubble':
                bubble_sort(height)
            elif method == 'insertion':
                insertion_sort(height)
            else:
                selection_sort(height, len(height))
            run = False
            pygame.time.delay(300)

# method to show the list of height


def show(height, j=-1):

    # loop to iterate each item of list
    for i in range(len(height)):
        if j != -1:
            if i == j:
                pygame.draw.rect(win, (255, 0, 0),
                                 (x + 47 * i, y, width, height[i]*2))
            else:
                pygame.draw.rect(win, (255, 255, 255),
                                 (x + 47 * i, y, width, height[i]*2))
        else:
            pygame.draw.rect(win, (255, 255, 255),
                             (x + 47 * i, y, width, height[i]*2))


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                t = array[j]
                array[j] = array[j + 1]
                array[j + 1] = t
                win.fill((0, 0, 0))
                show(array, j+1)
                pygame.time.delay(50)
                pygame.display.update()


def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            win.fill((0, 0, 0))
            show(array, j+1)
            pygame.time.delay(50)
            pygame.display.update()
            j -= 1
        array[j + 1] = key_item
        win.fill((0, 0, 0))
        show(array, j+1)
        pygame.time.delay(50)
        pygame.display.update()


def selection_sort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            # to sort in descending order, change > to < in this line
            if array[i] < array[min_idx]:
                min_idx = i
            win.fill((0, 0, 0))
            show(array, min_idx)
            pygame.time.delay(50)
            pygame.display.update()

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
        win.fill((0, 0, 0))
        show(array, min_idx)
        pygame.time.delay(50)
        pygame.display.update()
