import argparse
import os
# path = 'weatherdata/'

class run_code:
    def commandline(self):
        '''
        This is a function, this is responsible to run command and get report number and directory path from users

        Return:
            it will return the 2 parameters through parser.parse_args()
            1: Path
            2: Directory path
        '''
        parser = argparse.ArgumentParser(
            description="Usage: weatherman -h [report#] [data_dir]",
            usage="Usage: weatherman [report#] [data_dir]")
        parser.add_argument('Report_Number', choices=[1,2], type=int, help='Report# should be 1 or 2')
        parser.add_argument('Path')
        return parser.parse_args()


    def files(self, args):
        '''
        This is a function, it will return the list of files name that are available in the directory

        Parameter:
            1: args: it is representing the command line input, from where we can get directory path.
            we will use this to read the files name from the directory path

        Return:
            it will return 1 variable
            1: files_name_list
        '''
        path = args.Path
        files_name_list = ''
        try:
            files_name_list = os.listdir(path)
        except FileNotFoundError:
            print(f"files are not available on this path {path} \nor the path is incorrect")

        return files_name_list
