import PySide6.QtCore as pqc

def to_float(data: str) -> float:
    try:
        return float(data)
    except ValueError:
        return 0.0

class DataModel(pqc.QAbstractTableModel):
    def __init__(self, session, table_class, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = session
        self.table_class = table_class
        self.records = []
        for m in session.query(self.table_class).all():
            self.records.append(m.as_data_record)

    def data(self, index, role) -> str:
        if role == pqc.Qt.ItemDataRole.DisplayRole:
            return self.records[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        headers = self.table_class.data_record_header()
        if role == pqc.Qt.ItemDataRole.DisplayRole and orientation == pqc.Qt.Orientation.Horizontal:
            return headers[section]
        else:
            return super().headerData(section, orientation, role)

    def rowCount(self, parent):
        return len(self.records)

    def columnCount(self, parent):
        return self.table_class.data_record_columns()

if __name__=="__main__":
    print(to_float('1.0e4'))
    print(to_float(''))
    print(to_float('1.ww1'))