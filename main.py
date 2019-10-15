# your contributions here
import pygame.cdrom

def openTray():
    pygame.cdrom.init()
    cd = pygame.cdrom.CD(0)
    cd.init()
    cd.eject()
