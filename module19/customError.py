
class VoteNotAllowedError(Exception):
    pass
    

def vote_for_tvk(age):
    if age<18:
        raise VoteNotAllowedError("You are not eligible to vote")

try:
    vote_for_tvk(15)
except VoteNotAllowedError as e:
    print("Age error", e)