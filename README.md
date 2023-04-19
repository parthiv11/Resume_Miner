# Resume Miner
Welcome to Resume Miner :male_detective: the perfect tool to extract valuable information from resumes in PDF format :page_with_curl:. This powerful yet easy-to-use web app analyzes your uploaded resumes, identifying key details such as names, emails, highlights and skills :mag_right:. Simply upload your PDF files and watch as Resume Miner works its magic :sparkles:. Our user-friendly interface allows you to view the extracted information with just a few clicks, making it a breeze to quickly identify the best candidates for your job openings :fireworks:. With Resume Miner, finding the right talent has never been easier! :muscle:

To use the MindsDB NLP model for parsing resumes in this Streamlit app, you need to first create a model on the MindsDB platform.

* Log in to MindsDB and create a new project
* In the project, create a new model with the name resume_miner(OR anything of your choice)
* Copy and paste the following code into the MindsDB query editor:

```sql
CREATE MODEL mindsdb.resume_miner
PREDICT json
USING
    engine = 'openai',
    json_struct = {
        'email': 'email ',
        'name': 'name',
        'skills_list': 'skills_list {comma seperated}',
        'summary': 'informative summary with emojis giving information about experience  in  35-50 words without escape sequence char '
    },
    input_text = 'resume';
```
* Run the query to create a new model in MindsDB with whatever name you have given in the query. :rocket:

* In the utils.py file, add the MindsDB email, password, and model name to the variables provided.
```python
# EXAMPLE 
MDB_EMAIL="MINDSDB_EMAIL"
MDB_PWD="MINDSDB_PASSWORD"
MODEL_NAME="resume_miner"
```
* Install the prerequisites mentioned in the requirements.txt file. :hammer_and_wrench:
```python
pip install -r requirements.txt
```
* Run the Streamlit app to start using the Resume Miner tool. :computer:
```sql
streamlit run app.py
```






