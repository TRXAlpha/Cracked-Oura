<div align="center">
  <img src="frontend/public/icon.png" alt="Cracked Oura Logo" width="128">
  <h1>Cracked Oura - Windows Edition</h1>
  <p><b>Free application that gives you full access to your Oura ring data, fully optimized for Windows.</b></p>
  
  ![Status](https://img.shields.io/badge/Status-Alpha-red)
  ![Platform](https://img.shields.io/badge/Platform-Windows-blue)
</div>

---

### 🚀 About This Fork
This is a Windows-optimized fork of the original [Cracked-Oura](https://github.com/EIrno/Cracked-Oura) project by EIrno. 

The original project's build scripts and dependency resolutions were heavily configured for Unix environments (Mac/Linux). This fork patches the `package.json` scripts, integrates `cross-env`, resolves React version conflicts, and fixes PyInstaller pathing so the application can be seamlessly built and run natively on Windows via PowerShell.

---

### Pay for the ring, not for the app that is not even that good
Oura ring paywalls the data behind a subscription, but luckily you can export your data from Oura and import it to Cracked Oura.

**Cracked Oura** is an open-source desktop application that provides full access to your health metrics, stored locally on your machine.

**Key Benefits**
- **No Subscription:** See all of your Oura ring data without a subscription. 
- **Privacy First:** Your data is stored locally in an SQLite database. It never leaves your computer unless you export it.
- **Advanced Analytics:** Visualize trends, correlations, and deeper insights than the standard app provides. 

<img width="1470" height="916" alt="Cracked Oura front page" src="https://github.com/user-attachments/assets/cda629a9-5072-4a5f-9e5d-6ddb3873c0f0" />

---

## Features

### Oura ring data without subscription
See all of your Oura ring data without a subscription. Thanks to the EU's right to data portability, you can export your data from Oura and import it to Cracked Oura. 

**Automation that requests your data from Oura and imports it to Cracked Oura.** This populates the local database with your data. Population can also be done manually by importing a zip file from Oura that you can find at https://membership.ouraring.com/data-export. 

<img width="1470" height="916" alt="Cracked Oura automation" src="https://github.com/user-attachments/assets/8aa42539-f014-4254-8885-9d6dfabf13b2" />
<img width="1470" height="916" alt="Cracked Oura long term charts" src="https://github.com/user-attachments/assets/6cbd5345-d81e-4000-ade0-a0ea4e21508c" />


### Desktop Dashboard that can be customized
View your Sleep, Readiness, and Activity scores in a desktop dashboard that is at least as good as the official Oura dashboard. The dashboards can be customized to show the exact data you want to see. 

<img width="1470" height="916" alt="Cracked Oura widget editor" src="https://github.com/user-attachments/assets/39103072-e176-4b13-86df-95eaacdd3ac1" />


### AI Health Analyst
Oura's own AI advisor is quite limited. It does not have access to your historical data and cannot answer questions about your health trends, because it has only a few days of data available. 

Cracked Oura can leverage local LLMs to analyze your health data and provide insights. 

> [!NOTE]
> This feature is still experimental, not documented, and under development. 

<img width="1470" height="916" alt="Cracked Oura advisor" src="https://github.com/user-attachments/assets/e9ce6ac2-60da-486f-a01f-8cd03dce6337" />

---

## Getting Started

### Installation
1.  **Download** the latest `.exe` release from the [Releases page](../../releases).
2.  **Install & Run** the application.
3.  **Login** to your Oura account when prompted to sync your historical data.

> [!NOTE]
> Most of the features are still experimental and under development. This project is not affiliated with, associated with, or endorsed by Oura Health Oy. Use at your own risk.

---

## For Developers (Windows Guide)

We welcome contributions! The instructions below are specifically tailored for Windows environments using PowerShell.

### Tech Stack
-   **Frontend:** Electron, React, TypeScript, Tailwind
-   **Backend:** Python, FastAPI, SQLite

### Build from Source
```powershell
# 1. Clone Repository
git clone [https://github.com/YOUR_USERNAME/Cracked-Oura.git](https://github.com/YOUR_USERNAME/Cracked-Oura.git)
cd Cracked-Oura

# 2. Setup Backend (PowerShell)
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
pip install pyinstaller # Required for the final build

# 3. Setup Frontend
cd ../frontend
# Use --legacy-peer-deps to bypass React 18/19 version conflicts
npm install --legacy-peer-deps

# 4. Start Development Server
npm run dev
