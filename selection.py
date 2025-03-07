import sqlite3 as sq
import random

def selection_player_for_battel(id_player):
    conn = sq.connect('data_base_bs.db')
    cur = conn.cursor()
    cur.execute(f"SELECT elo FROM rang_c WHERE id = {id_player}") #сюда вставить переменную с айди

    result = cur.fetchall()

    if result == []:
        cur.execute(f"SELECT elo FROM rang_b WHERE id = {id_player}")
        result = cur.fetchall()
        

    elo_taple = result[0]
    elo_player = elo_taple[0]

    if elo_player <  60:
        random_number_for_rang_c = random.randint(1,4)
        cur.execute(f"SELECT id,name,elo FROM rang_c WHERE number = {random_number_for_rang_c}")
        result_request_for_rang_c = cur.fetchall()

        headers_for_c = [ "ID", "Name", "elo"]
        table_for_c = [headers_for_c] + result_request_for_rang_c  

       
        formatted_rows = [" | ".join(map(str, row)) for row in table_for_c]

        final_result_c = "```\n" + "\n".join(formatted_rows) + "\n```" 


        return f'ваш враг:\n{final_result_c}'
    
    elif elo_player < 210:
        random_number_for_rang_b = random.randint(1,4)
        cur.execute(f"SELECT id,name,elo FROM rang_b WHERE number = {random_number_for_rang_b}")
        result_request_for_rang_b = cur.fetchall()

        headers_for_b = [ "ID", "Name", "elo"]
        table_for_b = [headers_for_b] + result_request_for_rang_b


        formatted_rows = [" | ".join(map(str, row)) for row in table_for_b]

        final_result_b = "```\n" + "\n".join(formatted_rows) + "\n```" 


        return f'ваш враг:\n{final_result_b}'

        conn.close()  
