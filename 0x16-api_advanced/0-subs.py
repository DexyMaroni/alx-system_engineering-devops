#!/usr/bin/python3

""" A function that queries the Reddit API and returns the mumber of subscribers for a given subreddit"""


import requests 

def number_of_subscribers(subreddit):
    """ Takes in an arg in a json format and sends a GET request to the Reddit API to 
        get the number of subcribers 
        
        Parameter:
            subreddit: A subcategory of reddit website.

        Returns:
            The number of subcribers."""
    # Putting our url in a variable.
    address = "https://www.reddit.com/r/{}/about/.json".format(subreddit)

    
    # Creating a custom user_agent to avoid getting errors related to too many requests
    headers = {
        "Linux-2024.v1.0.0(user_1)"
    }

    # allow_redirects = False because i dont want to control redirects manually.
    response = requests.get(address, headers=headers, allow_redirects=False)

    # Initiating a control statement to help deal with error reponses
    if reponse.status_code ==404:
        return 0

   # Converting our response from a json  format into a Python data and storing it in a variable.
    results = response.json().get("data")
    return results.get("subscribers")
