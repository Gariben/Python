## Youtube Comment Scraper

This is a small script using Google's Youtube v3 api to scrape an entire video's comments 
for numeric values and organize them into a .csv for graphing and analysis.

This is accomplished by request comment content from the video via an api request,
grabbing individual usernames, then comments, and regexing the comments for any 3 number values
above a "reasonable" weight. This is all streamed into an .csv that can be opened in Excel.

It also provides console output while combing through the many pages.

Simply provide an api key for the **api_key** value and a youtube id (found at the end of the url) for the **video_id** value.

###Background

this was inspired by a contest youtuber Rob Chapman held to win a case of Mooer guitar pedals. 
To win the contest you had correctly guess Rob and two of his staffers' weights. 
There obviously isn't a way to "hack" a contest like this, but I'm terrible at guessing weights,
so Hargle8 gave me the idea make a script that would take "the wisdom of the crowd" in order to form an "educated guess".

Surprisingly, there isn't a tremendous amount of research large crowds and their ability to guess weights, 
but there has been a few articles here and there showing that people are never beyond, at most, 10%.
[Here's an NPR article where 17,205 guessed the weight of a cow within 5%.](http://www.npr.org/sections/money/2015/08/07/429720443/17-205-people-guessed-the-weight-of-a-cow-heres-how-they-did)

If I recall correctly **our final value was within 8% of being correct**. You can double check with the sample output again Rob's response to make sure.

###Special Thanks

To **Hargle8** for the idea to create the script, 
and to **Ellun** for helping me out with API stuff.
