from PyQt5.QtCore import Qt
from PIL import Image, ImageFilter
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QLabel, QHBoxLayout, QVBoxLayout, QFileDialog
class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "save/"
    def LoadImage(self, filename):
        self.filename = filename
        image_path = os.path.join(workdir, filename)
        self.image = Image.open(image_path)
    def showImage(self, path):
        picture.hide()
        pixmapimage = QPixmap(path)
        w, h = picture.width(), picture.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        picture.setPixmap(pixmapimage)
        picture.show()
    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    def do_grey(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_blured(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_mirrow(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
workdir = ''
def filter(files, extensions):
    result = list()
    for filename in files:
        for extension in extensions:
            if filename.endswith(extension):
                result.append(filename)
    return result
def showFilenamesList():
    chooseWordic()
    extensions = ['png', 'jpg']
    files = os.listdir(workdir)
    filenames = filter(files, extensions)
    list_of_pic.clear()
    for filename in filenames:
        list_of_pic.addItem(filename)
def chooseWordic():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def showChosenImage():
    if list_of_pic.currentRow() >= 0:
        filename = list_of_pic.currentItem().text()
        workimage.LoadImage(filename)
        image_path = os.path.join(workdir, workimage.filename)
        workimage.showImage(image_path)
app = QApplication([])
Editor = QWidget()
Editor.resize(800, 600)
Editor.setWindowTitle('Easy Editor')
workimage = ImageProcessor()
bth_dir = QPushButton('Папка')
bth_left = QPushButton('Лево')
bth_right = QPushButton('Право')
bth_mirrow = QPushButton('Зеркало')
bth_blured = QPushButton('Резкость')
bth_gray = QPushButton('Ч/б')
picture = QLabel('Картинка')
list_of_pic = QListWidget()
LayoutV1 = QVBoxLayout()
LayoutV2 = QVBoxLayout()
LayoutLIDER = QHBoxLayout()
LayoutH = QHBoxLayout()
LayoutV1.addWidget(bth_dir, alignment = Qt.AlignHCenter)
LayoutV1.addWidget(list_of_pic, alignment = Qt.AlignHCenter)
LayoutV2.addWidget(picture)
LayoutH.addWidget(bth_left)
LayoutH.addWidget(bth_right)
LayoutH.addWidget(bth_mirrow)
LayoutH.addWidget(bth_blured)
LayoutH.addWidget(bth_gray)
LayoutV2.addLayout(LayoutH)
LayoutLIDER.addLayout(LayoutV1)
LayoutLIDER.addLayout(LayoutV2)
Editor.setLayout(LayoutLIDER)
bth_dir.clicked.connect(showFilenamesList)
list_of_pic.currentRowChanged.connect(showChosenImage)
bth_gray.clicked.connect(workimage.do_grey)
bth_blured.clicked.connect(workimage.do_blured)
bth_left.clicked.connect(workimage.do_left)
bth_right.clicked.connect(workimage.do_right)
bth_mirrow.clicked.connect(workimage.do_mirrow)
Editor.show()
app.exec_()