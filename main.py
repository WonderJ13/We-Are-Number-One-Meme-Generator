from PyQt5 import QtCore, QtGui, uic, QtWidgets
import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import *
import os, sys, interface

class Window(QtWidgets.QMainWindow, interface.Ui_MainWindow):

	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.setupUi(self)
		self.btnOpenWAN1.clicked.connect(self.openWAN1)
		self.btnOpenVideo.clicked.connect(self.openVideo)
		self.btnSave.clicked.connect(self.saveVideo)
		self.wanFile = ''
		self.videoFile = ''
		self.saveDir = ''

	def openWAN1(self):
		options = QtWidgets.QFileDialog.Options()
		options |= QtWidgets.QFileDialog.DontUseNativeDialog
		self.wanFile, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		print(self.wanFile)
		self.wanEdit.setText(self.wanFile)

		self.wanFile = VideoFileClip(self.wanFile)

	def openVideo(self):
		options = QtWidgets.QFileDialog.Options()
		options |= QtWidgets.QFileDialog.DontUseNativeDialog
		self.videoFile, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		self.inputEdit.setText(self.videoFile)

		self.videoFile = VideoFileClip(self.videoFile)


	def saveVideo(self):
		options = QtWidgets.QFileDialog.Options()
		options |= QtWidgets.QFileDialog.DontUseNativeDialog
		self.saveDir = QtWidgets.QFileDialog.getExistingDirectory(self, 
					"Open Save Directory", os.path.expanduser('~'))
		self.outputEdit.setText(self.saveDir + '/output.mp4')
		self.combineVideos()

	def combineVideos(self):
		imageio.plugins.ffmpeg.download()
		times = [(39.2, 39.8), (45.2, 45.7), (56.9, 57.5), ((1, 17.9), (1, 18.3)),
		((1, 23.7), (1, 24.3)), ((1, 31.1), (1, 31.7)), ((2, 12.6), (2, 13.2)),
		((2, 19.3), (2, 20.1)), ((2, 36.3), (2, 36.8)), ((2, 42.3), (2, 42.8)),
		((2, 43.8), (2, 44.3)), ((2, 45.3), (2, 45.8))]

		videoparts = []

		oldt = 0
		for t0, t1 in times:
			videoparts.append(self.wanFile.subclip(oldt, t0))
			videoparts.append(self.videoFile)
			oldt = t1
		videoparts.append(self.wanFile.subclip(oldt))

		result = concatenate_videoclips(videoparts)

		outputFile = self.saveDir + '/output.mp4'
		result.write_videofile(outputFile,fps=23)
		self.lblFinished.setText("Your Video was successfully created!!")

def main():
	app = QtWidgets.QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()