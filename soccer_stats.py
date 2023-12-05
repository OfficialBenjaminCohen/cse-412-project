import pandas as pd
import numpy as np
import warnings

warnings.simplefilter(action="ignore", category=UserWarning)

import psycopg2

# replace with database dump
conn = psycopg2.connect(
    dbname="players-project",
    user="ben",
    password="",
    host="localhost",
)

# Edit queries to specify the data you wish to show
pd.set_option("display.float_format", "{:.2f}".format)
pd.set_option("display.precision", 2)  #


query = "SELECT C.c_langs[1] as Language_Spoken_By_Players, sum(P.p_goalsscored) as Goals FROM player P left join country C on P.p_citizenOf = C.c_name  group by C.c_langs[1] order by goals desc;"

df = pd.read_sql_query(query, conn)
df.fillna("Other", inplace=True)
print("The Languages That Score the Most:")
print(df)
print("\n")
print("\n")

print("\n")

print("\n")

print("The Highest Paid Managers in the Premier League:")
query = "SELECT S.s_name as Name, S.s_team as Team, S.s_salary as Salary, T.t_league as League from Staff S join Team T on S.s_team = T.t_name where S.s_role = 'manager'  order by s_salary desc;"
df = pd.read_sql_query(query, conn)
print(df)


print("\n")
print("\n")

print("\n")

print("\n")


print("Highest Scoring Player on Leeds United ")
query = "SELECT p_name as Name, p_goalsscored as Goals from Player where p_team = 'Leeds United' order by p_goalsscored desc limit 1;"
df = pd.read_sql_query(query, conn)
print(df)


while True:
    # Ask the user for a title
    title = input("Enter a title for your query (or 0 to stop): ")

    # Check if the user wants to stop the loop
    if title == "0":
        break

    # Ask the user for an SQL query
    sql_query = input("Enter your SQL query: ")
    try:
        df = pd.read_sql_query(sql_query, conn)
        print(title)
        print(df)
        print("\n\n\n\n")
    except Exception as e:
        print("An error occurred:", e)
    print()


conn.close()

print("Program Ended.")

# print query


# st.title("Soccer Stats Demo")
