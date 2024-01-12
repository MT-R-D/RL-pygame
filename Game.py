import pygame
import pygame.pixelcopy


from Ball import Ball


class Game:
    def __init__(self,
                 screen_width, screen_height,
                 player_width, player_height,
                 player_hover_level, player_speed,
                 ball_count, ball_radius, ball_speed, ball_cooldown_range,
                 FPS=None) -> None:

        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.PLAYER_WIDTH = player_width
        self.PLAYER_HEIGHT = player_height
        self.BALL_COUNT = ball_count
        self.FPS = FPS

        self.score = 0
        self.player_x = screen_width // 2 - player_width // 2
        self.player_y = screen_height - player_height - player_hover_level
        self.player_speed = player_speed

        self.clock = pygame.time.Clock()

        pygame.init()
        pygame.font.init()

        # Font for rendering the score
        self.font = pygame.font.Font(None, 36)  # Adjust font size as needed

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.running = True
        self.dt = 0

        self.balls = []
        for _ in range(ball_count):
            ball = Ball(0, 0, ball_radius, "red",
                        ball_speed, ball_cooldown_range)
            ball.spawn(screen_width)
            self.balls.append(ball)

    def start(self):
        while self.running:
            self.tick()

    def render(self):
        self.screen.fill((0, 0, 0))
        for ball in self.balls:
            ball.render(self.screen)
            # Render the score as text
            score_text = self.font.render(
                "Score: " + str(self.score), True, (255, 255, 255))  # White text color
            score_rect = score_text.get_rect(
                topleft=(10, 10))  # Position in top left corner
            self.screen.blit(score_text, score_rect)

            player_rect = pygame.Rect(
                self.player_x, self.player_y, self.PLAYER_WIDTH, self.PLAYER_HEIGHT)
            pygame.draw.rect(self.screen, (255, 255, 0), player_rect)

    def logic(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.player_x = max(0, self.player_x)
        self.player_x = min(self.SCREEN_WIDTH -
                            self.PLAYER_WIDTH, self.player_x)

        for ball in self.balls:
            ball.move(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

            if (ball.y >= self.player_y) and (ball.x >= self.player_x and ball.x <= self.player_x + self.PLAYER_WIDTH):
                ball.spawn(self.SCREEN_WIDTH)
                self.score += 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_x -= self.player_speed
        elif keys[pygame.K_RIGHT]:
            self.player_x += self.player_speed

    def read_logic(self):
        pass

    def tick(self):
        self.logic()
        self.render()

        if self.FPS is not None:
            self.clock.tick(self.FPS)

        pygame.display.flip()

    def quit(self):
        pygame.quit()


__all__ = ['Game']
