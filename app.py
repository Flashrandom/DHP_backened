from flask import Flask, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import numpy as np
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Sample data generation if file not found
def generate_sample_data():
    dates = pd.date_range(start='2018-01-01', end='2023-12-31', freq='M')
    tags = ['python', 'javascript', 'java', 'c#', 'php', 'android', 'html', 'css', 'reactjs', 'node.js']
    data = {
        'Upload Time': np.random.choice(dates, 500),
        'Tag': [np.random.choice(tags) for _ in range(500)]
    }
    return pd.DataFrame(data)

try:
    df = pd.read_csv("stackoverflow_questions.csv")
except FileNotFoundError:
    print("CSV file not found, generating sample data...")
    df = generate_sample_data()
    df.to_csv("stackoverflow_questions.csv", index=False)

# Data processing
df['Upload Time'] = pd.to_datetime(df['Upload Time'])
df['Year'] = df['Upload Time'].dt.year
df['Tag'] = df['Tag'].str.split(';')
df_exploded = df.explode('Tag')
tag_counts = df_exploded.groupby(['Year', 'Tag']).size().unstack(fill_value=0)
tag_totals_per_year = tag_counts.sum(axis=1)
relative_trend = tag_counts.div(tag_totals_per_year, axis=0) * 100  # Changed from 2100 to 100 for percentage

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/data')
def get_data():
    top_tags = tag_counts.sum().nlargest(10).index
    data = {
        "labels": relative_trend.index.astype(str).tolist(),
        "datasets": []
    }
    
    colors = [
        "#4e73df", "#1cc88a", "#36b9cc", "#f6c23e", 
        "#e74a3b", "#858796", "#5a5c69", "#f8f9fc",
        "#224abe", "#5cb85c"
    ]
    
    for i, tag in enumerate(top_tags):
        data["datasets"].append({
            "label": tag,
            "data": relative_trend[tag].fillna(0).tolist(),
            "borderColor": colors[i],
            "backgroundColor": colors[i] + "33",  # Add alpha
            "borderWidth": 2,
            "pointRadius": 3,
            "fill": False
        })
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)