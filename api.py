from fastapi import FastAPI
from database import get_connection
from groq import Groq


app=FastAPI()

def fetch_data(query,params=None):
    conn=get_connection()
    cursor=conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return data

@app.get("/news")
def home():
    return{"message":"News API is running"}

@app.get("/read")
def read():
    query="select headline from headlines"
    data=fetch_data(query)
    headlines=[row[0] for row in data]
    return{"headlines":headlines}

@app.get("/sentiment")
def sentiment():
    query="Select headline, sentiment_label from headlines"
    data= fetch_data(query)
    results=[]
    for row in data:
        results.append(
            {
                "Headlines":row[0],
                "Sentiment":row[1]
            }
        )
    return{"News":results}

@app.get("/sentiment_search")
def sentiment_search(choice:str):
    query="Select headline,sentiment_label from headlines where sentiment_label=%s"
    data=fetch_data(query,(choice,))
    results=[]
    for row in data:
        results.append(
            {
                "Headlines":row[0],
                "Sentiment":row[1]
            }
        )
    return{"News":results}

@app.get("/chat")
def chat(question:str):
    query="Select headline,sentiment_label from headlines"
    data=fetch_data(query)
    context=""
    for row in data:
        context +=f"- {row[0]} [{row[1]}]\n"
    client=Groq(api_key="")
    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"system","content":f"You are news assistant only. Only answer based on these headlines:\n{context}"},{"role":"user","content":question}]
        )
    answer=response.choices[0].message.content
    return {"answer":answer}

@app.get("/search")
def search(keyword:str):
    query="Select headline,sentiment_label from headlines where headline like %s"
    data=fetch_data(query,(f"%{keyword}%",))
    results=[]
    for row in data:
        results.append({
            "headline":row[0],
            "sentiment":row[1]
        })
    return{"Result":results}