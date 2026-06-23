from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>DevSecOps Pipeline</h1>
    <p>Developed by Madhukar Pendalwar</p>
    <p>Secured with GitHub Actions + Trivy + Docker</p>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy', 'app': 'devsecops-pipeline'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
