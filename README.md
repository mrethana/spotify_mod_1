# Spotify Song Feature Comparison Web App
###### Mod 1 Project: Analysis of audio features of songs for different genres, artists and tracks.

## Summary
We built an interactive dashboard using Flask and Dash to analyze/visualize the difference between the musical features of 10 different artists (50 songs each) and 5 different genres. The video below shows the functionality of the Dash app:

[Spotify Mod 1 Preview](https://www.youtube.com/watch?v=js15D7HlTRw)


### Data Gathering and Database Relationships

To seed our database we collected data from 5 of Spotify's available API's. These API's allowed us to gather data on the following:
  + Artist's most popular tracks
  + Information about each artist such as Spotify followers, Spotify id, popularity and genres associated.
  + Tracks from an artist's album of our choosing
  + Specific information on each track such as release date, featured artist, runtime, etc.
  + Audio features of each track- we analyzed 5 main features (valence, danceability, tempo, energy, acousticness). The definitions of each metric as defined by Spotify can be found [here](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/)

After analyzing all relationships needed to connect the data being scraped we used Object Oriented Programming and SQLAlchemy to create an Object-relational Database (ORD) in SQLite. All relationships can be found in the models.py file in the spotifypackage folder and an example of our classes can be found below:

![alt text](https://github.com/mrethana/)





### Artist Trends
+ On average, Migos' tracks had the highest danceability which wasn't expected, given the other artists in the admittedly limited sample such as Michael Jackson.
+ Average acousticness tended to be fairly low for all sampled artists.



### Genre Findings
+ Characteristics of artists within the same or similar genres varied across time.
+ Michael Jackson and Charlie Puth may both be considered high-profile solo pop artists during their respective generations. However, Jackson's songs tended to be higher in energy and valence.
+ This was also true for Migos and The Notorious B.I.G.
This may reflect different generational preferences in musical style.


### Popular Tracks Trends
+ Top tracks from sampled artists tended to be more high-energy and 'danceable', though the artists were diverse in genre and characteristics. Valence was more evenly distributed.



### Next Steps
+ What characterizes more popular genres, on average, vs less popular genres?
+ Do any features correlate with each other?
+ Do songs with featured artists tend to be more popular than songs with only one artist?
+ Include more artists for within-genre comparisons for a more comprehensive analysis.
+ Explore changes in characteristics for an artist over time (ex: Taylor Swift, Kanye West).
+ Predictive models of genre, based on input feature values or vice versa
+ Analyses across time to understand generational changes in sound preferences, paired with historical events (ex: recessions, presidential elections).
