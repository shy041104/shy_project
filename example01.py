import  pymysql
def main():
    colid=int(input("Enter colid number: "))
    colwebsite=input("Enter colwebsite: ")
    conn = pymysql.connect(host='192.168.221.70',port=3306,user='root',passwd='SSShyu1104.',db='sys',charset='utf8')
    try:
        with conn.cursor() as cursor:
            result=cursor.execute('update shy_college set colwebsite=%s where colid=%s',(colwebsite,colid))
            if result==1:
                print("添加成功")
            conn.commit()
    except Exception as error:
        print(error)
        conn.rollback()
    finally:
        conn.close()
    print(conn)
if __name__ == '__main__':
    main()