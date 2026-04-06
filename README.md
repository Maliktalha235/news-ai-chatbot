# 📰 News AI Chatbot

An AI-powered chatbot that scrapes live news headlines from Geo News, stores them in a MySQL database, and answers your questions using an LLM API.

> Built as part of my AI Engineering internship to learn web scraping, database integration, and LLM API usage.

---

## 🚀 What It Does

- Scrapes latest headlines from Geo News in real time
- Stores headlines in a MySQL database
- Uses Groq LLM API to answer questions based on scraped news
- Runs as an interactive terminal chatbot

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.10 | Core language |
| BeautifulSoup4 | Web scraping |
| MySQL | Data storage |
| Groq API (llama-3.1) | LLM responses |
| mysql-connector-python | Database connection |

---

## 📁 Project Structure

```
news-ai-chatbot/
│
├── scrape.py          # Scrapes headlines and saves to MySQL
├── database.py        # Database connection and setup functions
├── news_chatbot.py    # AI chatbot that answers questions
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
pip install requests beautifulsoup4 mysql-connector-python groq
```

**3. Setup MySQL**
```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'yourpassword';
FLUSH PRIVILEGES;
```

**4. Add your API key**

In `news_chatbot.py`, replace:
```python
api_key="your_groq_key_here"
```
Get a free key at: https://console.groq.com

**5. Run the scraper first**
```bash
python scrape.py
```

**6. Start the chatbot**
```bash
python news_chatbot.py
```

---

## 💬 Example

```
News Chatbot Ready! Ask me about today's news.
Type 'quit' to exit

You: What is the latest news about Pakistan?
Bot: Based on today's headlines, Pakistan's inflation forecast
     has been raised to 7.5% amid Middle East tensions...
```

---

## 📚 What I Learned

- Web scraping with BeautifulSoup and handling 403 blocks
- MySQL database design and connection management
- Integrating LLM APIs (RAG pattern)
- Debugging real-world errors independently

---

## 👤 Author

**Talha** — AI Engineer Intern
GitHub: [@Maliktalha235](https://github.com/Maliktalha235)
