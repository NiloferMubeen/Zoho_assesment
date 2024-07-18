# IMPORTING THE NECESSARY LIBRARIES

import psycopg2 as pg2
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

# Establishing Database connection

conn = pg2.connect(dbname="Zoho", user="postgres",port = 5433,password = 'SU')
curr = conn.cursor()


create = '''CREATE TABLE IF NOT EXISTS userdetails(
	user_name text,
	password varchar(8),
    age integer,
	Mobile bigint
     )'''
     
curr.execute(create)
conn.commit()



# Dashboard
st.set_page_config(page_title = 'Zoho_assessment',layout='wide')

st.markdown("<h1 style='text-align: center; color: black;'>ZOHO User Registration</h1>", unsafe_allow_html=True)


with st.sidebar:
    selected = option_menu("Main Menu", ["Register","Login", 'Update'], icons=['house', 'gear','gear'], menu_icon="cast", default_index=0)

# User options
    
if selected == "Register":
        st.subheader('Welcome to Registration Page',divider = 'rainbow')

        name1 = st.text_input("Enter the Username",value=None)
        pwd = st.text_input('Enter Password',value=None)
        age = st.text_input('Age',value=None)
        mob = st.text_input('Mobile',value=None)
        
        user_dic = { 'user':[],
                    'pwd': [],
                    'age': [],
                    'mob': []}
        button = st.button('Register')
        
        if name1 and pwd and age and mob and button:
                user_dic['user'].append(name1)
                user_dic['pwd'].append(pwd)
                user_dic['age'].append(age)
                user_dic['mob'].append(mob)
                       
        
              
        
        
        if button:
            try:
                curr.execute('Select user_name from userdetails')
                all_users = [i[0] for i in curr]
                if name1 in all_users:
                    st.error('Username already exists!!')
                else:
                    
                        insert = '''INSERT INTO  userdetails(user_name,password,age,Mobile)VALUES(%s,%s,%s,%s)'''
                        
                        details = (user_dic['user'][0],
                                user_dic['pwd'][0],
                                user_dic['age'][0],
                                user_dic['mob'][0])
                        
                        curr.execute(insert,details)
                        conn.commit()
                        if curr:
                            st.caption('Registration successfull!')      
            except IndexError: 
                st.markdown("<h5 style='text-align: center; color: red;'>Please fill in all the details to Register </h5>", unsafe_allow_html=True)  
            
                 
                
        if st.button('Display Registered Details'):
        
            st.write('Your details:')
            
            
            query = '''SELECT * FROM userdetails WHERE user_name = %s AND password = %s'''
            values = (name1,pwd)
            
            curr.execute(query,values)
            table1 = curr.fetchall()
            
            df = pd.DataFrame(table1,columns =['username','password','age','Mobile'])
            
            st.table(df)
            
            
            
            
if selected == 'Login':
    st.subheader(':purple[Welcome to the Login Page!!]',divider='rainbow')
    
    new_user = st.text_input('Username')
    password = st.text_input('Password')
    bn = st.button('login')
        
    if new_user and bn:
        query = '''SELECT user_name FROM userdetails WHERE user_name = %s AND password = %s'''
        curr.execute(query,(new_user,password))
        result = curr.fetchone()
        if result:
            st.write(f'Welcome, {new_user}')
        else:
            st.error('Invalid Username/password')
            
        
if selected == 'Update':
    st.subheader('Update you Details')
    curr.execute('Select * from userdetails')
    tab = curr.fetchall()
    df1 = pd.DataFrame(tab,columns =['username','password','age','Mobile'])
    
    
    user = st.text_input('Username',value=None, placeholder='Enter the username')
    
    if user:
        upd_name = st.text_input('User',df1.loc[df1['username'] == user,'username'].squeeze())
        upd_pwd = st.text_input('Password',df1.loc[df1['username'] == user,'password'].squeeze()) 
        upd_age = st.text_input('Age',df1.loc[df1['username'] == user,'age'].squeeze()) 
        upd_mob = st.text_input('Mobile',df1.loc[df1['username'] == user,'Mobile'].squeeze())
    
    button1 = st.button('Update') 
    
    if button1:
        
            query = "UPDATE userdetails SET user_name = %s,password = %s,age = %s,Mobile = %s WHERE user_name = %s"
            values = (upd_name,upd_pwd,upd_age,upd_mob,user)
            
            curr.execute(query,values)
            conn.commit()
            if curr:
                st.caption('Update Successfull !!')
            else:
                st.warning('Invalid Username ')
            
    