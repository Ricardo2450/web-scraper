"""
from bs4 import BeautifulSoup


def parse(markup):

    soup = BeautifulSoup(markup, "html.parser")

    courses = soup.select(".calendar-event")

    course_info = "Course Info\n\n"

    for course in courses:
        #if "Python" in course.h1.text: # this is needed at the moment because of the "invisible" text coming through
            course_info += course.h1.text + "\n"
            course_info += course.h2.text + "\n"
            course_info += "\n"

    return course_info







def parse(markup)

soup = BeautifulSoup(markup, "html.parser")
#print(soup.find("h1"))

courses = soup.select(".calendar-event")
#print(courses)

course_info = "Course Info\n"

#for course in courses:
    #print(course.prettify())
    #print()
    #print()
    #print(course.h1.text)
    #print(course.h2.text)

for course in courses:
    if "Python" in course.h1.text: # this is needed at the moment because of the "invisible" text coming through
        course_info += course.h1.text + "\n"
        course_info += course.h1.text + "\n"
        course_info += "\n"

return course_info

        print(course.h1.text)
        print(course.h2.text)
"""
