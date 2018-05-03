import scrapy

def transpose(l):
    return list(map(list, zip(*l)))

class Q2Spider(scrapy.Spider): 
    name = "q2"
    # start_urls = [ "http://www.cse.ust.hk/~raywong/temp/SimpleWebpage.html" ]

    def __init__(self, target_url="", *args, **kwargs):
        super(Q2Spider, self).__init__(*args, **kwargs)
        self.start_urls = [target_url]

    def parse(self, response):
        yield self.obtainStudentList(response) 
        # yield self.storeToMongoDB(response, student_list)

    def obtainStudentList(self, response):
        student_list = []
        for i in range(1,6):
            student_list.append(response.xpath("//tr/td["+str(i)+"]/text()").extract())
            
        student_list = transpose(student_list)

        with open("q2_tmp_student_list.txt", "w") as f:
            for student in student_list:
                f.write(",".join(student))
                f.write("\n")
