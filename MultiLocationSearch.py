# MultiLocationSearch.py by IMcPwn  2016

import xml.etree.ElementTree as et
import csv
import subprocess

fileName = "TO-BE-CHANGED.search-ms"
with open(fileName) as f:
	data = f.read()
	searchTerms = input("Enter the terms (comma separated) to search for: ")
	for i in searchTerms.split(","):
		searchFile = i + ".search-ms"
		with open(searchFile, "w+") as wf:
			wf.write(data.replace("TO-BE-CHANGED", i))
			subprocess.call("explorer.exe " + searchFile)
			
