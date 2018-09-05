from bs4 import BeautifulSoup

import requests

#url = input("Enter a website to extract the URL's from: ")

r  = requests.get("http://" + "catalog.unc.edu/courses/musc/")

data = r.text

soup = BeautifulSoup(data, "lxml")
html = ""
i = 0

# parse through individual pieces of the courseblocktitle string, such as course num
for link in soup.find_all("div", { "class" : "courseblock" }):
    
    courseBlock = link.find("p", { "class" : "courseblocktitle" })
    courseBlock = courseBlock.get_text()
    courseTuple = [x.strip() for x in courseBlock.split('.')]
    courseTuple[0] = courseTuple[0].replace(u'\xa0', u' ')
    # print(courseTuple)
    
    courseDesc = link.find("p", { "class" : "courseblockdesc" })
    courseDesc = courseDesc.get_text()
    
    #format html table
    html += """    
    <tr data-toggle="collapse" data-target="#course_""" + str(i) + """" class="accordion-toggle music-course">
      <th scope="row">""" + courseTuple[0] + """</th>
      <td>""" + courseTuple[1] + """</td>
      <td>""" + courseTuple[2] + """</td>
    </tr>
    <tr>
        <td colspan="6" class="hiddenRow">
            <div class="accordion-body collapse" id="course_""" + str(i) + """">""" + courseDesc + """</div>
        </td>
    </tr>
    """
    
    i += 1
    
with open("index.html", "w") as file:
    file.write(html)
