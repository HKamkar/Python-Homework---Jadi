import csv
from statistics import mean
from typing import OrderedDict
from operator import itemgetter

def calculate_averages(input_file_name, output_file_name):
    data = []
    #read the data from csv file
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            #Converting string scores to int
            for i in range(1,len(row)):
                row[i] = int(row[i])
            
            assemble = ['name', 0]
            assemble[0] = row[0]
            #print(row[0])
            assemble[1] = mean(row[1:])
            #print(assemble)
            data.append(assemble)
        #print(data)
            
                
    #write the data on csv file
    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        # write the data
        for i in data:
            writer.writerow(i)
    


def calculate_sorted_averages(input_file_name, output_file_name,reversed = False):
    data = OrderedDict()
    sorted_data = OrderedDict()
    calculate_averages(input_file_name,'mean.csv')
    #read the data from csv file
    with open('mean.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            #Converting string scores to int
            for i in range(1,len(row)):
                row[i] = float(row[i])

            data.update({row[0]: row[1]})
            sorted_data = sorted(data.items(), key=itemgetter(1), reverse= reversed)
        #print(sorted_data)
        
                  
    #write the data on csv file
    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        # write the data
        for i in sorted_data:
            writer.writerow(i)



def calculate_three_best(input_file_name, output_file_name):
    calculate_sorted_averages(input_file_name, 'sorted_mean.csv', reversed=True)
    data = OrderedDict()
    #read the data from csv file
    with open('sorted_mean.csv', 'r') as file:
        reader = csv.reader(file)
        row_index = 0
        for row in reader:
            #Converting string scores to int
            for i in range(1,len(row)):
                row[i] = float(row[i])
                
            # for writing just 3 rows
            if row_index == 3:
                break
            row_index += 1
            
            #Migrating sorted data to a dicttionary
            data.update({row[0]: row[1]})
    #print(data)
            
                
    #write the data on csv file
    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        # write the data
        for key in data.keys():
            file.write("%s, %s\n" % (key, data[key]))
    


def calculate_three_worst(input_file_name, output_file_name):
    calculate_sorted_averages(input_file_name, 'sorted_mean.csv')
    data = OrderedDict()
    #read the data from csv file
    with open('sorted_mean.csv', 'r') as file:
        reader = csv.reader(file)
        row_index = 0
        for row in reader:
        #Converting string scores to int
            for i in range(1,len(row)):
                row[i] = float(row[i])
                
            # for writing just 3 rows
            if row_index == 3:
                break
            row_index += 1
            
            #Migrating sorted data to a dicttionary
            data.update({row[0]: row[1]})
            #print(data)
            
                
    #write the data on csv file
    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        # write the data
        for key in data.keys():
            file.write("%s, %s\n" % (key, data[key]))
    


def calculate_average_of_averages(input_file_name, output_file_name):
    data = []
    mean_of_class = []
    calculate_averages(input_file_name, 'sorted_mean.csv')
    #read the data from csv file
    with open('sorted_mean.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            #Converting string scores to int
            for i in range(1,len(row)):
                row[i] = float(row[i])
            
            data.append(row[1])
                
        mean_of_class.append(mean(data))
        #print(type(data))
            
                
    #write the data on csv file
    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        # write the data
        
        writer.writerow(mean_of_class)