import QtQuick
import QtQuick.Window

import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls.Material 2.12

import "./components"


ApplicationWindow {
    visible: true
    width: 400
    height: 600
    title: qsTr("PeerFeed")

    Material.theme: Material.Dark
    Material.accent: Material.Purple

    UrlDialog {
        id: modalDialog
    }


    ColumnLayout {

        anchors.leftMargin: 10
        anchors.rightMargin: 10
        anchors.fill: parent

        Button {
            text: "Click Me"
            Layout.alignment: Qt.AlignHCenter
            Layout.fillWidth: true
                onClicked: {
                    modalDialog.open()
            }
        }

        ListView {
            id: mainview
            Layout.fillWidth: true
            Layout.fillHeight: true
            model: listModel



            spacing: 10
            delegate: Item {

                id: listitem
                width: ListView.view.width
                height: 170

                Rectangle {
                    x: -2 
                    y: -2
                    width: parent.width + 4
                    height: parent.height + 4
                    radius: 5
                    border.color: "black"
                    border.width: 2
                    color: "#222222"
                }

                Column {
                    Image {
                        id: itemThumbnail
                        source: model.imageSource
                        width: mainview.width
                        height: 100
                        fillMode: Image.PreserveAspectCrop
                    }
                    Text {
                        width: parent.width
                        height: listitem.height - itemThumbnail.height
                        text: title
                        color: "white"
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        wrapMode: Text.WordWrap
                    }
                }
            }
        }
    }
}

