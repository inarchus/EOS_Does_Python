from graphics import *
import math


def distance(p1, p2):
    return (pow(p1.getX() - p2.getX(), 2) + pow(p1.getY() - p2.getY(), 2)) ** 0.5


def safe_get(main_window):
    try:
        return main_window.getMouse()
    except GraphicsError:
        return Point(0, 0)


def dead_soldier_graphical():
    main_window = GraphWin("Dead Soldier Drawing", 750, 750)
    main_window.setBackground(color_rgb(0, 0, 0))

    reset_center = Point(50, 700)
    reset_circle = Circle(reset_center, 50)
    reset_circle.setFill('orange')
    reset_circle.draw(main_window)
    label = Text(reset_center, '\u2324 Reset')
    label.setTextColor('white')
    label.draw(main_window)

    exit_center = Point(700, 700)
    exit_circle = Circle(exit_center, 50)
    exit_circle.setFill('blue')

    label = Text(exit_center, '\u2660 Exit')
    label.setTextColor('white')
    exit_circle.draw(main_window)
    label.draw(main_window)

    soldier_entry = Entry(Point(25, 25), 5)
    soldier_entry.draw(main_window)
    step_entry = Entry(Point(25, 55), 5)
    step_entry.draw(main_window)

    click_pt = safe_get(main_window)
    while distance(click_pt, exit_center) > 50:
        n = -1; step = -1

        while n == -1:
            try:
                n = int(soldier_entry.getText())
                step = int(step_entry.getText())
            except ValueError:
                print('invalid type, go around')
                click_pt = main_window.getMouse()

        centers = [None for _ in range(n)]
        circles = [None for _ in range(n)]
        labels = [None for _ in range(n)]

        x = Point(375 + 300, 375)
        y = Point(375 + 300 * math.cos(2 * math.pi / n), 375 + 300 * math.sin(2 * math.pi / n))
        radius = distance(x, y) // 3
        for i in range(n):
            centers[i] = Point(375 - 300 * math.cos(2 * math.pi * i / n), 375 - 300 * math.sin(2 * math.pi * i / n))
            labels[i] = Text(centers[i], str(i + 1))
            labels[i].setTextColor('white')
            circles[i] = Circle(centers[i], max(10, radius))
            circles[i].setOutline('white'); circles[i].setFill("green")
            circles[i].draw(main_window)
            labels[i].draw(main_window)

        soldiers = [True for _ in range(n)]
        current = 0
        survivor_text = None

        while distance(click_pt, exit_center) > 50:
            if sum(1 for x in soldiers if x) > 1:

                count = 0
                i = 0
                while count < step:
                    if soldiers[(i + current) % n]:
                        count += 1
                    i += 1
                i -= 1
                current = (i + current) % n

                soldiers[current] = False

                circles[current].undraw()
                circles[current].setOutline('white'); circles[current].setFill("red")
                circles[current].draw(main_window)
                labels[current].undraw()
                labels[current].draw(main_window)
            elif not survivor_text:
                survivor_text = Text(Point(375, 375), 'The Survivor is: ' + str(soldiers.index(True) + 1))
                survivor_text.setTextColor('white')
                survivor_text.draw(main_window)

            click_pt = safe_get(main_window)
            if distance(click_pt, reset_center) <= 50:
                for i in range(n):
                    circles[i].undraw()
                    labels[i].undraw()
                    if survivor_text:
                        survivor_text.undraw()
                break

    main_window.close()


try:
    dead_soldier_graphical()
except GraphicsError:
    print('Terminating Window')
