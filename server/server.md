# The Server.

## Introduction
This is an attempt to both learn Django and to create a backend for Doorman. The goal is to display statistics of inhabitants' comings and goings, as well as serve as a backend for future projects using this data. Because I'm learning, there's a lot wrong here in terms of database design and templating, but I've outlined those exact shortcomings below. 

## Models
The models are best explained in `doorman/models.py`. I've documented them there, and you can see my very amateurish UserProfile system. The correct way to do user information and authentication is here: [`https://docs.djangoproject.com/en/1.6/topics/auth/customizing/#extending-the-existing-user-model'](https://docs.djangoproject.com/en/1.6/topics/auth/customizing/#extending-the-existing-user-model)
