import csv
import os
import subprocess
import pandas as pd

#Read the given csv file into the pandas DataFrame
# the four inputs the function takes are the file path to the csv input file
#the configured yml file which sets up the specifics for the ark, the parent ark, and
#the name of the output file

#need to add subprocess-- if row type is equal to work, run ezid script
#at end of that, call the create_arks
directory = raw_input('File directory:')
ezid_input = raw_input('EZID username and password:')

for filename in os.listdir(directory):
	file_path = directory + (str(filename)).strip()
	output_file = filename + '_export.csv'


	def call_ezid(file_path):
		cursor = csv.DictReader(open(file_path),
			delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

		for row in cursor:
			if row['Object type'] == 'Work':
				def create_mappings():
						title = row['Title']
						mappings_file = open("mappings.txt", "w+")
						string = 'erc.who: UCLA Library', ('\nerc.what: '+str(title))
						for s in string:
							mappings_file.write(s)
				create_mappings()
				cmd_ezid = ['python', 'ezid.py', ezid_input, 'mint', 'ark:/99999/fk4', '@', 'mappings.txt']
				parent_ark = subprocess.Popen(cmd_ezid, stdout=subprocess.PIPE).communicate()[0]
				parent_ark = (str(parent_ark)).replace('success: ', '')
				print(parent_ark)
			if row['Object type'] == 'Page':

				def create_arks(file_path, noid_file, parent_ark, output_file):

					def create_noid_yml(parent_ark):
		#parent_ark = read csv and manuscript row
						noid_file = open("Noid_test.yml", "w+")
						string = ['template: eeddeede \n',('scheme: ' + str(parent_ark[0:11])), ('\nnaa: ' + str(parent_ark[11:]))]
						for s in string:
							noid_file.write(s)
					create_noid_yml(parent_ark)

					data= pd.read_csv(file_path, sep=',', delimiter=None, header='infer')

#Create a list that the generated item arks will be appended to. 
#The first item in the parent_ark_list is empty as the manuscript does not have a parent.
					ark_list = [parent_ark]
					parent_ark_list = ['']

#A loop to create the necessary amount of unique ARKs and add them to the ark_list
#Runs the command line command from the NOID-Mint script
					row_count=data.shape[0]
	
					for f in range(1,row_count):
		#if for each csv row type is equal to page

						cmd = ['noid', '-f', noid_file]
						item_ark = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
						ark_list.append(item_ark)
						parent_ark_list.append(parent_ark)

					data['Parent Ark'] = parent_ark_list
					data['Item Ark'] = ark_list
	
#Writes DataFrame to a new csv file

					data.to_csv(path_or_buf=output_file, sep=',', na_rep='', float_format=None, index=False)

				create_arks(file_path, 'Noid_test.yml', parent_ark, output_file)

	call_ezid(file_path)


