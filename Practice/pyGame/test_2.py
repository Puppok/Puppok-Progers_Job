import pygame
import random
import math
import json

# === КОНСТАНТЫ ===
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)

# Состояния игры
STATE_MENU = "menu"
STATE_DIFFICULTY = "difficulty"
STATE_PLAYING = "playing"
STATE_PAUSED = "paused"
STATE_GAMEOVER = "gameover"


# === КЛАССЫ UI ===

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = (100, 150, 200)
        self.hover_color = (150, 200, 255)
        self.is_hovered = False

    def update(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered:
                return self.action()
        return None

    def draw(self, screen):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        pygame.draw.rect(screen, WHITE, self.rect, 3, border_radius=10)

        font = pygame.font.Font(None, 42)
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)


# === ИГРОВЫЕ КЛАССЫ ===

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 60))
        self.image.fill(BLUE)
        # Рисуем корабль
        pygame.draw.polygon(self.image, WHITE, [(25, 0), (0, 60), (50, 60)])

        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20

        self.speed = 350
        self.shoot_cooldown = 0
        self.shoot_delay = 0.2

        self.hp = 100
        self.max_hp = 100

    def update(self, dt, keys):
        # Движение
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed * dt

        # Ограничения
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        # Cooldown стрельбы
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt

    def shoot(self):
        if self.shoot_cooldown <= 0:
            self.shoot_cooldown = self.shoot_delay
            return Bullet(self.rect.centerx, self.rect.top, -500)
        return None

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed_y = speed_y

    def update(self, dt):
        self.rect.y += self.speed_y * dt

        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_type, difficulty):
        super().__init__()

        self.type = enemy_type

        if enemy_type == "basic":
            self.image = pygame.Surface((40, 40))
            self.image.fill(RED)
            self.hp = 20 * difficulty
            self.speed = 100 * difficulty
            self.score = 10
        elif enemy_type == "fast":
            self.image = pygame.Surface((30, 30))
            self.image.fill((255, 150, 0))
            self.hp = 10 * difficulty
            self.speed = 200 * difficulty
            self.score = 15
        else:  # "tank"
            self.image = pygame.Surface((60, 50))
            self.image.fill((150, 0, 0))
            self.hp = 50 * difficulty
            self.speed = 50 * difficulty
            self.score = 30

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.shoot_timer = random.uniform(1, 3)

    def update(self, dt):
        self.rect.y += self.speed * dt

        # Удаляем если вышли за экран
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

        # Стрельба
        self.shoot_timer -= dt

    def shoot(self):
        if self.shoot_timer <= 0:
            self.shoot_timer = random.uniform(2, 4)
            return Bullet(self.rect.centerx, self.rect.bottom, 300)
        return None

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            return True
        return False


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []

        # Создаём кадры взрыва
        for size in [10, 20, 30, 25, 15]:
            img = pygame.Surface((size * 2, size * 2))
            img.fill(BLACK)
            img.set_colorkey(BLACK)
            pygame.draw.circle(img, YELLOW, (size, size), size)
            pygame.draw.circle(img, (255, 150, 0), (size, size), size, 3)
            self.images.append(img)

        self.current_frame = 0
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=(x, y))

        self.frame_duration = 0.05
        self.frame_timer = 0

    def update(self, dt):
        self.frame_timer += dt

        if self.frame_timer >= self.frame_duration:
            self.frame_timer = 0
            self.current_frame += 1

            if self.current_frame >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.current_frame]


class Powerup(pygame.sprite.Sprite):
    def __init__(self, x, y, powerup_type):
        super().__init__()
        self.type = powerup_type

        self.image = pygame.Surface((30, 30))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        if powerup_type == "health":
            pygame.draw.circle(self.image, GREEN, (15, 15), 15)
            pygame.draw.rect(self.image, WHITE, (12, 7, 6, 16))
            pygame.draw.rect(self.image, WHITE, (7, 12, 16, 6))
        elif powerup_type == "shield":
            pygame.draw.circle(self.image, BLUE, (15, 15), 15)
            pygame.draw.circle(self.image, WHITE, (15, 15), 15, 3)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 100

    def update(self, dt):
        self.rect.y += self.speed * dt

        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# === ИГРОВОЕ СОСТОЯНИЕ ===

class Game:
    def __init__(self):
        self.state = STATE_MENU
        self.difficulty = 1
        self.score = 0
        self.wave = 1
        self.high_scores = self.load_high_scores()

        # Группы спрайтов
        self.all_sprites = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()

        self.player = None

        # Таймеры
        self.enemy_spawn_timer = 0
        self.enemy_spawn_interval = 2.0
        self.wave_timer = 0

        # Кнопки меню
        self.menu_buttons = [
            Button(350, 250, 300, 70, "Играть", self.start_difficulty_select),
            Button(350, 340, 300, 70, "Рекорды", self.show_highscores),
            Button(350, 430, 300, 70, "Выход", self.quit_game)
        ]

        # Кнопки сложности
        self.difficulty_buttons = [
            Button(300, 250, 150, 60, "Лёгкая", lambda: self.start_game(1)),
            Button(500, 250, 150, 60, "Средняя", lambda: self.start_game(2)),
            Button(700, 250, 150, 60, "Сложная", lambda: self.start_game(3))
        ]

        # Кнопка паузы
        self.pause_button = Button(420, 350, 160, 60, "Продолжить", self.unpause)

        # Кнопки game over
        self.gameover_buttons = [
            Button(350, 400, 300, 60, "Заново", self.restart),
            Button(350, 480, 300, 60, "Меню", self.go_to_menu)
        ]

    def load_high_scores(self):
        try:
            with open("highscores.json", "r") as f:
                return json.load(f)
        except:
            return [0, 0, 0, 0, 0]

    def save_high_scores(self):
        with open("highscores.json", "w") as f:
            json.dump(self.high_scores, f)

    def start_difficulty_select(self):
        self.state = STATE_DIFFICULTY

    def start_game(self, difficulty):
        self.difficulty = difficulty
        self.state = STATE_PLAYING
        self.score = 0
        self.wave = 1

        # Очистка
        self.all_sprites.empty()
        self.player_group.empty()
        self.enemies.empty()
        self.player_bullets.empty()
        self.enemy_bullets.empty()
        self.explosions.empty()
        self.powerups.empty()

        # Создание игрока
        self.player = Player()
        self.all_sprites.add(self.player)
        self.player_group.add(self.player)

    def pause(self):
        if self.state == STATE_PLAYING:
            self.state = STATE_PAUSED

    def unpause(self):
        self.state = STATE_PLAYING

    def game_over(self):
        self.state = STATE_GAMEOVER

        # Обновление рекордов
        if self.score > min(self.high_scores):
            self.high_scores.append(self.score)
            self.high_scores.sort(reverse=True)
            self.high_scores = self.high_scores[:5]
            self.save_high_scores()

    def restart(self):
        self.start_game(self.difficulty)

    def go_to_menu(self):
        self.state = STATE_MENU

    def show_highscores(self):
        pass  # Можно добавить отдельный экран

    def quit_game(self):
        return "QUIT"

    def update(self, dt, keys, events, mouse_pos):
        if self.state == STATE_MENU:
            for button in self.menu_buttons:
                button.update(mouse_pos)
                for event in events:
                    result = button.handle_event(event)
                    if result == "QUIT":
                        return False

        elif self.state == STATE_DIFFICULTY:
            for button in self.difficulty_buttons:
                button.update(mouse_pos)
                for event in events:
                    button.handle_event(event)

        elif self.state == STATE_PLAYING:
            # Пауза
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.pause()

            # Игрок
            self.player.update(dt, keys)

            # Стрельба игрока
            if keys[pygame.K_SPACE]:
                bullet = self.player.shoot()
                if bullet:
                    self.all_sprites.add(bullet)
                    self.player_bullets.add(bullet)

            # Враги
            self.enemies.update(dt)

            # Стрельба врагов
            for enemy in self.enemies:
                bullet = enemy.shoot()
                if bullet:
                    self.all_sprites.add(bullet)
                    self.enemy_bullets.add(bullet)

            # Пули
            self.player_bullets.update(dt)
            self.enemy_bullets.update(dt)

            # Взрывы
            self.explosions.update(dt)

            # Powerups
            self.powerups.update(dt)

            # Столкновения пуль игрока с врагами
            for bullet in self.player_bullets:
                hits = pygame.sprite.spritecollide(bullet, self.enemies, False)
                if hits:
                    bullet.kill()
                    for enemy in hits:
                        if enemy.take_damage(10):
                            explosion = Explosion(enemy.rect.centerx, enemy.rect.centery)
                            self.all_sprites.add(explosion)
                            self.explosions.add(explosion)

                            self.score += enemy.score
                            enemy.kill()

                            # Шанс выпадения powerup
                            if random.random() < 0.1:
                                powerup_type = random.choice(["health", "shield"])
                                powerup = Powerup(enemy.rect.centerx, enemy.rect.centery, powerup_type)
                                self.all_sprites.add(powerup)
                                self.powerups.add(powerup)

            # Столкновения пуль врагов с игроком
            hits = pygame.sprite.spritecollide(self.player, self.enemy_bullets, True)
            for hit in hits:
                self.player.take_damage(10)

            # Столкновения врагов с игроком
            hits = pygame.sprite.spritecollide(self.player, self.enemies, True)
            for hit in hits:
                self.player.take_damage(20)
                explosion = Explosion(hit.rect.centerx, hit.rect.centery)
                self.all_sprites.add(explosion)
                self.explosions.add(explosion)

            # Сбор powerups
            hits = pygame.sprite.spritecollide(self.player, self.powerups, True)
            for powerup in hits:
                if powerup.type == "health":
                    self.player.hp = min(self.player.hp + 30, self.player.max_hp)

            # Проверка смерти игрока
            if self.player.hp <= 0:
                self.game_over()

            # Появление врагов
            self.enemy_spawn_timer -= dt
            if self.enemy_spawn_timer <= 0:
                self.enemy_spawn_timer = self.enemy_spawn_interval

                enemy_type = random.choices(
                    ["basic", "fast", "tank"],
                    weights=[60, 30, 10]
                )[0]

                x = random.randint(50, SCREEN_WIDTH - 50)
                enemy = Enemy(x, -50, enemy_type, self.difficulty)
                self.all_sprites.add(enemy)
                self.enemies.add(enemy)

            # Увеличение сложности
            self.wave_timer += dt
            if self.wave_timer >= 30:
                self.wave_timer = 0
                self.wave += 1
                self.enemy_spawn_interval *= 0.9
                print(f"Волна {self.wave}!")

        elif self.state == STATE_PAUSED:
            self.pause_button.update(mouse_pos)
            for event in events:
                self.pause_button.handle_event(event)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.unpause()

        elif self.state == STATE_GAMEOVER:
            for button in self.gameover_buttons:
                button.update(mouse_pos)
                for event in events:
                    button.handle_event(event)

        return True

    def draw(self, screen):
        screen.fill(BLACK)

        if self.state == STATE_MENU:
            # Заголовок
            font = pygame.font.Font(None, 96)
            title = font.render("SPACE DEFENDER", True, YELLOW)
            screen.blit(title, (200, 100))

            # Кнопки
            for button in self.menu_buttons:
                button.draw(screen)

        elif self.state == STATE_DIFFICULTY:
            font = pygame.font.Font(None, 72)
            title = font.render("Выберите сложность", True, WHITE)
            screen.blit(title, (250, 150))

            for button in self.difficulty_buttons:
                button.draw(screen)

        elif self.state in [STATE_PLAYING, STATE_PAUSED]:
            # Игровое поле
            self.all_sprites.draw(screen)

            # HUD
            font = pygame.font.Font(None, 36)

            # Счёт
            score_text = font.render(f"Счёт: {self.score}", True, WHITE)
            screen.blit(score_text, (10, 10))

            # Волна
            wave_text = font.render(f"Волна: {self.wave}", True, WHITE)
            screen.blit(wave_text, (10, 50))

            # HP bar
            bar_width = 200
            bar_height = 20
            hp_ratio = self.player.hp / self.player.max_hp

            pygame.draw.rect(screen, (100, 0, 0), (SCREEN_WIDTH - bar_width - 10, 10, bar_width, bar_height))
            pygame.draw.rect(screen, GREEN, (SCREEN_WIDTH - bar_width - 10, 10, int(bar_width * hp_ratio), bar_height))
            pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - bar_width - 10, 10, bar_width, bar_height), 2)

            hp_text = font.render(f"HP: {self.player.hp}/{self.player.max_hp}", True, WHITE)
            screen.blit(hp_text, (SCREEN_WIDTH - bar_width - 10, 35))

            # Пауза
            if self.state == STATE_PAUSED:
                # Затемнение
                overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                overlay.fill(BLACK)
                overlay.set_alpha(150)
                screen.blit(overlay, (0, 0))

                pause_text = pygame.font.Font(None, 96).render("ПАУЗА", True, WHITE)
                screen.blit(pause_text, (370, 250))

                self.pause_button.draw(screen)

        elif self.state == STATE_GAMEOVER:
            font_big = pygame.font.Font(None, 96)
            font = pygame.font.Font(None, 48)

            title = font_big.render("GAME OVER", True, RED)
            screen.blit(title, (300, 150))

            score_text = font.render(f"Ваш счёт: {self.score}", True, WHITE)
            screen.blit(score_text, (380, 280))

            # Рекорды
            records_text = font.render("Рекорды:", True, YELLOW)
            screen.blit(records_text, (420, 550))

            small_font = pygame.font.Font(None, 32)
            for i, score in enumerate(self.high_scores):
                text = small_font.render(f"{i + 1}. {score}", True, WHITE)
                screen.blit(text, (450, 590 + i * 30))

            # Кнопки
            for button in self.gameover_buttons:
                button.draw(screen)


# === ГЛАВНЫЙ ЦИКЛ ===

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Defender")
    clock = pygame.time.Clock()

    game = Game()

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0

        mouse_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

        # Обновление
        if not game.update(dt, keys, events, mouse_pos):
            running = False

        # Отрисовка
        game.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()