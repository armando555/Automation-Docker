import os
from decouple import config
import subprocess

API_USERNAME = config('USERNAMEP')
API_URL = config('URL')
API_PASSWORD = config('PASSWORD')

class Parse:
    def parse(self, result_folder, jtl_path):
        res = os.system("psl-perfexp version")
        res1 = subprocess.check_output("psl-perfexp parse --results-dir "+result_folder+" jtl "+jtl_path, shell=True)
        return res1
    def login(self):
        print(API_URL+"\n"+API_USERNAME+"\n"+API_PASSWORD)
        configuration = "psl-perfexp configure -url "+API_URL+" -usr "+API_USERNAME+" -pass "+API_PASSWORD
        res2 = subprocess.check_output(configuration, shell=True)
        #res2 = subprocess.Popen(["psl-perfexp", "configure", "-url", API_URL, "-usr", API_USERNAME, "-pass", API_PASSWORD])
        #res2.wait()
        #print(res2)
        result = subprocess.check_output("psl-perfexp login", shell=True)
        #print(result)
        #res3 = os.system("psl-perfexp login")
        return result
    def send(self, test_info_path:str, results_path:str):
        res4 = subprocess.check_output("psl-perfexp send jmeter complete -inf "+test_info_path+" "+results_path, shell=True)
        return res4
