import praw;
import sys;

def get_headlines(reddit, num_posts, subreddit):
      headlines = set()
      counter = num_posts
      for submission in reddit.subreddit(subreddit).top(limit=None):
            print(submission.title)
            # print(submission.id)
            # print(submission.author)
            # print(submission.score)
            # print(submission.url)
            # print(submission.upvote_ratio)
            headlines.add(submission.title)
            num_posts-=1
            if(num_posts<=0):
                break
      print(len(headlines))
            
        
      

def main():
    the_user_agent = "Scrapper 1.0 by /u/ColorfulSquid"
    reddit = praw.Reddit(
        client_id = "tmMGDWYYmL9yI02Qli0Q_A",
        client_secret = "RbwT9McsSUQzZ2Id84TejuVyO75Hvg",
        user_agent = the_user_agent
    )
    #get_headlines(reddit)
    print("Hello and Welcome to the Reddit API User Expierience!")
    print("To see the top x posts in subreddit y use check x in y")
    print(sys.argv[1])
    if(sys.argv[1] == "check"):
          get_headlines(reddit,int(sys.argv[2]),sys.argv[3])

if __name__ == '__main__':
	main()