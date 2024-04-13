from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        #Create database or connect to one
        conn = sqlite3.connect('first_db.db')

        #Create A Cursor
        c = conn.cursor()

        #Create a Table 
        c.execute("""CREATE TABLE  if not exists customers(name text)""")

        
        #Commit our changes
        conn.commit()

              
        #Close our connection 
        conn.close()

        return Builder.load_file('first_db.kv')

       
    def submit(self):
        #Create database or connect to one
        conn = sqlite3.connect('first_db.db')

        #Create A Cursor
        c = conn.cursor()

       #Add A Record 
        c.execute("INSERT INTO customers VALUES (:first)",
            {
                'first': self.root.ids.word_input.text,
            })   
        #c.execute("INSERT INTO stocks VALUES ('GEORGE')")

        #Add A little a message
        self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'

        #Clear the input box
        self.root.ids.word_input.text = ''

        #Commit our changes
        conn.commit()

        #Close our connection 
        conn.close()

    def show_records(self):
        #Create database or connect to one
        conn = sqlite3.connect('first_db.db')

        #Create A Cursor
        c = conn.cursor()

        #Grab Records from database 
        c.execute("SELECT * FROM customers") 
        Records = c.fetchall()
       
        word = ''
        # Loop thru records
        for Record in Records:
            word = f'{word}\n{Record}'
            self.root.ids.word_label.text = f'{word}'
        
        #Commit our changes
        conn.commit()

              
        #Close our connection 
        conn.close()

MainApp().run()        
