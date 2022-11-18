# CPSC 254 - Group Project: Earth, Wind, Fire - Information Source Finder

## Description:

A source finder that will take a search query from the user and runs the query through a search powered by the IEEE Xplore API. The API will make search requests through the IEEE Xplore database and returns 25 responses to the page in the form of a table. The user is then allowed to scroll through the results to pick which sources to use.

## Group Members:
Jeffrey Nong - jeffreynong@csu.fullerton.edu

Steven Rico - ricosteven00@csu.fullerton.edu

Joshua Villasis - JJVillasis@csu.fullerton.edu

## Programming Languages Used:
- Javascript
- HTML
- CSS 
- Python

## Libraries used
### Python
- Flask - `pip install Flask`
- Requests - `pip install requests`
- Urllib
- Json

### HTML/CSS
- Jquery `https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js`

## Licences Used:
- IEEE Xplore API

## Execution:
Download the repository from the GitHub page  

Ensure that all libraries are installed (flask & requests) 

(Linux) download the flask to your system `sudo apt update`, then `sudo apt install Flask`  

Go to directory of the project  

(Windows) Run local server via `python server.py`  

(Linux) enter `FLASK_APP=server.py flask run` to start the local server.  

Go to URL server is running on (usually `http://127.0.0.1:5000`)  

Look up a term, and get some articles.

### IMPORTANT NOTE
The API keys provided can only be used to make 200 search queries a day.
