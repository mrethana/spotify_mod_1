# Spotify Song Feature Comparison Web App
###### Mod 1 Project: Analysis of audio features of songs for different genres, artists and tracks.

## Summary
For our Module 1 Project at Flatiron School my partner and I built an interactive dashboard using Flask and Dash to analyze/visualize the difference between the musical features of 10 different artists (40 songs each) and 5 different genres. The video below shows the functionality of the Dash app:

[Spotify Mod 1 Preview](https://www.youtube.com/watch?v=js15D7HlTRw)


### Data Gathering and Database Relationships

To seed our database we collected data from 5 of Spotify's available API's. These API's allowed us to gather data on the following:
  + Artist's most popular tracks
  + Information about each artist such as Spotify followers, Spotify id, popularity and genres associated.
  + Tracks from an artist's album of our choosing
  + Specific information on each track such as release date, featured artist, runtime, etc.
  + Audio features of each track- we analyzed 5 main features (valence, danceability, tempo, energy, acousticness). The definitions of each metric as defined by Spotify can be found [here](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/)

After analyzing all relationships needed to connect the data being scraped we used Object Oriented Programming and SQLAlchemy to create an Object-relational Database (ORD) in SQLite. All relationships can be found in the models.py file in the spotifypackage folder and an example of our classes can be found below.

![alt text](https://github.com/mrethana/spotify_mod_1/blob/master/Screenshots/ORD.png?raw=True)

We did have a many-to-many relationship between the tracks and features. To satisfy this relationship we created a join table named trackfeature. This class can be found below.

![alt text](https://github.com/mrethana/spotify_mod_1/blob/master/Screenshots/manytomany.png?raw=True)


## Data Visualization using Plotly and Dash

Once our database was seeded with all relevant data we created an etl.py file to extract, transform and load our data into our Dash app to visualize pertinent information in plotly.

#### Artist Trends
+ On average, Migos' tracks had the highest danceability which wasn't expected, given the other artists in the admittedly limited sample such as Michael Jackson (shown below).
+ Average acousticness tended to be fairly low for all sampled artists.

![alt text](https://github.com/mrethana/spotify_mod_1/blob/master/Screenshots/all_features.png?raw=True)


#### Genre Findings
+ Characteristics of artists within the same or similar genres varied across time.
+ Michael Jackson and Charlie Puth may both be considered high-profile solo pop artists during their respective generations. However, Jackson's songs tended to be higher in energy and valence.
+ This was also true for Migos and The Notorious B.I.G.
This may reflect different generational preferences in musical style.
+ Surprisingly, every artist from older generations had a higher average valence (positivity) than their new-school counterpart. Shown below with Notorious B.I.G. and Migos.


 ![alt text](https://github.com/mrethana/spotify_mod_1/blob/master/Screenshots/genres.png?raw=True)

#### Popular Tracks Trends
+ Top tracks from sampled artists tended to be more high-energy and 'danceable', though the artists were diverse in genre and characteristics. Valence was more normally distributed. All distributions are shown below.


 ![alt text](https://github.com/mrethana/spotify_mod_1/blob/master/Screenshots/popular.png?raw=True)


 + This was exemplified when analyzing Michael Jackson's most popular songs. His popular tracks were tracks with high danceability. This can be seen below. The more opaque points are songs that show up as top tracks on his Spotify page. The y-axis shows popularity and the x-axis shows how high danceability is.


  ![alt text](https://github.com/mrethana/spotify_mod_1/blob/master/Screenshots/tracks.png?raw=True)


## Challenges/Next Steps

#### Challenges
+ Moving forward when using the Spotify API I will use the spotipy Python library. This makes it easier to pull from each API. We had difficulty with our API key expiring. We also utilized many nested for loops slowing down our functions. Spotipy would help with this issue moving forward.
+ We only added a limited amount of artists due to this difficulty working with the API, we would like to add more artists/songs/genres to see if the initial trends we saw held up.


#### Next Steps
+ What characterizes more popular genres, on average, vs less popular genres?
+ Do any features correlate with each other?
+ Do songs with featured artists tend to be more popular than songs with only one artist?
+ Include more artists for within-genre comparisons for a more comprehensive analysis.
+ Explore changes in characteristics for an artist over time (ex: Taylor Swift, Kanye West).
+ Predictive models of genre, based on input feature values or vice versa
+ Analyses across time to understand generational changes in sound preferences, paired with historical events (ex: recessions, presidential elections).
