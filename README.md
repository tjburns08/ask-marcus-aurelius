# ask-marcus-aurelius
Type a question. Get the passages in Meditations by Marcus Aurelius that are most relevant. 

# How does this work?
Each passage (book and verse) in the Meditations has been mapped by the all-mpnet-v2 model within Sentence Transformers (based on BERT) into a 768 dimensional vector. The user types a question into the search bar. This question gets mapped into the same 768 dimensional vector space using the same model. Cosine distance is calculated between the question and the nearest passage. The program returns a table of passages in descending order of relevance. The passage with the lowest cosine distance (nearest neighbor in the vector space) comes first. Then the second lowest cosine distance. And so on. 

# Why is this not a web app? 
I tried to deploy it to Heroku, the best practices for Dash apps, but it was too big. This is a common problem when you want to deploy large AI/ML models. If there is enough popular demand, I might try to put it on AWS or something similar down the line. Until then, I have it here as a repo you can clone. For those who don't know how to code, I've made the setup and running of the program as simple as running a shell script (in the command line: ./some-text). 

# Before you install.
Please note that this will take up around 1 Gb of space on your computer. Again, it was too bulky for my usual deployment on Heroku. The instructions below are tailored toward Mac and Linux users. Instructions for Windows will follow. 

# Setup 
### Clone this repo: 
In the command line, type `git clone https://github.com/tjburns08/ask-marcus-aurelius`

### Go to the repo's root directory
In the command line, type `cd ask-marcus-aurelius`

### Run the setup shell script: 
This creates a virtual environment and installs the necessary python packages. Note that you only have to do this once. In the command line: `./setup.sh`


# Run
### Run the run shell script: 
In the command line: `./run.sh`
### Open your browser and go to the link Dash gives you:
In the command line after you do the above step, you'll get a message that gives you a link. Open up your browser and go there. Example on my computer: `Dash is running on http://127.0.0.1:8050/`

# Usage
### Type a question into the search bar and press submit
Note: output is organized by book and verse. Each row in descending order of relevance.

# Misc
The image was created by DALL-E2. The prompt was "A painting of Marcus Aurelius thinking deeply as a stoic philosopher in ancient Rome"

