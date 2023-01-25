import pygame
import random
from wordsvault import wordsare


def draw():
    window.fill(Blanc)

    # Titre
    text = title_font.render("PENDU", 1, Noir)
    window.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # Mots
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = word_Font.render(display_word, 1, Noir)
    window.blit(text, (400, 200))
    

    window.blit(images[statut_pendu], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(700)
    window.fill(Blanc)
    text = word_Font.render(message, 1, Noir)
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)


def gameloop():
    global statut_pendu


    # Setup game loop
    fps = 60
    clock = pygame.time.Clock()
    exit_game = True

    while exit_game:
        clock.tick(fps)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = False
                quit()
            if event.type == pygame.KEYDOWN:
                n = event
                keypressed(n)

        draw()
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            display_message("Tu as gagné !")
            break
        if statut_pendu == 6:
            display_message("Tu as perdu ! Le bon mot est " + word)
            break


def keypressed(n):
    if n.key == pygame.K_a:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_b:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_c:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_d:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_e:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_f:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_g:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_h:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_i:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_j:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_k:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_l:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_m:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_n:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_o:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_p:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_q:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_r:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_s:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_t:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_u:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_v:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_w:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_x:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_y:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_z:
        k = n.unicode
        keyvalue(k)


def keyvalue(k):
    global statut_pendu
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            if k == ltr.lower():
                letter[3] = False
                guessed.append(ltr)
                if ltr not in word:
                    statut_pendu += 1


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    
    exit_game = True
    
    # setup display
    WIDTH, HEIGHT = 1200, 500
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Le jeu du Pendu")
    
    while exit_game:

        letters = []
        x = []
        y = []
        A = 65
        for i in range(26):
            letters.append([x, y, chr(A + i), True])

        # Police
        letter_font = pygame.font.SysFont('Arial', 40)
        word_Font = pygame.font.SysFont('Arial', 60)
        title_font = pygame.font.SysFont('Arial', 70)

        # Charger images
        images = []
        for i in range(7):
            myimage = pygame.image.load("images/pendu" + str(i) + ".png")
            images.append(myimage)

        # Couleurs
        Blanc = (225, 225, 225)
        Noir = (0, 0, 0)

        # Variable
        statut_pendu = 0
        word = random.choice(wordsare).upper()
        print(word)
        guessed = []
        
        gameloop()
        