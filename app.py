import streamlit as st
from utils import *


def app():
    st.set_page_config(page_title='Resume Miner',
                       page_icon=':clipboard:', layout='wide')
    st.title('Resume Miner :sleuth_or_spy:')

    # Add a file uploader to allow the user to upload a resume
    uploaded_files = st.sidebar.file_uploader('##### Upload a resume in PDF format :arrow_up_small:', type=[
                                              'pdf', 'docx'], accept_multiple_files=True)


    # If a file has been uploaded, parse it and display the results
    if len(uploaded_files):
        try:
            result = None
            with st.spinner('Analyzing resume... :mag_right::hourglass_flowing_sand:'):
                result = parse_resume(uploaded_files)

                for index, row in result.iterrows():
                    with st.expander(f' Name: **{row["name"]}** '):
                        st.markdown(
                            f'**Email:** {row["email"]} :envelope_with_arrow:')
                        st.markdown(
                            f'**Highlights:** {row["summary"]} :star2:')
                        st.markdown('#### **Skills:** ')
                        for i in row["skills_list"].split(','):
                            st.markdown(f'* {i} ')

        except Exception as e:
            st.write('Error: Unable to parse the resume ', e)


# Run the Streamlit app
if __name__ == '__main__':
    app()
