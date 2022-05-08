# Project_DD2477

Project for DD2477

#### Google docs:
https://docs.google.com/document/d/1NM5Qjl-u9JclvHjXS2VGdY3qW_E4FfU4svRt1jC_tnc/edit

### Running the Program

The pogram is composed of 3 modules: the Elastic Search instance, the recommendation server and the interface.
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