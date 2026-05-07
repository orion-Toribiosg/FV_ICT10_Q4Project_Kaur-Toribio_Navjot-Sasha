from pyscript import document, display
import numpy as np
import matplotlib.pyplot as plt
from pyscript import display, HTML 


# PAGE 1 CODE START #

class Classmate: #this part is the basis for the entire code as it contains the attributes that are necessary for showing the list of previous classmates/inputted classmates
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject
    def introduce(self): #code for the sentence in the showing list
        return f"My name is {self.name}! I am from Grade 10-{self.section}, and my favorite subject is {self.favorite_subject}."

classmates = [ #existing students for showing the list
    Classmate("Navjot Kaur", "Sapphire", "Math"), 
    Classmate("Kelsey Tolentino", "Sapphire", "English"), 
    Classmate("Liam Lopez", "Sapphire", "Music"), 
    Classmate("Lorenzo Calida", "Sapphire", "Filipino"), 
    Classmate("Izeck Reynoso", "Sapphire", "Social Studies") 
    ]

def add_classmate(event):#this def is for adding classmates #code below is for the input boxes
    if not document.getElementById("name"):
        return
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("favorite_subject").value
    if name and section and subject:
        classmates.append(
            Classmate(name, section, subject)
        )
        document.getElementById("output1").innerHTML = (
            "Classmate added!"
        )
def list_classmates(event):
    if not document.getElementById("output1"):
        return
    document.getElementById("output1").innerHTML = ""
    for person in classmates:
        display(
            person.introduce(),
            target="output1",
            append=True
        )


# PAGE 2 START CODE #

days = []
absences = []
#code for graph appearing and making
def display_graph(event):
    if not document.getElementById("dayOfTheWeek"):
        return
    day = document.getElementById("dayOfTheWeek").value
    absence = int(document.getElementById("absences").value)
    document.getElementById("output2").innerHTML = "" #so that graph updates instead of repeats


    days.append(day)
    absences.append(absence)
    plt.clf()
    plt.plot(days, absences, marker="o")
    plt.title("Number of Absences per Day")
    display(plt.gcf(), target="output2")    

# PAGE 3 START CODE #

projects = [
    {"title": "Arnold Janssen Kalinga Foundation", "description": "An outreach activity where OBMC students support the Arnold Jassen Kalinga Foundation through donations and volunteer work to help communities in need.", "image": "Picture1.jpeg"},
    {"title": "Public Poetry Festival", "description": "Students showcase their creativity and confidence by performing and reciting original or chosen poems in front of an audience.", "image": "Picture2.jpeg"},
    {"title": "President's Day", "description": "A school celebration honoring leadership and student government.", "image": "Picture3.png"},
    {"title": "River Cleanup", "description": "A community service activity where students help clean local rivers to promote environmental awareness and responsibility.", "image": "Picture4.jpeg"},
    {"title": "Halloween Party", "description": "A fun school celebration where students dress up in costumes inspired by a K-pop hunters theme and enjoy performances.", "image": "Picture5.jpeg"},
    {"title": "INTRAMURALS 2025-2026", "description": "A school-wide sports event where students compete in different athletic games to build teamwork, school spirit, and sportsmanship.", "image": "Picture6.png"}
]

def render_gallery():
    if not document.getElementById("gallery-container"):
        return
    html_content = ""
    for item in projects:
        html_content += f"""
        <div class="card">
            <img src="{item['image']}">
            <div class="card-body">
                <h3>{item['title']}</h3>
                <p>{item['description']}</p>
            </div>
        </div>
        """
    # Wrap the content in HTML() so it renders as elements
    display(HTML(html_content), target="gallery-container", append=False)

render_gallery()