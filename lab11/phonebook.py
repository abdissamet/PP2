import psycopg2 as pgsql

conn=pgsql.connect(host="localhost", dbname="lab10", user="postgres", password="Almaty250505", port=5432)
cur=conn.cursor()


def createpattern():
    global query
    query="""SELECT * FROM PhoneBook
    WHERE """
    print(r"Do you want to search by surname(0)/name(1)/break(any num) enter the number:")
    mode=int(input())
    if mode==0:
            query+="surname"
            print("Enter string")
            substr=input()
            print("""Select option:
            1-surname is equal to string
            2-surname starts with the string
            3-surname ends with the string
            4-surname contains the string""")
            mode1=int(input())
            if mode1==1:
                query+="='{}'".format(substr)
            elif mode1==2:
                query+=" iLIKE '{}%'".format(substr)
            elif mode1==3:
                query+=" iLIKE '%{}'".format(substr)
            else:
                query+=" iLIKE '%{}%'".format(substr)
    elif mode==1:
            query+="""name"""
            print("Enter string")
            substr=input()
            print("""Select option:
            1-name is equal to string
            2-name starts with the string
            3-name ends with the string
            4-name contains the string""")
            mode1=int(input())
            if mode1==1:
                query+="='{}'".format(substr)
            elif mode1==2:
                query+=" iLIKE '{}%'".format(substr)
            elif mode1==3:
                query+=" iLIKE '%{}'".format(substr)
            else:
                query+=" iLIKE '%{}%'".format(substr)
    else:
         return "error"
    return query


def insert(surname, name, phone):
    cur.execute("SELECT count(*) FROM PhoneBook WHERE surname='{}' AND name='{}'".format(surname, name))
    if cur.fetchone()[0]==0:
         cur.execute("INSERT INTO PhoneBook (surname, name, phone) VALUES (%s, %s, %s)", (surname, name, phone))

    else:
         cur.execute("""UPDATE PhoneBook
         SET number={}
         WHERE surname='{}' AND name='{}'
         """.format(phone,surname, name))

def loopinsert():
    banned=[]
    while True:
        print("Want to enter a person's data? yes/no")
        mode=input()
        if mode == "no":
             break
        print("Enter surname, name, phone (separated by spaces):")
        person = input().split()  # деректерді бір қатарға енгізу
        
        if len(person) != 3:  # 3 дерек болуын тексереміз
            print("Incorrect input format. You must enter surname, name, and phone number.")
            banned.append(person)
            continue
        
        if not person[2].isdigit():  # Телефон нөмірі сан екенін тексереміз
            print("Phone number should be digits only.")
            banned.append(person)
            continue
        
        insert(*person)  # енгізілген деректерді insert функциясына жіберу
    
    if len(banned) > 0:
        print("This data were not added due to incorrect format:")
        for i in banned:
            print(i)


def pagination():
    query=createpattern()
    if query=="error":
        return "error"
    print("Need offset? yes/no:")
    mode=input()
    if mode=="yes":
         print("Enter offset:")
         offset=int(input())
         query+=" OFFSET {}".format(offset)
    print("Need limit? yes/no:")
    mode=input()
    if mode=="yes":
         print("Enter limit:")
         limit=int(input())
         query+=" LIMIT {}".format(limit)
    query +=";"
    return query

def delete():
    phone = input("Enter phone to delete: ")
    cur.execute(f"""
        DELETE FROM PhoneBook 
        WHERE phone = '{phone}'
    """)
    conn.commit()
    print("Deleted successfully.")


s1=createpattern()
if s1!="error":
     cur.execute(s1+";")
     print(cur.fetchall())
insert("Berik", "Serik", 12345)
loopinsert()
s1=pagination()
if s1!="error":
     cur.execute(s1+";")
     print(cur.fetchall())
delete()

conn.commit()
cur.close()
conn.close()