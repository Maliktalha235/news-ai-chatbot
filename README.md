# 📰 News AI Chatbot

An AI-powered pipeline that scrapes live news from Geo News, analyzes sentiment,
and lets you query everything through a FastAPI REST API and terminal chatbot.

> Built as part of my AI Engineering internship to learn web scraping,
> NLP, LLM APIs, and FastAPI.

---

## 🚀 What It Does

- Scrapes latest headlines from Geo News automatically
- Stores headlines in MySQL with no duplicates
- Analyzes sentiment of each headline using LLM (Groq API)
- Exposes everything as a REST API using FastAPI
- Runs as an interactive terminal chatbot with conversation memory

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.10 | Core language |
| BeautifulSoup4 | Web scraping |
| NLTK | Text preprocessing |
| MySQL | Data storage |
| Groq API (llama-3.1) | LLM responses + sentiment |
| FastAPI | REST API framework |
| Uvicorn | API server |

---

## 📁 Project Structure

```
news-ai-chatbot/
│
├── database.py          # Database connection and setup
├── scrape.py            # Scrapes headlines from Geo News
├── sentiment.py         # LLM-based sentiment analysis
├── news_chatbot.py      # Terminal chatbot with memory
├── api.py               # FastAPI REST API
├── main_pipeline.py     # Runs full pipeline automatically
└── README.md
```

---

## ⚙️ Setup & Run

**1. Clone the repo**
```bash
git clone https://github.com/Maliktalha235/news-ai-chatbot
cd news-ai-chatbot
```

**2. Install dependencies**
```bash
pip install requests beautifulsoup4 mysql-connector-python groq fastapi uvicorn nltk
```

**3. Setup MySQL**
```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'yourpassword';
FLUSH PRIVILEGES;
```

**4. Add your Groq API key**

Get a free key at: https://console.groq.com

Replace in `sentiment.py`, `news_chatbot.py` and `api.py`:
```python
api_key="your_groq_key_here"
```

**5. Run the full pipeline**
```bash
python main_pipeline.py
```

**6. Start the API (optional)**
```bash
uvicorn api:app --reload
```

---

## 🌐 API Endpoints

| Endpoint | Description | Example |
|---|---|---|
| GET /news | API status check | /news |
| GET /read | All headlines | /read |
| GET /sentiment | Headlines with sentiment labels | /sentiment |
| GET /sentiment_search | Filter by sentiment | /sentiment_search?choice=Positive |
| GET /search | Search by keyword | /search?keyword=Pakistan |
| GET /chat | Ask AI about today's news | /chat?question=Latest Pakistan news? |

---

## 💬 Example

**Terminal chatbot:**
```
News Chatbot Ready! Ask me about today's news.
You: What is the latest news about Pakistan?
Bot: Pakistan's inflation forecast has been raised to 7.5%...
```

**API:**
```
GET /search?keyword=Pakistan
→ returns all Pakistan related headlines with sentiment
```

---

## 📚 What I Learned

- Web scraping with BeautifulSoup and handling 403 blocks
- MySQL database design, connection management, duplicate prevention
- NLP concepts — tokenization, stopwords, stemming, sentiment analysis
- VADER limitations vs LLM-based sentiment for news headlines
- Building RAG pipelines — giving LLMs custom data as context
- REST API development with FastAPI
- Debugging real-world errors independently

---

## 👤 Author

**Talha Malik** — AI Engineer Intern
GitHub: [@Maliktalha235](https://github.com/Maliktalha235)
LinkedIn: [Talha Malik](https://www.linkedin.com/in/talha-malik-664189310/)]
