# -*-coding:utf-8-*-
import json
import os
import io
import codecs

abs = "/home/sia0940/crawling_daily/"

def summary_count(file_name):
    summary_data = []
    try:
        with open(file_name) as st_json:
            json_file = json.load(st_json)
            for i in json_file:
                if i["summary"] != "":
                    summary_data.append(i)
                summary_data.append(i)
    except:
        print('Error: {}'.format(file_name), flush=True)
    return summary_data


def write_summary(path, dir):
    print("\n")
    data = []
    result = []

    lis = os.listdir(path)
    print("total news  :", len(lis))
    for file_name in lis:
        data = summary_count(path+"/"+file_name)
        for tmp in data:
            result.append(tmp)
        print(file_name, len(data))
    with open(dir, "w") as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)

    return len(result)


def newsis():
    global abs
    path = abs+"result/newsis"
    dir = abs+"summary/summary_newsis.json"
    count = write_summary(path, dir)
    print("newsis summary :", count)
    return count


def nocut():
    global abs
    path = abs + "result/nocut_news"
    dir = abs+"summary/summary_nocut.json"
    count = write_summary(path, dir)
    print("nocut summary :", count)
    return count


def boan():
    global abs
    path = abs + "result/boan_news"
    dir = abs+"summary/summary_boan.json"
    count = write_summary(path, dir)
    print("boan summary :", count)
    return count


def khan():
    global abs
    path = abs + "result/khan"
    dir = abs+"summary/summary_khan.json"
    count = write_summary(path, dir)
    print("khan summary :", count)
    return count    


def herald():
    global abs
    path = abs + "result/herald"
    dir = abs+"summary/summary_herald.json"
    count = write_summary(path, dir)
    print("herald summary :", count)
    return count

def main():
    try:
        total = 0
        total += newsis()
        total += nocut()
        total += boan()
        total += khan()
        total += herald()
        print("\nAll news : ",total)
		
    except:
        print("Main error occured.")
        
if __name__ == '__main__':
    main()
