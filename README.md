# 🎬 Smart Media Server (v2.0)

Turn your PC into a local **Netflix-style Streaming Service**.  
Select a folder, start the server, and watch your media on any device on your Wi-Fi (Phone, TV, Tablet) with a beautiful dark interface.



![Screenshot](https://github.com/user-attachments/assets/0f8b61e4-a86f-4597-a700-be44e7805702)

![Screenshot](https://github.com/user-attachments/assets/f7f9342e-631c-4094-a5ce-afba595aa075)

![Screenshot](https://github.com/user-attachments/assets/7ecf64fe-1508-4085-a073-c7a3686a991b)

## ✨ New in v2.0 (The "Pro" Update)
- **🖼️ Auto-Metadata:** Automatically fetches Movie Posters, Titles, and Ratings from TMDB.
- **❤️ Favorites System:** "My List" feature to save media you want to watch.
- **🔐 PIN Security:** Optional PIN protection to keep your library private.
- **🖥️ Modern Control Panel:** Sleek Dark-Mode Windows UI with System Tray support.
- **👀 Live Client Monitor:** See who is connected to your server in real-time.
- **📁 Smart Folders:** Recognizes TV Show folders and applies special badges.

## ⚡ Core Features
- **Auto-Discovery:** Generates a QR Code and IP link automatically.
- **Resume Playback:** Remembers exactly where you left off on any device.
- **Dual Audio Support:** "Open in VLC" button for changing audio tracks/subtitles.
- **Batch Download:** Zip & Download entire seasons/folders with a progress bar.
- **Search & Sort:** Filter by Name, Date, Size, or Favorites.

## 🚀 Download
[Download the latest .exe here](https://github.com/adnaanaeem/Smart-Media-Server/releases/latest)

## 🔮 Upcoming Features (Roadmap)
- [ ] **Genre Filtering** (Action, Comedy, Sci-Fi filters).
- [ ] **Watch Party** (Sync video playback with friends).
- [ ] **Remote Access** (Share link over the internet).
- [ ] **User Accounts** (Separate history for different users).

## 🛠️ How to Run from Source
1. **Install Python 3.x**
2. **Clone the repo:**
   ```bash
   git clone https://github.com/adnaanaeem/Smart-Media-Server.git

## 🛠️ How to Run from Source
1. Install Python 3.x
2. Clone the repo:
   ```git clone https://github.com/adnaanaeem/Smart-Media-Server.git```

## 1. Install dependencies:

```pip install -r requirements.txt```

## 2. Run the app:

```python media_server.py```

##📦 How to Build EXE

```pyinstaller --noconsole --onefile --icon=static/favicon.ico --name="SmartMediaServer" --add-data "templates;templates" --add-data "static;static" --collect-all customtkinter media_server.py```

📄 License
This project is open-source under the MIT License.

## ⚖️ Credits & Attribution
Movie metadata and posters are provided by **[The Movie Database (TMDB)](https://www.themoviedb.org/)**.
This product uses the TMDB API but is not endorsed or certified by TMDB.