import csv
import os
import subprocess
import pandas as pd


#creates a mappings file that provides metadata to EZID


#creates a noid format file that suplies the parent ark for the NOID to be appended to



def create_noid_yml(parent_ark):

    noid_file = open("Noid_test.yml", "w+")
    string = ['template: eeddeede \n',('scheme: ' + str(parent_ark[0:11])), ('\nnaa: ' + str(parent_ark[11:]))]
    for s in string:
        noid_file.write(s)

def create_mappings():

    title = row['Title']
    mappings_file = open("mappings.txt", "w+")
    string = 'erc.who: UCLA Library', ('\nerc.what: '+str(title))
    for s in string:
        mappings_file.write(s)

#calls the EZID and NOID scripts based if the row is a Work or Page
#open all csvs in the directory
directory = raw_input('File directory:')
ark_shoulder = raw_input('ARK shoulder:')
works_file = raw_input('path to works.csv:')
ezid_input = raw_input('EZID username and password:')

ark_dict = {}

parent_ark_list = []

output_file = 'works_export.csv'
works_cursor = csv.DictReader(open(works_file),
    delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

for row in works_cursor:

    altidentifer = row['AltIdentifier.local']
    if row['Object Type'] == 'Work':
        create_mappings()
        cmd_ezid = ['python', 'ezid.py', ezid_input, 'mint', ark_shoulder, '@', 'mappings.txt']
        parent_ark = subprocess.Popen(cmd_ezid, stdout=subprocess.PIPE).communicate()[0]
        parent_ark = (str(parent_ark)).replace('success: ', '')
        parent_ark_list.append(parent_ark)
        ark_dict[altidentifer] = parent_ark

data= pd.read_csv(works_file, sep=',', delimiter=None, header='infer')
data['Item Ark'] = parent_ark_list
data.to_csv(path_or_buf=output_file, sep=',', na_rep='', float_format=None, index=False)



for filename in os.listdir(directory):
    if '.csv' in filename:
        file_path = directory + (str(filename))
        output_file = str(filename).replace('.csv', '') + '_export.csv'
        cursor = csv.DictReader(open(file_path),
            delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        item_ark_list = []
        local_parent_ark_list = []
        for row in cursor:
            if row['Object Type'] == 'Page':
                source = row['Source']
                if source in ark_dict.keys():
                    parent_ark = ark_dict[source]

                    create_noid_yml(parent_ark)
                    cmd = ['noid', '-f', 'Noid_test.yml']
                    item_ark = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
                        #   print(item_ark)
                    item_ark_list.append(item_ark)
                    local_parent_ark_list.append(parent_ark)

        data= pd.read_csv(file_path, sep=',', delimiter=None, header='infer')
        data['Item Ark'] = item_ark_list
        data['Parent Ark'] = local_parent_ark_list
        data.to_csv(path_or_buf=output_file, sep=',', na_rep='', float_format=None, index=False)

        

