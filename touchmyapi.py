import requests
import pika

# Replace the URL with the actual API endpoint
api_url = "http://127.0.0.1:8000/api/v1/course/create"

# Replace payload_data with the data you want to send in the POST request
courses_to_create = [
    {
        "course_title": "How to make cash",
        "course_description": "description",
        "course_duration": "2 hours",
        "price": "$1500",
    },
    {
        "course_title": "Python Programming",
        "course_description": "Learn Python from scratch",
        "course_duration": "4 weeks",
        "price": "$200",
    },
    {
        "course_title": "Web Development Basics",
        "course_description": "Introduction to web development",
        "course_duration": "3 weeks",
        "price": "$300",
    },
    # Add more courses as needed
    {
        "course_title": "Data Science Fundamentals",
        "course_description": "Basic concepts of data science",
        "course_duration": "5 weeks",
        "price": "$400",
    },
    {
        "course_title": "Machine Learning Basics",
        "course_description": "Introduction to machine learning",
        "course_duration": "6 weeks",
        "price": "$500",
    },
    {
        "course_title": "Advanced JavaScript",
        "course_description": "Deep dive into JavaScript",
        "course_duration": "4 weeks",
        "price": "$250",
    },
    {
        "course_title": "Mobile App Development",
        "course_description": "Building apps for iOS and Android",
        "course_duration": "8 weeks",
        "price": "$800",
    },
    {
        "course_title": "Cybersecurity Essentials",
        "course_description": "Fundamentals of cybersecurity",
        "course_duration": "3 weeks",
        "price": "$350",
    },
    {
        "course_title": "Digital Marketing Strategies",
        "course_description": "Effective online marketing techniques",
        "course_duration": "4 weeks",
        "price": "$300",
    },
    {
        "course_title": "Blockchain Basics",
        "course_description": "Understanding blockchain technology",
        "course_duration": "5 weeks",
        "price": "$450",
    },
    {
        "course_title": "Graphic Design Fundamentals",
        "course_description": "Introduction to graphic design",
        "course_duration": "3 weeks",
        "price": "$200",
    },
    {
        "course_title": "UI/UX Design Principles",
        "course_description": "Designing user-friendly interfaces",
        "course_duration": "4 weeks",
        "price": "$250",
    },
    {
        "course_title": "Project Management Essentials",
        "course_description": "Basic principles of project management",
        "course_duration": "3 weeks",
        "price": "$300",
    },
    {
        "course_title": "Agile Development Practices",
        "course_description": "Adopting agile methodologies in development",
        "course_duration": "4 weeks",
        "price": "$350",
    },
    {
        "course_title": "Cloud Computing Fundamentals",
        "course_description": "Introduction to cloud computing",
        "course_duration": "5 weeks",
        "price": "$400",
    },
    {
        "course_title": "Artificial Intelligence Overview",
        "course_description": "Understanding AI concepts",
        "course_duration": "6 weeks",
        "price": "$550",
    },
    {
        "course_title": "DevOps Practices",
        "course_description": "Implementing DevOps in software development",
        "course_duration": "4 weeks",
        "price": "$400",
    },
    {
        "course_title": "Networking Basics",
        "course_description": "Fundamentals of computer networking",
        "course_duration": "3 weeks",
        "price": "$300",
    },
    {
        "course_title": "E-commerce Strategies",
        "course_description": "Strategies for successful e-commerce",
        "course_duration": "4 weeks",
        "price": "$350",
    },
    {
        "course_title": "Responsive Web Design",
        "course_description": "Designing websites for various devices",
        "course_duration": "3 weeks",
        "price": "$250",
    },
]

query_params = {
    "token": "your_intoken_value",
}
headers = {
    "access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VyX3VpZCI6IjY0YjZkODA0LTE0NmItNDZhNy05OGJkLTE1Mzc2ODRhMDkzNCJ9.m3Ghqth_SNxpSsVunwofHqKd1Ru2dg5b8crWpJFFbFwN2GD9EArvnvP6JNli2Ik4y4j9CEUD85DHKj2RnVgTyTuR5d0JIHDkKVyfjV5V_v8NcxF1-TXkuc_0Kjcerbar29XgAYWWHs4hx3Bl8Rm8Q5NZKbyKXU_dyQWRXYUCjYiwvfqRbeqTZH0Y3j0wNgjtAFJkrvUKezqVYk57WbX1lltTRV0zqOqQCHtGq2iIUsmWQzTLASuRj6TY1Bt3KLRJRf83Z_o7spPh8WkPMU1dqzgoPUgIagqM6OVgszy7jKi2YSxmNhfdpYlLyUVk7G8PuQmifQ-yPjBt5q2D6whKqA"
}


# Make a POST request
def create():
    for i in range(len(courses_to_create)):
        response = requests.post(api_url, json=courses_to_create[i], headers=headers)


# response = requests.post(api_url, json=payload_data, headers=headers)

# Check the response status
# if response.status_code == 200:
#     print("POST request successful!")
#     print(response)

#     print("Response JSON:", response.json())
# else:
#     print(f"POST request failed with status code {response.status_code}")
#     print("Response content:", response.text)
i = 0
while i < 10:
    create()
    i = i + 1
# import uuid


# def _create_user_wallet():
#     connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
#     channel = connection.channel()
#     channel.queue_declare(queue="auth_to_pms")
#     channel.basic_publish(
#         exchange="", routing_key="auth_to_mms", body=str(uuid.uuid4())
#     )
#     print(" [x] Sent  data to mms")
#     connection.close()


# i = 0
# while i < 1000:
#     _create_user_wallet()
#     i = i + 1
