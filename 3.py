import tkinter as tk
import random

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 20
DELAY = 200  # milliseconds

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")

        # Create a frame for the canvas and buttons
        self.frame = tk.Frame(master)
        self.frame.pack()

        # Create canvas
        self.canvas = tk.Canvas(self.frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="blue")
        self.canvas.pack()

        # Create reset button
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset_game)
        self.reset_button.pack()

        self.reset_game()

    def reset_game(self):
        self.snake = [(60, 100), (40, 100), (20, 100)]
        self.food = self.create_food()
        self.direction = "Right"
        self.score = 0
        self.paused = False
        self.game_over = False
        self.speed = DELAY
        self.draw()
        self.move()

    def draw(self):
        self.canvas.delete("all")
        # Draw snake
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="green")
        # Draw food
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + CELL_SIZE, self.food[1] + CELL_SIZE, fill="red")
        # Display score
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill="white")
        if self.game_over:
            self.canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, text="Game Over!", fill="white", font=("Arial", 20))

    def create_food(self):
        while True:
            x = random.randint(0, (CANVAS_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (CANVAS_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in self.snake:
                return x, y

    def move(self):
        if not self.paused and not self.game_over:
            head_x, head_y = self.snake[0]
            if self.direction == "Up":
                head_y -= CELL_SIZE
            elif self.direction == "Down":
                head_y += CELL_SIZE
            elif self.direction == "Left":
                head_x -= CELL_SIZE
            elif self.direction == "Right":
                head_x += CELL_SIZE

            new_head = (head_x, head_y)
            self.snake.insert(0, new_head)

            if new_head == self.food:
                self.score += 1
                self.food = self.create_food()
                self.speed = max(self.speed - 2, 10)  # Increase speed
            else:
                self.snake.pop()

            if (head_x < 0 or head_x >= CANVAS_WIDTH or
                head_y < 0 or head_y >= CANVAS_HEIGHT or
                new_head in self.snake[1:]):
                self.game_over = True

            self.draw()
            if not self.game_over:
                self.master.after(self.speed, self.move)

    def on_key_press(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            if (event.keysym == "Up" and self.direction != "Down" or
                event.keysym == "Down" and self.direction != "Up" or
                event.keysym == "Left" and self.direction != "Right" or
                event.keysym == "Right" and self.direction != "Left"):
                self.direction = event.keysym
        elif event.keysym == "p":
            self.paused = not self.paused
            if not self.paused:
                self.move()

def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.bind("<Key>", game.on_key_press)
    root.mainloop()

if __name__ == "__main__":
    main()
