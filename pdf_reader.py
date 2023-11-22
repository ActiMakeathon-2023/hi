from PyPDF2 import PdfReader
import os
import re
from PyPDF2 import PdfReader

def extract_fault_numbers(pdf_path):
	# Load the PDF file
	pdf_reader = PdfReader(pdf_path)

	# Regular expression to match fault numbers
	fault_number_regex = re.compile(r'^(\d+)\n', re.MULTILINE)

	# Extract text from each page and search for fault numbers
	fault_numbers = []
	for page in pdf_reader.pages:
		page_text = page.extract_text()
		if page_text:
			found_fault_numbers = fault_number_regex.findall(page_text)
			for number in found_fault_numbers:
				if int(number) < 2100:  # Only add numbers less than 2100
					fault_numbers.append(number)
	return fault_numbers

def extract_fault_descriptions(pdf_path):
	# Load the PDF file
	pdf_reader = PdfReader(pdf_path)
	# Regular expression to match the format of the fault descriptions
	# It captures the category and the specific fault
	fault_description_regex = re.compile(r'^\d+\n([A-Za-z ]+):\n(.+)', re.MULTILINE)
	# Extract text from each page and search for fault descriptions
	fault_descriptions = []
	for page in pdf_reader.pages:
		page_text = page.extract_text()
		if page_text:
			matches = fault_description_regex.findall(page_text)
			for category, description in matches:
				if (category != 'Place'):
					fault_descriptions.append(f"{category}: {description}")
	return fault_descriptions


# Path to your PDF file
pdf_path = '100261_faults1.pdf'

# # Extract and print the fault numbers
# fault_numbers = extract_fault_numbers(pdf_path)
# descriptions = extract_fault_descriptions(pdf_path)
# print(descriptions)
