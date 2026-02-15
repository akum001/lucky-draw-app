# Lucky Draw - Random Name Generator

A beautiful, lightweight Flask application for conducting lucky draws by randomly selecting names from uploaded files.

## Features

- 📁 Upload CSV or TXT files with names
- 🎲 Random selection without replacement (no duplicates in results)
- 🎨 Beautiful, responsive UI with animations
- 🚀 Production-ready and deployment-ready
- ✅ Input validation and error handling
- 🔄 Automatic duplicate removal from input

---

## How It Works - The Logic Behind Lucky Draw

### 1. **File Upload & Parsing**

When you upload a file (CSV or TXT), the application processes it in the following way:

#### **For TXT Files:**
- Reads the file line by line
- Checks if each line contains commas (`,`)
  - **If YES**: Splits the line by commas and treats each part as a separate name
  - **If NO**: Treats the entire line as one name
- Strips whitespace from each name
- Example:
  ```text
  John Doe
  Jane Smith, Bob Johnson
  Alice Williams
  ```
  Results in: `["John Doe", "Jane Smith", "Bob Johnson", "Alice Williams"]` → **4 names**

#### **For CSV Files:**
- Uses Python's CSV reader to parse the file
- Each **cell** (not row) is treated as a separate name
- Handles quoted values and special characters properly
- Example:
  ```csv
  John Doe,Jane Smith,Bob Johnson
  Alice Williams,Charlie Brown
  ```
  Results in: `["John Doe", "Jane Smith", "Bob Johnson", "Alice Williams", "Charlie Brown"]` → **5 names**

#### **Duplicate Removal:**
After parsing, the app automatically removes duplicate names while preserving the original order:
```python
# If input has: ["John", "Jane", "John", "Bob"]
# Output will be: ["John", "Jane", "Bob"]
```

---

### 2. **Random Selection Algorithm**

The app uses Python's `random.sample()` function for winner selection:

```python
selected_names = random.sample(names, count)
```

#### **How `random.sample()` Works:**
- **Random**: Each name has an equal probability of being selected
- **Without Replacement**: Once a name is selected, it cannot be selected again in the same draw
- **Cryptographically Secure**: Uses Mersenne Twister algorithm (secure for fair draws)

#### **Example:**
```
Input: ["John", "Jane", "Bob", "Alice", "Charlie"]
Request: 3 winners

Possible outcomes (each equally likely):
- ["Jane", "Charlie", "Alice"]
- ["Bob", "John", "Jane"]
- ["Alice", "Charlie", "Bob"]
... and so on
```

#### **Why This Method?**
- ✅ **Fair**: Every name has equal chance
- ✅ **No Duplicates**: Can't win twice in same draw
- ✅ **Efficient**: O(n) time complexity
- ✅ **Professional**: Industry-standard algorithm

---

### 3. **Application Flow**

```
┌─────────────────┐
│  User uploads   │
│   CSV/TXT file  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  File Parsing   │
│  - Read content │
│  - Split names  │
│  - Remove dupes │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Store in       │
│  JavaScript     │
│  array (client) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  User enters    │
│  number (e.g.5) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Send names +   │
│  count to Flask │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Flask validates│
│  and runs       │
│  random.sample()│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Return winners │
│  Display results│
└─────────────────┘
```

---

### 4. **Validation & Security**

#### **File Upload Validation:**
```python
# File size limit: 16MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Only allow CSV and TXT files
if not file.filename.endswith(('.csv', '.txt')):
    return error
```

#### **Winner Count Validation:**
```python
# Must be positive
if count <= 0:
    return error("Count must be greater than 0")

# Cannot exceed available names
if count > len(names):
    return error("Cannot select 5 names from 3 total names")
```

#### **Input Sanitization:**
- All names are stripped of leading/trailing whitespace
- Empty lines/cells are ignored
- Duplicate names are removed automatically

---

## Technical Architecture

### **Backend (Flask)**
- **Route `/`**: Serves the HTML page
- **Route `/upload`**: Processes uploaded file, returns parsed names
- **Route `/generate`**: Takes names array + count, returns random selection

### **Frontend (Vanilla JavaScript)**
- **File Upload**: Sends file to `/upload` endpoint via FormData
- **Data Storage**: Stores parsed names in JavaScript array
- **Generate**: Sends names + count to `/generate` endpoint via JSON
- **Display**: Animates and displays winners with staggered effects

### **No Database Required**
- All data is processed in-memory
- No persistent storage needed
- Session-based (data cleared on page refresh)

---

## File Format Examples

### **TXT Format (Recommended)**
```text
John Doe
Jane Smith
Bob Johnson
Alice Williams
Charlie Brown
```
Each line = 1 name → **5 names total**

### **CSV Format (Multiple per row)**
```csv
John Doe,Jane Smith,Bob Johnson
Alice Williams,Charlie Brown
```
Each cell = 1 name → **5 names total**

### **CSV Format (One per row)**
```csv
John Doe
Jane Smith
Bob Johnson
Alice Williams
Charlie Brown
```
Each row = 1 name → **5 names total**

### **Mixed TXT Format (Flexible)**
```text
John Doe
Jane Smith, Bob Johnson
Alice Williams
Charlie Brown
```
Auto-detects commas → **5 names total**

---

## Algorithm Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| File Parse | O(n) | O(n) |
| Duplicate Removal | O(n) | O(n) |
| Random Selection | O(k) | O(k) |
| Display | O(k) | O(k) |

Where:
- `n` = total names in file
- `k` = number of winners requested

**Total**: O(n) time, O(n) space - highly efficient even for large lists!

---

## Local Setup

1. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

---

## Deployment

### Deploy to Heroku

```bash
heroku login
heroku create your-app-name
git init
git add .
git commit -m "Initial commit"
git push heroku main
```

### Deploy to Railway

1. Visit [Railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway auto-detects Flask and deploys

### Deploy to Render

1. Visit [Render.com](https://render.com)
2. Click "New" → "Web Service"
3. Connect repository
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `gunicorn app:app`

---

## Use Cases

- 🎁 **Giveaways**: Select random winners from participants
- 🏢 **Office Events**: Pick team members for activities
- 🎓 **Classroom**: Randomly select students for presentations
- 🎪 **Raffles**: Conduct fair lucky draws at events
- 🎮 **Gaming**: Random team assignment
- 📊 **Surveys**: Select random respondents for prizes

---

## FAQ

**Q: Can the same name win twice?**  
A: No, `random.sample()` selects without replacement. Each name can only win once per draw.

**Q: Is the selection truly random?**  
A: Yes, Python's `random.sample()` uses the Mersenne Twister algorithm, which is suitable for fair random selection.

**Q: What if I have 100 names and want 5 winners?**  
A: Works perfectly! The app can handle any size list (up to 16MB file).

**Q: Can I upload the same file multiple times for new draws?**  
A: Yes, click "Start Over" and upload again for a fresh draw.

**Q: What happens to duplicate names in the file?**  
A: They are automatically removed during upload. If "John Doe" appears 3 times, it's counted as 1 name.

---

## Security Notes

- Maximum file upload size: **16MB**
- Allowed file types: **CSV, TXT only**
- All inputs validated server-side
- No data stored permanently
- XSS protection via JSON responses

---

## License

MIT License - Free to use for any purpose!

---

## Contributing

Feel free to open issues or submit pull requests for improvements!