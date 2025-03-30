from hyperon import * # type: ignore
import google.generativeai as genai
import ast
import json
import os
from dotenv import load_dotenv


class Knowledge:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("API_KEY")
        genai.configure(api_key = api_key )
        self.client = genai.GenerativeModel("gemini-2.0-flash")
        
        self.metta  = MeTTa() # type: ignore
        self.mettaKnowledge = self.metta.run( # type: ignore
            '''
            !(add-atom &self (CV ((description "Update your CV every week for HR review") (frequency 'Weekly') (importance 'High'))))
            !(add-atom &self (Meeting ((Sunday ((description 'Staff meeting to present weekly progress and plan') (frequency "Weekly") (mandatory "for both staff and interns") (time "7:00 AM - 8:00 AM")))
                                (Wednesday ((description 'Intern meeting to present weekly progress and plan') (frequency 'Weekly') (mandatory 'only for interns') (time "7:00 AM - 8:00 AM"))))))
            !(add-atom &self (Responsibility ((Attendance "Minimum 40 office hours per month") 
                                            (CV "Update CV every week before Sunday midnight") 
                                            (Training "Attend training every Saturday") 
                                            (Confidentiality "Maintain confidentiality of company information and proprietary data") 
                                            (Professionalism "Maintain professional demeanor and respect in all interactions")
                                            (Task-Completion "Complete assigned tasks on time and report progress to supervisors")
                                            (Documentation "Maintain proper documentation for work and progress updates"))))
            !(add-atom &self (Mentor ((description "Each intern at iCog-Labs has a mentor for guidance") 
                                    (change "To change a mentor, interns must inform HR") 
                                    (responsibility "Mentors guide interns in their projects") 
                                    (work "Interns and mentors collaborate on mentor-led projects")
                                    (feedback "Mentors provide regular feedback to interns on performance and skill development"))))
            !(add-atom &self (Mentor-Change ((description "To change a mentor, inform HR") 
                                            (process "HR will assign a new mentor upon request"))))
            !(add-atom &self (Training ((description "Training sessions are mandatory and occur on Saturdays") 
                                        (grading "Intern performance is evaluated based on attendance and engagement") 
                                        (courses "Interns must complete five mandatory courses during their internship")
                                        (participation "Active participation in training is required to qualify for further internship opportunities"))))
            !(add-atom &self (Performance-Evaluation ((description "Interns are evaluated based on performance and attendance") 
                                                    (grouping "Top 5 in Group 1 are prioritized for intern-to-staff transition")
                                                    (criteria "Evaluation includes punctuality, work quality, communication, and team collaboration"))))
            !(add-atom &self (Communication ((description "Interns must maintain open communication with mentors and team members") 
                                            (reporting "Interns should regularly update project progress and challenges") 
                                            (official-channels "Use official channels for communication and documentation submission")
                                            (email "Use professional email etiquette when communicating with HR and supervisors"))))
            !(add-atom &self (Key-Contacts ((HR "icoglabs89@gmail.com, icoghrteam1@gmail.com") 
                                            (Mentor "Assigned mentor for guidance") 
                                            (Team-Leads "Project-specific questions directed to respective team leads"))))
            !(add-atom &self (Work-Ethics ((Punctuality "Interns must arrive on time for meetings and work sessions") 
                                        (Respect "Respect colleagues, mentors, and staff members") 
                                        (Teamwork "Collaborate effectively with peers and contribute to group tasks")
                                        (Integrity "Uphold honesty and transparency in all tasks and reporting"))))
            !(add-atom &self (Leave-Policy ((Request "Interns must request leave in advance and get approval from HR") 
                                            (Limitations "Unapproved absences may affect performance evaluation")
                                            (Emergency "In case of emergencies, notify HR and mentors immediately"))))
            !(add-atom &self (Internship-Completion ((Certificate "Interns receive a certificate upon successful completion") 
                                                    (Extension "Outstanding interns may be offered an extended internship or job opportunity")
                                                    (Final-Review "HR and mentors conduct a final review before internship completion"))))
            !(add-atom &self (Hello ((description "Hello, I am an AI designed to assist with HR-related queries")
                                    (functionality "I can provide information on company policies, responsibilities, and HR procedures")
                                    (knowledge "I have access to the latest HR data and guidelines")
                                    (limitations "I cannot provide legal advice or personal opinions"))))
            !(add-atom &self (Goodbye ((description "Goodbye, I hope I was able to assist you with your HR query")
                                    (functionality "I can provide information on company policies, responsibilities, and HR procedures")
                                    (knowledge "I have access to the latest HR data and guidelines")
                                    (limitations "I cannot provide legal advice or personal opinions"))))
            !(add-atom &self (help ((description "I can provide information on company policies, responsibilities, and HR procedures")
                                    (functionality "I have access to the latest HR data and guidelines")
                                    (limitations "I cannot provide legal advice or personal opinions"))))
            !(add-atom &self (HR-Query ((description "I can provide information on company policies, responsibilities, and HR procedures")
                                    (functionality "I have access to the latest HR data and guidelines")
                                    (limitations "I cannot provide legal advice or personal opinions"))))
            !(add-atom &self (HR-Response ((description "I can provide information on company policies, responsibilities, and HR procedures")
                                    (functionality "I have access to the latest HR data and guidelines")
                                    (limitations "I cannot provide legal advice or personal opinions"))))
            !(add-atom &self (start ((description "Hello, I am an AI designed to assist with HR-related queries at Icog-Lab AI research center")
                                    (functionality "I can provide information on company policies, responsibilities, and HR procedures")
                                    (knowledge "I have access to the latest HR data and guidelines")
                                    (limitations "I cannot provide legal advice or personal opinions"))))
            
            
            '''
        )

        
        self.graph = ["CV", "Meeting", "Responsibility","Mentor","Mentor-Change",
        "Training","Performance-Evaluation","Communication","Key-Contacts", "Work-Ethics","Leave-Policy","Internship-Completion",
        "Hello","Goodbye","help","HR-Query","HR-Response","start"]
        self.allKnowledge = self.metta.run('!(get-atoms &self)')
    def query(self, query):
        
        result = self.metta.run(f'!(match &self ({query} $x) $x)')
     
        return result
    def addKnowledge(self, newKnowledge):
        self.metta.run(f'!(add-atom &self {newKnowledge})')
        return "Done"
    import ast
    

    def processQuestion(self, question):
        command = f'''
        You are an AI designed to evaluate a given list of words alongside a specific question.
        Your objective is to extract and return a list of words from the initial list that are 
        relevant, related, or mentioned in connection to the question.Input:  {self.graph} {question} Instructions: 
        1.Analyze the provided question for keywords, context, and overall intent.
        2.Cross-reference the keywords and context with the list of words.
        3.Identify and extract only those words from the list that have a direct  relevance the word muest be in question or the synonym must be in the question.
        4. return only list of word not other format the format must be ["word1", "word2", "word3"].
        '''
        
        # Generate response from model
        response = self.client.generate_content(
            command
        )
   
        try:
            converted_list = json.loads(response.text)  # use json.loads() for JSON data
        except json.JSONDecodeError:
            try:
                converted_list = ast.literal_eval(response.text)
            except Exception as e:
               
                return "Error parsing the response"

        domain_knowledge = []
        for word in converted_list:
            domain_knowledge.append(self.query(word)[0])

        # Handle case where domain knowledge is empty
        
        if not domain_knowledge or not domain_knowledge[0]:
            domain_knowledge = "for specific  this type of question pleas contact HR"
        
        return domain_knowledge

    
    def getAnswer(self, question):
        domain_knowledge = obj.processQuestion(question)
        
        comand = f'''
        You are an AI designed to provide comprehensive and formal responses utilizing specified domain knowledge.
        Please ensure that your responses reflect the professionalism and thoroughness expected of a Human Resources representative.
        Structure your output in a coherent paragraph format, elaborating on key points and providing detailed explanations 
        that align with HR best practices.You are to integrate the provided domain knowledge and respond to the input question 
        by synthesizing relevant information, including synonyms and related concepts, to enhance your response.Your training encompasses 
        data up until October 2023, and you must utilize this knowledge effectively.Input domain_knowledge: {domain_knowledge} Input question: {question} 
        Please respond with a well-articulated, formal paragraph that comprehensively addresses the question while showcasing your domain expertise and the respond must beon
        only python string with out any special other character.
        '''
        response = self.client.generate_content(
             comand
        )
        
       
        return response.text
obj = Knowledge()


# print(domain_knowledge)
obj.getAnswer("what is the responsibility of intern")
