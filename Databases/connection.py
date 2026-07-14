import psycopg2

con = psycopg2.connect(dbname="studentdb",user="postgres",password="admin123",host="localhost",port="5432")
print(con)