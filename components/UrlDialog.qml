// ModalDialog.qml
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Dialog {
    // size
    width: 400  
    height: 120

    id: dialog
    title: "Save to Feed"
    standardButtons: Dialog.Ok | Dialog.Cancel

    TextField {
    width: parent.width
    placeholderText: qsTr("Enter name")
    }

    onAccepted: console.log("Ok clicked")
    onRejected: console.log("Cancel clicked")
}