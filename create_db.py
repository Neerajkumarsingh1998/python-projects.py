import pymysql
def create_db():
    con = pymysql.connect(host="localhost", user="root", password="Neeraj@123", database="employee")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS COURSE(cid INTEGER PRIMARY KEY AUTO_INCREMENT,name text,duration text,charges text,description text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTO_INCREMENT,name text,email text,gender text,dob text,contact text,admission text,course text,state text,city text,pin text,address text  )")
    con.commit()
    cur.execute( "CREATE TABLE IF NOT EXISTS result(cid INTEGER PRIMARY KEY AUTO_INCREMENT,roll text,name text,course text,marks_ob text,full_marks text,per text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS students(cid INTEGER PRIMARY KEY AUTO_INCREMENT,fname text, lname text, contact text, email text, quection text, answer text, password text)")
    con.commit()



    con.close()

create_db()
