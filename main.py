# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path
from extract import generate_list_item

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex


class ListModel(QAbstractListModel):
    TitleRole = Qt.UserRole + 1
    DescriptionRole = Qt.UserRole + 2
    ImageRole = Qt.UserRole + 3

    def __init__(self, parent=None):
        super().__init__(parent)
        self._items = []

    def rowCount(self, parent=QModelIndex()):
        return len(self._items)

    def data(self, index, role):
        if not index.isValid() or index.row() >= len(self._items):
            return None
        item = self._items[index.row()]
        if role == ListModel.TitleRole:
            return item.title
        elif role == ListModel.DescriptionRole:
            return item.description
        elif role == ListModel.ImageRole:
            return item.imageSource
        return None

    def roleNames(self):
        roles = super().roleNames()
        roles[ListModel.TitleRole] = b"title"
        roles[ListModel.DescriptionRole] = b"description"
        roles[ListModel.ImageRole] = b"imageSource"
        return roles

    def addItem(self, item):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._items.append(item)
        self.endInsertRows()


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    model = ListModel()
    model.addItem(
        generate_list_item(
            "https://www.rockpapershotgun.com/nine-sols-review?utm_source=pocket_shared"
        )
    )

    context = engine.rootContext()
    context.setContextProperty("listModel", model)

    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
