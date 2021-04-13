class User():
    https://www.udemy.com/course/100-days-of-code/learn/lecture/19964886
    
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self,user): 
        ''' Increases the follower count of the user passed
            and increases the followers by one 
        '''
        user.followers += 1 # NB not the object that passed the hence no self
        self.following += 1


user1 = User('001','Peter')
user2 = User('002','Karen')

user1.follow(user2) # User 1 follows user 2

print(user1.following) 
print(user1.followers)
print(user2.following)
print(user2.followers)



