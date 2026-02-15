# Lucky Draw - Random Name Generator

A beautiful, lightweight Flask application for conducting lucky draws by randomly selecting names from uploaded files.

## Features

- 📁 Upload CSV or TXT files with names
- 🎲 Random selection without replacement
- 🎨 Beautiful, responsive UI with animations
- 🚀 Production-ready and deployment-ready
- ✅ Input validation and error handling

## Local Setup

1. **Clone or create the project directory**

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## File Format

### CSV Format
```csv
John Doe,Jane Smith,Bob Johnson
Alice Williams,Charlie Brown
```

### TXT Format
```text
John Doe
Jane Smith
Bob Johnson
Alice Williams
Charlie Brown
```

## Deployment

### Deploy to Heroku

1. **Install Heroku CLI**
   ```bash
   # Visit https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create a new app**
   ```bash
   heroku create your-app-name
   ```

4. **Deploy**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```

### Deploy to Railway

1. Visit [Railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway will auto-detect Flask and deploy

### Deploy to Render

1. Visit [Render.com](https://render.com)
2. Click "New" → "Web Service"
3. Connect your repository
4. Use these settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

### Deploy to PythonAnywhere

1. Upload files to PythonAnywhere
2. Create a virtual environment
3. Install requirements
4. Configure WSGI file to point to your app

## Environment Variables

For production, you may want to set:
```bash
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

## Security Notes

- Maximum file upload size is set to 16MB
- Only CSV and TXT files are accepted
- All inputs are validated server-side

## License

MIT License - Feel free to use this for any purpose!