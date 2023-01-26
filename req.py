import requests

response = requests.get("https://gitlab.com/api/v4/users/9656669/projects")
my_project = response.json()

for anyproject in my_project:
    print(f"Project Name is {anyproject['name']}, Project URL is {anyproject['web_url']}")

print(f"Total number of your projects is {len(my_project)}")