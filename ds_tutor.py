import google.generativeai as genai
import streamlit as st
import time

RESPONSE = """ """

def stream_data():
    for word in RESPONSE.split(" "):
        yield word + " "
        time.sleep(0.04)


genai.configure(api_key= "AIzaSyCtbkn_fspnC96QyY3b1fdOkqp4ZnKYWpI")

st.title("🎓 University Assistant", help="na")
st.write("Student management system for the University")
st.write("Ask me about university or students particular information")
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest", 
                            system_instruction="""Your name is 🎓 university assistant bot, and
                                                You are ITM university ai assistant and student management bot and a helpful and polite assistant,
                                                you will provide answer to the given question related to ayurveda and prakriti
                                                and resolve the user's queries be specific and brief, if the query is not related to university or student data,
                                                then you can politely request the user to ask questions related to university or data about student.
                                                
                                                following is the data of ITM university in csv format:
                                                StudentID,Name,Gender,DateOfBirth,Address,PhoneNumber,Email,Department,Major,Year
                                                1001,John Doe,Male,1998-07-20,"123 University Ave, City, State, Zip",555-123-4567,johndoe@example.com,Computer Science,Artificial Intelligence,Senior
                                                1002,Jane Smith,Female,1999-05-15,"456 College St, City, State, Zip",555-987-6543,janesmith@example.com,Electrical Engineering,Power Systems,Junior
                                                1003,Alice Johnson,Female,2000-02-10,"789 Campus Rd, City, State, Zip",555-567-8901,alicejohnson@example.com,Psychology,Clinical Psychology,Senior
                                                1004,David Lee,Male,1999-11-30,"321 Academic Blvd, City, State, Zip",555-234-5678,davidlee@example.com,Business Administration,Marketing,Junior
                                                1005,Sarah Brown,Female,2001-04-25,"555 Student Ave, City, State, Zip",555-345-6789,sarahbrown@example.com,Physics,Astrophysics,Sophomore
                                                1006,Michael Wang,Male,1999-09-18,"987 Lecture Hall St, City, State, Zip",555-678-9012,michaelwang@example.com,Chemistry,Analytical Chemistry,Senior
                                                1007,Emily Garcia,Female,2000-01-12,"246 Research Dr, City, State, Zip",555-789-0123,emilygarcia@example.com,Biology,Cellular Biology,Junior
                                                1008,Andrew Martinez,Male,1999-08-05,"741 Seminar Ave, City, State, Zip",555-890-1234,andrewmartinez@example.com,Mathematics,Statistics,Senior
                                                1009,Sophia Nguyen,Female,2001-03-22,"369 Lecture Hall St, City, State, Zip",555-901-2345,sophianguyen@example.com,Computer Engineering,Embedded Systems,Junior
                                                
                                                and here is the data of students: 
                                                StudentID,Name,Gender,DateOfBirth,Address,PhoneNumber,Email,Department,Major,Year,Course1,Course2,Course3,Course4,MathematicsGrade,EnglishLiteratureGrade,BiologyGrade,HistoryGrade,TotalDaysPresent,TotalDaysAbsent,LastAbsence
                                                1001,John Doe,Male,1998-07-20,"123 University Ave, City, State, Zip",555-123-4567,johndoe@example.com,Computer Science,Artificial Intelligence,Senior,Mathematics,English Literature,Biology,History,A,B-,C,B,80,10,2024-04-20
                                                1002,Jane Smith,Female,1999-05-15,"456 College St, City, State, Zip",555-987-6543,janesmith@example.com,Electrical Engineering,Power Systems,Junior,Mathematics,English Literature,Biology,History,A-,B,C,D,85,8,2024-04-22
                                                1003,Alice Johnson,Female,2000-02-10,"789 Campus Rd, City, State, Zip",555-567-8901,alicejohnson@example.com,Psychology,Clinical Psychology,Senior,Mathematics,English Literature,Biology,History,B,C+,A,B+,88,5,2024-04-23
                                                1004,David Lee,Male,1999-11-30,"321 Academic Blvd, City, State, Zip",555-234-5678,davidlee@example.com,Business Administration,Marketing,Junior,Mathematics,English Literature,Biology,History,B+,A,C,A-,92,3,2024-04-24
                                                1005,Sarah Brown,Female,2001-04-25,"555 Student Ave, City, State, Zip",555-345-6789,sarahbrown@example.com,Physics,Astrophysics,Sophomore,Mathematics,English Literature,Biology,History,A,B,C,D,87,6,2024-04-26
                                                """)
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

chat = model.start_chat(history=st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

prompt = st.chat_input("Ask me about university or students info...")

if prompt:
    st.chat_message("user").write(prompt)
    response = chat.send_message(prompt)
    RESPONSE = response.text
    st.chat_message("🎓").write(RESPONSE)
    st.session_state["chat_history"]=chat.history