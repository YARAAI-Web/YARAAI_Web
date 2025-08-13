# YARAAI_Web

> **Automated Malware Analysis and YARA Rule Generation Platform**  
> YARAAI_Web is a web-based malware analysis platform that integrates static/dynamic analysis results to automatically generate YARA rules, visualize findings, and support threat hunting workflows.

---

##  Features

- **File Upload & Analysis**
  - Upload PE files (`.exe`, `.dll`) via a web interface
  - Automatic static and dynamic analysis pipeline
- **YARA Rule Generation**
  - Extracts key artifacts from analysis results
  - Automatically generates YARA rules from JSON output
- **Suricata Rule Conversion**
  - Converts generated YARA rules into Suricata signatures for network detection
- **Interactive Visualization**
  - Function Call Graph visualization (PyVis)
  - CAPA rule hits, MITRE ATT&CK mapping, CWE mapping
- **Report Generation**
  - HTML-based interactive reports

---

##  Tech Stack

### Backend
- **FastAPI** – REST API server for file analysis & rule generation
- **Python 3.10+** – Main language for data processing & automation
- **CAPA** – Capability-based malware analysis
- **Suricata** – Network IDS integration

### Frontend
- **React + TypeScript** – User interface
- **Vite** – Build tool for fast development

### Analysis Tools
- **Cuckoo Sandbox** – Dynamic malware analysis
- **YARA** – Signature-based detection
- **VirusTotal API** – Threat intelligence enrichment

---

## Project Structure

```
YARAAI_Web/
├── backend/            # API 서버 (FastAPI)
├── public/             # 정적 리소스
├── src/                # React 소스 코드
│   ├── components/     # UI 컴포넌트
│   ├── pages/          # 페이지 단위
│   ├── hooks/          # 커스텀 훅
│   ├── services/       # API 연동 로직
│   └── utils/          # 공용 유틸
├── tailwind.config.js  # Tailwind 설정
├── vite.config.ts      # Vite 빌드 설정
└── package.json

```
##  Installation & Setup

### 1. Clone Repository
- git clone https://github.com/YARAAI-Web/YARAAI_Web.git
- cd YARAAI_Web
  
### 2. Backend Setup
- cd backend
- python -m venv venv
- source venv/bin/activate  # Windows: venv\Scripts\activate
- pip install -r requirements.txt

### 3. Frontend Setup
- npm install
- npm run dev
  
### Usage
Start Backend
uvicorn main:app --reload --port 8000
Start Frontend
npm run dev
Access Web UI
Open http://localhost:5173 in your browser.

---

### 2. Workflow
Upload File – User uploads .exe/.dll

Static Analysis – Extract sections, imports, strings

Dynamic Analysis – Execute in Cuckoo Sandbox & capture behaviors

YARA Rule Generation – Extract IoCs & create detection rules

Visualization – Call graph, MITRE ATT&CK mapping, CWE mapping

Report – Generate HTML report and optionally export Suricata rules

```
## Example Generated YARA Rule
rule AutoGen_1234abcd
{
    meta:
        description = "Auto-generated rule from sample analysis"
        author = "YARAAI_Web"
    strings:
        $s1 = "VirtualAllocEx"
        $s2 = "CreateRemoteThread"
    condition:
        all of them
}
```
License
This project is licensed under the MIT License.

```
Author: YARAAI_Web Development Team
Email: malyaraai72@gmail.com 
