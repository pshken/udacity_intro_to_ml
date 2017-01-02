#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

from __future__ import division
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

cnt = 0

for key, value in enron_data.iteritems():
	if value['total_payments'] == 'NaN' and value['poi'] == True:
		cnt += 1

print cnt
print len(enron_data)
print cnt / len(enron_data) * 100