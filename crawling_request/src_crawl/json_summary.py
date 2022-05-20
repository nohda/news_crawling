# -*-coding:utf-8-*-
import json,os
import io
import codecs

json_load_data = []
def summary_count(file_name):
    global json_load_data
    try:
        with open(file_name) as st_json:
            json_file = json.load(st_json)
        
        if json_file["summary"] != "":
            json_load_data.append(json_file)
    except:
        print('Error: {}'.format(file_name),flush=True)

if __name__ == '__main__':

   # print(json.load(codecs.open(path, 'r', 'utf-8-sig'))['summary'])

#    path = "./result"
#    lis = os.listdir(path)
#    for file_name in lis:
#        summary_count(path+"/"+file_name)
#    with open("./nocut_news_summary.json", "w") as json_file:
#        json.dump(json_load_data, json_file, ensure_ascii=False,indent=4)
   
    #path = "./result"
    path = "./result_ba"
    lis = os.listdir(path)
    print(lis)
    for file_name in lis:
        summary_count(path+"/"+file_name)
    with open("./boan_news_summary.json", "w") as json_file:
        json.dump(json_load_data, json_file, ensure_ascii=False,indent=4)
