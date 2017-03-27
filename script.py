from datetime import date, timedelta
import os
import sys, ast

def get_input_from_user():
	inputList = ast.literal_eval( sys.argv[1] )
	return inputList

def get_date_format():
	yesterday = date.today() - timedelta(1)
	yesterday_formated = yesterday.strftime('%y-%m-%d')
	return str(yesterday)

def format_list(entities_list,date_format):
	reports_name = []s
	for entity in range(len(entities_list)):
		formater_report_name = str(entities_list[entity] + '_rep_' + date_format + '.csv')
		reports_name.append(formater_report_name)
	return reports_name

def check_report_arrived(report_names):
	for report in range(len(report_names)):
		print os.path.exists(report_names[report])


entities_to_check = get_input_from_user()

yesterday = get_date_format()

formated_report_names = format_list(entities_to_check,yesterday)

check_report_arrived(formated_report_names)

# command line cant expect just one entity name example:
# python script,py 'admeta' wont work 
# but python script.py 'adneta', will work
