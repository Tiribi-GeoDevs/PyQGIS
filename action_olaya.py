import webbrowser

url = 'https://en.wikipedia.org/wiki/' + '[%wikipedia%]'
try:
	webbrowser.open(url, new=0, autoraise=True)
except:
	QMessageBox.warning(None, "Wrong value", "The corresponding Wikipedia page does not exist")
	

