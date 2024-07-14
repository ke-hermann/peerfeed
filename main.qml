import QtQuick
import QtQuick.Window

import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    width: 400
    height: 600
    title: qsTr("PeerFeed")

    ColumnLayout {
        anchors.fill: parent

        Button {
            text: "Click Me"
            Layout.alignment: Qt.AlignHCenter
            Layout.fillWidth: true
        }

        ListView {
            id: mainview
            Layout.fillWidth: true
            Layout.fillHeight: true
            model: listModel
            delegate: Item {
                width: ListView.view.width
                height: 100

                Rectangle {
                    width: parent.width
                    height: parent.height
                    radius: 5
                    border.color: "black"
                    border.width: 5
                    color: "white"
                }

                Column {
                    spacing: 10
                    Image {
                        source: model.imageSource
                        width: mainview.width
                        height: 150
                        fillMode: Image.PreserveAspectCrop
                    }
                    Text {
                        width: parent.width
                        text: title
                        font.bold: true
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        wrapMode: Text.WordWrap
                    }
                }
            }
        }
    }
}

