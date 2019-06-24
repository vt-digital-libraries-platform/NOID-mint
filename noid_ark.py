
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
#The first item in the parent_ark_list is empty as the manuscript does not have a parent.
	ark_list = [parent_ark]
	parent_ark_list = ['']


#A loop to create the necessary amount of unique ARKs and add them to the ark_list
#Runs the command line command from the NOID-Mint script
	row_count=data.shape[0]
	

	for f in range(1,row_count):

		cmd = ['noid', '-f', noid_file]
		item_ark = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
		ark_list.append(item_ark)
		parent_ark_list.append(parent_ark)

#Writes the list of parent ARKs to a new column in the DataFrame		
#Wrties the list of the item ARKs to a new column in the DatFrame

	data['Parent Ark'] = parent_ark_list
	data['Item Ark'] = ark_list
	
#Writes DataFrame to a new csv file

	data.to_csv(path_or_buf=output_file, sep=',', na_rep='', float_format=None, index=False)

#add the function the the correct inputs here to run the script
