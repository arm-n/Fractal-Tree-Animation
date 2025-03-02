import turtle
import random

def draw_branch(branch_length, t):
    if branch_length > 5:
        # Randomize the angle for a wind effect
        angle = random.randint(15, 25)

        # Branch thickness decreases with length
        t.width(max(1, branch_length // 15))

        # Change color to green at the tips (leaves)
        if branch_length < 20:
            t.color("green")
        else:
            t.color("brown")

        # Draw main branch
        t.forward(branch_length)
        t.right(angle)

        # Recursive call for right branch
        draw_branch(branch_length - random.randint(10, 20), t)

        t.left(angle * 2)

        # Recursive call for left branch
        draw_branch(branch_length - random.randint(10, 20), t)

        t.right(angle)
        t.backward(branch_length)

def draw_stars(num_stars, t):
    t.penup()
    t.color("white")

    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(0, 300)
        t.goto(x, y)
        t.dot(random.randint(2, 4))

    t.pendown()

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Majestic Fractal Tree")

    # Create turtle for the tree
    tree = turtle.Turtle()
    tree.speed(0)
    tree.left(90)
    tree.penup()
    tree.goto(0, -250)
    tree.pendown()

    # Create turtle for the stars
    star_turtle = turtle.Turtle()
    star_turtle.hideturtle()

    # Draw stars in the sky
    draw_stars(100, star_turtle)

    # Draw the fractal tree
    draw_branch(120, tree)

    screen.exitonclick()

if __name__ == "__main__":
    main()
