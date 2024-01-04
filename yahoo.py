import pandas as pd
from requests_html import HTMLSession
import requests
import json


def scrape_site():
    print("processing----")
    with open("info_to_scrape.json", "r") as json_file:
        datas = json.load(json_file)
    for item in datas:
        url = item["url"]
        excel_file_name = item["excel_file_name"]

        # Create an HTML session
        session = HTMLSession()

        # Send a GET request
        try:
            response = session.get(url)
        except requests.exceptions.MissingSchema:
            raise ValueError(
                "Invalid URL format. Please include the scheme (e.g., 'http://' or 'https://')."
            )

        # # Render the JavaScript on the page
        response.html.render()

        # Find the <tbody> element
        tbody = response.html.find("tbody", first=True)

        # Initialize lists to store data
        dates = []
        adj_closes = []
        volumes = []

        # Extract data from each <tr> within the <tbody>
        if tbody:
            # Find all <tr> elements within the <tbody>
            rows = tbody.find("tr")

            # Extract data for each <tr>
            for row in rows:
                date = row.find("td span", first=True).text
                all_elements = row.find("td span")

                # Check if there are at least 7 elements before accessing index 5 and 6
                if len(all_elements) > 6:
                    adj_close = all_elements[5].text
                    volume = all_elements[6].text

                    # Append data to lists
                    dates.append(date)
                    adj_closes.append(adj_close)
                    volumes.append(volume)
        else:
            print("Arghhhhh, No tbody found on the page,")

        # Create a DataFrame from the extracted data
        data = {"Date": dates, "adj close": adj_close, "volumes": volumes}
        data_frame = pd.DataFrame(data)

        # Write the DataFrame to an Excel file
        data_frame.to_excel(excel_file_name + ".xlsx", index=False)

        # Close the session
        session.close()
        print("done.....")


scrape_site()
