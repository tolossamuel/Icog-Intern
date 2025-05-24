from hyperon import MeTTa, SymbolAtom, ExpressionAtom, GroundedAtom
import os
import glob

metta = MeTTa()
metta.run(f"!(bind! &space (new-space))")

def load_dataset(path: str) -> None:
    if not os.path.exists(path):
        raise ValueError(f"Dataset path '{path}' does not exist.")
    paths = glob.glob(os.path.join(path, "**/*.metta"), recursive=True)
    if not paths:
        raise ValueError(f"No .metta files found in dataset path '{path}'.")
    for path in paths:
        print(f"Start loading dataset from '{path}'...")
        try:
            metta.run(f'''
                !(load-ascii &space {path})
                ''')
            print(path)
        except Exception as e:
            print(f"Error loading dataset from '{path}': {e}")
    print(f"Finished loading {len(paths)} datasets.")

# Example usage:
try:
    dataset = load_dataset("./Data")
   
except Exception as e:
    print(f"An error occurred: {e}")
print(dataset)
# # 2 Points
def get_transcript(node):
    node = node[0]
    
    # result = metta.run("!(get-atoms &space)")
    # print(result)
    command = f"""!(match &space (transcribed_to ({node}) ($y $x)) (transcribed_to ({node}) ($y $x)))"""
    
    transcript = metta.run(command)
    return transcript[0]
 

# #2 Points
def get_protein(node):
    
    node = node[0]
    command = f"""
    !(match &space (transcribed_to ({node}) ($y $x)) (
        (match &space (translates_to (transcript $x) ($z $t)) (transcribed_to (transcript $x) ($z $t)))
        ))
    """
    
    protein = metta.run(command) 
    return protein
# gene = get_transcript(['gene ENSG00000166913'])
# print(gene)
#6 Points
def recurssive_seralize(metta_expression, result):
    for node in metta_expression:
        if isinstance(node, SymbolAtom):
            result.append(node)
        elif isinstance(node, GroundedAtom):
            result.append(node)
        elif isinstance(node, ExpressionAtom):
            recurssive_seralize(node.get_children(), result)
    return result
def metta_seralizer(metta_result):
    result = []
    for node in metta_result:
        data = node.get_children()
        result.append({
            'edge': data[0].get_name(),
            'source': f"{data[1].get_children()[0]} {data[1].get_children()[1]}",
            'target': f"{data[2].get_children()[0]} {data[2].get_children()[1]}"
        })
        # print(data)
        # print(data.get_node_type())
    
    return result


# # #1
transcript_result= (get_transcript(['gene ENSG00000166913']))
print(transcript_result) 
# # """
# # Expected Output Format::
# # # [[(, (transcribed_to (gene ENSG00000166913) (transcript ENST00000372839))), (, (transcribed_to (gene ENSG00000166913) (transcript ENST00000353703)))]]
# # """ 

# # #2
protein_result= (get_protein(['gene ENSG00000166913']))
print(protein_result) 
# # """
# # Expected Output Format::
# # # [[(, (translates_to (transcript ENST00000353703) (protein P31946))), (, (translates_to (transcript ENST00000372839) (protein P31946)))]]
# # """

# #3
print("===============================================")
parsed_result = metta_seralizer(transcript_result)
print(parsed_result)
"""
Expected Output Format:
[
    {'edge': 'transcribed_to', 'source': 'gene ENSG00000175793', 'target': 'transcript ENST00000339276'}
]
# """
