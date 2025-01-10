from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Rectangle
from kivy.vector import Vector
import random

class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super(SnakeGame, self).__init__(**kwargs)

        # Game properties
        self.snake = [(200, 200), (180, 200), (160, 200)]  # Initial snake body
        self.snake_direction = Vector(20, 0)  # Initial movement direction (right)
        self.snake_size = 20  # Size of each snake block
        self.food = (0, 0)  # Initial food position
        self.score = 0  # Initialize score
        self.game_over = False

        # Set up the score label
        self.score_label = Label(text=f"Score: {self.score}", font_size=32, color=(1, 1, 1, 1),
                                 size_hint=(None, None), size=(200, 50), pos_hint={"right": 1, "top": 1})
        self.add_widget(self.score_label)

        # Schedule the game loop (frame update every 1/15th of a second)
        Clock.schedule_interval(self.update, 1.0 / 15.0)
        
        # Generate the first food
        self.generate_food()

    def update(self, dt):
        """Game update loop: move the snake, check for collisions."""
        if not self.game_over:
            self.move_snake()
            self.check_collisions()
            self.check_food_collision()
            self.update_score()
        else:
            self.game_over_screen()

    def move_snake(self):
        """Move the snake by adding the new head and removing the tail."""
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.snake_direction.x, head_y + self.snake_direction.y)
        self.snake = [new_head] + self.snake[:-1]

    def check_collisions(self):
        """Check for collisions with walls or the snake itself."""
        head_x, head_y = self.snake[0]

        # Collision with the walls
        if head_x < 0 or head_x >= Window.width or head_y < 0 or head_y >= Window.height:
            self.game_over = True

        # Collision with the snake's own body
        if (head_x, head_y) in self.snake[1:]:
            self.game_over = True

    def check_food_collision(self):
        """Check if the snake eats the food."""
        head_x, head_y = self.snake[0]
        food_x, food_y = self.food
        if head_x == food_x and head_y == food_y:
            self.snake.append(self.snake[-1])  # Add a new block to the snake's body
            self.score += 1  # Increase the score
            self.generate_food()  # Generate a new food item

    def generate_food(self):
        """Generate a new food item at a random location."""
        self.food = (random.randint(0, (Window.width // self.snake_size) - 1) * self.snake_size,
                     random.randint(0, (Window.height // self.snake_size) - 1) * self.snake_size)

    def update_score(self):
        """Update the score label text."""
        self.score_label.text = f"Score: {self.score}"

    def game_over_screen(self):
        """Display the game over screen."""
        game_over_label = Label(text=f"Game Over! Final Score: {self.score}", font_size=40,
                                color=(1, 0, 0, 1), size_hint=(None, None), size=(400, 100),
                                pos_hint={"center": (0.5, 0.5)})
        self.add_widget(game_over_label)

    def on_touch_up(self, touch):
        """Allow the player to control the snake's movement via touch."""
        if self.game_over:
            return  # Don't allow movement when the game is over

        x, y = touch.pos
        if x > self.snake[0][0]:
            self.snake_direction = Vector(self.snake_size, 0)  # Move right
        elif x < self.snake[0][0]:
            self.snake_direction = Vector(-self.snake_size, 0)  # Move left
        elif y > self.snake[0][1]:
            self.snake_direction = Vector(0, self.snake_size)  # Move up
        elif y < self.snake[0][1]:
            self.snake_direction = Vector(0, -self.snake_size)  # Move down

    def on_key_down(self, window, key, scancode, codepoint, modifier):
        """Allow the player to control the snake using the keyboard."""
        if self.game_over:
            return  # Don't allow movement when the game is over

        if key == 273:  # Up arrow key
            self.snake_direction = Vector(0, self.snake_size)
        elif key == 274:  # Down arrow key
            self.snake_direction = Vector(0, -self.snake_size)
        elif key == 275:  # Right arrow key
            self.snake_direction = Vector(self.snake_size, 0)
        elif key == 276:  # Left arrow key
            self.snake_direction = Vector(-self.snake_size, 0)

class SnakeApp(App):
    def build(self):
        game = SnakeGame()
        Window.bind(on_key_down=game.on_key_down)  # Bind the keyboard controls
        return game

if __name__ == "__main__":
    SnakeApp().run()
