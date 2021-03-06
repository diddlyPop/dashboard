import requests
import datetime


def update_streaks(github_user, last_modified):
    """
    checks if a streak should be updated and returns the appropriate message to the user
    - if 'last_update' was less than 24
    :param github_user:
    :param last_modified:
    :return:
    """
    result = False
    message = "Empty message"
    today = datetime.date.today()
    # If there is a problem with the github username
    if github_user is None or github_user == " " or len(github_user) < 3:
        message = "Update your github username at the profile page."
    # If user made a commit today
    elif user_made_commit(github_user, today):
        # Get yesterdays date
        print(f"Apparently {github_user} made a commit on {today}")
        yesterday = today - datetime.timedelta(days=1)
        # If user hasn't started a streak
        if last_modified is None:
            result = True
            message = "Starting a new streak, you got this!"
        # User has a streak
        else:
            # Compare yesterdays date and the last modified date
            last_modified = last_modified.date()
            if last_modified == yesterday:
                message = "Confirmed mark, adding to streak."
                result = True
            # If the last modified date was before yesterday (lost streak)
            elif last_modified < yesterday:
                result = True
                message = "Reset"
            # Last modified is > yesterday (could be today)
            else:
                message = "Already streaked today."
    # There was no commit today
    else:
        message = 'No commit found for today. Refresh in a few minutes.'
    return result, message


def user_made_commit(github_user, today):
    """
    check github api with todays date against provided github username
    :param github_user:
    :param today:
    :return:
    """
    verified_commit = False
    dates = []
    url = f'https://api.github.com/search/commits?q=author:{github_user}+author-date:{today}'
    result = requests.get(url, headers={'Accept': 'application/vnd.github.cloak-preview'})
    if result.json()['total_count'] > 0:
        try:
            for item in result.json()['items']:
                commit_date_str = item['commit']['author']['date'][:10]
                commit_date = datetime.datetime.strptime(commit_date_str, '%Y-%m-%d')
                commit_date = datetime.datetime.date(commit_date)
                dates.append(commit_date)
            if today in dates:
                verified_commit = True
        except Exception as e:
            print(e)
    return verified_commit
