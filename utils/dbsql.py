"""
操作数据库类
"""

import cx_Oracle as oracle
import pymysql as mysql

from utils.config import Config

"""
操作数据库步骤：
1.连接数据库，通过connect函数连接，并且生成一个数据库的connection对象
2.定义游标，cursor,通过游标执行脚本并且获取结果数据
3.关闭连接
"""

def execute_sql(sql, params):
    if Config().get_key('db', 'dbtype') =='oracle':
        # 1. 连接oracle
        # oracle数据库信息 oraclehost，oracleport，oraclesid
        db_session = 'oracle'
        dns_tns = oracle.makedsn(Config().get_key(db_session, 'oraclehost'), Config().get_key(db_session, 'oracleport'),
                                 Config().get_key(db_session, 'oraclesid'))
        conn = oracle.connect(user=Config().get_key(db_session, 'oracleuser'),
                              password=Config().get_key(db_session, 'oraclepassword'), dsn=dns_tns)
    else:
        # 1.连接mysql
        conn = mysql.connect(host="10.0.62.43", user="root",
                             password='root',
                             db='mdm_std_output', port=3306, use_unicode=True, charset="utf8")
    '''
    connection对象常用方法:
    1.cursor()游标，使用游标操作数据库或者返回结果
    2.commit()提交，在数据库数据修改的时候，insert,update,delete需要commit
    3.rollback()回滚数据
    4.close()关闭当前连接
    '''
    # 2. 建立游标
    cursor = conn.cursor()
    '''
    cursor游标常用操作方法:
    1.excute()执行数据库命令，将结果传回给客户端
    2.fetchone() 获取结果集的下一行
    3.fetchall() 获取结果集的全部数据
    4.fetchmany()获取结果的多行数据，可以加参数指定多少行
    5.close() 关闭游标 rowcount() 显示脚本影响了多少行数据
    '''
    # 3. 执行脚本
    try:
        #执行sql语句
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        #如果这行的是select 需要获取全部结果集
        if sql.startswith('SELECT'):
            query_result = cursor.fetchall()
            # conn.commit()
            cursor.close()
            conn.close()
            return query_result
        else:
            #其他操作 insert，delete，update需要进行提交操作
            conn.commit()
            cursor.close()
            conn.close()
            return None
    except Exception as e:
        print(e.__str__())
        # log.error(f"数据库操作失败，错误原因：{e.__str__()}")



if __name__=="__main__":
    ##oracle测试 sql语句中参数使用：1，：2 传参时 使用params=(xxx,)
    sql_select = """SELECT USER_NAME FROM T_DRG_USER_INFO"""
    res_select = execute_sql(sql_select, params=None)
    print(res_select)
    sql_selectp= """SELECT USER_NAME FROM T_DRG_USER_INFO WHERE USER_TYPE=:1"""
    res_selectp = execute_sql(sql_selectp,params=('01',))
    print(res_selectp)

    # sql_update = "UPDATE T_DRG_USER_INFO SET USER_NAME='dsUPDATE' WHERE ACCOUNT_NO='ds'"
    # res_upt = execute_sql(sql_update, params=None)
    # print(res_upt)

    # sql_insert="INSERT INTO T_DRG_USER_ROLE(USR_ROLE_ID,USER_ID,ROLE_ID,CREATOR,CREATE_TIME) VALUES (:1,:2,:3,:4,:5)"
    # #将字符串转化为实践戳
    # time=datetime.datetime.strptime("2020-12-16 00:00:00", '%Y-%m-%d %H:%M:%S')
    # res_insert=execute_sql(sql_insert,params=(*(1,1,1,1,time),))

    # sql_del="""DELETE FROM T_DRG_USER_ROLE WHERE USER_ID= :1"""
    # res_del=execute_sql(sql_del,params=('1',))

    # ##mysql sql语句中参数使用%s 传参时 使用params=[xxx]
    # sql = """SELECT std_code,std_name,std_score FROM project_安徽医疗网 WHERE code=%s"""
    # std_value = execute_sql(sql, params=['11001800009',])
    # print(std_value)

