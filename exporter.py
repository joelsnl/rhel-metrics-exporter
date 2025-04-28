from flask import Flask, Response
import psutil

app = Flask(__name__)

def generate_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    metrics = f"""
# HELP system_cpu_usage CPU usage percentage
# TYPE system_cpu_usage gauge
system_cpu_usage {cpu}

# HELP system_memory_usage Memory usage percentage
# TYPE system_memory_usage gauge
system_memory_usage {memory}

# HELP system_disk_usage Disk usage percentage
# TYPE system_disk_usage gauge
system_disk_usage {disk}
"""
    return metrics

@app.route('/metrics')
def metrics():
    return Response(generate_metrics(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
