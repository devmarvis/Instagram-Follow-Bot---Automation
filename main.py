from instagram import InstaFollower
import time

insta_follower = InstaFollower()
insta_follower.login()

time.sleep(6)

insta_follower.find_followers()
time.sleep(4)

insta_follower.follow()
