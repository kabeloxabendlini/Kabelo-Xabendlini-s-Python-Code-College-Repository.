import sys
from time import sleep
import random
import math
import pygame
from bullet import Bullet
from alien import Alien

touch_left_rect = None
touch_right_rect = None
touch_shoot_rect = None


def create_stars(ai_settings):
    stars = []
    for _ in range(ai_settings.star_count):
        x = random.randint(0, ai_settings.screen_width)
        y = random.randint(0, ai_settings.screen_height)
        size = random.randint(1, 3)
        brightness = random.randint(150, 255)
        stars.append((x, y, size, brightness))
    return stars


def draw_stars(screen, stars):
    for (x, y, size, brightness) in stars:
        pygame.draw.circle(screen, (brightness, brightness, brightness), (x, y), size)


def draw_flash_effects(screen, stats):
    still_flashing = []
    for (rect, timer) in stats.flash_aliens:
        if timer > 0:
            alpha = int(255 * (timer / 8))
            flash_surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
            flash_surf.fill((255, 255, 100, alpha))
            screen.blit(flash_surf, rect)
            still_flashing.append((rect, timer - 1))
    stats.flash_aliens = still_flashing


def draw_level_up_banner(screen, ai_settings, stats):
    if stats.show_level_up:
        overlay = pygame.Surface(
            (ai_settings.screen_width, ai_settings.screen_height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 60))
        screen.blit(overlay, (0, 0))

        font_big = pygame.font.SysFont("consolas", 80, bold=True)
        font_small = pygame.font.SysFont("consolas", 32)

        title = font_big.render(f"LEVEL {stats.level}", True, (0, 255, 255))
        screen.blit(title, title.get_rect(
            center=(ai_settings.screen_width // 2,
                    ai_settings.screen_height // 2 - 30)))

        sub = font_small.render("Aliens are faster!", True, (200, 200, 100))
        screen.blit(sub, sub.get_rect(
            center=(ai_settings.screen_width // 2,
                    ai_settings.screen_height // 2 + 50)))

        stats.level_up_timer -= 1
        if stats.level_up_timer <= 0:
            stats.show_level_up = False


def draw_lives_lost(screen, ai_settings, stats):
    if stats.show_lives_lost:
        alpha = min(200, stats.lives_lost_timer * 10)
        overlay = pygame.Surface(
            (ai_settings.screen_width, ai_settings.screen_height), pygame.SRCALPHA)
        overlay.fill((150, 0, 0, alpha))
        screen.blit(overlay, (0, 0))

        font = pygame.font.SysFont("consolas", 60, bold=True)
        msg = font.render("SHIP DESTROYED!", True, (255, 80, 80))
        screen.blit(msg, msg.get_rect(
            center=(ai_settings.screen_width // 2,
                    ai_settings.screen_height // 2)))

        lives_font = pygame.font.SysFont("consolas", 30)
        lives_msg = lives_font.render(
            f"{stats.ships_left} ship(s) remaining", True, (255, 180, 180))
        screen.blit(lives_msg, lives_msg.get_rect(
            center=(ai_settings.screen_width // 2,
                    ai_settings.screen_height // 2 + 60)))

        stats.lives_lost_timer -= 1
        if stats.lives_lost_timer <= 0:
            stats.show_lives_lost = False


def draw_game_over(screen, ai_settings, stats):
    overlay = pygame.Surface(
        (ai_settings.screen_width, ai_settings.screen_height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 200))
    screen.blit(overlay, (0, 0))

    font_title = pygame.font.SysFont("consolas", 80, bold=True)
    font_score = pygame.font.SysFont("consolas", 40, bold=True)
    font_hint  = pygame.font.SysFont("consolas", 24)

    cx = ai_settings.screen_width // 2
    cy = ai_settings.screen_height // 2

    title = font_title.render("GAME OVER", True, (255, 60, 60))
    screen.blit(title, title.get_rect(center=(cx, cy - 120)))

    pygame.draw.line(screen, (255, 60, 60),
                     (cx - 200, cy - 70), (cx + 200, cy - 70), 2)

    score_text = font_score.render(f"Score: {stats.score:,}", True, (0, 255, 255))
    screen.blit(score_text, score_text.get_rect(center=(cx, cy - 30)))

    high_text = font_score.render(
        f"Best:  {stats.high_score:,}", True, (100, 180, 255))
    screen.blit(high_text, high_text.get_rect(center=(cx, cy + 30)))

    level_text = font_score.render(
        f"Level: {stats.level}", True, (200, 200, 100))
    screen.blit(level_text, level_text.get_rect(center=(cx, cy + 90)))

    pygame.draw.line(screen, (0, 100, 160),
                     (cx - 200, cy + 130), (cx + 200, cy + 130), 1)

    hint = font_hint.render("Click PLAY to try again", True, (150, 150, 200))
    screen.blit(hint, hint.get_rect(center=(cx, cy + 160)))


def draw_quit_confirm(screen, ai_settings):
    """Draw quit confirmation as a non-blocking overlay."""
    overlay = pygame.Surface(
        (ai_settings.screen_width, ai_settings.screen_height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))

    font_big = pygame.font.SysFont("consolas", 52, bold=True)
    font_small = pygame.font.SysFont("consolas", 30)

    msg = font_big.render("Quit the game?", True, (0, 255, 255))
    screen.blit(msg, msg.get_rect(
        center=(ai_settings.screen_width // 2,
                ai_settings.screen_height // 2 - 40)))

    hint = font_small.render("Y = Return to title   |   N = Cancel",
                              True, (200, 200, 200))
    screen.blit(hint, hint.get_rect(
        center=(ai_settings.screen_width // 2,
                ai_settings.screen_height // 2 + 30)))


def draw_controls(screen, ai_settings):
    global touch_left_rect, touch_right_rect, touch_shoot_rect

    panel_height = 60
    panel_y = ai_settings.screen_height - panel_height

    panel_surface = pygame.Surface((ai_settings.screen_width, panel_height), pygame.SRCALPHA)
    for i in range(panel_height):
        alpha = int(200 - (i / panel_height) * 80)
        pygame.draw.line(panel_surface, (0, 0, 50, alpha),
                         (0, i), (ai_settings.screen_width, i))
    screen.blit(panel_surface, (0, panel_y))

    pygame.draw.line(screen, (0, 255, 255),
                     (0, panel_y), (ai_settings.screen_width, panel_y), 1)
    pygame.draw.line(screen, (0, 80, 120),
                     (0, panel_y + 1), (ai_settings.screen_width, panel_y + 1), 1)

    pulse = (pygame.time.get_ticks() / 600) % (2 * math.pi)
    glow_alpha = int(40 + 30 * math.sin(pulse))

    btn_w = 70
    btn_h = 44
    btn_y = panel_y + (panel_height - btn_h) // 2
    margin = 12
    gap = 6

    touch_left_rect = pygame.Rect(margin, btn_y, btn_w, btn_h)
    touch_right_rect = pygame.Rect(margin + btn_w + gap, btn_y, btn_w, btn_h)
    touch_shoot_rect = pygame.Rect(
        ai_settings.screen_width - btn_w - margin, btn_y, btn_w, btn_h)

    def draw_btn(rect, border_color, glow_color, symbol, label):
        glow_rect = rect.inflate(8, 8)
        glow_surf = pygame.Surface((glow_rect.width, glow_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(glow_surf, (*glow_color, glow_alpha),
                         glow_surf.get_rect(), border_radius=12)
        screen.blit(glow_surf, glow_rect)

        bg_surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        pygame.draw.rect(bg_surf, (0, 0, 30, 100),
                         bg_surf.get_rect(), border_radius=10)
        screen.blit(bg_surf, rect)

        pygame.draw.rect(screen, (*border_color, 180), rect, 2, border_radius=10)

        sym_font = pygame.font.SysFont("consolas", 22, bold=True)
        sym = sym_font.render(symbol, True, border_color)
        screen.blit(sym, sym.get_rect(center=(rect.centerx, rect.centery - 5)))

        lbl_font = pygame.font.SysFont("consolas", 11, bold=True)
        lbl = lbl_font.render(label, True, border_color)
        screen.blit(lbl, lbl.get_rect(center=(rect.centerx, rect.bottom - 8)))

    draw_btn(touch_left_rect,  (0, 200, 255), (0, 150, 255), "<", "LEFT")
    draw_btn(touch_right_rect, (0, 200, 255), (0, 150, 255), ">", "RIGHT")
    draw_btn(touch_shoot_rect, (255, 80, 80),  (255, 50, 50),  "^", "FIRE")

    font = pygame.font.SysFont("consolas", 13, bold=True)
    hints = ["[< >] Move", "[SPC] Shoot", "[P] Pause", "[Q] Quit"]
    total = len(hints)
    center_start = margin + btn_w + gap + btn_w + 20
    center_end = ai_settings.screen_width - btn_w - margin - 20
    center_width = center_end - center_start

    for i, hint in enumerate(hints):
        x = int(center_start + (i + 0.5) * center_width / total)
        y = panel_y + panel_height // 2
        hint_surf = font.render(hint, True, (0, 180, 220))
        screen.blit(hint_surf, hint_surf.get_rect(center=(x, y)))


def check_keydown_events(event, ai_settings, screen, stats, ship, bullets):
    # ✅ Handle quit confirm screen first
    if stats.show_quit_confirm:
        if event.key == pygame.K_y:
            stats.show_quit_confirm = False
            stats.game_active = False
            stats.show_game_over = False
            stats.game_paused = False
            pygame.mouse.set_visible(True)
        elif event.key == pygame.K_n:
            stats.show_quit_confirm = False
            stats.game_paused = False
        return

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if not stats.game_paused:
            fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_p:
        if stats.game_active:
            stats.game_paused = not stats.game_paused
    elif event.key == pygame.K_q:
        if stats.game_active:
            stats.show_quit_confirm = True
            stats.game_paused = True


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_touch_events(event, ai_settings, screen, stats, ship, bullets):
    global touch_left_rect, touch_right_rect, touch_shoot_rect
    if touch_left_rect is None:
        return
    pos = event.pos
    if event.type in (pygame.MOUSEBUTTONDOWN, pygame.FINGERDOWN):
        if touch_left_rect.collidepoint(pos):
            ship.moving_left = True
        if touch_right_rect.collidepoint(pos):
            ship.moving_right = True
        if touch_shoot_rect.collidepoint(pos):
            if not stats.game_paused:
                fire_bullet(ai_settings, screen, ship, bullets)
    elif event.type in (pygame.MOUSEBUTTONUP, pygame.FINGERUP):
        if touch_left_rect.collidepoint(pos):
            ship.moving_left = False
        if touch_right_rect.collidepoint(pos):
            ship.moving_right = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stats.show_quit_confirm = True
            stats.game_paused = True
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
            if stats.game_active:
                check_touch_events(event, ai_settings, screen, stats, ship, bullets)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(ai_settings, screen, stats, sb, play_button,
                                  ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type in (pygame.FINGERDOWN, pygame.FINGERUP):
            if stats.game_active:
                event.pos = (int(event.x * ai_settings.screen_width),
                             int(event.y * ai_settings.screen_height))
                check_touch_events(event, ai_settings, screen, stats, ship, bullets)


def check_play_button(ai_settings, screen, stats, sb, play_button,
                      ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        stats.game_paused = False
        stats.show_game_over = False
        stats.show_level_up = False
        stats.show_lives_lost = False
        stats.show_quit_confirm = False
        stats.flash_aliens = []
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, stars):
    screen.fill(ai_settings.bg_color)
    draw_stars(screen, stars)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    draw_flash_effects(screen, stats)
    sb.show_score()
    draw_controls(screen, ai_settings)

    if not stats.game_active:
        overlay = pygame.Surface(
            (ai_settings.screen_width, ai_settings.screen_height), pygame.SRCALPHA)
        overlay.fill((0, 0, 20, 180))
        screen.blit(overlay, (0, 0))

        title_font = pygame.font.SysFont("consolas", 72, bold=True)
        title = title_font.render("ALIEN INVASION", True, (0, 255, 255))
        screen.blit(title, title.get_rect(
            center=(ai_settings.screen_width // 2,
                    ai_settings.screen_height // 2 - 80)))

        hint_font = pygame.font.SysFont("consolas", 20)
        hint = hint_font.render("Press F11 for fullscreen", True, (80, 120, 160))
        screen.blit(hint, hint.get_rect(
            center=(ai_settings.screen_width // 2,
                    ai_settings.screen_height // 2 + 60)))

        if stats.show_game_over:
            draw_game_over(screen, ai_settings, stats)

        play_button.draw_button()

    if stats.show_level_up:
        draw_level_up_banner(screen, ai_settings, stats)

    if stats.show_lives_lost:
        draw_lives_lost(screen, ai_settings, stats)

    if stats.game_paused and stats.game_active and not stats.show_quit_confirm:
        overlay = pygame.Surface(
            (ai_settings.screen_width, ai_settings.screen_height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))
        pause_font = pygame.font.SysFont("consolas", 72, bold=True)
        pause_text = pause_font.render("PAUSED", True, (0, 255, 255))
        screen.blit(pause_text, pause_text.get_rect(
            center=(ai_settings.screen_width // 2,
                    ai_settings.screen_height // 2 - 30)))
        hint_font = pygame.font.SysFont("consolas", 28)
        hint_text = hint_font.render("Press P to resume", True, (200, 200, 200))
        screen.blit(hint_text, hint_text.get_rect(
            center=(ai_settings.screen_width // 2,
                    ai_settings.screen_height // 2 + 40)))

    # ✅ Draw quit confirm overlay on top of everything
    if stats.show_quit_confirm:
        draw_quit_confirm(screen, ai_settings)

    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens_hit in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens_hit)
            sb.prep_score()
            for alien in aliens_hit:
                stats.flash_aliens.append((alien.rect.copy(), 8))
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        stats.show_level_up = True
        stats.level_up_timer = 120
        create_fleet(ai_settings, screen, ship, aliens)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()
        stats.show_lives_lost = True
        stats.lives_lost_timer = 80
    else:
        stats.game_active = False
        stats.show_game_over = True
        pygame.mouse.set_visible(True)

    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
    sleep(0.5)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    return int(available_space_x / (2 * alien_width))


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - 85
                         - (3 * alien_height) - ship_height)
    return int(available_space_y / (2 * alien_height))


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = 85 + alien.rect.height * row_number + 5 * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)