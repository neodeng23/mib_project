import sys

from PyQt5.QtCore import QAbstractItemModel, QModelIndex, Qt, QAbstractListModel, QMimeData, \
    QDataStream, QByteArray, QJsonDocument, QVariant, QJsonValue, QJsonParseError
from PyQt5.QtWidgets import QApplication, QFileDialog, QTreeView
from func.string_handler import get_desktop


class QJsonTreeItem(object):
    def __init__(self, parent=None):
        self.mParent = parent
        self.mChilds = []
        self.mType = ""
        self.mOid = ""
        self.mValue = {}
        self.mAttribute = []

    def appendChild(self, item):
        self.mChilds.append(item)

    def child(self, row: int):
        return self.mChilds[row]

    def parent(self):
        return self.mParent

    def childCount(self):
        return len(self.mChilds)

    def row(self):
        if self.mParent is not None:
            return self.mParent.mChilds.index(self)
        return 0

    def setKey(self, key: str):
        self.mKey = key

    def setOid(self, oid: str):
        self.mOid = oid

    def setValue(self, value: str):
        self.mValue = value

    def setType(self, type: QJsonValue.Type):
        self.mType = type

    def key(self):
        return self.mKey

    def oid(self):
        return self.mOid

    def value(self):
        return self.mValue

    def attribute(self):
        return self.mAttribute

    def load(self, value, parent=None):
        rootItem = QJsonTreeItem(parent)
        rootItem.setKey("root")
        jsonType = None

        try:
            value = value.toVariant()
            jsonType = value.type()
        except AttributeError:
            pass

        try:
            value = value.toObject()
            jsonType = value.type()

        except AttributeError:
            pass

        if isinstance(value, dict):
            # process the key/value pairs
            for key in value:
                v = value[key]
                child = self.load(v, rootItem)
                child.setKey(key)
                try:
                    child.setType(v.type())
                except AttributeError:
                    child.setType(v.__class__)
                rootItem.appendChild(child)

        elif isinstance(value, list):
            # process the values in the list
            for i, v in enumerate(value):
                child = self.load(v, rootItem)
                child.setKey(str(i))
                child.setType(v.__class__)
                rootItem.appendChild(child)

        else:
            # value is processed
            rootItem.setOid(value)
            try:
                rootItem.setType(value.type())
            except AttributeError:
                if jsonType is not None:
                    rootItem.setType(jsonType)
                else:
                    rootItem.setType(value.__class__)

        return rootItem


class QJsonModel(QAbstractItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mRootItem = QJsonTreeItem()
        self.mHeaders = ['Name', 'OID', 'Value', 'attribute']

    def load(self, fileName):
        if fileName is None or fileName is False:
            return False

        with open(fileName, "rb", ) as file:
            if file is None:
                return False
            self.loadJson(file.read())

    def loadJson(self, json):
        error = QJsonParseError()
        self.mDocument = QJsonDocument.fromJson(json, error)
        if self.mDocument is not None:
            self.beginResetModel()
            if self.mDocument.isArray():
                self.mRootItem.load(list(self.mDocument.array()))
            else:
                self.mRootItem = self.mRootItem.load(self.mDocument.object())
            self.endResetModel()

            return True

        print("QJsonModel: error loading Json")
        return False

    def data(self, index: QModelIndex, role: int = ...):
        if not index.isValid():
            return QVariant()

        item = index.internalPointer()
        col = index.column()

        if role == Qt.DisplayRole:
            if col == 0:
                return str(item.key())
            elif col == 1:
                return str(item.oid())
            elif col == 2:
                return str(item.value())
            elif col == 3:
                return str(item.attribute())

        return QVariant()

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if role != Qt.DisplayRole:
            return QVariant()

        if orientation == Qt.Horizontal:
            return self.mHeaders[section]

        return QVariant()

    def index(self, row: int, column: int, parent: QModelIndex = ...):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parentItem = self.mRootItem
        else:
            parentItem = parent.internalPointer()
        try:
            childItem = parentItem.child(row)
            return self.createIndex(row, column, childItem)
        except IndexError:
            return QModelIndex()

    def parent(self, index: QModelIndex):
        if not index.isValid():
            return QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self.mRootItem:
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent: QModelIndex = ...):
        if parent.column() > 0:
            return 0
        if not parent.isValid():
            parentItem = self.mRootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def columnCount(self, parent: QModelIndex = ...):
        return 4

    def getValue(self, name, data_dict):
        return data_dict[name]


if __name__ == '__main__':
    app = QApplication(sys.argv)

    view = QTreeView()
    view.setDragEnabled(True)
    model = QJsonModel()
    view.setModel(model)

    jsonpath = get_desktop() + '\\OID.json'
    model.load(jsonpath)
    view.show()
    view.resize(1000, 800)

    sys.exit(app.exec_())
