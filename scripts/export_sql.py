import json

def json_to_sql():
    with open('data/kerata_basa.json', 'r') as f:
        data = json.load(f)
        
    with open('kawruh_dump.sql', 'w') as sql_file:
        sql_file.write("CREATE TABLE IF NOT EXISTS kerata_basa (id VARCHAR(10) PRIMARY KEY, word VARCHAR(50), kerata_basa TEXT, philosophy TEXT, category VARCHAR(50));\n")
        
        for item in data:
            # Escape single quotes
            kerata_basa = item['kerata_basa'].replace("'", "''")
            philosophy = item['philosophy'].replace("'", "''")
            sql = f"INSERT INTO kerata_basa (id, word, kerata_basa, philosophy, category) VALUES ('{item['id']}', '{item['word']}', '{kerata_basa}', '{philosophy}', '{item['category']}');\n"
            sql_file.write(sql)
            
    print("SQL Dump generated: kawruh_dump.sql")

if __name__ == "__main__":
    json_to_sql()