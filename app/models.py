import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from .database.db_connection import get_db_connection










# # 用户类示例
# class User:
#
#     def __init__(self, username, password):
#         self.username = username
#         self.password = generate_password_hash(password)
#
#     def save_to_db(self):
#         # 使用 get_db_connection 函数来获取数据库连接
#         connection = get_db_connection()
#         cursor = connection.cursor()
#         try:
#             # 使用参数化查询来防止 SQL 注入
#             cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (self.username, self.password))
#             connection.commit()
#         except mysql.connector.Error as err:
#             # 处理可能发生的错误
#             print("An error occurred: {}".format(err))
#         finally:
#             cursor.close()
#             connection.close()

    # 其他方法...