from flask import Flask, render_template, jsonify
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Route for home page
@app.route('/')
def index():
    # Read the scraped data from JSON
    jobs_df = pd.read_json('jobs_data.json')

    # Top 5 Job Titles, Companies, and Locations
    top_job_titles = jobs_df['Job_Title'].value_counts().head(5)
    top_companies = jobs_df['Company'].value_counts().head(5)
    top_locations = jobs_df['Location'].value_counts().head(5)

    # Pass data to the HTML page
    return render_template('index.html', top_job_titles=top_job_titles, 
                           top_companies=top_companies, top_locations=top_locations)

# Route to fetch data as JSON
@app.route('/data')
def data():
    # Read the scraped data from JSON
    jobs_df = pd.read_json('people_data.json')
    # Send the data as JSON response
    return jsonify(jobs_df.to_dict(orient='records'))

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
