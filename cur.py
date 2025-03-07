import sqlite3 as sq

def get_formatted_table(): #Нужна для вывода общей таблицы
    
    
    def fetch_data():
      
        conn = sq.connect('data_base_bs.db')
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM overall_table")
        result = cur.fetchall()  
        
        conn.close()  
        return result

    def format_table(data):
        
        headers = ["Number", "ID", "Name", "Score", "Rank"]
        table = [headers] + data  

       
        formatted_rows = [" | ".join(map(str, row)) for row in table]

        return "```\n" + "\n".join(formatted_rows) + "\n```" 

  
    data = fetch_data()  
    return format_table(data)  



telegram_message = get_formatted_table()


