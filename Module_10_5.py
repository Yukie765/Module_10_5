import multiprocessing
import time
from datetime import datetime
from multiprocessing import Pool

files_names = ["file 1.txt","file 2.txt","file 3.txt","file 4.txt" ]

def read_info(name):
    all_data = []
    with open(name, 'r',encoding='utf-8',) as file:
        for line in file:
            if line == "":
                break
            all_data.append(line)

# start_time = datetime.now()
# for i in  range(len(files_names)):
#     read_info(files_names[i])
# end_time = datetime.now()
# print(end_time-start_time)


if __name__ == '__main__':
    start_time = datetime.now()
    pool = Pool()
    pool.map(read_info, files_names)
    end_time = datetime.now()
    print(end_time-start_time)
