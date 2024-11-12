from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy
spacy.load('en_core_web_sm')
# from spacy.lang.en import English
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('<b>VTOP BOT</b>')

# nlp = spacy.load("en_core_web_sm")

chatbot = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Hi there, Welcome to VTOP! 👋 If you need any assistance, I'm always here.Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br><br>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///db.sqlite3'   
) 
trainer = ListTrainer(chatbot)

# python app.py
# Training with Personal Ques & Ans 

conversation = [
"Hi",
"Helloo!",
"Hey",

"How are you?",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> Student's Section Enquiry.</br>Faculty Section Enquiry. </br>Parent's Section Enquiry.</br>Visitor's Section Enquiry.</br>",

"Great",
"Go ahead and write the number of any query. 😃✨ <br> Student's Section Enquiry.</br>Faculty Section Enquiry. </br>Parent's Section Enquiry.</br>Visitor's Section Enquiry.</br>",

"good",
"Go ahead and write the number of any query. 😃✨ <br> Student's Section Enquiry.</br> Faculty Section Enquiry. </br>Parent's Section Enquiry.</br>Visitor's Section Enquiry.</br>",

"fine",
"Go ahead and write the number of any query. 😃✨ <br> Student's Section Enquiry.</br> Faculty Section Enquiry. </br>Parent's Section Enquiry.</br>Visitor's Section Enquiry.</br>",

"Thank You",
"Your Welcome 😄",

"Thanks",
"Your Welcome 😄",

"Bye",
"Thank You for visiting!..",

"What do you do?",
"I am made to give Information about VTOP Vellore. ",


"What else can you do?",
"I can help you know more about VTOP",
    
    "student",
    "<b>STUDENT <br>The following are frequently searched terms related to student . Please select one from the options below : <br> <br> Curriculars <br>Extra-Curriculars<br> Administrative<br> Examination <br> Placements </b>",
    
    "curricular",
    "<b> CURRICULAR <br>  These are the top results: <br> <br> Academic Calendar <br>Library </b>",
    
    "academic calender",
    "<b >Academic Calender<br>The link to Academic Calender👉<a href=" 'https://vit.ac.in/wp-content/uploads/2024/08/Academic-Calendar-for-Winter-Semester-2024-25.pdf' " target="'blank'">Click Here</a> </b>",
    "library",
    "<b>Moodle<br>The link to Moddle 👉 <a href='http://www.google.com/file:///C:/Users/Lenovo/OneDrive/Desktop/webpage/moddle.html' target='_blank'>Click Here</a></b>",

    "extra curriculars",
    "<b>EXTRA-CURRICULAR<br>These are the top results: <br> <br>Events<br>Student Chapters <br>Student's Council</b>",
    "events",
    "<b > Events<br>The link to Events👉 <a href=" 'https://vit.ac.in/campus-category/campus-events' " target="'blank'">Click Here</a></b>",
    "student chapters",
    "<b > Student Chapters<br>The link to Student Chapters👉<a href=" 'https://vit.ac.in/campus-category/chapters' " target="'blank'">Click Here</a> </b>",
    "student council",
    "<b >Student's Council <br>The link to Student's Council👉 <a href=" 'https://vit.ac.in/campus-category/student-council' " target="'blank'">Click Here</a> </b>",

    "administrative",
    "<b>ADMINISTRATIVE<br>These are the top results: <br> <br> Students Portal<br> Newsletter </b>",
    "student portal",
    "<b>Students Portal<br>The link to Students Portal👉 <a href=" 'https://vtop.vit.ac.in/vtop/login' " target="'blank'">Click Here</a> </b>",
    "newsletter",
    "<b>Newsletter<br>The link to Notices👉 <a href=" 'https://vit.ac.in/newsletter-score' " target="'blank'">Click Here</a> </b>",

    "examination",
    "<b > EXAMINATION <br>These are the top results:<br> Exam Notices<br> Examination Process  </b>",
    "exam notices",
    "<b > Exam Notices<br>The link to Notices👉 <a href=" 'https://vit.ac.in/' " target="'blank'">Click Here</a> </b>",
    "examination process",
    "<b >Examination Process<br>The link to Examination Process👉<a href=" 'https://vit.ac.in/academics/coe' " target="'blank'">Click Here</a> </b>",
    
    "placement",
    "<b > PLACEMENTS These are the top results:<br> Overview <br> Our Recruiters <br> Placement Statistics </b>",
    "overview",
    "<b> Overview<br>The link to Placements👉 <a href=" 'https://vit.ac.in/cdc-overview' " target="'blank'">Click Here</a> </b>",
    "our recruiter",
    "<b> Our Recruiters Contact us<br>The link to Contact👉<a href=" 'https://vit.ac.in/cdc-contact-us' " target="'blank'">Click Here</a> </b>",
    "placement statistics",
    "<b > Placement Tracker<br>The link to Placement tracker👉 <a href=" 'https://vit.ac.in/cdc-tracker' " target="'blank'">Click Here</a> </b>",

    "faculty",
    "<b >FACULTY<br>The following are frequently searched terms related to faculty. Please select one from the options below :</br></br> Portals<br> Change Personal Details </b>",
    
    "portals",
    "<b > PORTALS These are the top results:<br> Biometric Attendance System <br> Moodle </b>",
    "biometric",
    "<b> Biometric Attendance<br>The link to Biometric Attendance👉<a href=" 'https://vtop.vit.ac.in/vtop/login' " target="'blank'">Click Here</a> </b>",
    "moodle",
    "<b> Moodle<br>The link to Moodle👉<a href="'https://moovit.vit.ac.in/login/index.php'" target="'blank'">Click Here</a> </b>",

    "change personal detail",
    "<b > CHANGE PERSONAL DETAILS These are the top results:<br> <br>Site Login <br> </b>",
    "site login",
    "<b>Site Login<br>The link to Site Login👉<a href=" 'https://vtop.vit.ac.in/vtop/login' " target="'blank'">Click Here</a> </b>",
   
    "parent",
    "<b> PARENTS <br>The following are frequently searched terms related to Parents. Please select one from the options below : <br> <br> About Us <br> Notices <br> Fee Payment <br> Placements </b> " ,

    "about us",
    "<b > ABOUT US<br>These are the top results:<br> <br> About Vit <br> Director's <br> About Contact us </b>",
    "about vit",
    "<b >About vit<br>The link to About Vit👉 <a href=" 'https://vit.ac.in/about-vit' " target="'blank'">Click Here</a> </b>",
    "director",
    "<b > Director's  <br>The link to Director's 👉<a href=" 'https://vit.ac.in/directors' " target="'blank'">Click Here</a> </b>",
    "about contact us",
    "<b >Contact us <br>The link to Contact us👉 <a href=" 'https://vit.ac.in/contactus' " target="'blank'">Click Here</a> </b>",

    "notices",
    "<b > NOTICES<br>These are the top results:<br> <br> Annoucement  </b>",
    "annoucement",
    "<b >annoucement <br>The link to All Notices👉 <a href=" 'https://vit.ac.in/' " target="'blank'">Click Here</a> </b>",

    "Payment",
    "<b > Payment <br>These are the top results:<br> <br> Payment Details <br> Online Payment Portal </b>",
    "payment details",
    "<b > Payment Details<br>The link to Payment Details 👉 <a href=" 'https://vtop.vit.ac.in/vtop/open/page' " target="'blank'">Click Here</a> </b>",
    "online payment portal",
    "<b > Payment Portal <br>The link to Payment Portal👉<a href=" 'https://vtop.vit.ac.in/vtop/open/page' " target="'blank'">Click Here</a> </b>",

    "placement result",
    "<b > PLACEMENTS These are the top results:<br> <br>Placement Detail<br> Placement Contact <br> Placement Tracker </b>",
    "placement detail",
    "<b> Placements<br>The link to Placements👉 <a href=" 'https://vit.ac.in/cdc-overview' " target="'blank'">Click Here</a> </b>",
    "placement contact",
    "<b>Contact us<br>The link to Contact us👉<a href=" 'https://vit.ac.in/cdc-contact-us' " target="'blank'">Click Here</a> </b>",
    "placement tracker",
    "<b > Placement Tracker<br>The link to Placement Tracker👉 <a href=" 'https://vit.ac.in/cdc-tracker' " target="'blank'">Click Here</a> </b>",

    "visitors",
    "<b VISITORS <br>The following are frequently searched terms related to visitors. Please select one from the options below : <br> <br> Visitor detail<br> Programs We Offer <br>Student Bodies </b>",
    
    "vistior detail",
    "<b > ABOUT US<br>These are the top results:<br> <br> About Vit<br> Director's Address <br> Principal's Address </b>",
    "about vit",
    "<b >About Vit<br>The link to About CRCE👉 <a href=" 'https://vit.ac.in/about-vit' " target="'blank'">Click Here</a> </b>",
    "director address",
    "<b > Director's  <br>The link to Director's 👉<a href=" 'https://vit.ac.in/directors' " target="'blank'">Click Here</a> </b>",
    "Principal's Address",
    "<b >Contact us <br>The link to Contact us👉 <a href=" 'https://vit.ac.in/contactus' " target="'blank'">Click Here</a> </b>",

    "Programs We Offer",
    "<b > PROGRAMS WE OFFER <br>These are the top results:<br> <br> Under-Graduate <br> Post-Graduate<br> Ph.D </b>",
    "Under-Graduate",
    "<b > Under-Graduate<br>The link to Under-Graduate👉 <a href=" 'https://vit.ac.in/all-courses/ug' " target="'blank'">Click Here</a> </b>",
    " Post-Graduate",
    "<b > Post-Graduate <br>The link to Post-Graduate👉<a href=" 'https://vit.ac.in/all-courses/pg' " target="'blank'">Click Here</a> </b>",
    "phd",
    "<b > Ph.D <br>The link to Ph.D👉 <a href=" 'https://vit.ac.in/admissions/research' " target="'blank'">Click Here</a> </b>",

    "student bodies",
    "<b > STUDENT BODIES <br>These are the top results:<br> <br> Council  <br>  Chapter <br>  Project  </b>",
    "council",
    "<b >  Students Council  <br>The link to Students Council  👉 <a href=" 'https://vit.ac.in/campus-category/student-council' " target="'blank'">Click Here</a> </b>",
    "chapter",
    "<b >  Students Chapter <br>The link to Students Chapter 👉<a href=" 'https://vit.ac.in/campus-category/chapters' " target="'blank'">Click Here</a> </b>",
    "project",
    "<b > Students Project Groups <br>The link to Students Project Groups👉 <a href=" 'https://scoreprojects.vit.ac.in/' " target="'blank'">Click Here</a> </b>",
]

trainer.train(conversation)