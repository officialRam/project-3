import instaloader

loading = instaloader.Instaloader()

username = input("Enter the Instagram username: ")

loading.download_profile(username, profile_pic_only=False)

for post in loading.get_profile_posts(username):
    loading.download_post(post, target=username)
print("Posts downloaded successfully!")