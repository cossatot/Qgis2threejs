# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\minorua\QGIS\plugins\Qgis2threejs\ui\keyframedialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KeyframeDialog(object):
    def setupUi(self, KeyframeDialog):
        KeyframeDialog.setObjectName("KeyframeDialog")
        KeyframeDialog.resize(400, 440)
        KeyframeDialog.setMinimumSize(QtCore.QSize(400, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(KeyframeDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButtonPrev = QtWidgets.QToolButton(KeyframeDialog)
        self.toolButtonPrev.setObjectName("toolButtonPrev")
        self.horizontalLayout.addWidget(self.toolButtonPrev)
        self.horizontalSlider = QtWidgets.QSlider(KeyframeDialog)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(0, 30))
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.toolButtonNext = QtWidgets.QToolButton(KeyframeDialog)
        self.toolButtonNext.setObjectName("toolButtonNext")
        self.horizontalLayout.addWidget(self.toolButtonNext)
        self.lineEditCurrentTrans = QtWidgets.QLineEdit(KeyframeDialog)
        self.lineEditCurrentTrans.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lineEditCurrentTrans.setReadOnly(True)
        self.lineEditCurrentTrans.setObjectName("lineEditCurrentTrans")
        self.horizontalLayout.addWidget(self.lineEditCurrentTrans)
        self.labelTransCount = QtWidgets.QLabel(KeyframeDialog)
        self.labelTransCount.setObjectName("labelTransCount")
        self.horizontalLayout.addWidget(self.labelTransCount)
        self.toolButtonPlay = QtWidgets.QToolButton(KeyframeDialog)
        self.toolButtonPlay.setCheckable(True)
        self.toolButtonPlay.setObjectName("toolButtonPlay")
        self.horizontalLayout.addWidget(self.toolButtonPlay)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.labelName = QtWidgets.QLabel(KeyframeDialog)
        self.labelName.setMinimumSize(QtCore.QSize(60, 0))
        self.labelName.setObjectName("labelName")
        self.gridLayout.addWidget(self.labelName, 0, 0, 1, 1)
        self.doubleSpinBoxOpacity = QtWidgets.QDoubleSpinBox(KeyframeDialog)
        self.doubleSpinBoxOpacity.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.doubleSpinBoxOpacity.setDecimals(1)
        self.doubleSpinBoxOpacity.setMaximum(1.0)
        self.doubleSpinBoxOpacity.setSingleStep(0.1)
        self.doubleSpinBoxOpacity.setProperty("value", 1.0)
        self.doubleSpinBoxOpacity.setObjectName("doubleSpinBoxOpacity")
        self.gridLayout.addWidget(self.doubleSpinBoxOpacity, 1, 1, 1, 1)
        self.comboBoxMaterial = QtWidgets.QComboBox(KeyframeDialog)
        self.comboBoxMaterial.setObjectName("comboBoxMaterial")
        self.gridLayout.addWidget(self.comboBoxMaterial, 2, 1, 1, 1)
        self.labelEffect = QtWidgets.QLabel(KeyframeDialog)
        self.labelEffect.setMinimumSize(QtCore.QSize(60, 0))
        self.labelEffect.setObjectName("labelEffect")
        self.gridLayout.addWidget(self.labelEffect, 3, 0, 1, 1)
        self.lineEditName = QtWidgets.QLineEdit(KeyframeDialog)
        self.lineEditName.setObjectName("lineEditName")
        self.gridLayout.addWidget(self.lineEditName, 0, 1, 1, 1)
        self.labelMaterial = QtWidgets.QLabel(KeyframeDialog)
        self.labelMaterial.setMinimumSize(QtCore.QSize(60, 0))
        self.labelMaterial.setObjectName("labelMaterial")
        self.gridLayout.addWidget(self.labelMaterial, 2, 0, 1, 1)
        self.comboBoxEffect = QtWidgets.QComboBox(KeyframeDialog)
        self.comboBoxEffect.setObjectName("comboBoxEffect")
        self.gridLayout.addWidget(self.comboBoxEffect, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 2)
        self.labelOpacity = QtWidgets.QLabel(KeyframeDialog)
        self.labelOpacity.setMinimumSize(QtCore.QSize(60, 0))
        self.labelOpacity.setObjectName("labelOpacity")
        self.gridLayout.addWidget(self.labelOpacity, 1, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(KeyframeDialog)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 5, 0, 1, 2)
        self.labelNarration = QtWidgets.QLabel(KeyframeDialog)
        self.labelNarration.setObjectName("labelNarration")
        self.gridLayout.addWidget(self.labelNarration, 4, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line2 = QtWidgets.QFrame(KeyframeDialog)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.verticalLayout.addWidget(self.line2)
        self.gridLayout2 = QtWidgets.QGridLayout()
        self.gridLayout2.setObjectName("gridLayout2")
        self.labelDuration = QtWidgets.QLabel(KeyframeDialog)
        self.labelDuration.setObjectName("labelDuration")
        self.gridLayout2.addWidget(self.labelDuration, 0, 2, 1, 1)
        self.lineEditDuration = QtWidgets.QLineEdit(KeyframeDialog)
        self.lineEditDuration.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditDuration.setObjectName("lineEditDuration")
        self.gridLayout2.addWidget(self.lineEditDuration, 1, 2, 1, 1)
        self.labelDelay = QtWidgets.QLabel(KeyframeDialog)
        self.labelDelay.setObjectName("labelDelay")
        self.gridLayout2.addWidget(self.labelDelay, 0, 0, 1, 1)
        self.lineEditDelay = QtWidgets.QLineEdit(KeyframeDialog)
        self.lineEditDelay.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditDelay.setObjectName("lineEditDelay")
        self.gridLayout2.addWidget(self.lineEditDelay, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelBegin = QtWidgets.QLabel(KeyframeDialog)
        self.labelBegin.setMinimumSize(QtCore.QSize(50, 0))
        self.labelBegin.setObjectName("labelBegin")
        self.horizontalLayout_2.addWidget(self.labelBegin)
        self.labelTimeBegin = QtWidgets.QLabel(KeyframeDialog)
        self.labelTimeBegin.setMinimumSize(QtCore.QSize(80, 0))
        self.labelTimeBegin.setObjectName("labelTimeBegin")
        self.horizontalLayout_2.addWidget(self.labelTimeBegin)
        self.labelEnd = QtWidgets.QLabel(KeyframeDialog)
        self.labelEnd.setMinimumSize(QtCore.QSize(50, 0))
        self.labelEnd.setObjectName("labelEnd")
        self.horizontalLayout_2.addWidget(self.labelEnd)
        self.labelTimeEnd = QtWidgets.QLabel(KeyframeDialog)
        self.labelTimeEnd.setMinimumSize(QtCore.QSize(80, 0))
        self.labelTimeEnd.setObjectName("labelTimeEnd")
        self.horizontalLayout_2.addWidget(self.labelTimeEnd)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(KeyframeDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout3.setObjectName("horizontalLayout3")
        self.pushButtonPlayAll = QtWidgets.QPushButton(KeyframeDialog)
        self.pushButtonPlayAll.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButtonPlayAll.setCheckable(True)
        self.pushButtonPlayAll.setObjectName("pushButtonPlayAll")
        self.horizontalLayout3.addWidget(self.pushButtonPlayAll)
        self.label = QtWidgets.QLabel(KeyframeDialog)
        self.label.setObjectName("label")
        self.horizontalLayout3.addWidget(self.label)
        self.labelTotal = QtWidgets.QLabel(KeyframeDialog)
        self.labelTotal.setObjectName("labelTotal")
        self.horizontalLayout3.addWidget(self.labelTotal)
        self.buttonBox = QtWidgets.QDialogButtonBox(KeyframeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout3.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout3)

        self.retranslateUi(KeyframeDialog)
        self.buttonBox.accepted.connect(KeyframeDialog.accept)
        self.buttonBox.rejected.connect(KeyframeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(KeyframeDialog)

    def retranslateUi(self, KeyframeDialog):
        _translate = QtCore.QCoreApplication.translate
        KeyframeDialog.setWindowTitle(_translate("KeyframeDialog", "Keyframe"))
        self.toolButtonPrev.setToolTip(_translate("KeyframeDialog", "Previous keyframe"))
        self.toolButtonPrev.setText(_translate("KeyframeDialog", "<"))
        self.toolButtonNext.setToolTip(_translate("KeyframeDialog", "Next keyframe"))
        self.toolButtonNext.setText(_translate("KeyframeDialog", ">"))
        self.lineEditCurrentTrans.setText(_translate("KeyframeDialog", "1"))
        self.labelTransCount.setText(_translate("KeyframeDialog", "/ N"))
        self.toolButtonPlay.setToolTip(_translate("KeyframeDialog", "Perform a transition between current keyframe and next keyframe."))
        self.labelName.setText(_translate("KeyframeDialog", "Name"))
        self.labelEffect.setText(_translate("KeyframeDialog", "Effect"))
        self.labelMaterial.setText(_translate("KeyframeDialog", "Material"))
        self.labelOpacity.setText(_translate("KeyframeDialog", "Opacity"))
        self.plainTextEdit.setPlaceholderText(_translate("KeyframeDialog", "empty - no stop at this keyframe"))
        self.labelNarration.setText(_translate("KeyframeDialog", "Narrative content"))
        self.labelDuration.setText(_translate("KeyframeDialog", "Duration (msec)"))
        self.lineEditDuration.setToolTip(_translate("KeyframeDialog", "length of time to complete a transition"))
        self.labelDelay.setText(_translate("KeyframeDialog", "Delay (msec)"))
        self.lineEditDelay.setToolTip(_translate("KeyframeDialog", "duration to wait before starting a transition"))
        self.labelBegin.setText(_translate("KeyframeDialog", "Begin: "))
        self.labelTimeBegin.setToolTip(_translate("KeyframeDialog", "time to begin this transition"))
        self.labelEnd.setText(_translate("KeyframeDialog", "End:"))
        self.labelTimeEnd.setToolTip(_translate("KeyframeDialog", "time to complete this transition"))
        self.pushButtonPlayAll.setToolTip(_translate("KeyframeDialog", "Perform transitions of this keyframe group from the beginning."))
        self.pushButtonPlayAll.setText(_translate("KeyframeDialog", "Play all"))
        self.label.setText(_translate("KeyframeDialog", "Total time:"))
        self.buttonBox.setToolTip(_translate("KeyframeDialog", "time to complete transitions of this keyframe group"))
