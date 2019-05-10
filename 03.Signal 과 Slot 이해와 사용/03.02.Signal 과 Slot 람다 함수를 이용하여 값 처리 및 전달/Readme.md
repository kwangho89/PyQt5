# Signal �� Slot ���� �Լ��� �̿��Ͽ� �� ó�� �� ����
���� �Լ��� ����Ͽ� ���� ó���ϴ� ����� ������ ���̴�.
���� �Լ��� ���� ����, ���� Ʃ�丮���� �ص� ������ �Ѵ�.

## lambda ǥ�����̶�?
[Python �ڽ���](https://docs.python.org/ko/3.7/tutorial/controlflow.html#lambda-expressions)�� ������, lambdaǥ������ �����ϰ� �Լ��� ����� ����̶�� �����Ѵ�.
## �׷��� lambda ǥ������ �� ��°�?
���⼭ lambda ǥ������ ����� ������ 
* label�� setText�� ���Ͽ� text�� �޴µ� (���ڵ� ���� �� �ִ�. ����� �Ʒ�����)
* slider�� ��� ���� �������� �����̴�. 

�̸� �����ֱ� ���ؼ� lambda x�� �޾� 
1. str���·� �ٲٰ�, 
2. �̸� label�� ����

�ϱ� ���ߴ� ��
## UI �׸���
1. Template �� Widget ����
2. ���� ǥ���ϱ� ���� label ����
3. ���� ���ϱ� ���� horizentalSlider ����
## Python �����ϱ�
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
        # lambda ǥ������ ���, ���� �ñ׳�/������ ������ �ʰ� �ٷ� �������־���.
        self.ui.horizontalSlider.valueChanged.connect(
                lambda x: self.ui.label.setText(str(x)))
    
if __name__=='__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.ui.show()
    sys.exit(app.exec_())
```
## �� ��� ����� ���°�? Qt Designer���� �ٷ� �����ϱ�
�̴� ���� �������� �ʰڴ�. �տ��� ���´�� ui �󿡼� �ٷ� �̾��ָ� ���� ����� ���´�.
���� �ڵ忡���� lambda ǥ���� �κи� �������ָ� �����ϰ� ������ �� �ִ�.

## PyUIC�� ���� Ȯ���ϱ� - Qt Designer������ slider ���� ��� label�� �����Ͽ�����?
�׷��� Qt Designer�� ��� Python �ڵ带 ®����?
�̴� ��ɾ ���ؼ� Ȯ�� �����ϴ�.
```�ܼ�
python -m PyQt5.uic.pyuic -x <��ȯ�ϰ��� �ϴ� ���� ex tut5.ui> -o <��ȯ�� ���� �̸� ex tut5c.py>
```

```�ܼ�
python -m PyQt5.uic.pyuic -x lambda_link.ui -o lambda_link_c.py
```
�̶� ��ȯ�� python �ڵ忡���� �Ʒ��� ���� ���������� �� �� �ִ�.
```python
        self.horizontalSlider.valueChanged['int'].connect(self.label.setNum)
```
���� Python ���� �ڵ带 �Ʒ��� ���� §�� �ϴ���, ���� �����ϴ�.
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