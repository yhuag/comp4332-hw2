import os
import pymongo

def readTargetUrl():
    with open("link.txt") as f:
        lines = f.read().splitlines()
    return lines

def storeToMongoDB():
    # Load student list
    with open("hw2/q2_tmp_student_list.txt") as f:
        student_list = f.read().splitlines()
    student_list = [student.split(",") for student in student_list]

    # Question 2 [a.]
    configs = []
    with open("config-MongoDB.txt") as f:
        configs = f.read().splitlines()
    host = configs[0].rstrip()
    database_name = configs[1].rstrip()

    # Connect to MongoDB
    try:
        client = pymongo.MongoClient(host)
        db = client[database_name]

        # Question 2 [b.]
        for student in student_list:
            db.student.insert({
                "sid": student[0], 
                "sname": student[1], 
                "chemistry": int(student[2]),
                "history": int(student[3]), 
                "computer": int(student[4])
            })
        print("Inserting Data is Successful!")

        # Question 2 [c.]
        db.student.remove({"computer":{"$lt" : 50}})
        print("Deleting Documents is Successful!")

        # Question 2 [d.]
        ans = db.student.find({"chemistry":{"$gt" : 50}},{"_id":0}).sort([("sname",1)])
        ans = [x for x in ans]
        print("Obtaining Documents is Successful!")

        # Question 2 [e.]
        with open("output-MongoDB.txt", "w") as f:
            f.write(str(len(ans)) + "\n")
            for s in ans:
                f.write(s["sid"]+","+s["sname"]+","+str(s["chemistry"])+","+str(s["history"])+","+str(s["computer"]))
                f.write("\n")
        print("Writing Documents is Successful!")

        # Question 2 [f.]
        db.student.drop()
        print("Dropping Collection is Successful!")

        # Close the MongoDB
        client.close()

    except pymongo.errors.ConnectionFailure as error: print(error)

#### Main Execution
if __name__ == "__main__":
    target_url = readTargetUrl()[0]
    os.system('cd hw2/ && scrapy crawl q2 -a target_url="'+ target_url +'"')
    storeToMongoDB()