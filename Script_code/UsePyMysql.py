import pymysql

class UsePyMysql:

    def __init__(self,host,user,password,database):
        '''连接mysql数据库并创建游标'''
        self.db = pymysql.connect(host,user,password,database)
        self.cursor = self.db.cursor()

    def select_sql(self,sql):
        '''执行查询操作'''
        try:
            self.cursor.execute(sql)    # 执行SQL语句
            results = self.cursor.fetchall()    # 获取所有记录列表
            print(results)
            # for row in results:     # 打印结果
            #     fname = row[0]
            #     lname = row[1]
            #     age = row[2]
            #     sex = row[3]
            #     income = row[4]
            #     print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
            #           (fname, lname, age, sex, income))
        except Exception as e:
            print(e)

    def update_sql(self,sql):
        # SQL 更新语句
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except Exception as e:
            # 发生错误时回滚
            self.db.rollback()
            print(e)

    def __del__(self):
        # 关闭数据库连接
        self.db.close()

if __name__ == '__main__':
    usemysql = UsePyMysql('sister','study','study','study')
    usemysql.select_sql('use study')
    usemysql.select_sql('show tables')
    usemysql.select_sql("CREATE TABLE EMPLOYEE ( FIRST_NAME  CHAR(20) NOT NULL,LAST_NAME  CHAR(20),AGE INT,SEX CHAR(1),INCOME FLOAT)")
