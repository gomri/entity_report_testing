from datetime import date, timedelta
import os
import sys, ast


test_file_name = 'admeta-pwf_rep_2017_03-28.csv'

def test_setup():
	f= open(test_file_name,"w+")
	f.close()

def test_clean_up():
	os.remove(test_file_name)

def get_input_from_user():
	inputList = ast.literal_eval( sys.argv[1] )
	return inputList

def get_date_format():
	yesterday = date.today() - timedelta(1)
	yesterday_formated = yesterday.strftime('%y-%m-%d')
	return str(yesterday)

def format_list(entities_list,date_format):
	# This is for testing
	prefix = "C:/Users/gomri/Desktop/entity_report_testing/"

	reports_name = []
	for entity in range(len(entities_list)):
		formated_report_name = prefix + entities_list[entity] + '_rep_' + date_format + '.csv'
		reports_name.append(formated_report_name)
	return reports_name

def check_report_arrived(report_names):
	for report in range(len(report_names)):
		print report_names[report]
		arrived = os.path.exists(report_names[report])
		print arrived
		# if arrived == True:


# test_setup()

entities_to_check = get_input_from_user()

yesterday = get_date_format()

formated_report_names = format_list(entities_to_check,yesterday)

print formated_report_names

check_report_arrived(formated_report_names)

# test_clean_up()

# command line cant expect just one entity name example:
# python script,py "'admeta'"" wont work 
# but python script.py "'admeta'," will work
