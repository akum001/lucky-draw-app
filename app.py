from flask import Flask, render_template, request, jsonify
import csv
import io
import random

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not file.filename.endswith(('.csv', '.txt')):
        return jsonify({'error': 'Only CSV and TXT files are allowed'}), 400
    
    try:
        # Read file content
        file_content = file.read().decode('utf-8')
        names = []
        
        if file.filename.endswith('.csv'):
            # Parse CSV file
            csv_reader = csv.reader(io.StringIO(file_content))
            for row in csv_reader:
                # Add all non-empty values from each row
                names.extend([name.strip() for name in row if name.strip()])
        else:
            # Parse TXT file (one name per line)
            names = [line.strip() for line in file_content.split('\n') if line.strip()]
        
        if not names:
            return jsonify({'error': 'No names found in file'}), 400
        
        return jsonify({
            'success': True,
            'total_names': len(names),
            'names': names
        })
    
    except Exception as e:
        return jsonify({'error': f'Error processing file: {str(e)}'}), 400

@app.route('/generate', methods=['POST'])
def generate_names():
    data = request.get_json()
    
    if not data or 'names' not in data or 'count' not in data:
        return jsonify({'error': 'Invalid request data'}), 400
    
    names = data['names']
    count = data['count']
    
    if not isinstance(names, list) or not names:
        return jsonify({'error': 'Names list is empty or invalid'}), 400
    
    try:
        count = int(count)
        if count <= 0:
            return jsonify({'error': 'Count must be greater than 0'}), 400
        
        if count > len(names):
            return jsonify({'error': f'Cannot select {count} names from {len(names)} total names'}), 400
        
        # Generate random selection without replacement
        selected_names = random.sample(names, count)
        
        return jsonify({
            'success': True,
            'selected_names': selected_names
        })
    
    except ValueError:
        return jsonify({'error': 'Invalid count value'}), 400
    except Exception as e:
        return jsonify({'error': f'Error generating names: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)