import psycopg2

try:
    # Ma'lumotlar bazasiga bog'lanish uchun bog'lanish o'rnating
    conn = psycopg2.connect(
        dbname="davomat_teamx",
        user="postgres",
        password="najmiddin",
        host="80.68.156.34",
        port="5432"
    )
    print("Ma'lumotlar bazasiga muvaffaqiyatli bog'landi.")
    
    # Bog'lanishni yopish
    conn.close()
    print("Bog'lanish yopildi.")
    
except (Exception, psycopg2.Error) as error:
    print("Ma'lumotlar bazasiga ulanib bo'lmadi:", error)