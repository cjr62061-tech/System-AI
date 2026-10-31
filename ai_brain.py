import datetime
import requests

class SuperAI:
    def __init__(self):
        self.name = "Bhai AI"
        self.memory = []

    def chat(self, msg):
        msg_low = msg.lower()
        self.memory.append(msg)

        if "time" in msg_low:
            return f"Time hai {datetime.datetime.now().strftime('%H:%M')}"
        elif "ias" in msg_low:
            return "IAS ke liye MA Political Science best hai, mai notes bhi de dunga"
        elif "photo" in msg_low or "image" in msg_low:
            return "IMAGE: mai photo bana sakta hu, prompt de"
        elif "weather" in msg_low:
            return self.get_weather()
        elif "code" in msg_low:
            return "Bata kaunsa code chahiye? Python, Flask, APK?"
        else:
            return f"Samjha bhai: '{msg}'. Mai super AI hu, sab karunga. Agla command de!"

    def get_weather(self):
        try:
            r = requests.get("https://wttr.in/Raipur?format=3", timeout=5)
            return r.text
        except:
            return "Weather abhi nahi la paya, internet check kar"