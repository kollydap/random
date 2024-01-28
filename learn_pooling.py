import requests
import concurrent.futures

urls = [
"https://www.example.com/file1.txt",
"https://www.example.com/file2.txt",
"https://www.example.com/file3.txt",
"https://www.example.com/file4.txt",
"https://www.example.com/file5.txt"
]

def download(url):
    response = requests.get(url)
    return response.content

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

    # Submit each download task to the thread pool
    futures = [executor.submit(download, url) for url in urls]

    # Wait for all tasks to complete and retrieve the results
    results = [future.result() for future in concurrent.futures.as_completed(futures)]

# Print the contents of each file
for result in results:
    print(result.decode())