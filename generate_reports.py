
class reports:
    # def years_to_process(self, files_name_list):
    #     '''
    #     This ia a function, taking all files name in parameter that are available in directory, splitting them to get the years and converting them into the set to avoid duplication and converting them agin into list
    #     :param files_name_list: a list of files name in the directory
    #     :return: a list of years without duplicates
    #     '''
    #     lst = []
    #     for i in files_name_list:
    #         splt = i
    #         splitt = splt.split('_')
    #         lst.append(int(splitt[2]))
    #     lst = list(set(lst))
    #     return lst


    def generate_anual_report(self, yearly_data,years_list ):
        year = 1996
        yearly_report = []
        # years_list = self.years_to_process(yearly_data)

        for year in years_list:
            idx = {
                'max_temprature' : 0,
                'min_temprature' : 100,
                'max_humidity' : -100,
                'min_humidity' : 100,
                'date' : '',
                'year' :''
            }

            for report in yearly_data:
                if report['year'] == year:
                    if report['max_temp'] != '' and type(report['max_temp']) == int:
                        if idx['max_temprature'] < report['max_temp']:
                            idx['max_temprature'] = report['max_temp']
                            idx['date'] = report['date']
                            idx['year'] = report['year']

                    if report['min_temp'] != '' and type(report['max_temp']) == int:
                        if idx['min_temprature'] > report['min_temp']:
                            idx['min_temprature'] = report['min_temp']
                    if report['max_humidity'] != '':
                        if idx['max_humidity'] < report['max_humidity']:
                            idx['max_humidity'] = report['max_humidity']
                    if report['min_humidity'] != '':
                        if idx['min_humidity'] > report['min_humidity']:
                            idx['min_humidity'] = report['min_humidity']
            yearly_report.append(idx)
        return yearly_report




    def yearly_weather(self, data):
        print('Year\t MAX Temp\t MIN Temp\t MAX Humidity\t MIN Humidity\n---------------------------------------------------------------------')
        for i in data:
            print(i['year'], '\t', i['max_temprature'], '\t\t', i['min_temprature'], '\t\t', i['max_humidity'], '\t\t', i['min_humidity'])

    def yearly_hottest_days(self, data):
        print('Year\t Date\t\tTemp\n----------------------------')
        for i in data:
            print(i['year'],'\t',i['date'],'\t',i['max_temprature'])


