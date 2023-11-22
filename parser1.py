
def get_operation(id_string, text):
	id_index = text.find(id_string)
	if id_index == -1:
		return "unknown"
	start_index = text.find("Required operations", id_index + len(id_string))
	if start_index == -1:
		return "unknown"
	end_index = text.find("Consequence", start_index)
	if end_index == -1:
		return "unknown"
	operation = text[start_index + len("Required operations"):end_index].strip()
	return operation

# def get_desc(id_string, text):
# 	start_index = text.find(id_string)
# 	if start_index == -1:
# 		return "unknown"
# 	end_index = text.find("\nTest objective", start_index)
# 	if end_index == -1:
# 		return "unknown"
# 	desc = text[start_index + len(id_string):end_index].strip()
# 	return desc

def get_all_desc(text):
	id_string = "FLT "
	all_flts = {}
	all_desc = {}
	start_index = 0

	while True:
		start_index = text.find(id_string, start_index)
		if start_index == -1:
			break
		end_index = text.find("\n", start_index)
		if end_index == -1:
			end_index = len(text)
		flt_id = text[start_index:end_index].strip()
		all_flts[flt_id] = start_index
		desc_start = text.find("\n", end_index)
		desc_end = text.find("\nTest objective", desc_start)
		if desc_end == -1:
			desc_end = len(text)
		desc = text[desc_start + 1:desc_end].strip()
		all_desc[flt_id] = desc
		start_index = desc_end
	return all_flts, all_desc



