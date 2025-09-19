from operator import itemgetter

import requests

# Make an API call and check the response. 
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status Code: {r.status_code}")

# Process information about each submission. 
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a new API call for each submission. 
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article. 
    #Some articles have no comments or disabled, try else block here to assign 0 if no comments. 
    try:
        comments = response_dict['descendants']
    except KeyError:
        comments = 0
    else:
        comments = response_dict['descendants']
    #Build the submission dictionary with response, hacker news link and comments count. 
    submission_dict = {
    'title': response_dict.get('title', 'No title'),
    'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
    'comments': comments,
    }   
    submission_dicts.append(submission_dict)

    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), 
                                                    reverse=True)
    
    
    for submission_dict in submission_dicts:
        print(f"\nTitle: {submission_dict['title']}")
        print(f"\nDiscussion link: {submission_dict['hn_link']}")
        print(f"Comments: {submission_dict['comments']}")