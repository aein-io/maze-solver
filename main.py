from graphics import Window, Point, Line


def main():
    # create window
    win = Window(800, 600)

    # create lines from points
    line1 = Line(Point(50, 50), Point(400, 400))
    line2 = Line(Point(100, 100), Point(100, 900))

    # draw lines
    win.draw_line(line1, "black")
    win.draw_line(line2, "red")

    win.wait_for_close()


if __name__ == "__main__":
    main()
