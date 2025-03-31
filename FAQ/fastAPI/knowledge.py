from hyperon import * # type: ignore
import google.generativeai as genai
import ast
import json
import os
from dotenv import load_dotenv
from metta_knowledge import metta_knowledge


class Knowledge:
    def __init__(self,graph):
        load_dotenv()
        api_key = os.getenv("API_KEY")
        genai.configure(api_key = api_key )
        self.client = genai.GenerativeModel("gemini-2.0-flash")
        
        self.metta  = MeTTa() # type: ignore
        

        
        self.graph = graph
        self.allKnowledge = self.metta.run('!(get-atoms &self)')
    def query(self, query):
        
        result = self.metta.run(f'!(match &self ({query} $x) $x)')
   
        relation = self.metta.run(
            f'!(match &self ({query} have-relation $x) (collapse (match &self ($x $y) $y)))'
        )
    
        return result +  relation
    def addKnowledge(self, newKnowledge):
        self.metta.run(f'!(add-atom &self {newKnowledge})')
        return "Done"
    import ast
    

    def processQuestion(self, question):
        command = f'''
        You are an AI that extracts relevant words from a given list based on a question.
        **Input:**
        - List of words: {self.graph}
        - Question: {question}
        
        **Instructions:**
        1. Identify words from the provided list that are explicitly mentioned in the question or have synonyms in the question.
        2. Return only the matching words in a Python list format.
        3. If no words match, return an empty list: `[]`.
        4. Do not include any explanations, metadata, or formatting other than the list itself.
        
        **Output format:**
        ["word1", "word2", "word3"]
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
            domain_knowledge = "for specific  this type of question pleas contact HR with email icoghrteam1@gmail.com"
        
        return domain_knowledge

    
    def getAnswer(self, question):
        
        domain_knowledge = self.processQuestion(question)
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
    def extractAndAddKnowledge(self, question):
        command = f'''
            You are an AI assistant. Your task is to extract the most relevant key word 
            from the provided description. one word that best represents the core topic of the description.
            
            Instructions:
            Analyze the description to identify the central theme.
            Extract only one key word that encapsulates the main idea.
            Exclude filler words, minor details, and unnecessary information.
            Return only the single most relevant word in Python list format: ["keyword"].
            ***Input***
            {question}
            '''
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

        for word in converted_list:
            self.metta.run(f"!(add-atom &self ({word} ({question})))")
            self.graph.append(word)
  
        return "Successfully added!!"
        
        

