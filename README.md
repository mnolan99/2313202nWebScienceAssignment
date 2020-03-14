# Twitter API Crawler - Web Science Assessment 2313202n

The main focus of this project was to develop a Twitter data crawler so that I could complete network based social media analytics. This network crawler makes use of the Twitter API to collect data from tweets in real time. 


### Dependencies

- Tweepy
- Pymongo
- MongoDB
- Pandas
- TwitterSearch
- Scikit-learn pip install scikit-learn


### Installing Dependencies


```
pip install tweepy
```

```
pip install pymongo
```

```
pip install pandas
```

```
pip install TwitterSearch
```

```
pip install Scikit-learn
```

### Running

- Search file - Add your Twitter Developer keys and change the keywords to your chosen topic and run using
```
python "Twitter Search.py"
```

- Crawler file - Add your Twitter Developer keys and change the keywords to your chosen topic. You must also ensure that you have MongoDB set up correctly on your machine. Finally run using
```
python "Twitter Crawler.py"
```

- Cluster file - To write out to a file, uncomment each "file.write" line and edit the file name (file = open(r<"YOUR_FILENAME.txt">,"a"). Run using

```
python "Cluster.py"
```


## Authors

- **Martin Nolan (2313202n)** - [mnolan99](https://github.com/mnolan99)

## Acknowledgments

- [GitHub For Twitter Search](https://github.com/ckoepp/TwitterSearch)
- [Clustering using Scikit-Learn Stackoverflow](https://stackoverflow.com/questions/27889873/clustering-text-documents-using-scikit-learn-kmeans-in-python?fbclid=IwAR13agTGUdH3e7Xdpt2x6ee6R8vrzjWCuguWgCgTklOcmcYBwVdO6ak8c3k)
- [GitHub for Twitter Crawler](https://github.com/SamDelgado/twitter-to-mongo)
- [Tweepy Documentation](http://docs.tweepy.org/en/latest/)
- [Twitter Developer Documentation](https://developer.twitter.com/en/docs)
