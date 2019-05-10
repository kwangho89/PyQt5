# Signal과 slot 연결 기본

큰 순서는 
* UI 구성
* Python으로 연결
와 같다.

## UI 구성
1. 기본 템플릿은 Widget으로 (이것은 다를 수 있다.)
2. Input Widgets → Dial 선택, 배치
3. Input Widgets → Horizental Slider 선택, 배치
4. 편집 → 시그널/슬롯 편집 선택 후 Dial과 Horizental Slider 서로 연결하기
	4.1. 시그널은 valueChanged(int), 슬롯은 setValue(int) 로 연결
## Python으로 연결
앞의 예제에서도 그러하지만 기본적인 구조는 아래와 같다.
```python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget 
from PyQt5.QtWidgets import QApplication
# uic는 앞에서 꾸민 ui를 변환하는데 쓴다.
from PyQt5 import uic
 
class Form(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = uic.loadUi("dial.ui")
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.ui.show()
    sys.exit(app.exec_())
```

## 추가
위의 예제를 푸는 방법은 Qt Designer에서 제공하는 시그널/슬롯 편집 기능을 이용한 것이다.
만약 UI에서 시그널/슬롯 편집 기능을 사용하지 않고, 배치에서 종료하였다고 하였을 시 Python 코드는 아래와 같이 바뀐다.
```python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget 
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
 
class Form(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = uic.loadUi("dial_wo.ui")
        # 아래가 시그널/슬롯을 연결하는 구문이다.
        self.ui.dial.valueChanged.connect(self.ui.horizontalSlider.setValue)
        self.ui.horizontalSlider.valueChanged.connect(self.ui.dial.setValue)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.ui.show()
    sys.exit(app.exec_())
```
