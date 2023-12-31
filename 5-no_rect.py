import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

#obstacle
# creating the obstacle
obstacle_surf = pygame.image.load('alpha.png').convert_alpha()
obstacle_pos= (100,100)
obstacle_mask = pygame.mask.from_surface(obstacle_surf)

# mask -> surface
new_obstacle_surf = obstacle_mask.to_surface()
new_obstacle_surf.set_colorkey((0,0,0))

# filling in the surface with a color
surf_w, surf_h = new_obstacle_surf.get_size()
for x in range(surf_w):
    for y in range(surf_h):
        if new_obstacle_surf.get_at((x,y))[0] != 0:
            new_obstacle_surf.set_at((x,y), 'orange')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('grey')

    #obstacle
    #complex way to create an outline
    offset = 4
    screen.blit(new_obstacle_surf, (obstacle_pos[0]+offset,obstacle_pos[1])) # right
    screen.blit(new_obstacle_surf, (obstacle_pos[0]-offset,obstacle_pos[1])) # left
    screen.blit(new_obstacle_surf, (obstacle_pos[0],obstacle_pos[1]+offset)) # top
    screen.blit(new_obstacle_surf, (obstacle_pos[0],obstacle_pos[1]-offset)) # bottom
    screen.blit(new_obstacle_surf, (obstacle_pos[0]+offset,obstacle_pos[1]-offset)) # toprignt
    screen.blit(new_obstacle_surf, (obstacle_pos[0]+offset,obstacle_pos[1]+offset)) # bottomrignt
    screen.blit(new_obstacle_surf, (obstacle_pos[0]-offset,obstacle_pos[1]+offset)) # bottomleft
    screen.blit(new_obstacle_surf, (obstacle_pos[0]-offset,obstacle_pos[1]-offset)) # topleft
    screen.blit(obstacle_surf, obstacle_pos)

    # simple way to create an loutline from a mask
    """ obstacle_mask.outline() # 문자 안 쪽 구멍 윤곽선은 못 잡는다.and
    for point in obstacle_mask.outline():
        x = point[0] + 100
        y = point[1] + 100
        pygame.draw.circle(screen, 'red', (x,y),3) """
    
    # 
   
    pygame.display.update()
    clock.tick(60)