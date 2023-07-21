def find_most_liked_users(users_likes_count):
    highest_liked_users = []
    highest_likes_count = 0
    for user in users_likes_count.keys():
        user_likes_count = users_likes_count[user]
        if user_likes_count > highest_likes_count:
            highest_liked_users = []
            highest_liked_users.append(user)
            highest_likes_count = user_likes_count
        elif user_likes_count == highest_likes_count:
            highest_liked_users.append(user)
        
    return highest_liked_users

def calculate_user_likes(n, user_post_data):
    users_likes_count = {}
    for index in range(n):
        current_user = user_post_data[index][0]
        if current_user not in users_likes_count.keys():
            users_likes_count[current_user] = user_post_data[index][2]
        else:
            users_likes_count[current_user] += user_post_data[index][2]
    
    return users_likes_count

def find_most_popular_users(n, user_post_data):
    users_likes_count = calculate_user_likes(n, user_post_data)
    highest_liked_users = find_most_liked_users(users_likes_count)
    
    popular_users_and_posts = []
    for user in highest_liked_users:
        maximum_likes = 0
        popular_post_id = 999999999
        for index in range(n):
            user_name = user_post_data[index][0]
            post_id = user_post_data[index][1]
            likes = user_post_data[index][2]
            if user_name == user:
                if likes > maximum_likes:
                    maximum_likes = likes
                    popular_post_id = post_id
                elif likes == maximum_likes:
                    popular_post_id = min(popular_post_id, post_id)
        popular_users_and_posts.append([user, popular_post_id])
        
    popular_users_and_posts.sort()
    return popular_users_and_posts
    
def main():
    num_posts = int(input())
    user_post_data = []
    for i in range(num_posts):
        user_name, post_id, likes =input().split()
        post_id = int(post_id)
        likes = int(likes)
        user_post_data.append([user_name, post_id, likes])
    
    popular_users_and_posts = find_most_popular_users(num_posts, user_post_data)
    
    for user_post in popular_users_and_posts:
        print(user_post[0] + " " + str(user_post[1]))
    
main()