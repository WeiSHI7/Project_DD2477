# Project_DD2477

Project for DD2477

### Data Collection

#### Web Scraping

First, collect and write the target urls into a file with URLScraper.py. Specify the Goodreads url of book list in the file and saved file path, then run ```python URLScraper.py```.

Second, collect data based on url files saved by the former step. In writetofiles.py, specify the saved url files in the last step, the file path to save the book data, and a file path that records the failed urls. Then run ```python writetofiles.py```. Again specify the failed urls file as the saved url file, a file path to save data, and a new failed urls file path. Then run ```python writetofiles.py```. Repeat until there are no failed urls. The data will be stored in json format.

#### Load Data to Elasticsearch

Specify the directory path of the data in load_json.py, run ```python load_json.py```

### Running the Program

The program is composed of 3 modules: the Elastic Search instance, the recommendation server and the interface.
Once all the modules are up and running, it is expected that the search is performed with no aditional problems.

#### Elastic Search

First thing needed is to fill elastic search with the information that was scraped from Goodreads. To do that,
one could use the ```load_json.py``` script. Before running it, it's necessary to set two environment variables:
```ELASTIC_USER``` (w/ the ES username) and ```ELASTIC_PWD``` (w/ the ES password). The path to ES's CA certificates
may also need tweaking, this is hardcoded in line 30.

#### Recommendation Server

Once the ES instance is running as has the appropriate data, next step is to run the server. This can be achieved
by just running the scritp ```server.py```. Again, the credentials to ES are needed as env. variables, and the CA
certificates path might need tweking (on line 19)

#### Interface

For the interface, we're using Angular. To run it, one need angular installed. This can be achieved with *npm* through
the command ```npm install -g @angular/cli```. Once angular is installed, the interface can be started with the command
```ng serve```, that should be executed inside the interface folder.