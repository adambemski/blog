
import pytest

from PyQt5.QtWidgets import QLabel


@pytest.fixture
def label(qtbot):
    qlabel = QLabel()
    qlabel.setText("Hello World")
    qtbot.addWidget(qlabel)
    return qlabel


def test_label(label):
    assert label.text() == "Hello World"
