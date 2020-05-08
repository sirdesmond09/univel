#working with sql

import pymysql.cursors

connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '',
                             db = 'chalky',
                             charset = 'utf8',
                             cursorclass = pymysql.cursors.DictCursor)

with connection.cursor() as cursor:


    # file = open("global_results.csv", "r")

    # datas = file.readlines()
    # datas.pop(0)
    # for data in datas:
    #     _list = data.split(',')
    #     date = _list[0]
    #     temp = _list[1]

    #     # print(f"date = {date}\ntemp = {temp}" )
    #     sql = f"INSERT INTO temp_table (temp, date) VALUES ({temp}, {date})"
    


    fetch ="SELECT temp FROM temp_table WHERE temp < 20"
    cursor.execute(fetch)
    many = cursor.fetchmany(10)
    print(many)
    # connection.commit()
