import re

def get_all_testable_flts_lst():

	# Replace 'your_file.txt' with the actual path to your file
	file_path = 'master_cut.txt'

  # Read the contents of the file
  with open(file_path, 'r') as file:
  file_contents = file.read()

  # Use regular expression to find numbers after 'FLT'
  matches = re.findall(r'FLT\s*(\d+\.?\d*)', file_contents)
  
  switch = 0
  filtered_flt = []

  for i in range(len(matches)):
    if matches[i] == '1024':
      switch = 1
    if switch == 1 and matches[i] != '1024':
      filtered_flt.append(matches[i])
  return (filtered_flt)


def get_all_nontestable_flts_lst():

  # Replace 'your_file.txt' with the actual path to your file
  file_path = 'master_cut.txt'

  # Read the contents of the file
  with open(file_path, 'r') as file:
  file_contents = file.read()

  # Use regular expression to find numbers after 'FLT'
  matches = re.findall(r'FLT\s*(\d+\.?\d*)', file_contents)


  switch = 1
  filtered_flt = []

  for i in range(len(matches)):
    if matches[i] == '1024':
      switch = 0
    if switch == 1:
      filtered_flt.append(matches[i])
  return (filtered_flt)

