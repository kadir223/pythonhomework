from bs4 import BeautifulSoup
import sqlite3
import requests
import json
import csv


# Task 1: Weather Forecast Scraper
def scrape_weather():
    with open("weather.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    weather_data = []
    for row in soup.find("tbody").find_all("tr"):
        cols = row.find_all("td")
        day, temp, condition = cols[0].text, int(cols[1].text[:-2]), cols[2].text
        weather_data.append((day, temp, condition))

    highest_temp = max(weather_data, key=lambda x: x[1])
    sunny_days = [day for day, _, condition in weather_data if condition == "Sunny"]
    avg_temp = sum(temp for _, temp, _ in weather_data) / len(weather_data)

    print("Weather Data:", weather_data)
    print("Hottest Day:", highest_temp)
    print("Sunny Days:", sunny_days)
    print("Average Temperature:", avg_temp)


# Task 2: Job Listings Scraper
def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for job_elem in soup.find_all("div", class_="card-content"):
        title = job_elem.find("h2", class_="title").text.strip()
        company = job_elem.find("h3", class_="company").text.strip()
        location = job_elem.find("p", class_="location").text.strip()
        desc = job_elem.find("div", class_="description").text.strip()
        link = job_elem.find("a", class_="apply")['href']
        jobs.append((title, company, location, desc, link))

    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            link TEXT,
            UNIQUE(title, company, location)
        )
    """)

    for job in jobs:
        cursor.execute("""
            INSERT INTO jobs (title, company, location, description, link)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(title, company, location) DO UPDATE SET
            description=excluded.description,
            link=excluded.link
        """, job)

    conn.commit()
    conn.close()


def export_jobs_to_csv(filter_by=None, value=None):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    query = "SELECT * FROM jobs"
    params = ()
    if filter_by and value:
        query += f" WHERE {filter_by} = ?"
        params = (value,)
    cursor.execute(query, params)
    jobs = cursor.fetchall()
    conn.close()

    with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Location", "Description", "Link"])
        writer.writerows(jobs)
    print("Jobs exported to jobs.csv")


# Task 3: Laptop Data Scraper
def scrape_laptops():
    url = "https://www.demoblaze.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    laptops = []

    for item in soup.find_all("div", class_="card-block"):
        name = item.find("h4", class_="card-title").text.strip()
        price = item.find("h5").text.strip()
        desc = item.find("p", class_="card-text").text.strip()
        laptops.append({"name": name, "price": price, "description": desc})

    with open("laptops.json", "w", encoding="utf-8") as file:
        json.dump(laptops, file, indent=4)
    print("Laptop data saved to laptops.json")


# Running tasks
scrape_weather()
scrape_jobs()
scrape_laptops()
export_jobs_to_csv("location", "Remote")
