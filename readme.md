# ⚡ Suspicious Electricity Reading Detector

This is a **command-line Python 3.13 application** that detects anomalous electricity readings from input files in **CSV** or **XML** format. The application follows the **Hexagonal Architecture** pattern.

---

## 🧠 Problem Description

We suspect that some electricity readings may indicate fraudulent activity. Examples include:

- **Unusually high readings.**
- **Unusually low readings.**

Each client provides **12 monthly readings per year**. A reading is considered suspicious if it's **50% above or below the median** of their annual readings.

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python **3.13.1**
- [pip](https://pip.pypa.io/en/stable/)
- (Optional) Docker

### 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run the application
To start the application, run the following command in your terminal:
```bash
python main.py <path-to-input-file>
```

Example:
```bash
python main.py ./test/data/2016-readings.csv
python main.py ./test/data/2016-readings.xml
```

### 🔧 Setting PYTHONPATH
If you're running the app or tests outside Docker, set PYTHONPATH=src to enable imports.

##### ▶️ Linux/macOS (bash):
```bash
export PYTHONPATH=src
```

##### ▶️ Windows (PowerShell):
```bash
$env:PYTHONPATH = "src"
```

### 🧪 Run tests

```bash
pytest tests/
```
### 🧪 Check linting

```bash
pylint src tests main.py
```

----
## Input File Formats
### ✅ XML
```bash
<readings>
    <reading clientID="123" period="2016-01">37232</reading>
    ...
</readings>
```
### ✅ CSV 
```bash
client,period,reading
123,2016-01,37232
...
```
Each client must have 12 rows (months).

----
## 📊 Output Format

| Client          | Month   | Suspicious | Median   |
|-----------------|---------|------------|----------|
| 583ef6329d7b9   | 2016-09 | 3564       | 42566.5  |


Values are printed in a formatted table using the tabulate package.

---

## 🐳 Running with Docker (Optional)
Build the Docker image:
```bash
docker build -t e-reading-detector .
```

### Then run the application using a local input file.
▶️ Run with local file on Windows
```bash
docker run --rm -v ${pwd}/tests/data:/data e-reading-detector /data/2016-readings.csv
```

▶️ Run with local file on Linux/macOS
```bash
docker run --rm -v "$(pwd)/tests/data:/data" e-reading-detector /data/2016-readings.csv
```

---

## 🧩 Possible Extensions
- Store outputs in a database or file
- Accept file from API or others file formats
- Add CLI options for thresholds, filtering by client, etc.
