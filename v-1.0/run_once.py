import sqlite3

def create_database():
    conn = sqlite3.connect('csi_dashboard.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS packages
                      (id INTEGER PRIMARY KEY,
                       name TEXT,
                       current_version TEXT,
                       latest_version TEXT,
                       cve_count INTEGER,
                       ontap_version TEXT)''')
    
    # Insert some sample data
    sample_data = [
        ('PHP', '9.16.1', '9.16.2', 3, '9.14.1'),
        ('SQLite', '3.35.5', '3.35.5', 0, '9.14.1'),
        ('Apache', '2.4.46', '2.4.48', 2, '9.14.1'),
        ('Python', '3.9.5', '3.9.6', 1, '9.14.1')
    ]
    
    cursor.executemany('''INSERT INTO packages (name, current_version, latest_version, cve_count, ontap_version)
                          VALUES (?, ?, ?, ?, ?)''', sample_data)
    
    conn.commit()
    conn.close()

    print("Database created successfully with sample data.")

if __name__ == "__main__":
    create_database()