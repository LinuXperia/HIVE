from django.db import models
from django.contrib.auth.models import User

#This file defines the database structure for the project (the db name is "hive" if you're looking for it in mysql)
#Don't touch anything here unless you know what you're doing and have a specific reason for changing it.
#As always, make sure to backup the db before making any major changes. 

class Investigator(models.Model):
	Fname = models.TextField(default='')
	MI = models.TextField(default='')
	Lname = models.TextField(default='')
	department = models.TextField(default='')
	position = models.TextField(default='')
	email = models.EmailField(default='')
	city = models.TextField(default='')
	state = models.TextField(default='')
	country = models.TextField(default='')
	office = models.CharField(max_length=50,default='')
	institution = models.TextField(default='')
	phone = models.CharField(max_length=25,default='')
	investigator_tag = models.TextField(default='')
	picture = models.ImageField(blank=True, null=True)

class Grant(models.Model):
	docNum = models.CharField(max_length=30,default='')
	guidelink = models.URLField(default='')
	title = models.TextField(default='')
	agency = models.CharField(max_length=30, default='')
	expiryDate = models.DateField(blank=True, null=True)
	openDate = models.DateField(blank=True, null=True)
	parentFOA = models.CharField(max_length=10, default='')

class Publication(models.Model):
	pmid = models.TextField(default='')
	title = models.TextField(default='')
	abstract = models.TextField(default='')
	affiliation = models.TextField(default='')
	authors = models.TextField(default='')
	investigator_id = models.TextField(default='')
	source = models.TextField(default='')
	datePublished = models.TextField(default='')
	meshHeadings = models.TextField(default='')

class terms_list(models.Model):
	term = models.TextField(default='')

class term_vectors(models.Model):
	termVector = models.TextField(default='')


class author2citation(models.Model):
	author = models.TextField(default='')
	citation_id = models.TextField(default=0)


class author_abstracts(models.Model):
	author = models.TextField(default='')
	citation_id = models.IntegerField(default=0)
	abstract = models.TextField(default='')

class author_grant_vectors(models.Model):
	item = models.TextField(default='')
	grantvector = models.TextField(default='')

class authors_grants_pairwise_cosine_similarity_matrix(models.Model):
	y_axis = models.TextField(default='')
	x_axis = models.TextField(default='')
	cosine_score = models.DecimalField(max_digits=10, decimal_places=10)

class grant_documents(models.Model):
	grantTitle= models.TextField(default='')
	grantID = models.TextField(default='')
	grantText = models.TextField(default='')
	grantLink = models.URLField(default='')

class authors_grants_list(models.Model):
	item = models.TextField(default='')

