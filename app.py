from flask import Flask,render_template
import psutil
import sqlite3

def log_to_db(cpu, memory, disk):
    conn = sqlite3.connect("system_health.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS health_log (
        timestamp TEXT, cpu REAL, memory REAL, disk REAL
    )""")
    c.execute("INSERT INTO health_log VALUES (datetime('now'), ?, ?, ?)", (cpu, memory, disk))
    conn.commit()
    conn.close()


app = Flask(__name__)

def get_system_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    log_to_db(cpu,memory,disk)

    alerts = []
    if cpu >80:
        alerts.append(f"High CPU usage:{cpu}%")
    if memory >80:
        alerts.append(f"High memory usage:{memory}%")
    if disk >80:
        alerts.append(f"High disk usage:{disk}%")

    return {
        "cpu":cpu,
        "memory":memory,
        "disk":disk,
        "alerts":alerts
    }

@app.route('/')
def index():
    health = get_system_health()
    conn = sqlite3.connect("system_health.db")
    c = conn.cursor()
    c.execute("SELECT * FROM health_log ORDER BY timestamp DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()

    rows.reverse()  # So we see data in time order

    timestamps = [r[0] for r in rows]
    cpu_data = [r[1] for r in rows]
    memory_data = [r[2] for r in rows]
    disk_data = [r[3] for r in rows]
    return render_template('index.html', health=health,
                       timestamps=timestamps,
                       cpu_data=cpu_data,
                       memory_data=memory_data,
                       disk_data=disk_data)


import csv
from flask import Response

@app.route('/download')
def download_csv():
    conn = sqlite3.connect("system_health.db")
    c = conn.cursor()
    c.execute("SELECT * FROM health_log ORDER BY timestamp DESC")
    rows = c.fetchall()
    conn.close()

    # Create CSV in memory
    def generate():
        data = ['timestamp,cpu,memory,disk\n']
        for row in rows:
            line = f"{row[0]},{row[1]},{row[2]},{row[3]}\n"
            data.append(line)
        return data

    return Response(generate(), mimetype='text/csv',
                    headers={"Content-Disposition": "attachment; filename=system_health.csv"})

if __name__ == '__main__':
    app.run(debug=True)
