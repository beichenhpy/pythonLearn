import pymysql
import demo
import traceback

image_path = '2.jpg'
number=demo.get_license_plate(image_path)
print(number)
# 打开数据库连接
db=pymysql.connect("207.148.104.108","root","123456","car")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO carinfo (carnumber) VALUES (\"%s\")"%(str(number))


try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except Exception:
    traceback.print_exc()# 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()

















