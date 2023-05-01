# Resume Miner🕵️
Welcome to [Resume Miner](https://tinyurl.com/resume-miner) :male_detective: the perfect tool to extract valuable information from resumes in PDF format :page_with_curl:. This powerful yet easy-to-use web app analyzes your uploaded resumes, identifying key details such as names, emails, highlights and skills :mag_right:. Simply upload your PDF files and watch as Resume Miner works its magic :sparkles:. Our user-friendly interface allows you to view the extracted information with just a few clicks, making it a breeze to quickly identify the best candidates for your job openings :fireworks:. With Resume Miner, finding the right talent has never been easier! :muscle:

## 👨‍💼🤖 Don't believe us?

🤣 We could tell you about how Resume Miner helped a company find their next CEO, but that would just be bragging. Instead, here are some more modest examples:

👨‍💼 **Hiring manager** : "I used to spend hours reading through resumes, but now with Resume Miner, I can find the perfect candidate in just minutes! It's like having a personal assistant that never sleeps."

👩‍💻 **Recruiter**: "I love using Resume Miner to find top-notch candidates. It's like a metal detector for resumes - it helps me uncover hidden gems that I might have missed otherwise."

🕵️‍♂️ **Detective**: "Okay, so I'm not actually a detective, but sometimes it feels like it when I'm trying to find the right candidate for a job. With Resume Miner, it's like I have X-ray vision - I can see right through a resume and find the information I need."

See? Even fictional characters can benefit from Resume Miner! Give it a try and see for yourself. 😉

## Here we Go

To use the MindsDB NLP model for parsing resumes in this Streamlit app, you need to first create a model on the MindsDB platform.

* Log in to [MindsDB](https://cloud.mindsdb.com/) and create a new project
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

## Clone Repo And use it
* Clone resume_miner repo using below command
```git
git clone https://github.com/parthiv11/Resume_Miner.git
```


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

>>Explore the MindsDB [documentation](https://docs.mindsdb.com/) to learn more about the platform's capabilities.

>> You can also check out the live demo of the Resume Miner tool [here](https://tinyurl.com/resume-miner).



