# WebScienceAE - 2313202n
# If you wish to print out the cluster file to a text document
# you must uncomment every line beginning "file." and also
# change the path on line 11 when opening the file.  

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

# file = open(r".txt","a")

# Get tweets from csv file
tweets = pd.read_csv("Football Database.csv")
# get usernames from each tweet
usernames = tweets['username']
# get hashtags from each tweet
hashtag = tweets['hashtags']
# Extract text from tweets
tText = tweets['text']

vectorizer = TfidfVectorizer(stop_words='english')
# Vectorise the usernames
username = vectorizer.fit_transform(usernames)
# Create a vector of the hashtags
hashtags = vectorizer.fit_transform(hashtag)
# Create a vector of the tweet
text = vectorizer.fit_transform(tText)

k = 8

# Cluster usernames
usernamesK = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1)
usernamesK.fit(username)

# Print usernames for each cluster
print("Top usernames per cluster:")
#file.write("Top usernames per cluster:")
centroids = usernamesK.cluster_centers_.argsort()[:, ::-1]
username = vectorizer.get_feature_names()
for i in range(k):
    print("\n")
    #file.write("\n")
    print ("Cluster %d:" % i)
    #file.write("Cluster %d:" % i + "\n")
    for ind in centroids[i, :10]:
        print (' %s' % username[ind])
        #file.write(' %s' % username[ind] + "\n")

print("\n")
#file.write("\n")

# Cluster hashtags
hashtagK = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1)
hashtagK.fit(hashtags)

# Print usernames for each cluster
print("Top hashtags per cluster:")
#file.write("Top hashtags per cluster:")
centroids = hashtagK.cluster_centers_.argsort()[:, ::-1]
hashtags_ = vectorizer.get_feature_names()
for i in range(k):
    print("\n")
    #file.write("\n")
    print ("Cluster %d:" % i)
    #file.write("Cluster %d:" % i + "\n")
    for ind in centroids[i, :10]:
        print(' %s' % hashtags_[ind])
        #file.write(' %s' % hashtags_[ind] + "\n")

print("\n")
#file.write("\n")

# Cluster tweets 
textK = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1)
textK.fit(text)

# Print usernames for each cluster
print("Top text per cluster:")
#file.write("Top text per cluster:")
centroids = textK.cluster_centers_.argsort()[:, ::-1]
text_ = vectorizer.get_feature_names()
for i in range(k):
    print("\n")
    #file.write("\n")
    print ("Cluster %d:" % i)
    #file.write("Cluser %d" % i + "\n")
    for ind in centroids[i, :10]:
        print (' %s' % text_[ind])
        #file.write(' %s' % text_[ind] + "\n")

#file.close()

