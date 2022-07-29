from TestInfoJson import TestInfoJson
from jtl import Parse
from decouple import config
from jmeter import Jmeter


PROJECT_NAME = config('PROJECT_NAME')
APP_NAME = config("APP_NAME")
TRANSACTION_NAME = config("TRANS_NAME")
JOB = config("JOB")
BUILD = config("BUILD")
VERSION = config("VERSION")
TEST_PLAN = config("TEST_PLAN")
TAG = config("TAG")
THREADS = config("THREADS")
ENDPOINT = config("ENDPOINT")
URL2 = config("URL2")
PORT = config("PORT")
RAMPUP = config("RAMPUP")
DURATION = config("DURATION")
TIME = config("TIME")
JTL_FILE = config('JTL_FILE')
JMX_FILE = config("JMX_FILE")
TEST = config("TEST")
SHUTDOWN = config("SHUTDOWN")
INITIAL = config("INITIAL")



def main():
    #GET DATA FROM COMMAND LINE
    print(ENDPOINT)
    data = Jmeter.get_data_from_cmd(Jmeter)
    print("GETTING DATA FROM CMD")
    #if(len(data) != 10):
    #    exit()
    #LAUNCH SCRIPT JMX with Jmeter
    url = URL2
    port = PORT
    threads = THREADS
    rampup = RAMPUP
    endpoint = ENDPOINT
    duration = DURATION
    time_wait = TIME
    name_file_jtl = JTL_FILE
    name_file_jmx = JMX_FILE
    shutdown = SHUTDOWN
    initial = INITIAL
    if(TEST == "stress_all" and ENDPOINT== "all"):
        jmeter = Jmeter.run_script_jmx(Jmeter,url,port,threads,rampup,endpoint,duration,time_wait,name_file_jtl,"AllEndPoints.jmx",shutdown,initial)

    elif ( ENDPOINT == "add" or ENDPOINT == "subtract" or ENDPOINT == "multiply" or ENDPOINT == "divide" ) and TEST == "stress_one":
        jmeter = Jmeter.run_script_jmx(Jmeter,url,port,threads,rampup,endpoint,duration,time_wait,name_file_jtl,"Automation.jmx",shutdown,initial)

    elif (TEST == "peak_all" and ENDPOINT == "all"):
        jmeter = Jmeter.run_script_jmx(Jmeter,url,port,threads,rampup,endpoint,duration,time_wait,name_file_jtl,"peak_load_test.jmx",shutdown,initial)

    elif ( ENDPOINT == "add" or ENDPOINT == "subtract" or ENDPOINT == "multiply" or ENDPOINT == "divide" ) and TEST == "peak_one":
        jmeter = Jmeter.run_script_jmx(Jmeter,url,port,threads,rampup,endpoint,duration,time_wait,name_file_jtl,"peak_one_endpoint.jmx",shutdown,initial)

    elif ( ENDPOINT == "add" or ENDPOINT == "subtract" or ENDPOINT == "multiply" or ENDPOINT == "divide" ) and TEST == "spike_one":
        jmeter = Jmeter.run_script_jmx(Jmeter,url,port,threads,rampup,endpoint,duration,time_wait,name_file_jtl,"spike_one_test.jmx",shutdown,initial)
    
    elif (TEST == "spike_all" and ENDPOINT == "all"):
        jmeter = Jmeter.run_script_jmx(Jmeter,url,port,threads,rampup,endpoint,duration,time_wait,name_file_jtl,"spike_all_test.jmx",shutdown,initial)

    if( "Error" in jmeter.decode() or "error" in jmeter.decode()):
        resultb = False
        print("\n\nThere is an error in JMX\n----------------------------------------------------------------------------------------------------------------------------\n "+jmeter.decode()+"\n----------------------------------------------------------------------------------------------------------------------------")
        exit()
    else:
        print("\n\nJMX EXECUTION successful\n----------------------------------------------------------------------------------------------------------------------------\n  "+jmeter.decode()+"\n----------------------------------------------------------------------------------------------------------------------------")
    
    #PARSE RESULTS
    results = Parse.parse(Parse, "./results", "./jtl/"+name_file_jtl+".jtl")
    resultb = True
    if "Error" in results.decode() or "error" in results.decode():
        resultb = False
        print("\n\nThere is an error in PARSE\n----------------------------------------------------------------------------------------------------------------------------\n "+results.decode()+"\n----------------------------------------------------------------------------------------------------------------------------")
    else:
        print("\n\nParsed successful\n----------------------------------------------------------------------------------------------------------------------------\n  "+results.decode()+"\n----------------------------------------------------------------------------------------------------------------------------")
    
    #Login to the Perfomance explorer
    login = Parse.login(Parse)
    loginb = True
    if ("Error" in login.decode() or "error" in login.decode()) and resultb:
        print("\n\nThere is an error in LOGIN\n----------------------------------------------------------------------------------------------------------------------------\n "+login.decode()+"\n----------------------------------------------------------------------------------------------------------------------------")
    else:
        loginb = False
        print("\n\nLogin successful\n----------------------------------------------------------------------------------------------------------------------------\n  "+login.decode()+"\n----------------------------------------------------------------------------------------------------------------------------")
    
    #JSON FILE GENERATION
    instance = TestInfoJson.load_data_source(TestInfoJson,"json",PROJECT_NAME,APP_NAME,TRANSACTION_NAME,
                            JOB,BUILD,VERSION,TEST_PLAN,TAG,THREADS,"./results/")
    print("Builded TestInfoJson")

    #Send data to the Perfomance explorer
    send = Parse.send(Parse,"./results/testInfo.json","./results/")
    sendb = True
    if ("Error" in send.decode() or "error" in send.decode()) and loginb:
        sendb = False
        print("\n\nThere is an error in SEND\n----------------------------------------------------------------------------------------------------------------------------\n "+login.decode()+"\n----------------------------------------------------------------------------------------------------------------------------")
    else:
        print("\n\nSent successful\n----------------------------------------------------------------------------------------------------------------------------\n  "+login.decode()+"\n----------------------------------------------------------------------------------------------------------------------------")
    
    

if __name__ == "__main__":
    main()