# TicketingSystem

## Table of contents
* [About](#about)
* [Technology](#Technology)
* [Endpoints](#endpoints)


## About
This is the backend of a Ticketing System App. 

It uses SQLAlchemy to communicate with the database locally and a REST API to communicate with the frontend. 

The service is hosted on pythonanywhere. 

## Technology


### 1 - Basics

Python

### 2 -  Used to create the API 

Flask 
Flask-restful 

### 3 - Database Management

SQLAlchemy

### 4 - Other 

ConfigParser - Loading config information

## Endpoints

You can interact with the endpoints of the system using a request like the snippet below 

'''
{
	"secretkey": "dskjfkjawnvciuwhvbiu0qewgry0uhgbnb0ziuxcve2",
	"payload": {
		"password": "haslo1234",
		"login" : "pawelkirszniok",
	  "email" : "pawelkirszniok@gmail.com"
	}
}
'''

you need to pass a dictionary with the secretkey and payload variables. 

Payload will be a dictionary containing whatever data is required by the endpoint. 

You can find the list of endpoints below: 

'''

get_user = http://tb.pawelkirszniok.com/getuser
get_ticket = http://tb.pawelkirszniok.com/getticket
get_users = http://tb.pawelkirszniok.com/getusers
get_tickets = http://tb.pawelkirszniok.com/gettickets
get_posts = http://tb.pawelkirszniok.com/getposts
save_user = http://tb.pawelkirszniok.com/saveuser
save_ticket = http://tb.pawelkirszniok.com/saveticket
save_post = http://tb.pawelkirszniok.com/savepost
save_relation = http://tb.pawelkirszniok.com/saverelation
validate_user = http://tb.pawelkirszniok.com/validateuser
str_search_users = http://tb.pawelkirszniok.com/strsearchusers

'''
