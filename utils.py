import pdfplumber as pp
import mindsdb_sdk as mdb
import pandas as pd
import docx2txt
import os


MDB_EMAIL=os.environ['email']
MDB_PWD=os.environ['pwd']
MODEL_NAME=os.environ['model']



def parse_resume(files):
    arr=[]
    for file in files:
        if file.name.endswith('.pdf'):
            text=extract_text_from_pdf(file)
        elif file.name.endswith('.docx'):
             text=extract_text_from_doc(file)
        else:
             raise Exception("This file format is Not supported. \nOnly pdf and docx are supported")
        
        arr.append(text)
        
    df=pd.DataFrame(arr, columns=['resume'])
    return _from_mindsdb(df)


def _from_mindsdb(df: pd.DataFrame):
    server=mdb.connect(login=MDB_EMAIL,password=MDB_PWD)
    model=server.get_project('mindsdb').get_model(MODEL_NAME)
    entity_df=model.predict(df)
    json_df = pd.DataFrame(entity_df['json'].tolist())
    entity_df = pd.concat([entity_df, json_df], axis=1)
    entity_df = entity_df.drop('json', axis=1)
    return entity_df 


def extract_text_from_pdf(file):
    with pp.open(file) as pdf:
            text=''
            for page in pdf.pages:
                text=text + page.extract_text()
            return text
    
def extract_text_from_doc(file):
    try:
        text = docx2txt.process(file)
        return text
    except Exception as e:
        raise(f"Error: Unable to extract text from document {file}. {e}")