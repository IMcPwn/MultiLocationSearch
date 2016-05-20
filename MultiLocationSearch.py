'''
Copyright 2016 IMcPwn .  All rights reserved.
Use of this source code is governed by a BSD-style
license that can be found in the LICENSE file.

Search in multiple locations for multiple files using the "power" of Windows explorer.
'''

import xml.etree.ElementTree as et
import csv
import subprocess
import os

def restartExplorer():
	subprocess.call("C:\\Windows\\System32\\taskkill.exe /F /IM explorer.exe")
	subprocess.Popen("C:\\windows\\explorer.exe")

def main():
	magicWord = "TO-BE-CHANGED"
	fileName = magicWord + ".search-ms"
	with open(fileName) as f:
		data = f.read()
		searchTerms = input("Enter the terms (comma separated) to search for: ")
		'''
		This could be improved. Instead of opening a new window for each search term
		a value1 OR value2 clause could be used but that would require actually parsing the XML.
		Or maybe this way is better..?
		'''
		for i in searchTerms.split(","):
			searchFile = i + ".search-ms"
			with open(searchFile, "w+") as wf:
				wf.write(data.replace(magicWord, i))
				subprocess.call("explorer.exe " + searchFile)

		deleteQuest = input("Would you like to delete the new saved searches? (WILL ALSO CLOSE THEM IF OPEN) y | n: ")
		if deleteQuest.lower().startswith("y"):
			for i in searchTerms.split(","):
				os.remove(i + ".search-ms")

			restartExpQuest = input("Would you like to restart explorer? (to remove the extra explorer Windows?) y | n: ")
			if restartExpQuest.lower().startswith("y"):
				restartExplorer()

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		restartExplorer()

