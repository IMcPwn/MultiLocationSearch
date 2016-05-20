# MultiLocationSearch.py by IMcPwn  2016

import xml.etree.ElementTree as et
import csv
import subprocess
import os

def restartExplorer():
	subprocess.call("C:\\Windows\\System32\\taskkill.exe /F /IM explorer.exe")
	subprocess.Popen("C:\\windows\\explorer.exe")

def main():
	fileName = "TO-BE-CHANGED.search-ms"
	with open(fileName) as f:
		data = f.read()
		searchTerms = input("Enter the terms (comma separated) to search for: ")
		for i in searchTerms.split(","):
			searchFile = i + ".search-ms"
			with open(searchFile, "w+") as wf:
				wf.write(data.replace("TO-BE-CHANGED", i))
				subprocess.call("explorer.exe " + searchFile)
		deleteQuest = input("Would you like to delete the new saved searches? (WILL ALSO CLOSE THEM IF OPEN) y | n: ")
		if deleteQuest.lower().startswith("y"):
			for i in searchTerms.split(","):
				os.remove(i + ".search-ms")
			restartExpQuest = input("Would you like to restart explorer? (to remove the extra explorer Windows? y | n: ")
			if restartExpQuest.lower().startswith("y"):
				restartExplorer()

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		restartExplorer()

