import streamlit as st
import pdfplumber 
import pandas as pd
import openpyxl
import xlsxwriter
import io


#upload file

st.header("Extracting tables from PDF files")
file= st.file_uploader('upload file')

if file is not None:

    #now extract the file
    all_tables= []
    with pdfplumber.open(file) as pdf:
        for i, page in enumerate (pdf.pages):
            tables= page.extract_tables()

            for i,t in enumerate (tables):
                df=pd.DataFrame(t)

                all_tables.append(df)
              #  st.write(all_tables)

        st.subheader('Preview')
        selected_tables= []
 
        for i, j in enumerate(all_tables):
            st.markdown(f'Table {i+1}')
            st.dataframe(j, hide_index= True)
            if st.checkbox(f'Table {i+1}'):
               selected_tables.append(j)          
        
        name= st.text_input(" Name the file")

        b= st.button('To excel')
        

        if b :
            #create emplty file in memory
            output= io.BytesIO()
            
            with pd.ExcelWriter( output,engine= 'xlsxwriter') as writer:
             start_row=0
             for i , df in enumerate (selected_tables):
         
                 df.to_excel(writer,sheet_name="Tables",startrow=start_row, header= False,index= False)

            start_row= start_row + len(df) +2
            output.seek(0)
            st.download_button(label='Download Excel', data= output,file_name= f'{name}.xlsx', mime= 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                 

            st.success("Excel created")
    
