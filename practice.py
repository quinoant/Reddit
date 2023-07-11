import praw;

def get_headlines(reddit):
      headlines = set()
      for submission in reddit.subreddit('politics').hot(limit=None):
            print(submission.title)
            print(submission.id)
            print(submission.author)
            print(submission.score)
            print(submission.url)
            print(submission.upvote_ratio)
            headlines.add(submission.title)
            break
      print(len(headlines))
            
        
      

def main():
    the_user_agent = "Scrapper 1.0 by /u/ColorfulSquid"
    reddit = praw.Reddit(
        client_id = "tmMGDWYYmL9yI02Qli0Q_A",
        client_secret = "RbwT9McsSUQzZ2Id84TejuVyO75Hvg",
        user_agent = the_user_agent
    )
    get_headlines(reddit)

if __name__ == '__main__':
	main()