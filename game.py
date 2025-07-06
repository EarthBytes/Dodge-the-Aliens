import pygame, sys
from entities import draw_player, enemy_list, drop_enemies, update_enemy_positions, draw_enemies, collision_check, player_img
from high_scores import save_score
from settings import screen, clock, font, big_font, WIDTH, HEIGHT, player_size, enemy_size, collision_sound

background_img = pygame.image.load("assets/starry_background.png").convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

def get_player_name():
    input_active = True
    name_input = ""
    while input_active:
        screen.blit(background_img, (0, 0))

        title = big_font.render("Enter Your Name", True, (255, 255, 255))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 200))
        name_surface = font.render(name_input + "|", True, (255, 255, 255))
        screen.blit(name_surface, (WIDTH // 2 - 100, 300))
        prompt = font.render("Press Enter to Start", True, (255, 255, 255))
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

def draw_explosion(surface, position, frame):
    max_radius = 100
    growth_rate = 6
    radius = frame * growth_rate
    alpha = max(255 - frame * 10, 0)

    explosion_surf = pygame.Surface((max_radius*2, max_radius*2), pygame.SRCALPHA)

    pygame.draw.circle(explosion_surf, (255, 120, 0, alpha), (max_radius, max_radius), radius)
    pygame.draw.circle(explosion_surf, (255, 240, 100, alpha), (max_radius, max_radius), radius // 2)

    surf_x = position[0] + player_size // 2 - max_radius
    surf_y = position[1] + player_size // 2 - max_radius
    surface.blit(explosion_surf, (surf_x, surf_y))

def start_game(speed, spawn_chance, player_name):
    enemy_list.clear()
    player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
    score = 0
    running = True
    player_speed = 10  

    while running:
        screen.blit(background_img, (0, 0)) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        # Horizontal movement
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
            player_pos[0] += player_speed
        # Vertical movement
        if keys[pygame.K_UP] and player_pos[1] > 0:
            player_pos[1] -= player_speed
        if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
            player_pos[1] += player_speed

        drop_enemies(enemy_list, spawn_chance)
        update_enemy_positions(enemy_list, speed)

        if collision_check(player_pos, enemy_list):
            collision_sound.play()

            for frame in range(20):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                screen.blit(background_img, (0, 0))
                draw_enemies(enemy_list)

                fade_alpha = max(255 - frame * 20, 0)
                faded_player = pygame.transform.scale(player_img, (player_size, player_size)).convert_alpha()
                faded_player.set_alpha(fade_alpha)
                screen.blit(faded_player, player_pos)

                draw_explosion(screen, player_pos, frame)

                pygame.display.update()
                clock.tick(30)

            running = False

        draw_player(player_pos)
        draw_enemies(enemy_list)

        score_text = font.render("Score: " + str(score), True, (255, 255, 255))        
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(30)
        score += 1

    save_score(player_name, score)
