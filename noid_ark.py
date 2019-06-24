
import csv
import os
import subprocess
import pandas as pd

#Read the given csv file into the pandas DataFrame
# the four inputs the function takes are the file path to the csv input file
#the configured yml file which sets up the specifics for the ark, the parent ark, and
#the name of the output file

def create_arks(file_path, noid_file, parent_ark, output_file):

	data= pd.read_csv(file_path, sep=',', delimiter=None, header='infer')

#Create a list that the generated item arks will be appended to. 
	ark_list = ['']


#A loop to create the necessary amount of unique ARKs and add them to the ark_list
#Runs the command line command from the NOID-Mint script
	row_count=data.shape[0]
	

	for f in range(1,row_count):

		cmd = ['noid', '-f', noid_file]
		item_ark = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
		ark_list.append(item_ark)

#Wrties the list of the item arks to a new column in the DatFrame	
	data['Parent Ark'] = parent_ark
	data['Item Ark'] = ark_list
	

#Writes DataFrame to a new csv file

	data.to_csv(path_or_buf=output_file, sep=',', na_rep='', float_format=None, index=False)



#creating the needed files for new item arks. this can be changed to accomodate new files
create_arks('Sinai_57.csv', 'sinai_57.yml', 'ark:/21198/z15q60cw', 'sinai_57_arks.csv')
create_arks('Sinai_65.csv', 'sinai_65.yml', 'ark:/21198/z1x64r73', 'sinai_65_arks.csv')
create_arks('Sinai_67.csv', 'sinai_67.yml', 'ark:/21198/z1sf40hr', 'sinai_67_arks.csv')
create_arks('Sinai_100.csv', 'sinai_100.yml', 'ark:/21198/z1ns1z7t', 'sinai_100_arks.csv')
create_arks('Sinai_60.csv', 'sinai_60.yml', 'ark:/21198/z11z57pm', 'sinai_60_arks.csv')
