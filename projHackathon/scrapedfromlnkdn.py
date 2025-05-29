import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# Step 1: Set up URL and headers
url = "https://www.linkedin.com/jobs/search?keywords=Python&location=pakistan&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
headers = {"User-Agent": "Mozilla/5.0"}

# Step 2: Send request to linkedin
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print("Request failed. Try again later.")
else:
    # Step 3: Parse HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, "lxml")

    # Step 4: Find job from linkedin
    job_cards_title = soup.find_all("h3", class_="base-search-card__title")
    job_cards_location = soup.find_all("span", class_="job-search-card__location")
    job_cards_companies = soup.find_all("h4", class_="base-search-card__subtitle")
    job_cards_dates = soup.find_all("time")
    
    # Step 5: Display job titles
    print("Top Job Titles from linkedin:")
    
jobs_df = pd.DataFrame({
    'Job_Title': [job.text.strip() for job in job_cards_title],
    'Company': [comp.text.strip() for comp in job_cards_companies],
    'Location': [loc.text.strip() for loc in job_cards_location],
    'Date_Posted': [dte.get("datetime") for dte in job_cards_dates]
})
# print(jobs_df)
jobs_df.to_json('jobs_data.json', orient="records", indent=4)