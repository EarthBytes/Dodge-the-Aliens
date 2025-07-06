import pygame, sys
from settings import *
from button import Button
from high_scores import get_high_scores
from game import start_game

background_img = pygame.image.load("assets/starry_background.png").convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

def get_player_name():
    input_active = True
    name_input = ""
    while input_active:
        screen.blit(background_img, (0, 0)) 

        title = big_font.render("Enter Your Name", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 200))
        name_surface = font.render(name_input + "|", True, WHITE)
        screen.blit(name_surface, (WIDTH // 2 - 100, 300))
        prompt = font.render("Press Enter to Start", True, WHITE)
        screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, 400))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name_input.strip():
                    return name_input.strip()
                elif event.key == pygame.K_BACKSPACE:
                    name_input = name_input[:-1]
                elif len(name_input) < 12 and event.unicode.isprintable():
                    name_input += event.unicode

        pygame.display.update()
        clock.tick(30)

def main_menu():
    global music_on
    if music_on and not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(-1)
    elif not music_on:
        pygame.mixer.music.pause()

    def go_to_difficulty():
        select_difficulty()

    def go_to_high_scores():
        show_high_scores()

    def go_to_settings():
        settings_menu()

    def quit_game():
        pygame.quit()
        sys.exit()

    buttons = [
        Button("Difficulty", WIDTH // 2 - 100, 280, 200, 60, go_to_difficulty),
        Button("High Scores", WIDTH // 2 - 100, 360, 200, 60, go_to_high_scores),
        Button("Settings", WIDTH // 2 - 100, 440, 200, 60, go_to_settings),
        Button("Quit Game", WIDTH // 2 - 100, 520, 200, 60, quit_game),
    ]

    while True:
        screen.blit(background_img, (0, 0))  
        title = big_font.render("Dodge the Aliens", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 120))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button.check_click(pygame.mouse.get_pos())

        for button in buttons:
            button.draw(screen)

        pygame.display.update()
        clock.tick(60)

def select_difficulty():
    difficulties = [("Easy", 3, 0.01), ("Medium", 5, 0.02), ("Hard", 7, 0.04), ("Insane", 10, 0.07)]

    def back():
        main_menu()

    buttons = []
    y_start = 280
    for i, (name, speed, spawn) in enumerate(difficulties):
        def make_start(s=speed, sp=spawn):
            def start():
                player_name = get_player_name()
                start_game(s, sp, player_name)
            return start

        buttons.append(Button(name, WIDTH // 2 - 100, y_start + i * 80, 200, 60, make_start()))

    back_button = Button("Back", WIDTH // 2 - 100, y_start + len(difficulties) * 80 + 20, 200, 60, back)
    buttons.append(back_button)

    while True:
        screen.blit(background_img, (0, 0))  
        title = big_font.render("Select Difficulty", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 150))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button.check_click(pygame.mouse.get_pos())

        for button in buttons:
            button.draw(screen)

        pygame.display.update()
        clock.tick(60)

def show_high_scores():
    scores = get_high_scores()

    def back():
        main_menu()

    back_button = Button("Back", WIDTH // 2 - 100, HEIGHT - 100, 200, 60, back)

    while True:
        screen.blit(background_img, (0, 0))  
        title = big_font.render("High Scores", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

        y_offset = 180
        for i, (name, score, _) in enumerate(scores[:10]):
            score_text = font.render(f"{i+1}. {name}: {score}", True, WHITE)
            screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, y_offset + i * 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_click(pygame.mouse.get_pos()):
                    return

        back_button.draw(screen)
        pygame.display.update()
        clock.tick(60)

def settings_menu():
    global music_on

    def toggle_music():
        global music_on
        music_on = not music_on
        if music_on:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

    def back():
        main_menu()

    music_button = Button(f"Music: {'On' if music_on else 'Off'}", WIDTH // 2 - 100, 280, 200, 60, toggle_music)
    back_button = Button("Back", WIDTH // 2 - 100, 360, 200, 60, back)

    while True:
        screen.blit(background_img, (0, 0)) 
        title = big_font.render("Settings", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 150))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                music_button.check_click(pygame.mouse.get_pos())
                if back_button.check_click(pygame.mouse.get_pos()):
                    return

        music_button.text = f"Music: {'On' if music_on else 'Off'}"
        music_button.draw(screen)
        back_button.draw(screen)

        pygame.display.update()
        clock.tick(60)
