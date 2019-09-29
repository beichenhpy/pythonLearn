import sys
import pygame

def run_game():
    pygame.init()
    screen=pygame.display.set_mode((1280,720)) #对象是一个suface
    pygame.display.set_caption("Alien invasion")
    bg_color=(230,230,230) #设置背景色

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        screen.fill(bg_color) #每次都重绘屏幕  fill()方法填充屏幕
        pygame.display.flip()  #让最近绘制的屏幕可见
run_game()