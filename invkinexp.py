import pygame
import math
import random

joints = int(input("how many joints: "))
length = int(input("Length of segment (in pixels): "))
mode = input("Mode (Mouse-Tracking (M) / Arrow Keys (A)): ")
pygame.init()

screen = pygame.display.set_mode((1440, 960))

pygame.display.set_caption("Playing Around with Inverse Kinematics")
pygame.display.set_icon(pygame.image.load("icon.png"))

def renderarm(canvas, positions):
    for i in range(1,len(positions)):
        pygame.draw.line(screen, (255, 0, 0), positions[i - 1], positions[i], 5)
        

    for i in range(len(positions)):
        pygame.draw.circle(screen, (0, 0, 255), positions[i], length / 10, 0)

def anglestopositions(angles):
    res = [[720, 480]]
    for angle in angles:
        lastx, lasty = res[-1]
        res.append([lastx + length * math.sin(angle), lasty - length * math.cos(angle)])
    return res

def loss(prop, act):
    return [(prop[0] - act[0]) ** 2, (prop[1] - act[1]) ** 2]

def dloss(prop, act):
    return [(prop[0] - act[0]), (prop[1] - act[1])]

alpha = 0.00001
def update(angles, dangles):
    for i in range(len(angles)):
        angles[i] -= alpha * dangles[i] - random.uniform(-0.001, 0.001) # so it favors bending clockwise i think

def getdangles(dloss, angles):
    dangles = []
    for angle in angles:
        dangles.append(dloss[0] * length * math.cos(angle) + dloss[1] * length * math.sin(angle))
    
    return dangles


angles = [random.uniform(0, 3.14)for i in range(joints)]
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
running = True
curx = 720
cury = 480
x,y = 720, 480
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check for close event
            running = False
    screen.fill((30, 30, 30))
    
    if mode == "M":
        pygame.draw.circle(screen, (255, 255, 255), (x, y), length / 8, 0)
    else:
        pygame.draw.circle(screen, (255, 255, 255), (curx, cury), length / 8, 0)

    positions = anglestopositions(angles)
    renderarm(screen, positions)

    intpositions = [[int(x), int(y)] for x,y in positions]
    text_surface = font.render(f"Joint positions are {intpositions}", True, (255, 255, 255))
    screen.blit(text_surface, (100, 100))

    pygame.display.flip()

    x, y = pygame.mouse.get_pos()

    if mode == "M":
        update(angles, getdangles(dloss(positions[-1], [x, y]), angles))
    else:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cury -= 10
            elif event.key == pygame.K_DOWN:
                cury += 10
            if event.key == pygame.K_LEFT:
                curx -= 10
            elif event.key == pygame.K_RIGHT:
                curx += 10
        update(angles, getdangles(dloss(positions[-1], [curx, cury]), angles))
    
    clock.tick(60)
# Quit Pygame
pygame.quit()
