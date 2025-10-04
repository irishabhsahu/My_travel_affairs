from flask import Flask, request, render_template, url_for
import csv, os
from datetime import datetime
import json

app = Flask(__name__)

DATA_DIR = os.path.join(app.root_path, "data")
os.makedirs(DATA_DIR, exist_ok=True)
CSV_FILE = os.path.join(DATA_DIR, "users.csv")

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "timestamp","username","password","email","whatsapp","updates","country_clicked","category"
        ])

# ----------------------
# Destinations data
# ----------------------
DESTINATIONS = [
    { "name": "Japan", "img": "img/japan.jpeg",
      "cities": ["Tokyo", "Kyoto", "Osaka", "Hiroshima"],
      "itinerary": [
          { "morning": "Arrival in Japan" },
          { "morning": "Tokyo", "afternoon": "Kyoto", "evening": "Osaka" }
      ]
    },
    { "name": "Cambodia", "img": "img/cambodia.jpeg",
      "cities": ["Phnom Penh", "Siem Reap", "Tonle Sap", "Angkor Thom", "Angkor Wat"],
      "itinerary": [
          {
            "morning": "Arrival at Phnom Penh airport, transfer to hotel",
            "afternoon": "Visit Royal Palace, Silver Pagoda, National Museum",
            "evening": "Walk along Riverfront Park, visit Central Market"
          },
          {
            "morning": "Visit Tuol Sleng Genocide Museum and Russian Market",
            "afternoon": "Shuttle bus to Siem Reap",
            "evening": "Overnight at hotel in Siem Reap"
          }
      ]
    },
    { "name": "France", "img": "img/france.jpeg",
      "cities": ["Paris", "Nice", "Lyon"],
      "itinerary": [
          { "morning": "Arrival in France" },
          { "morning": "Paris", "afternoon": "Lyon", "evening": "Nice" }
      ]
    },
    { "name": "Greece", "img": "img/greece.jpeg",
      "cities": ["Athens", "Santorini", "Mykonos"],
      "itinerary": [
          { "morning": "Arrival in Greece" },
          { "morning": "Athens", "afternoon": "Santorini", "evening": "Mykonos" }
      ]
    },
    { "name": "Malaysia", "img": "img/malaysia.jpeg",
      "cities": ["Kuala Lumpur", "Penang", "Langkawi"],
      "itinerary": [
          { "morning": "Arrival in Malaysia" },
          { "morning": "Kuala Lumpur", "afternoon": "Penang", "evening": "Langkawi" }
      ]
    },
    { "name": "Oman", "img": "img/oman.jpeg",
      "cities": ["Muscat", "Nizwa", "Salalah"],
      "itinerary": [
          { "morning": "Arrival in Oman" },
          { "morning": "Muscat", "afternoon": "Nizwa", "evening": "Salalah" }
      ]
    }
]

POPULAR_CHOICES = ["Japan", "France", "Greece", "Malaysia", "Oman"]

# ----------------------
# Routes
# ----------------------
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    email = request.form.get('email', '')
    whatsapp = request.form.get('whatsapp', '')
    updates = 'Yes' if request.form.get('updates') else 'No'
    country = request.form.get('country', '')
    category = request.form.get('category', '')

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(), username, password, email, whatsapp, updates, country, category
        ])
    return "Sign-in successful! ✅"

@app.route('/contact', methods=['POST'])
def contact():
    username = request.form.get('username', '')
    whatsapp = request.form.get('whatsapp', '')
    message = request.form.get('message', '')
    country = request.form.get('country', '')
    category = request.form.get('category', '')

    CONTACT_FILE = os.path.join(DATA_DIR, "contacts.csv")
    if not os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp","username","whatsapp","message","country_clicked","category"])

    with open(CONTACT_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().isoformat(), username, whatsapp, message, country, category])

    return "Message sent successfully! ✅"

@app.route('/test')
def test():
    return "Hello, Flask is working!"

@app.route('/itinerary/<country>')
def itinerary(country):
    country_data = next((d for d in DESTINATIONS if d['name'].lower() == country.lower()), None)
    if not country_data:
        return "Country not found!", 404

    # Make sure each destination has a proper static URL for JS
    destinations_with_urls = []
    for d in DESTINATIONS:
        d_copy = d.copy()  # avoid modifying original
        d_copy['img'] = url_for('static', filename=d_copy['img'])
        destinations_with_urls.append(d_copy)

    return render_template(
        'itinerary.html',
        country_name=country_data['name'],
        country_img=url_for('static', filename=country_data['img']),
        destinations_json=json.dumps(destinations_with_urls),
        popular_choices_json=json.dumps(POPULAR_CHOICES)
    )

@app.route('/search')
def search():
    query = request.args.get('q', '')
    return render_template('search_results.html', query=query)

if __name__ == '__main__':
    app.run(debug=True)