from groq import Groq
from database import get_connection

conn=get_connection()
cursor=conn.cursor()
cursor.execute("Select headline from headlines")
rows=cursor.fetchall()
cursor.close()
conn.close()

headlines="\n".join([row[0]for row in rows])

#starting chatbot
print("New Chatbot Ready! Ask me About today's news.")
print("Type quit to exit\n")
client=Groq(api_key="your-API-key")

while True:
    question= input("You:")
    if question.lower()=="quit":
        break
    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role":"system","content":f"Yor are a news assitant. Only answer based  on these headlines:\n{headlines}"},
            {"role": "user","content": question}
            ])
    print("Bot:", response.choices[0].message.content)
    print()