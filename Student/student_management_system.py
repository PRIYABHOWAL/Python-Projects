import psycopg2
#password goes here
password = ""
connection = psycopg2.connect(user= "postgres",password= password,database= "student")
cursor = connection.cursor()
try:
    
    i=1
    table_name=input("ENTER THE NAME OF TABLE")
    column_no=int(input("ENTER THE NO OF COLUMNS IN TABLE"))
except:
    print("INVALID INPUT")
def create(cursor,connection,column_no,table_name):
    try:
        cursor.execute(f'CREATE TABLE {table_name} ();')
        connection.commit()
        i=1
        for i in range(1,column_no+1):
            column_name=input("ENTER THE NAME OF NO"+" "+str(i)+" "+"COLUMN IN TABLE")
            column_data_type=input("ENTER THE DATA TYPE OF NO"+" "+str(i)+" "+"COLUMN IN NO TABLE" ) 
            cursor.execute(f'''ALTER TABLE {table_name}
                    ADD {column_name} {column_data_type} NOT NULL;''')
            connection.commit()
            print("Table created successfully in PostgreSQL ")
    except:
        print("INVALID")    
def insert(cursor,connection):
    while True:
            try:
                which_table=input(" ENTER THE NAME OF TABLE IN WHICH U WANT TO INSERT ")
                cursor.execute(f'''SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{which_table}';''')
                connection.commit()
                data=cursor.fetchall()
                columns=[]
                col_data_type=[]
                for i in range(len(data)):
                    columns.append(data[i][3])
                    col_data_type.append(data[i][7])
                rows=[]
                for i in range(len(columns)):
                    inputs=input(f'ENTER VALUE OF {columns[i]}')
                    if(col_data_type[i]=='integer'):
                        rows.append(f'{inputs}')
                    else:
                        rows.append(f"\'{inputs}\'")
                record=','.join(columns)
                values=','.join(rows)
                cursor.execute(f'''INSERT INTO {which_table} ({record}) VALUES ({values});''')
                connection.commit()
                break
            except:
                print("INVALID")
def display(cursor,connection):
    while True:
        try:
            which_table=input(" ENTER THE NAME OF TABLE IN WHICH U WANT TO SEE ")
            cursor.execute(f'''SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{which_table}';''')
            connection.commit()
            data=cursor.fetchall()
            print("************************************")
            for i in range(len(data)):
                print(data[i][3].ljust(10,' '),end='')
            print("\n************************************")
            cursor.execute(f'''SELECT * FROM {which_table};''')
            connection.commit()
            record=cursor.fetchall()
            for i in record:
                for j in i:
                    print(str(j).ljust(10,' '),end='')
            print("\n************************************")
            break
        except:
            print("INVALID")
def delete(cursor,connection):
    while True:
        try:
            which_table=input(" ENTER THE NAME OF TABLE IN WHICH U WANT TO DELETE ")
            cursor.execute(f'''SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{which_table}';''')
            connection.commit()
            data=cursor.fetchall()
            for i in range(len(data)):
                print(f" PRESS {i} TO DELETE BY {data[i][3]}")
            a=int(input("ENTER YOUR OPERATION"))
            value=input("ENTER VALUE TO DELETE")
            cursor.execute(f'''DELETE FROM {which_table} WHERE {data[a][3]}='{value}';''')
            connection.commit()
            print("row deleted")
            break
        except:
            print("INVALID")
def search(cursor,connection):
    while True:
        try:
            which_table=input(" ENTER THE NAME OF TABLE IN WHICH U WANT TO SEARCH ")
            cursor.execute(f'''SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{which_table}';''')
            connection.commit()
            data=cursor.fetchall()
            
            for i in range(len(data)):
                print(f" PRESS {i} TO SEARCH BY {data[i][3]}")
            a=int(input("enter your operation"))
            value=input("ENTER VALUE TO SEARCH")
            cursor.execute(f'''SELECT * FROM {which_table} WHERE {data[a][3]}='{value}';''')
            connection.commit()
            print("row searched")
            record=cursor.fetchall()
            print("\n************************************")
            for i in record:
                for j in i:
                    print(str(j).ljust(10,' '),end=' ')
            print("\n************************************")
            break
        except:
            print('Invalid!')
print("*************************************")
print("Welecome To Student Management System")
print("*************************************")
while True:
    x = int(input('Enter your choice: \n 1. Create Table \n 2. Display \n 3. Insert \n 4. Search \n 5. Delete \n 6. Exit \n :'))
    if x == 1:
        create(cursor,connection,column_no,table_name)
    elif (x==2):
        display(cursor,connection)
    elif (x==3):
        insert(cursor,connection)
    elif (x==4):
        search(cursor,connection)
    elif (x==5):
        delete(cursor,connection)
    elif (x==6):
        exit


    