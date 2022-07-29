import json
from testInfoInterfaces import ITestInfo

json_file = {}

class TestInfoJson(ITestInfo):
    
    def load_data_source(self, extension: str, project_name: str, app_name: str, transaction_name: str, 
                        job_name: str, build_number: str, version: str, test_name: str, tag: str, threads: str, path: str):
        #CREATING JSON STRUCTURE
        json_file["scn_project_name"] = project_name
        json_file["scn_application_name"] = app_name
        json_file["scn_transaction_name"] = transaction_name
        json_file["scn_job_name"] = job_name
        json_file["scn_build_number"] = build_number
        json_file["scn_version"] = version
        json_file["scn_test_name"] = test_name
        json_file["scn_tag"] = tag
        json_file["scn_threads"] = threads
        #creating file
        name = "testInfo."+extension
        with open(""+path+name,'w') as convert_file:
            convert_file.write(json.dumps(json_file))

    
