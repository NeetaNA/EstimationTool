import os,ConfReader


class CommonFunctions():

    def __init__(self):
        pass

    def get_value_from_conf_file(self,conf_file_name,key):
        # Get the credentials file
        conf_file = os.path.join(os.path.dirname(__file__),conf_file_name)
        # Get value for the given key from credentials file
        return ConfReader.get_value(conf_file,key)