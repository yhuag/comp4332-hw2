## MySQL
import mysql.connector

def obtainStudentList():
    L = []
    with open("student.txt") as f:
        lines = f.read().splitlines()
        for line in lines[1:]:
            L.append(line.split(","))
    return L

def storeToMySQL(_studentList):
    # Question 2 [a.]
    [username, password, ip_address, database_name] = readMySQLConfigs()

    try:
        client = connectToMySQL(username, password, ip_address, database_name)
        cursor = client.cursor()

        # Question 2 [b.]
        createTableMySQL(cursor)

        # Question 2 [c.]
        insertDataMySQL(cursor, _studentList)

        # Question 2 [d.]
        deleteDataMySQL(cursor)

        # Question 2 [e.]
        ans = obtainDataMySQL(cursor)

        # Question 2 [f.]
        writeToFile(ans, "output-MySQL.txt")

        # Question 2 [g.]
        dropTableMySQL(cursor)


        client.commit()
        cursor.close()
        client.close()
    except mysql.connector.Error as error: print(error)


#### Helper Functions ####
def connectToMySQL(_user, _password, _host, _database):
    client = mysql.connector.connect(
        user=_user, 
        password=_password, 
        host=_host, 
        database=_database)
    return client

def readMySQLConfigs():
    configs = []
    with open("config-MySQL.txt") as f:
        configs = f.read().splitlines()
    return configs

def createTableMySQL(cursor):
    stringSQL = "create table student (sid char(4), sname varchar(200), chemistry int, history int, computer int, primary key (sid))" 
    cursor.execute(stringSQL)
    print("Creating Table is Successful!")

def insertDataMySQL(cursor, studentList):
    for student in studentList:
        stringSQL = "insert into student values ('" + str(student[0]) + "', '" + str(student[1]) + "', " + student[2] + ", " + student[3] + ", " + student[4] + ")" 
        cursor.execute(stringSQL)
    print("Inserting Data is Successful!")

def deleteDataMySQL(cursor):
    stringSQL = "delete from student where computer < 50" 
    cursor.execute(stringSQL)
    print("Deleting Records is Successful!")

def obtainDataMySQL(cursor):
    stringSQL = "select * from student where chemistry > 50 order by sname" 
    cursor.execute(stringSQL)
    ans = [list(student) for student in cursor]
    print("Obtaining Records is Successful!")
    return ans

def writeToFile(_dataList, _fileName):
    with open(_fileName, 'w') as f:
        f.write(str(len(_dataList)) + "\n")
        for data in _dataList:
            f.write(",".join(castToStrs(data)) + "\n")
    print("Writing Records is Successful!")

def castToStrs(_data):
    return [str(x) for x in _data]

def dropTableMySQL(cursor):
    stringSQL = "drop table if exists student" 
    cursor.execute(stringSQL)
    print("Dropping Table is Successful!")



#### Start of main execution ####
if __name__ == "__main__":
    studentList = obtainStudentList()
    storeToMySQL(studentList)