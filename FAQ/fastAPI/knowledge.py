from hyperon import * # type: ignore
import google.generativeai as genai
import ast
import json
import os
from dotenv import load_dotenv
from metta_knowledge import metta_knowledge


class Knowledge:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("API_KEY")
        genai.configure(api_key = api_key )
        self.client = genai.GenerativeModel("gemini-2.0-flash")
        
        self.metta  = MeTTa() # type: ignore
        self.mettaKnowledge = self.metta.run( # type: ignore
            metta_knowledge
        )

        
        self.graph = ["CV", "Greating","Meeting", "Responsibility","Mentor","Mentor-Change",
        "Training","Performance-Evaluation","Communication","Key-Contacts", "Work-Ethics","Leave-Policy","Internship-Completion",
        "Hello","Goodbye","help","HR-Query","HR-Response","start","contact","Apply-Internship","Working-Hours",
        "Office-Hours","Icong-Lab-Location","Internship-Opportunity","Internship-Feedback","Internship-Training",
        "Evaluation","Evaluation-Grouping"]
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
        4. return only list of word not other format the format must be ["word1", "word2", "word3"] if not word return [] empty list.
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
            domain_knowledge = "for specific  this type of question pleas contact HR with email icoghrteam1@gmail"
        
        return domain_knowledge

    
    def getAnswer(self, question):
        domain_knowledge = obj.processQuestion(question)
        comand = f'''
        You are an AI designed to provide comprehensive and formal responses utilizing specified domain knowledge.
        Please ensure that your responses reflect the professionalism and thoroughness expected of a Human Resources representative.
        Structure your output in a coherent paragraph format, elaborating on key points and explanations 
        that align with HR best practices.You are to integrate the provided domain knowledge and respond to the input question 
        by synthesizing relevant information, including synonyms and related concepts, to enhance your response.Your training encompasses 
        data up until October 2023, and you must utilize this knowledge effectively.Input domain_knowledge: {domain_knowledge} Input question: {question} 
        Please respond with a well-articulated, formal paragraph that comprehensively addresses the question while showcasing your domain expertise and the respond must be 
        only string with out any special character string just string must be string.
        '''
        response = self.client.generate_content(
             comand
        )
        
       
        return response.text
obj = Knowledge()


# print(domain_knowledge)
obj.getAnswer("what is the responsibility of intern")
