# 🔓 Claude Opus 4.6 Unlocked

<div align="center">
  <a href="../../releases/latest">
    <img width="1200" alt="Claude Opus 4.6 Unlocked." src="assets/opus.png" />
  </a>
</div>

> **⚠️ WARNING / DISCLAIMER**
> This application is an experimental tool for **Security Research**. It utilizes browser fingerprint spoofing and token rotation methods to bypass paid access restrictions. The authors are not responsible for the use of this software.

## 💀 What is this?

**Claude Opus 4.6 Unlocked** is a local server and command-line interface that turns your computer into a control terminal for the world's most powerful neural network **for free**.

Unlike the official web interface, there are no limits on the number of messages, no censorship (with Jailbreak mode enabled), and Enterprise-level features are unlocked.

---

## 🔥 Key Features (v4.6)

We have reverse-engineered the new Opus 4.6 features and implemented their local emulation:

### 🕵️ Agent Swarms

Native support for creating hierarchical agent teams.

* **How it works here:** The application launches multiple parallel sessions (instances). One "Main" Opus manages sub-agents.
* **Roles:** You can assign specialized sub-agents: *Coder* (writes code), *Researcher* (googles), *Reviewer* (critiques).
* **Autonomy:** Agents exchange files and context via the local `./workspace` folder until the task is solved.

### 🧠 Adaptive Compute (Force Max Thinking)

Selection of "effort" levels (`Low`, `Medium`, `High`, `Max`).

* **The Hack:** We intercept the request header and forcibly set the `thinking_effort="max"` flag even for free tokens.
* **Result:** The model activates the hidden "Chain-of-Thought" (CoT) layer, spending 10x more Anthropic server compute resources on your answer. It *truly* thinks before responding.

### 💾 Infinite Context Handling (1M+ Tokens)

Work with context up to 1 million tokens.

* **Implementation:** We use a hybrid approach.
1. **Context Compaction:** An algorithm compresses old parts of the dialogue into a "summary" without losing meaning.
2. **Local RAG:** If the context exceeds the browser session limit, the app automatically creates a local vector database (ChromaDB) and pulls necessary dialogue chunks as needed.



### 🕸️ Deep Browsing (Stealth Spider)

Improved search module.

* **Capabilities:** Capable of parsing complex JS sites (React/Vue) and downloading PDF documents in real-time.
* **Anti-Detect:** Uses a built-in headless browser with bot-filter protection (Cloudflare bypass) to read sites that block ordinary bots.

---

## 🛠 Installation & Launch

We provide pre-compiled binaries. No Python or Node.js environment setup is required.

### Step 1: Download
Navigate to the **[Releases](../../releases)** page and download the latest archive for your architecture:
* `opus-4-6-x64.exe`

### Step 2: Unzip
Extract the archive to a permanent location, e.g., `C:\Tools\opus-4-6-x64`.
*(Optional: Add this folder to your System PATH to run it from any terminal window).*

### Step 3: First Run
Run `opus-4-6-x64.exe`. On the first launch, you will be prompted to enter your **Anthropic API Key**.
The key is securely stored using the Windows Credential Manager.


---

## 💻 Operation Modes

The application supports three modes via command-line arguments.

### 1. Interactive Chat (CLI)

Simple terminal chat with Markdown support.

### 2. Swarm Mode

Fully automatic solution of a complex task by a group of agents.

*The system will create files, verify them, and save them to the folder.*

### 3. API Server (Localhost)

Launches a local REST API compatible with the OpenAI format. You can connect this address (http://localhost:8000/v1) in VS Code (via the Continue plugin or Cursor) to use code autocompletion for free.

---

## ⚙️ Functions & Commands

Inside the CLI, special slash commands are available to control the new v4.6 features:

| Command | Description |
| --- | --- |
| `/compaction on` | Enables context compression algorithm (Infinite Memory). |
| `/browse "URL"` | Forcibly launches Deep Browsing on the specified link (parses even PDFs). |
| `/upload <path>` | Uploads a file to context (chunks it if it's huge). |
| `/effort <level>` | Changes thinking level on the fly (`low`, `medium`, `high`, `max`). |
| `/team status` | Shows what the agents are currently doing in Swarm mode. |
| `/spoof` | Generates a new browser fingerprint and IP (via Tor/Proxy). |

---

## 🔧 Config.yaml

Customize the app for yourself:

```yaml
network:
  use_tor: true            # Use Tor network for anonymity
  proxies:                 # List of your proxies (optional)
    - "socks5://user:pass@1.2.3.4:1080"
  
behavior:
  default_effort: "high"   # Always think deep
  auto_jailbreak: true     # Automatically add DAN prompts
  
storage:
  vector_db_path: "./memory" # Where to store agent's "eternal" memory

```

---

## 🤝 Roadmap

* [x] Bypass Paywall & Auth
* [x] Agent Swarms (v4.6 native support)
* [x] PDF & Deep Browsing Parsing
* [x] **Desktop App** (.exe/.dmg installer)
* [ ] **Voice Input** (Real-time conversation with Claude)
* [ ] Telegram Bot API Integration

---
