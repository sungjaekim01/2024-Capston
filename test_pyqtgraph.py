
import pyqtgraph as pg

from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        pg.setConfigOptions(background='w')  # 배경 흰색으로.. ; global configuration options

        y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        y2 = [0, 1, 2, 4, 12, 14, 16, 17, 14, 22]
        x = range(0, 10)

        pw = pg.PlotWidget()
        pw.showGrid(x=True, y=True)

        # pw.addLegend()  # legend 글씨와 마크가 붙어서 출력됨 -- 시인성 나쁨
        pw.addLegend(size=(100, 10))  # LegendItem() 없으면, 생성후 반환 ; 매개변수는 LegendItem() 에서 사용 ==> size=(width,height)

        pw.setLabel("left", text="Value", units="v")   # PlotItem() 메소드
        pw.setLabel('bottom', text="Time", units='s')

        pw.setXRange(0, 10)   # 내부적으로 ViewBox() 메소드 사용함. -- setXRange(min, max, padding=None, update=True)
        pw.setYRange(0, 25)

        pw.plot(x, y, pen='b', symbol='x', symbolPen='g', symbolBrush=0.2, name='green')
        pw.plot(x, y2, pen='r', symbol='o', symbolPen='b', symbolBrush=0.2, name='blue')

        layout = QHBoxLayout()
        layout.addWidget(pw)
        self.setLayout(layout)

        self.setGeometry(300, 100, 550, 650)  # x, y, width, height
        self.setWindowTitle("pyqtgraph 예제 2")
        self.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())

