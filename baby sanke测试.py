from graphics import GraphWin, Rectangle, Point
import time

SQUARE_SIZE = 50 
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
DELAY = 0.001    # seconds to wait between each update

def main():
    win = GraphWin("Baby Snake", CANVAS_WIDTH, CANVAS_HEIGHT)
    start_y = CANVAS_HEIGHT / 2 - SQUARE_SIZE / 2
    end_y = start_y + SQUARE_SIZE

    # 创建矩形
    square = Rectangle(Point(0, start_y), Point(SQUARE_SIZE, end_y))
    square.setFill("blue")
    square.draw(win)

    # 动画循环
    for x in range(int(CANVAS_WIDTH / 2 - SQUARE_SIZE / 2)):
        square.move(1, 0)
        time.sleep(DELAY)

    win.getMouse()  # 点击窗口关闭

if __name__ == "__main__":
    main()