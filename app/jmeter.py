import sys
import os
import subprocess


class Jmeter:
    def get_data_from_cmd(self):
        argumments = sys.argv
        return argumments
    def run_script_jmx(self,url,port,threads,rampup,endpoint,duration,time_wait,name_file_jtl,name_file_jmx,shutdown,initial):
        configuration = "jmeter -n -t ./jmx/"+name_file_jmx+" -Jurl="+url+" -Jpuerto="+port+" -Jthreads="+threads+" -Jrampup="+rampup+" -Jendpoint="+endpoint+" -Jtime="+duration+" -JtimeWait="+time_wait+" -JpathSave=./jtl/"+name_file_jtl+".jtl -Jshutdown="+shutdown+" -Jinitial="+initial
        res = subprocess.check_output(configuration, shell=True)
        return res