🖥️ System Health Monitoring Dashboard
A real-time system monitoring dashboard built using Python (Flask) and Chart.js to display CPU, Memory, and Disk usage. It logs system health metrics to a SQLite database and supports CSV download of all records. The dashboard auto-refreshes every 10 seconds and includes alert warnings when usage exceeds safe thresholds.

🔧 Tech Stack
Backend: Python, Flask, psutil, SQLite

Frontend: HTML, CSS, Chart.js

Optional Features: Auto-refresh, CSV download, usage logging

🚀 Features
✅ Displays current CPU, Memory, and Disk usage

✅ Highlights high usage with alert messages (above 80%)

✅ Line chart of last 10 usage entries using Chart.js

✅ Logs data to system_health.db (SQLite)

✅ Auto-refreshes every 10 seconds

✅ One-click CSV export of historical data

▶️ How to Run the Project
1.Clone the repo
git clone https://github.com/yourusername/system-monitor.git
cd system-monitor

2.Install dependencies
pip install -r requirements.txt

3.Run the Flask app
python app.py

4.Visit in browser
http://127.0.0.1:5000

📥 CSV Download
Click the ⬇️ Download CSV button to export all system health logs as a .csv file.

Data includes timestamp, CPU, memory, and disk usage.

