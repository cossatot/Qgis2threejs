# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\minorua\.qgis2\python\developing_plugins\Qgis2threejs\ui\demproperties.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DEMPropertiesWidget(object):
    def setupUi(self, DEMPropertiesWidget):
        DEMPropertiesWidget.setObjectName("DEMPropertiesWidget")
        DEMPropertiesWidget.resize(386, 656)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DEMPropertiesWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_DEMLayer = QtWidgets.QFormLayout()
        self.formLayout_DEMLayer.setObjectName("formLayout_DEMLayer")
        self.label_DEMLayer = QtWidgets.QLabel(DEMPropertiesWidget)
        self.label_DEMLayer.setObjectName("label_DEMLayer")
        self.formLayout_DEMLayer.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_DEMLayer)
        self.comboBox_DEMLayer = QtWidgets.QComboBox(DEMPropertiesWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_DEMLayer.sizePolicy().hasHeightForWidth())
        self.comboBox_DEMLayer.setSizePolicy(sizePolicy)
        self.comboBox_DEMLayer.setMaximumSize(QtCore.QSize(350, 16777215))
        self.comboBox_DEMLayer.setObjectName("comboBox_DEMLayer")
        self.formLayout_DEMLayer.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_DEMLayer)
        self.verticalLayout_2.addLayout(self.formLayout_DEMLayer)
        self.groupBox_Resampling = QtWidgets.QGroupBox(DEMPropertiesWidget)
        self.groupBox_Resampling.setObjectName("groupBox_Resampling")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_Resampling)
        self.verticalLayout_6.setContentsMargins(-1, 6, -1, 6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.radioButton_Simple = QtWidgets.QRadioButton(self.groupBox_Resampling)
        self.radioButton_Simple.setChecked(True)
        self.radioButton_Simple.setObjectName("radioButton_Simple")
        self.verticalLayout_6.addWidget(self.radioButton_Simple)
        self.verticalLayout_Simple = QtWidgets.QVBoxLayout()
        self.verticalLayout_Simple.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_Simple.setObjectName("verticalLayout_Simple")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSlider_DEMSize = QtWidgets.QSlider(self.groupBox_Resampling)
        self.horizontalSlider_DEMSize.setEnabled(True)
        self.horizontalSlider_DEMSize.setMinimum(1)
        self.horizontalSlider_DEMSize.setMaximum(6)
        self.horizontalSlider_DEMSize.setSingleStep(1)
        self.horizontalSlider_DEMSize.setPageStep(1)
        self.horizontalSlider_DEMSize.setProperty("value", 2)
        self.horizontalSlider_DEMSize.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_DEMSize.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_DEMSize.setTickInterval(1)
        self.horizontalSlider_DEMSize.setObjectName("horizontalSlider_DEMSize")
        self.horizontalLayout.addWidget(self.horizontalSlider_DEMSize)
        self.label_Resolution = QtWidgets.QLabel(self.groupBox_Resampling)
        self.label_Resolution.setMinimumSize(QtCore.QSize(80, 0))
        self.label_Resolution.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Resolution.setObjectName("label_Resolution")
        self.horizontalLayout.addWidget(self.label_Resolution)
        self.verticalLayout_Simple.addLayout(self.horizontalLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_Resampling)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_Resampling)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_HRes = QtWidgets.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_HRes.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_HRes.sizePolicy().hasHeightForWidth())
        self.lineEdit_HRes.setSizePolicy(sizePolicy)
        self.lineEdit_HRes.setReadOnly(True)
        self.lineEdit_HRes.setObjectName("lineEdit_HRes")
        self.horizontalLayout_4.addWidget(self.lineEdit_HRes)
        self.label_9 = QtWidgets.QLabel(self.groupBox_Resampling)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.lineEdit_VRes = QtWidgets.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_VRes.setEnabled(True)
        self.lineEdit_VRes.setReadOnly(True)
        self.lineEdit_VRes.setObjectName("lineEdit_VRes")
        self.horizontalLayout_4.addWidget(self.lineEdit_VRes)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.verticalLayout_Simple.addLayout(self.formLayout_2)
        self.formLayout_Surroundings = QtWidgets.QFormLayout()
        self.formLayout_Surroundings.setObjectName("formLayout_Surroundings")
        self.checkBox_Surroundings = QtWidgets.QCheckBox(self.groupBox_Resampling)
        self.checkBox_Surroundings.setObjectName("checkBox_Surroundings")
        self.formLayout_Surroundings.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBox_Surroundings)
        self.gridLayout_Surroundings = QtWidgets.QGridLayout()
        self.gridLayout_Surroundings.setObjectName("gridLayout_Surroundings")
        self.label_2 = QtWidgets.QLabel(self.groupBox_Resampling)
        self.label_2.setEnabled(False)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_Surroundings.addWidget(self.label_2, 0, 0, 1, 1)
        self.spinBox_Size = QtWidgets.QSpinBox(self.groupBox_Resampling)
        self.spinBox_Size.setEnabled(False)
        self.spinBox_Size.setMinimumSize(QtCore.QSize(70, 0))
        self.spinBox_Size.setMinimum(3)
        self.spinBox_Size.setMaximum(9)
        self.spinBox_Size.setSingleStep(2)
        self.spinBox_Size.setProperty("value", 5)
        self.spinBox_Size.setObjectName("spinBox_Size")
        self.gridLayout_Surroundings.addWidget(self.spinBox_Size, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_Resampling)
        self.label_3.setEnabled(False)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_Surroundings.addWidget(self.label_3, 0, 2, 1, 1)
        self.spinBox_Roughening = QtWidgets.QSpinBox(self.groupBox_Resampling)
        self.spinBox_Roughening.setEnabled(False)
        self.spinBox_Roughening.setMinimumSize(QtCore.QSize(70, 0))
        self.spinBox_Roughening.setMinimum(2)
        self.spinBox_Roughening.setMaximum(64)
        self.spinBox_Roughening.setSingleStep(4)
        self.spinBox_Roughening.setProperty("value", 4)
        self.spinBox_Roughening.setObjectName("spinBox_Roughening")
        self.gridLayout_Surroundings.addWidget(self.spinBox_Roughening, 0, 3, 1, 1)
        self.formLayout_Surroundings.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.gridLayout_Surroundings)
        self.verticalLayout_Simple.addLayout(self.formLayout_Surroundings)
        self.verticalLayout_6.addLayout(self.verticalLayout_Simple)
        self.radioButton_Advanced = QtWidgets.QRadioButton(self.groupBox_Resampling)
        self.radioButton_Advanced.setObjectName("radioButton_Advanced")
        self.verticalLayout_6.addWidget(self.radioButton_Advanced)
        self.verticalLayout_Advanced = QtWidgets.QVBoxLayout()
        self.verticalLayout_Advanced.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_Advanced.setObjectName("verticalLayout_Advanced")
        self.horizontalLayout_Advanced1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Advanced1.setObjectName("horizontalLayout_Advanced1")
        self.label_11 = QtWidgets.QLabel(self.groupBox_Resampling)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_Advanced1.addWidget(self.label_11)
        self.spinBox_Height = QtWidgets.QSpinBox(self.groupBox_Resampling)
        self.spinBox_Height.setEnabled(True)
        self.spinBox_Height.setMinimum(1)
        self.spinBox_Height.setMaximum(8)
        self.spinBox_Height.setProperty("value", 4)
        self.spinBox_Height.setObjectName("spinBox_Height")
        self.horizontalLayout_Advanced1.addWidget(self.spinBox_Height)
        self.label_10 = QtWidgets.QLabel(self.groupBox_Resampling)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_Advanced1.addWidget(self.label_10)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_Resampling)
        self.lineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_Advanced1.addWidget(self.lineEdit)
        self.verticalLayout_Advanced.addLayout(self.horizontalLayout_Advanced1)
        self.horizontalLayout_Advanced2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Advanced2.setObjectName("horizontalLayout_Advanced2")
        self.label_Focus = QtWidgets.QLabel(self.groupBox_Resampling)
        self.label_Focus.setObjectName("label_Focus")
        self.horizontalLayout_Advanced2.addWidget(self.label_Focus)
        self.toolButton_PointTool = QtWidgets.QToolButton(self.groupBox_Resampling)
        self.toolButton_PointTool.setObjectName("toolButton_PointTool")
        self.horizontalLayout_Advanced2.addWidget(self.toolButton_PointTool)
        self.verticalLayout_Advanced.addLayout(self.horizontalLayout_Advanced2)
        self.horizontalLayout_Advanced3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Advanced3.setObjectName("horizontalLayout_Advanced3")
        self.label_centerX = QtWidgets.QLabel(self.groupBox_Resampling)
        self.label_centerX.setMinimumSize(QtCore.QSize(30, 0))
        self.label_centerX.setObjectName("label_centerX")
        self.horizontalLayout_Advanced3.addWidget(self.label_centerX)
        self.lineEdit_centerX = QtWidgets.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_centerX.setEnabled(True)
        self.lineEdit_centerX.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_centerX.setReadOnly(True)
        self.lineEdit_centerX.setObjectName("lineEdit_centerX")
        self.horizontalLayout_Advanced3.addWidget(self.lineEdit_centerX)
        self.label_centerY = QtWidgets.QLabel(self.groupBox_Resampling)
        self.label_centerY.setMinimumSize(QtCore.QSize(30, 0))
        self.label_centerY.setObjectName("label_centerY")
        self.horizontalLayout_Advanced3.addWidget(self.label_centerY)
        self.lineEdit_centerY = QtWidgets.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_centerY.setEnabled(True)
        self.lineEdit_centerY.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_centerY.setReadOnly(True)
        self.lineEdit_centerY.setObjectName("lineEdit_centerY")
        self.horizontalLayout_Advanced3.addWidget(self.lineEdit_centerY)
        self.verticalLayout_Advanced.addLayout(self.horizontalLayout_Advanced3)
        self.horizontalLayout_Advanced4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Advanced4.setObjectName("horizontalLayout_Advanced4")
        self.label_rectWidth = QtWidgets.QLabel(self.groupBox_Resampling)
        self.label_rectWidth.setEnabled(True)
        self.label_rectWidth.setMinimumSize(QtCore.QSize(30, 0))
        self.label_rectWidth.setObjectName("label_rectWidth")
        self.horizontalLayout_Advanced4.addWidget(self.label_rectWidth)
        self.lineEdit_rectWidth = QtWidgets.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_rectWidth.setEnabled(True)
        self.lineEdit_rectWidth.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_rectWidth.setReadOnly(True)
        self.lineEdit_rectWidth.setObjectName("lineEdit_rectWidth")
        self.horizontalLayout_Advanced4.addWidget(self.lineEdit_rectWidth)
        self.label_rectHeight = QtWidgets.QLabel(self.groupBox_Resampling)
        self.label_rectHeight.setMinimumSize(QtCore.QSize(30, 0))
        self.label_rectHeight.setObjectName("label_rectHeight")
        self.horizontalLayout_Advanced4.addWidget(self.label_rectHeight)
        self.lineEdit_rectHeight = QtWidgets.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_rectHeight.setEnabled(True)
        self.lineEdit_rectHeight.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_rectHeight.setReadOnly(True)
        self.lineEdit_rectHeight.setObjectName("lineEdit_rectHeight")
        self.horizontalLayout_Advanced4.addWidget(self.lineEdit_rectHeight)
        self.verticalLayout_Advanced.addLayout(self.horizontalLayout_Advanced4)
        self.verticalLayout_6.addLayout(self.verticalLayout_Advanced)
        self.verticalLayout_2.addWidget(self.groupBox_Resampling)
        self.groupBox_DisplayType = QtWidgets.QGroupBox(DEMPropertiesWidget)
        self.groupBox_DisplayType.setObjectName("groupBox_DisplayType")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_DisplayType)
        self.verticalLayout_4.setContentsMargins(-1, 6, -1, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_MapCanvas = QtWidgets.QRadioButton(self.groupBox_DisplayType)
        self.radioButton_MapCanvas.setChecked(True)
        self.radioButton_MapCanvas.setObjectName("radioButton_MapCanvas")
        self.verticalLayout.addWidget(self.radioButton_MapCanvas)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton_LayerImage = QtWidgets.QRadioButton(self.groupBox_DisplayType)
        self.radioButton_LayerImage.setObjectName("radioButton_LayerImage")
        self.horizontalLayout_5.addWidget(self.radioButton_LayerImage)
        self.label_LayerImage = QtWidgets.QLabel(self.groupBox_DisplayType)
        self.label_LayerImage.setEnabled(False)
        self.label_LayerImage.setText("")
        self.label_LayerImage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_LayerImage.setObjectName("label_LayerImage")
        self.horizontalLayout_5.addWidget(self.label_LayerImage)
        self.toolButton_SelectLayer = QtWidgets.QToolButton(self.groupBox_DisplayType)
        self.toolButton_SelectLayer.setEnabled(False)
        self.toolButton_SelectLayer.setObjectName("toolButton_SelectLayer")
        self.horizontalLayout_5.addWidget(self.toolButton_SelectLayer)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_ImageFile = QtWidgets.QHBoxLayout()
        self.horizontalLayout_ImageFile.setObjectName("horizontalLayout_ImageFile")
        self.radioButton_ImageFile = QtWidgets.QRadioButton(self.groupBox_DisplayType)
        self.radioButton_ImageFile.setEnabled(True)
        self.radioButton_ImageFile.setObjectName("radioButton_ImageFile")
        self.horizontalLayout_ImageFile.addWidget(self.radioButton_ImageFile)
        self.lineEdit_ImageFile = QtWidgets.QLineEdit(self.groupBox_DisplayType)
        self.lineEdit_ImageFile.setEnabled(False)
        self.lineEdit_ImageFile.setObjectName("lineEdit_ImageFile")
        self.horizontalLayout_ImageFile.addWidget(self.lineEdit_ImageFile)
        self.toolButton_ImageFile = QtWidgets.QToolButton(self.groupBox_DisplayType)
        self.toolButton_ImageFile.setEnabled(False)
        self.toolButton_ImageFile.setObjectName("toolButton_ImageFile")
        self.horizontalLayout_ImageFile.addWidget(self.toolButton_ImageFile)
        self.verticalLayout.addLayout(self.horizontalLayout_ImageFile)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.radioButton_SolidColor = QtWidgets.QRadioButton(self.groupBox_DisplayType)
        self.radioButton_SolidColor.setObjectName("radioButton_SolidColor")
        self.horizontalLayout_7.addWidget(self.radioButton_SolidColor)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.groupBox_DisplayType)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.lineEdit_Color = QtWidgets.QLineEdit(self.groupBox_DisplayType)
        self.lineEdit_Color.setEnabled(False)
        self.lineEdit_Color.setObjectName("lineEdit_Color")
        self.horizontalLayout_7.addWidget(self.lineEdit_Color)
        self.toolButton_Color = QtWidgets.QToolButton(self.groupBox_DisplayType)
        self.toolButton_Color.setEnabled(False)
        self.toolButton_Color.setObjectName("toolButton_Color")
        self.horizontalLayout_7.addWidget(self.toolButton_Color)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_TextureSize = QtWidgets.QLabel(self.groupBox_DisplayType)
        self.label_TextureSize.setObjectName("label_TextureSize")
        self.gridLayout.addWidget(self.label_TextureSize, 0, 0, 1, 1)
        self.comboBox_TextureSize = QtWidgets.QComboBox(self.groupBox_DisplayType)
        self.comboBox_TextureSize.setObjectName("comboBox_TextureSize")
        self.gridLayout.addWidget(self.comboBox_TextureSize, 0, 1, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.groupBox_DisplayType)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 1, 0, 1, 1)
        self.spinBox_demtransp = QtWidgets.QSpinBox(self.groupBox_DisplayType)
        self.spinBox_demtransp.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_demtransp.sizePolicy().hasHeightForWidth())
        self.spinBox_demtransp.setSizePolicy(sizePolicy)
        self.spinBox_demtransp.setPrefix("")
        self.spinBox_demtransp.setMinimum(0)
        self.spinBox_demtransp.setMaximum(100)
        self.spinBox_demtransp.setSingleStep(10)
        self.spinBox_demtransp.setProperty("value", 0)
        self.spinBox_demtransp.setObjectName("spinBox_demtransp")
        self.gridLayout.addWidget(self.spinBox_demtransp, 1, 1, 1, 1)
        self.checkBox_TransparentBackground = QtWidgets.QCheckBox(self.groupBox_DisplayType)
        self.checkBox_TransparentBackground.setObjectName("checkBox_TransparentBackground")
        self.gridLayout.addWidget(self.checkBox_TransparentBackground, 1, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.checkBox_Shading = QtWidgets.QCheckBox(self.groupBox_DisplayType)
        self.checkBox_Shading.setChecked(True)
        self.checkBox_Shading.setObjectName("checkBox_Shading")
        self.verticalLayout_4.addWidget(self.checkBox_Shading)
        self.verticalLayout_2.addWidget(self.groupBox_DisplayType)
        self.groupBox_Clip = QtWidgets.QGroupBox(DEMPropertiesWidget)
        self.groupBox_Clip.setObjectName("groupBox_Clip")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_Clip)
        self.formLayout.setObjectName("formLayout")
        self.checkBox_Clip = QtWidgets.QCheckBox(self.groupBox_Clip)
        self.checkBox_Clip.setObjectName("checkBox_Clip")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBox_Clip)
        self.comboBox_ClipLayer = QtWidgets.QComboBox(self.groupBox_Clip)
        self.comboBox_ClipLayer.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_ClipLayer.sizePolicy().hasHeightForWidth())
        self.comboBox_ClipLayer.setSizePolicy(sizePolicy)
        self.comboBox_ClipLayer.setMaximumSize(QtCore.QSize(220, 16777215))
        self.comboBox_ClipLayer.setObjectName("comboBox_ClipLayer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_ClipLayer)
        self.verticalLayout_2.addWidget(self.groupBox_Clip)
        self.groupBox_Accessories = QtWidgets.QGroupBox(DEMPropertiesWidget)
        self.groupBox_Accessories.setObjectName("groupBox_Accessories")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_Accessories)
        self.verticalLayout_5.setContentsMargins(-1, 6, -1, 6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox_Sides = QtWidgets.QCheckBox(self.groupBox_Accessories)
        self.checkBox_Sides.setChecked(True)
        self.checkBox_Sides.setObjectName("checkBox_Sides")
        self.verticalLayout_5.addWidget(self.checkBox_Sides)
        self.checkBox_Frame = QtWidgets.QCheckBox(self.groupBox_Accessories)
        self.checkBox_Frame.setObjectName("checkBox_Frame")
        self.verticalLayout_5.addWidget(self.checkBox_Frame)
        self.verticalLayout_2.addWidget(self.groupBox_Accessories)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)

        self.retranslateUi(DEMPropertiesWidget)
        self.checkBox_Clip.toggled['bool'].connect(self.comboBox_ClipLayer.setEnabled)
        self.radioButton_LayerImage.toggled['bool'].connect(self.label_LayerImage.setEnabled)
        self.radioButton_LayerImage.toggled['bool'].connect(self.toolButton_SelectLayer.setEnabled)
        self.radioButton_ImageFile.toggled['bool'].connect(self.lineEdit_ImageFile.setEnabled)
        self.radioButton_ImageFile.toggled['bool'].connect(self.toolButton_ImageFile.setEnabled)
        self.radioButton_SolidColor.toggled['bool'].connect(self.lineEdit_Color.setEnabled)
        self.radioButton_SolidColor.toggled['bool'].connect(self.toolButton_Color.setEnabled)
        self.checkBox_Clip.toggled['bool'].connect(self.checkBox_Frame.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(DEMPropertiesWidget)

    def retranslateUi(self, DEMPropertiesWidget):
        _translate = QtCore.QCoreApplication.translate
        DEMPropertiesWidget.setWindowTitle(_translate("DEMPropertiesWidget", "Form"))
        self.label_DEMLayer.setText(_translate("DEMPropertiesWidget", "DEM Layer"))
        self.groupBox_Resampling.setTitle(_translate("DEMPropertiesWidget", "&Resampling"))
        self.radioButton_Simple.setText(_translate("DEMPropertiesWidget", "Simple"))
        self.label_Resolution.setText(_translate("DEMPropertiesWidget", "about 200 x 200 px"))
        self.label_8.setText(_translate("DEMPropertiesWidget", "Grid spacing:"))
        self.label_4.setText(_translate("DEMPropertiesWidget", "X"))
        self.label_9.setText(_translate("DEMPropertiesWidget", "Y"))
        self.checkBox_Surroundings.setText(_translate("DEMPropertiesWidget", "Surroundings"))
        self.label_2.setText(_translate("DEMPropertiesWidget", "Size"))
        self.label_3.setText(_translate("DEMPropertiesWidget", "Roughening"))
        self.radioButton_Advanced.setText(_translate("DEMPropertiesWidget", "Advanced (quad tree)"))
        self.label_11.setText(_translate("DEMPropertiesWidget", "Quad tree height"))
        self.label_10.setText(_translate("DEMPropertiesWidget", "Quad size"))
        self.lineEdit.setText(_translate("DEMPropertiesWidget", "64"))
        self.label_Focus.setText(_translate("DEMPropertiesWidget", "Focus point"))
        self.toolButton_PointTool.setText(_translate("DEMPropertiesWidget", "Get point from map"))
        self.label_centerX.setText(_translate("DEMPropertiesWidget", "x"))
        self.label_centerY.setText(_translate("DEMPropertiesWidget", "y"))
        self.label_rectWidth.setText(_translate("DEMPropertiesWidget", "Width"))
        self.label_rectHeight.setText(_translate("DEMPropertiesWidget", "Height"))
        self.groupBox_DisplayType.setTitle(_translate("DEMPropertiesWidget", "&Display type"))
        self.radioButton_MapCanvas.setText(_translate("DEMPropertiesWidget", "Map canvas image"))
        self.radioButton_LayerImage.setText(_translate("DEMPropertiesWidget", "Layer image"))
        self.toolButton_SelectLayer.setText(_translate("DEMPropertiesWidget", "Select layer(s)..."))
        self.radioButton_ImageFile.setText(_translate("DEMPropertiesWidget", "Image file"))
        self.toolButton_ImageFile.setText(_translate("DEMPropertiesWidget", "Browse..."))
        self.radioButton_SolidColor.setText(_translate("DEMPropertiesWidget", "Solid color"))
        self.label.setText(_translate("DEMPropertiesWidget", "Color"))
        self.lineEdit_Color.setPlaceholderText(_translate("DEMPropertiesWidget", "0xrrggbb"))
        self.toolButton_Color.setText(_translate("DEMPropertiesWidget", "..."))
        self.label_TextureSize.setText(_translate("DEMPropertiesWidget", "Resolution"))
        self.label_17.setText(_translate("DEMPropertiesWidget", "Transparency (%)"))
        self.checkBox_TransparentBackground.setText(_translate("DEMPropertiesWidget", "Transparent background"))
        self.checkBox_Shading.setText(_translate("DEMPropertiesWidget", "Enable shading"))
        self.groupBox_Clip.setTitle(_translate("DEMPropertiesWidget", "Clip"))
        self.checkBox_Clip.setText(_translate("DEMPropertiesWidget", "Clip DEM with polygon layer"))
        self.groupBox_Accessories.setTitle(_translate("DEMPropertiesWidget", "&Sides and frame"))
        self.checkBox_Sides.setText(_translate("DEMPropertiesWidget", "Build sides"))
        self.checkBox_Frame.setText(_translate("DEMPropertiesWidget", "Build frame"))

