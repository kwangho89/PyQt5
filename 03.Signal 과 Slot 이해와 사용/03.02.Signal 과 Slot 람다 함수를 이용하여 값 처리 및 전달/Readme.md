# Signal 과 Slot 람다 함수를 이용하여 값 처리 및 전달
람다 함수를 사용하여 값을 처리하는 방법을 설명한 것이다.
람다 함수와 관련 없이, 앞의 튜토리얼대로 해도 동작은 한다.

## lambda 표현식이란?
[Python 자습서](https://docs.python.org/ko/3.7/tutorial/controlflow.html#lambda-expressions)에 따르면, lambda표현식은 간단하게 함수를 만드는 방법이라고 설명한다.
## 그러면 lambda 표현식을 왜 썼는가?
여기서 lambda 표현식을 사용한 이유는 
* label은 setText를 통하여 text를 받는데 (숫자도 받을 수 있다. 방법은 아래서술)
* slider의 출력 값은 정수였기 때문이다. 

이를 맞춰주기 위해서 lambda x를 받아 
1. str형태로 바꾸고, 
2. 이를 label에 연결

하기 위했던 것
## UI 그리기
1. Template → Widget 선택
2. 글을 표시하기 위한 label 삽입
3. 수가 변하기 위한 horizentalSlider 삽입
## Python 연결하기
```python
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

class Form(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = uic.loadUi("lambda.ui")
        # lambda 표현식을 사용, 따로 시그널/슬롯을 만들지 않고 바로 연결해주었다.
        self.ui.horizontalSlider.valueChanged.connect(
                lambda x: self.ui.label.setText(str(x)))
    
if __name__=='__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.ui.show()
    sys.exit(app.exec_())
```
## 이 방법 말고는 없는가? Qt Designer에서 바로 연결하기
이는 따로 설명하지 않겠다. 앞에서 나온대로 ui 상에서 바로 이어주면 글은 제대로 나온다.
연결 코드에서는 lambda 표현식 부분만 삭제해주면 간단하게 연결할 수 있다.

## PyUIC를 통해 확인하기 - Qt Designer에서는 slider 값을 어떻게 label에 연결하였을까?
그러면 Qt Designer는 어떻게 Python 코드를 짰을까?
이는 명령어를 통해서 확인 가능하다.
```콘솔
python -m PyQt5.uic.pyuic -x <변환하고자 하는 파일 ex tut5.ui> -o <변환된 파일 이름 ex tut5c.py>
```

```콘솔
python -m PyQt5.uic.pyuic -x lambda_link.ui -o lambda_link_c.py
```
이때 변환된 python 코드에서는 아래와 같이 연결했음을 알 수 있다.
```python
        self.horizontalSlider.valueChanged['int'].connect(self.label.setNum)
```
따라서 Python 연결 코드를 아래와 같이 짠다 하더라도, 연결 가능하다.
```python
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

class Form(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = uic.loadUi("lambda.ui")
        self.ui.horizontalSlider.valueChanged.connect(self.ui.label.setNum)
    
if __name__=='__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.ui.show()
    sys.exit(app.exec_())
```