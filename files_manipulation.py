from importlib.metadata import files

from read_directory import run_code
import os
from datetime import date
from generate_reports import reports

class read_data(run_code, reports):
    yearly_data = []

    def run_commandline(self):
        objj = run_code()
        command = objj.commandline()
        path = command.Path
        report = command.Report_Number
        read_files_name = objj.files(command)
        return path,report, read_files_name

    def declaration(self,time, max_temp, min_temp, max_humidity, min_humidity):

        data_dictionary = {
            'year' : time.year,
            'date': time ,
            'max_temp': max_temp,
            'min_temp' : min_temp,
            'max_humidity' : max_humidity,
            'min_humidity' : min_humidity

        }

        self.yearly_data.append(data_dictionary)
        data = {}




    def read_files(self, command, read_files_name):
        if command[-1] != '/':
            command = command + '/'


        for file_name in read_files_name:

            file =  open(os.path.join(command + file_name), 'r')
            for line in file:
                if line[0] == 'P':
                    break
            # temp_list = []
            for l in file:
                temp = l
                file_line = temp.split("\n") # it will split line from end of line
                for x in file_line: # this loop will work for each row
                    # temp_list = [] # it's a temporary list where we can store data for each row
                    row_data = x.split(",") #it will split each row from ,
                    # print(row_data)
                    # for u in row_data:
                    #     temp_list.append(u)
                    # print(row_data)

                    if len(row_data) >= 9:
                        time = ''
                        max_temp = ''
                        min_temp = ''
                        max_humidity = ''
                        min_humidity = ''
                        if row_data[0] != '':
                            temp_date = row_data[0].split("-")
                            time = date(int(temp_date[0]), int(temp_date[1]), int(temp_date[2]))
                        if row_data[1] != '':
                            max_temp = int(row_data[1])
                        if row_data[3] != '':
                            min_temp = int(row_data[3])
                        if row_data[7] != '':
                            max_humidity = int(row_data[7])
                        if row_data[9] != '':
                            min_humidity = int(row_data[9])
                        self.declaration(time, max_temp, min_temp, max_humidity, min_humidity)




    def years_to_process(self, data):
        '''
        This ia a function, taking all files name in parameter that are available in directory, splitting them to get the years and converting them into the set to avoid duplication and converting them agin into list
        :param files_name_list: a list of files name in the directory
        :return: a list of years without duplicates
        '''
        # year_list = obj.files()

        lst = []
        for i in data:
            splt = i
            splitt = splt.split('_')
            lst.append(int(splitt[2]))
        lst = list(set(lst))

        return lst

obj = read_data()
a = obj.run_commandline()


file = obj.years_to_process(a[2])
obj.read_files(a[0],a[2])
var1 = obj.generate_anual_report(obj.yearly_data, file)
if a[1] == 1:
    obj.yearly_weather(var1)
elif a[1] == 2:
    obj.yearly_hottest_days(var1)





