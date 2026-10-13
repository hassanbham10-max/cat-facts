import requests

url = "https://catfact.ninja/fact"


def get_cat_fact():
  response = requests.get(url)

  if response.status_code == 200:
    data = response.json()
    print("Cat Fact:", data["fact"])
  else:
    print("Failed to get cat fact")


while True:
  user_input = input("Press Enter for a cat fact or q to quit: ")

  if user_input.lower() == "q":
    break

  get_cat_fact()