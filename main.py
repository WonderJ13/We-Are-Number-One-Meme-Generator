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

		self.videoFile = VideoFileClip(self.videoFile).set_fps(23).resize((1280, 720))


	def saveVideo(self):
		options = QtWidgets.QFileDialog.Options()
		options |= QtWidgets.QFileDialog.DontUseNativeDialog
		self.saveDir = QtWidgets.QFileDialog.getExistingDirectory(self, 
					"Open Save Directory", os.path.expanduser('~'))
		self.outputEdit.setText(self.saveDir + '/output.mp4')
		self.combineVideos()

	def combineVideos(self):
		imageio.plugins.ffmpeg.download()
		times = [(39.21739, 39.82608), (45.21739, 45.69565), (56.91304, 57.52173), ((1, 17.91304), (1, 18.30434)),
		((1, 23.69565), (1, 24.30434)), ((1, 31.086956), (1, 31.69565)), ((2, 12.60869), (2, 13.21739)),
		((2, 19.30434), (2, 20.086956)), ((2, 36.30434), (2, 36.82608)), ((2, 42.30434), (2, 42.82608)),
		((2, 43.82608), (2, 44.30434)), ((2, 45.30434), (2, 45.82608))]

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
