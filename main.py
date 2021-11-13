import streamlit as st
# db
import sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()

def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS blogtable(author TEXT,title TEXT,article TEXT,postdate DATE)')

def add_date(author,title,article,postdate):
    cur.execute('INSERT INTO blogtable(author,title,article,postdate) VALUES (?,?,?,?)', (author,title,article,postdate))
    con.commit()

def view_all_notes():
    cur.execute('SELECT * FROM blogtable')
    data = cur.fetchall()
    return data

def view_all_titles():
    cur.execute('SELECT DISTINT title FROM blogtable')
    # 35:!4 minutos

def get_blog_by_title(title):
    cur.execute('SELECT * FROM blogtable WHERE title = "{}"'.format(title))
    data = cur.fetchall()
    return data


# Layout templates
title_Temp = """"
    <div style="background-color:#464e5f;padding_10px,margin:10px;">
    <h4 style="color:white;text-align_center;">{}</h4>
    <img src=http://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;
    <h4 style="color:white;text-align_center;">Author: {}</h4>

    <p>{}</p>

    <h6 style="color:white;text-align_center;">Post date: {}</h6>
    </div>
    """

article_temp ="""
    <div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
    <h4 style="color:white;text-align:center;">{}</h1>
    <h6>Author: {}</h6>
    <h6>Post Date: {}</h6>
    <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align:">
    <br/>
    <br/>
    <p style="text-align:justify">{}</p>
    </div>
    """

head_message_temp="""
    <div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
    <h4 style="color:white;text-align:center;">{}</h1>
    <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align:">
    <h6>Author: {}</h6>
    <h6>Post Date: {}</h6>
    </div>
    """

full_message_temp="""
    <div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
        <p style="text-align:justify;color:black;padding:10px">{}</p>
    </div>
    """


def main():
    '''a simple blog CRUD'''
    st.title("Data blog")

    menu = ["Home","View","Add","Search","Manage"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        result = view_all_notes()
        st.write(result)
        for i in result:
          b_author = i[0]
          b_title = i[1]
          b_article = str(i[2])[0:30]
          b_post_date = i[3]
          st.markdown(title_temp.format(b_title,b_author,b_article,b_post_date), unsafe_allow_html=True)

    elif choice == "View":
        st.subheader("View")
        all_titles = [i[0] for i in view_all_list()]
        postlist = st.sidebar.selectbox("View Post", all_titles)
        post_result = get_blog_by_title(postlist)
        for i in post_result:
            b_author = i[0]
            b_title = i[1]
            b_article = i[2]
            b_post_date = i[3]
            st.markdown(head_message_temp.format(b_title,b_author,b_article,b_post_date), unsafe_allow_html=True)
            st.markdown(full_message_temp.format(b_title,b_author,b_article,b_post_date), unsafe_allow_html=True)

    
    
    elif choice == "Add":
        st.subheader("Add articles")
        create_table()
        blog_author = st.text_input("Enter Author Name", max_chars=50)
        blog_title = st.text_input("Enter Post", max_chars=50)
        blog_article = st.text_area("Post article here", height=100)
        blog_post_date = st.date_input("Date")
        if st.button("Add"):
            add_data(blog_author,blog_title,blog_article,blog_post_date)
            st.success(f"Post:{blog_title} saved")
        

    elif choice == "Search":
        st.subheader("Search articles")
        search_term = st.text_input('Enter Search Term')
        search_choice = st.radio("Field to Search By", ("title", "author"))
        if search_choice == "title":
            article_result = get_blog_by_title(search_term)
        elif search_choice == "author":
            article_result = get_blog_by_author(searcn_term)



    elif choice == "Manage":
        st.subheader("Manage articles")

if '__name__' == '__main__'_
    main()