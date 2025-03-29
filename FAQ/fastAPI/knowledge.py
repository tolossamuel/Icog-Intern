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
            !(add-atom &self (Meeting ((Sunday ((description 'staff Meeting present weekly progress also weekly plan') (frequency "Weekly") (mandatory "for both staff and intern") (time "morning 7:00 Am - 8:00 AM")))
                            (Wednesday ((description 'intern meeting present wekkly progress also weekly plan') (frequency 'weekly') (mandatory 'only for intern') (time "morning 7:00 Am - 8:00 AM"))))))
            !(add-atom &self (Responsibility ((Attendance "Minimum 40 office hours per month") (CV "update CV every week before Sunday mid night") (Traling "attend traling every saturday")
            )))
            !(add-atom &self (CV ((description "the update include weekly progress"))))
            !(add-atom &self (Mentor ((description "In Icog-Lab we have a mentorship program for intern every intern have a mentor")
                            (change "to change a mentor you need to inform HR") (responsibility "mentor is responsible to guide intern in their project")
                            (work "intern and mentor work together in the project that is a project of the mentor")
                            )))
            !(add-atom &self (Mentor-Change ((description "To change a mentor you need to inform HR") (process "To change a mentor you need to inform HR and HR will assign a new mentor for you"))))
            '''
        )
        
        self.graph = ""
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
        relevant, related, or mentioned in connection to the question.Input: ["CV", "Meeting", "Responsibility", "Mentor", "Mentor-Change"], 
        {question} Instructions: 1.Analyze the provided question for keywords, context, and overall intent.
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
        print(domain_knowledge)
        if not domain_knowledge or not domain_knowledge[0]:
            domain_knowledge = "No domain knowledge, use your own knowledge"
        
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
        Please respond with a well-articulated, formal paragraph that comprehensively addresses the question while showcasing your domain expertise.
        '''
        response = self.client.generate_content(
             comand
        )
        
       
        return response.text
obj = Knowledge()


# print(domain_knowledge)
obj.getAnswer("what is the responsibility of intern")
