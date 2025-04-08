# 🔗 Alai Presentation Automation

This project automates the creation of visually engaging **Alai presentations** from any webpage URL using the **Firecrawl API** and **Alai's internal APIs**.  
It scrapes structured content from a given website and generates a ready-to-share presentation link — **no manual effort needed**.

---

## 🚀 How It Works

Once you run the `main.py` file, the script will:

1. Take a **webpage URL** you want to turn into a presentation.  
2. **Log in to Alai** using your email and password.  
3. Use **Firecrawl API** to scrape the content from the URL.  
4. Send the structured content to Alai's backend.  
5. Return a **public presentation link** that you can open in your browser.  

---

## ⚙️ Configuration (Required Before Running)

> 🛠️ You need to set up the following variables manually for now.  
> In the future, these will be managed via a frontend or `.env` file.

| Variable                | Location               | Description                        |
|------------------------|------------------------|------------------------------------|
| `URL`                  | `main.py`              | 🔗 URL to parse                    |
| `EMAIL`                | `main.py`              | 📧 Alai login email               |
| `PASSWORD`             | `main.py`              | 🔐 Alai password                  |
| `FIRECRAWL_API_KEY`    | `firecrawl_scraper.py` | 🔑 Firecrawl API key             |

---
