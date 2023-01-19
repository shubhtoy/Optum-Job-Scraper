# Optum Job Scraper
# Made by @shubhtoy

import requests, json

# Define Global Variables
OUTPUT = "jobs.json"

# Define the headers and parameters for the API request
headers = {
    "authority": "jobsapi-google.m-cloud.io",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.5",
    "referer": "https://careers.unitedhealthgroup.com/",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}

params = {
    "callback": "jobsCallback",
    "pageSize": "100",
    "offset": "0",
    "companyName": "companies/072a4277-f508-43f1-82a0-7cfb2b963d88",
    "customAttributeFilter": 'ats_portalid="Smashfly" AND country="IN"',
    "orderBy": "relevance desc",
}

# Get the number of pages
def get_pages():
    response = requests.get(
        "https://jobsapi-google.m-cloud.io/api/job/search",
        params=params,
        headers=headers,
    )
    resp = response.text
    resp = resp.replace("jobsCallback(", "")
    resp = resp[:-1]

    # get total number of jobs
    data = json.loads(resp)
    total_jobs = int(data["totalHits"])
    pages_list = [total_jobs // 100, total_jobs % 100]
    return pages_list


# Get the jobs
def get_jobs(page_list):
    all_jobs = []
    for i in range(page_list[0]):
        params["offset"] = str(i * 100)
        response = requests.get(
            "https://jobsapi-google.m-cloud.io/api/job/search",
            params=params,
            headers=headers,
        )
        resp = response.text
        resp = resp.replace("jobsCallback(", "")
        resp = resp[:-1]
        data = json.loads(resp)
        for job in data["searchResults"]:
            all_jobs.append(job["job"])
    # print(data)
    params["offset"] = str(page_list[0] * 100)
    params["pageSize"] = str(page_list[1])
    response = requests.get(
        "https://jobsapi-google.m-cloud.io/api/job/search",
        params=params,
        headers=headers,
    )
    resp = response.text
    resp = resp.replace("jobsCallback(", "")
    resp = resp[:-1]
    data = json.loads(resp)
    for job in data["searchResults"]:
        all_jobs.append(job["job"])
    return all_jobs


# Convert to JSON
def to_json(data):
    new_json = {}
    new_json["Company"] = "Optum"
    new_json["count"] = len(data)
    new_json[
        "CareerPage"
    ] = "https://careers.unitedhealthgroup.com/job-search-results/?location=India&country=IN&radius=25"
    new_json["Jobs"] = data
    with open(OUTPUT, "w") as f:
        json.dump(new_json, f, indent=4)


def main():
    page_list = get_pages()
    jobs = get_jobs(page_list)
    to_json(jobs)


if __name__ == "__main__":
    main()
