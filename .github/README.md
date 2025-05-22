
<h1 align="center">
DeadlineTech Music
</h1>

<p align="center">
    <img src="https://files.catbox.moe/lxn8yz.jpg" width="400">
</p>

<p align="center">
    <a href="https://github.com/deadlineTech/Music/stargazers">
        <img src="https://img.shields.io/github/stars/deadlineTech/Music?color=ffd700&style=for-the-badge&logo=github" />
    </a>
    <a href="https://github.com/deadlineTech/Music/network/members">
        <img src="https://img.shields.io/github/forks/deadlineTech/Music?color=blue&style=for-the-badge&logo=github" />
    </a>
    <a href="https://github.com/deadlineTech/Music/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/deadlineTech/Music?color=purple&style=for-the-badge&logo=open-source-initiative" />
    </a>
    <a href="https://www.python.org">
        <img src="https://img.shields.io/badge/Made%20With-Python-306998?style=for-the-badge&logo=python&logoColor=yellow" />
    </a>
</p>

---

## 🎧 Advanced Telegram Group Music Bot

> A modern Telegram bot for high-quality group music streaming using PyTgCalls and API keys.

---

## ✨ Features

- 🎵 Stream music in group voice/video chats
- 🚀 Fast, stable and scalable performance
- 🖼️ Auto thumbnails with song metadata
- 🎛️ Full admin control panel
- 🧠 Smart music queue system
- ⚙️ Easy to deploy via Heroku or VPS

---

## 📜 Commands Introduction

> Below are the main commands to interact with the bot.

### 🎵 Music Playback
- `/play <song name or YouTube URL>` – Stream music/audio in VC.
- `/vplay <video name or URL>` – Play videos directly in video chat.
- `/pause` – Pause the current stream.
- `/resume` – Resume a paused stream.
- `/skip` – Skip to the next song in queue.
- `/end` – Stop the music and clear the queue.

### 🧰 Utilities
- `/start` – Start the bot and get welcome/help message.
- `/help` – Show detailed help menu with available commands.
- `/ping` – Check bot’s latency and responsiveness.
- `/stats` – View bot usage stats and system info.

### 🎛️ Admin Controls
- `/auth` – Authorize a user to use admin commands.
- `/unauth` – Remove a user from authorized list.
- `/authusers` – Show list of authorized users.

### 📋 Queue System
- `/queue` – Show the current music queue.
- `/shuffle` – Shuffle the songs in queue.
- `/loop` – Toggle loop for current song.

---

## 🔐 Get Your API Key

- 🌐 [Buy from Website](https://deadlinetech.site)
- 📩 [Contact Developer](https://t.me/DeadlineTechOwner)

---

## 🚀 Deployment Options

<details>
<summary><b>🔹 Deploy to Heroku </b></summary>

[![Deploy](https://img.shields.io/badge/Deploy%20to-Heroku-4700f5?style=for-the-badge&logo=heroku)](https://dashboard.heroku.com/new?template=https://github.com/deadlineTech/Music)

</details>

<details>
<summary><b>🔸 Deploy on VPS / Localhost</b></summary>
    
**1.Install Dependencies**

```bash
sudo apt-get update && sudo apt-get upgrade -y
```
```bash
sudo apt-get install python3-pip ffmpeg -y
```
```bash
sudo pip3 install -U pip
```

**2. Install NodeJS**
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash && source ~/.bashrc && nvm install v18
```

**3. Clone & Setup Project**
```bash
git clone https://github.com/deadlineTech/music
```
```bash
cd music
```
```bash
pip3 install -U -r requirements.txt
```

**4. Create .env with sample.env**
```bash
cp sample.env .env
```
- Edit .env with your vars

**5. Editing Vars:**
```bash
vi .env
```

- Press I button on keyboard to start editing.
- Press Ctrl + C once you are done with editing vars and type :wq to save .env or :qa to exit editing.

 **6. Run the Bot**
```bash
sudo apt install tmux && tmux
```
```bash
bash start
```
(Detach: Ctrl + B then D)

</details>

---

## 🔧 Environment Variables

> Copy from `sample.env` and configure:

```env
API_ID=123456
API_HASH=abcdef1234567890abcdef1234567890
BOT_TOKEN=YOUR_BOT_TOKEN
OWNER_ID=123456789
MONGO_DB_URI=mongodb+srv://username:password@cluster.mongodb.net/dbname
API_KEY=  #Get api key from @DeadlineApiBot
STRING_SESSION=YOUR_STRING_SESSION
```

---

## 👥 Support & Community

- 🔔 [Channel](https://t.me/DeadlineTechTeam)
- 💬 [Support Group](https://t.me/DeadlineTechSupport)
- 🧑‍💻 [Developer Contact](https://t.me/DeadlineTechOwner)

---

## 🧠 Credits

- ⚙️ Base: [Anon Music](https://github.com/AnonymousX1025/AnonXMusic)
- 💻 Core Contributors: `@DeadlineTechOwner`, Open Source Helpers

---

## 📄 License

> This project is licensed under the MIT License.

---

## 🔗 Quick Links

- 💰 [Buy API Key](https://deadlinetech.site)
- 👨‍💻 [Developer Contact](https://t.me/DeadlineTechOwner)
- 🛠️ [Join Support Group](https://t.me/DeadlineTechSupport)

---

<p align="center">
  <b>Made with ❤️ by <a href="https://t.me/DeadlineTechTeam">DeadlineTech</a></b>
</p>
