# AI Customer Service Chatbot

A Python-based customer service chatbot that answers user questions in real time using sentence similarity and a knowledge base. Designed to demo plug-and-play automation for business FAQs, with a clean UI.

---

## What This Does

This project implements a real, interactive customer service chatbot.
Users can type questions in natural language (even slang or typos) and the bot will match to the closest answer in its knowledge base.
I included 100+ real user question variations for robust coverage. The UI is clean and professional after a few ugly first drafts.

---

## Key Features

- Universal FAQ matching: Works with a customizable CSV knowledge base

- Modern UI: Responsive CSS, animated answer display, looks good on desktop and mobile

- Handles typos and slang: Not just exact matching

- Plug-and-play: Swap in your own CSV data, no code changes

- Live demo ready: Flask backend, HTML+CSS frontend

--- 

## Setup & Installation

You'll need Python 3.8+ and a few libraries.
Install dependencies with:

```bash
pip3 install flask pandas sentence-transformers scikit-learn
```

That’s it. No external APIs or paid services needed.

---

## Universal Usage & Custom Data

You can use this script for any company, FAQ, or info domain—just change the CSV.
Examples

Start the server locally:

```bash
python3 main.py
```

Go to:

http://localhost:5000

To change the chatbot's knowledge:

    Edit or replace knowledge_base.csv (columns: question,answer)

    Reload the page

---

## How to Run

Just run the main script:

```bash
python3 main.py
```

The app will:

- Load the chatbot UI at localhost:5000

- Respond to user questions in real time

- Match even messy/natural questions to the right answer

- Let you upload a new FAQ (CSV) from the web UI

---

## Understanding the Results

- The bot answers 100+ types of questions, including order status, support, returns, payments, and more

- If the bot isn’t confident, it will offer to connect the user to a human

---

## What I Learned

This was my first chatbot project where:

- I started with a basic UI, but after some ugly attempts, I improved my frontend and made it look professional

- I focused on handling messy user input and making the bot useful for real support

- I made it easy to extend with more data or for new companies

---

## Next Steps & Improvements

Some ideas for future versions:

- Add real order lookup and user authentication

- Human handoff/live chat integration

- Multilingual support

- Admin dashboard for analytics

---

Ian Angel, 2025
