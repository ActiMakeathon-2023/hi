import docx2txt as d2t
from parser1 import get_all_desc, get_operation
from ai_stuff import call_ai
import csv
import re
import pdf_reader as pdf
import argparse

def remove_flt(text):
	pattern = r"FLT \d+:\s"
	res = re.sub(pattern, '', text)
	return res

def remove_non_ascii(string):
	return ''.join(i for i in string if ord(i) < 128)

def clean_text(path_master_cut :str):
	with open(path_master_cut, 'r', encoding='ISO-8859-1') as file:
		content = file.read()
		content = remove_non_ascii(content)
	return content.lower()


path_all = '100XXX_QD_AFT-Kartonierer_Exec_en_Makeathon.docx'


output_file = open('output.csv', 'w')
csv_writer = csv.writer(output_file)
csv_header = ['FAULT CODE', 'OPERATION']
csv_writer.writerow(csv_header)

# Example usage
text = "Here is some sample text. ID123 Required operations: Operation A, Operation B Consequence: Outcome ID234 Required operations: Operation C, Operation D Consequence:"

def remove_flt(text):
	pattern = r"FLT \d+:\s"
	res = re.sub(pattern, '', text)
	return res

def filter_desc(text):
	all_flts, all_desc = get_all_desc(text)
	faults = []
	index = 0
	for desc in all_desc:
		faults.append(desc)
	for fault in faults:
		faults[index] = remove_flt(fault)
		index += 1
	# for fault in faults:
	# 	print(fault)
	return faults

if __name__ == "__main__":
	f = open("file.txt", 'a')
	pdf_path = '100261_faults1.pdf'
	all_pos_ids = pdf.extract_fault_numbers(pdf_path)
	all_pos_disc = pdf.extract_fault_descriptions(pdf_path)
	text = d2t.process(path_all)
	#text = clean_text('master_cut.txt')
	all_desc = filter_desc(text)
	i = 0
	for i in range(0,len(all_pos_ids)):
		operation = get_operation("FLT " + all_pos_ids[i] + ": ", text)
		if (operation != "unknown"):
			csv_row = [operation]
			print(operation)
			f.write(operation)
			csv_writer.writerow(csv_row)
		else:
			for desc in all_desc:
				try:
					prompt = "Onlye answer with 0 or 1. Answer with 1 if these two error description are allmost the same in meaning with 0 if they are different.\nHere is the first description: " + desc + "/nhere is the second description: " + all_pos_disc[i]
					chat_gpt_answer = call_ai(prompt)
					print(chat_gpt_answer)
					if (chat_gpt_answer == "1"):
							action = "GUESS: " + get_operation(desc, text)
							csv_row = [desc]
							f.write(desc)
							csv_writer.writerow(csv_row)
							break
				except:
					pass
	# fault_code_list = parse_error_pdf()
	# for fault_code in fault_codes_list:
	# 	operation = get_operation(fault_code, text)
	# 	if operation == 'unknown':
	# 		call_ai()
	# 	else:
	#

