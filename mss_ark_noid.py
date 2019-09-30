import csv
import os
import subprocess
import pandas as pd


#creates a mappings file that provides metadata to EZID
def create_mappings():

	cursor = csv.DictReader(open(file_path),
		delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

	for row in cursor:
		if row['Object type'] == 'Work':
			title = row['Title']
			mappings_file = open("mappings.txt", "w+")
			string = 'erc.who: UCLA Library', ('\nerc.what: '+str(title))
			for s in string:
				mappings_file.write(s)

#creates a noid format file that suplies the parent ark for the NOID to be appended to
def create_noid_yml(parent_ark):

	noid_file = open("Noid_test.yml", "w+")
	string = ['template: eeddeede \n',('scheme: ' + str(parent_ark[0:11])), ('\nnaa: ' + str(parent_ark[11:]))]
	for s in string:
		noid_file.write(s)

#calls the EZID and NOID scripts based if the row is a Work or Page
def call_ezid(file_path):

	cursor = csv.DictReader(open(file_path),
		delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

	item_ark_list = []
	parent_ark_list = ['']

	for row in cursor:
		if row['Object type'] == 'Work':
			create_mappings()
			cmd_ezid = ['python', 'ezid.py', ezid_input, 'mint', ark_shoulder, '@', 'mappings.txt']
			parent_ark = subprocess.Popen(cmd_ezid, stdout=subprocess.PIPE).communicate()[0]
			parent_ark = (str(parent_ark)).replace('success: ', '')
			print(parent_ark)
			create_noid_yml(parent_ark)
			item_ark_list.append(parent_ark)
			

		if row['Object type'] == 'Page':
			cmd = ['noid', '-f', 'Noid_test.yml']
			item_ark = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
			item_ark_list.append(item_ark)
			parent_ark_list.append(parent_ark)

#writes the new parent ARKs and Item ARKs to new columns in an export csv
	data= pd.read_csv(file_path, sep=',', delimiter=None, header='infer')
	data['Parent Ark'] = parent_ark_list
	data['Item Ark'] = item_ark_list
	data.to_csv(path_or_buf=output_file, sep=',', na_rep='', float_format=None, index=False)


#input from the command line to supply directory of files,
# the EZID credientials, and the preferred ARK shoulder

directory = raw_input('File directory:')
ezid_input = raw_input('EZID username and password:')
ark_shoulder = raw_input('ARK shoulder:')
				

#runs through the functions for all csvs in the directory supplied			
for filename in os.listdir(directory):
	if '.csv' in filename:
		file_path = directory + (str(filename))
		output_file = str(filename).replace('.csv', '') + '_export.csv'
		print(filename)
		call_ezid(file_path)
		

