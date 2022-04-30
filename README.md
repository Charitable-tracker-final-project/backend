# Charitable Tracker API

This API allows a user to Create, Set and Track Monetary and Volunteer Goals.
Tracked Goals will then be displayed in interactive Graphs.


## Models

- **User**
- **Profile**
    - Fields
        - User: FK
        - annual_income: intField
- **Donation Goal**
    - Fields
        - User: FK
        - goaltitle: CharField
        - donationGoal: IntField
        - interval: CharField (Drop Down)
- **Volunteer Goal**
    - Fields
        - user: FK
        - goaltitle: CharField
        - volunteergoal: IntField
        - interval: CharField (Drop Down)
- **Donation Record**
    - Fields
        - amountdonated: IntField
        - created at: DateField
        - organization: CharField
        - donation receipt: ImgeField
        - donation record: FK
        - user: FK
        - cause: CharField (Drop Down)
- **Volunteer Record**
	- Fields
    	- hours: IntField
    	- created_at: DateField
	    - organization: CharField
    	- description: CharField
	    - volunteerreceipt: ImgField
    	- volunteerrecord: FK
    	- cause: CharField
- **Document**
	- Fields
		- User: FK
		- uploaded_at: DateTimeField
		- upload: ImgField
- **EmailReminder**
	- Fields
		- user: FK
		- Email:EmailField
		- subscribe: Boolean
		- Your_reminder: CharField
		- Interval: (Drop Down)



## API Endpoints

|  Method  |  Endpoint  |  Description |  Deployed  |
| -------- | ---------- | ------------ | ---------- |
|GET|[/api/Dgoals/](#view-all-donation-goals)|View All Donation Goals filter form newest to oldest| Yes|
|POST|[/api/Dgoals/](#add-a-donation-goal)|Add a donation goal|Yes
|GET|[/api/Dgoal/<int:pk>/](#view-a-singular-donation-goal)|View a singular donation goal|Yes|
|PUT|[/api/Dgoal/<int:pk>/](#edit-a-singular-donation-goal)|Edit a singular donation goal|Yes|
|DELETE|[/api/Dgoal/<int:pk>/](#delete-a-singular-donation-goal)|Delete a singular donation goal|Yes|
|GET|[/api/Vgoals/](#view-all-volunteer-goals)|View all volunteer goals filter from newest to oldest|Yes|
|POST|[/api/Vgoals/](#create-a-volunteer-goal)|Create a volunteer goal|Yes|
|PUT|[/api/Vgoal/<int:pk>/](#edit-a-volunteer-goal)|Edit a volunteer goal|Yes|
|Delete|[/api/Vgoal/<int:pk>/](#delete-a-volunteer-goal)|Delete a volunteer goal|Yes|
|GET|[/api/Drecords/](#View-all-donation-records)|View all donation records|Yes|
|POST|[/api/Drecords/](#Create-a-new-donation-record)|Create a new donation record||
|GET|[/api/Drecord/<int:pk>/](#View-a-specific-donation-record)|View a specific donation record|Yes|
|PUT|[/api/Drecord/<int:pk>/](#Edit-a-specific-donation-record)|Edit a specific donation record|Yes|
|DELETE|[/api/Drecord/<int:pk>/](#Delete-a-specific-donation-record)|Delete a specific donation record|Yes|
|GET|[/api/Vrecords/](#view-all-volunteer-goals)|View all volunteer records|Yes|
|POST|[/api/Vrecords/](#add-a-volunteer-record)|Add a volunteer record|Yes|
|GET|[/api/Vrecord/<int:pk>/](#view-a-specific-volunteer-record)|View a specific volunteer record|Yes|
|PUT|[/api/Vrecord/<int:pk>/](#edit-a-specific-volunteer-record)|Edit a specific volunteer record|Yes|
|DELETE|[/api/Vrecord/<int:pk>/](#delete-a-specific-volunteer-record)|Delete a specific volunteer record|Yes|
|GET|[/auth/login](#login)|Login|Yes|
|GET|[api/annualincome/](#how-much-each-user-makes)|How much Each user Makes|Yes|
|POST|[api/annualincome/](#how-much-each-user-makes)|How much Each user Makes|Yes|
|PUT|[api/annualincome/<int:pk>/](#edit-how-much-each-user-makes)|Edit How much Each user Makes|Yes|
|DELETE|[api/annualincome/<int:pk>/](#delete-how-much-each-user-makes)|Delete How much Each user Makes|Yes|
|POST|[/api/upload/](#upload-img)|Upload Img|Yes|
|GET|[/api/reminders/](#view-all-reminders)|View All Reminders|No|
|POST|[/api/reminders/]|Add a Reminder|No|
|PUT|[/api/reminders/<int:pk>/]|Edit a Reminder|No|
|DELETE|[/api/reminders/<int:pk>/]|Delete a Reminder|NO|
|||||
|||||
|||||
|||||

<!-------------------------- View all donation goals ------------------------------>


[Back to Endpoints](#api-endpoints)

## View all donation goals

```
GET /View all donation goals no filter/
```

```json
This Can be Empty
```

### response

```json

{
	"pk": 1,
	"user": 1,
	"goaltitle": "Black Empowerment",
	"donationgoal": 100,
	"interval": "Year"
}



```


<!-------------------------- Add a donation goal ------------------------------>


[Back to Endpoints](#api-endpoints)


## Add a donation goal

```
GET /Add a donation goal/
```


```json
{
	
	"user": 1,
	"goaltitle": "Lovely Ladies",
	"donationgoal": 50,
	"interval": "Year"
}

```

### response

```json

{
	"pk": 2,
	"user": 1,
	"goaltitle": "Lovely Ladies",
	"donationgoal": 50,
	"interval": "Year"
}


```

<!-------------------------- View a singular donation goal ------------------------------>


[Back to Endpoints](#api-endpoints)

## View a singular donation goal

```
GET /View a singular donation goal/
```

```json
This Can be Empty
```

### response

```json

{
	"pk": 1,
	"user": 1,
	"goaltitle": "Black Empowerment",
	"donationgoal": 100,
	"interval": "Year"
}



```

<!-------------------------- Edit a singular donation goal ------------------------------>


[Back to Endpoints](#api-endpoints)

## Edit a singular donation goal

```
PUT /Edit a singular donation goal/
```

```json
{
	"pk": 1,
	"goaltitle": "donation amount test",
	"donationgoal": 20,
	"interval": "Week"
}
```

### response

```json

{
	"pk": 1,
	"goaltitle": "donation amount test",
	"donationgoal": 20,
	"interval": "Week"
}

```

<!-------------------------- Delete a singular donation goal ------------------------------>


[Back to Endpoints](#api-endpoints)

## Delete a singular donation goal

```
DELETE /Delete a singular donation goal/
```

```json
This Can be blank
```

### response

```json
No body returned for response
```


<!-------------------------- View all volunteer goals ------------------------------>


[Back to Endpoints](#api-endpoints)

## View all volunteer goals

```
GET /View all volunteer goals no filter/
```

```json
This Can be blank
```

### response

```json
[
	{
		"pk": 1,
		"hours": 5,
		"created_at": "2022-04-28",
		"organization": "Bellevue Presbyterian Church",
		"description": "-Sang for 20 minutes, practiced for 50, sang again, etc",
		"cause": "Religion",
		"volunteerrecord": 2
	},
	{
		"pk": 3,
		"hours": 1,
		"created_at": "2022-04-28",
		"organization": "Steve's Place",
		"description": "Worked in the soup kitchen for the men's shelter",
		"cause": "Community Development",
		"volunteerrecord": 3
	},
	{
		"pk": 2,
		"hours": 25,
		"created_at": "2022-04-28",
		"organization": "Red Cross of Canada",
		"description": "Went on trip to help survivors of mudslides in British Columbia",
		"cause": "Human Services",
		"volunteerrecord": 3
	}
]
```

<!-------------------------- Create a volunteer goal ------------------------------>


[Back to Endpoints](#api-endpoints)

## Create a volunteer goal

```
POST /Create a volunteer goal/
```

```json
{
	"user": 1,
	"goaltitle": "Women Empowerment",
	"volunteergoal": 50,
	"interval": "Year"
}

```

### response

```json
{
	"pk": 1,
	"user": 1,
	"goaltitle": "Women Empowerment",
	"volunteergoal": 50,
	"interval": "Year"
}

```

<!-------------------------- Edit a volunteer goal ------------------------------>


[Back to Endpoints](#api-endpoints)

## Edit a volunteer goal

```
PUT /Edit a volunteer goal/
```

```json
{
	"pk": 1,
	"goaltitle": "first volunteer goal",
	"volunteergoal": 30,
	"interval": "Month"
}

```

### response

```json
{
	"pk": 1,
	"goaltitle": "first volunteer goal",
	"volunteergoal": 30,
	"interval": "Month"
}

```

<!-------------------------- Delete a volunteer goal ------------------------------>


[Back to Endpoints](#api-endpoints)

## Delete a volunteer goal

```
Delete /Delete a volunteer goal/
```

```json
This Can be Empty

```

### response

```json
No body returned for response
```

<!-------------------------- View all volunteer goals ------------------------------>


[Back to Endpoints](#api-endpoints)

## View all volunteer goals

```
GET /View all volunteer goals filter from newest to oldest/ 
api/Vallgoals/
```

```json
This Can be blank
```

### response

```json
[
	{
		"pk": 1,
		"hours": 5,
		"created_at": "2022-04-28",
		"organization": "Bellevue Presbyterian Church",
		"description": "-Sang for 20 minutes, practiced for 50, sang again, etc",
		"cause": "Religion",
		"volunteerrecord": 2
	},
	{
		"pk": 3,
		"hours": 1,
		"created_at": "2022-04-28",
		"organization": "Steve's Place",
		"description": "Worked in the soup kitchen for the men's shelter",
		"cause": "Community Development",
		"volunteerrecord": 3
	},
	{
		"pk": 2,
		"hours": 25,
		"created_at": "2022-04-28",
		"organization": "Red Cross of Canada",
		"description": "Went on trip to help survivors of mudslides in British Columbia",
		"cause": "Human Services",
		"volunteerrecord": 3
	}
]
```

<!-------------------------- View all donation records ------------------------------>


[Back to Endpoints](#api-endpoints)

## View all donation records

```
GET /View all donation records/
```

```json
This Can be Empty

```

### response

```json

{
	"pk": 3,
	"amountdonated": 3,
	"created_at": "2022-04-27",
	"organization": "womens rights",
	"cause": "Women's Rights",
	"donationrecord": 2
	}


```

<!-------------------------- Create a new donation record ------------------------------>


[Back to Endpoints](#api-endpoints)

## Create a new donation record

```
POST /Create a new donation record/
```

```json
{
	"amountdonated": 3,
	"created_at": "2022-04-27",
	"organization": "Testing Insomnia",
	"cause": "Women's Rights",
	"donationrecord": 2
}
```

### response

```json

{
	"pk": 7,
	"amountdonated": 3,
	"created_at": "2022-04-27",
	"organization": "Testing Insomnia",
	"cause": "Women's Rights",
	"donationrecord": 2
}

```

<!-------------------------- View a specific donation record ------------------------------>


[Back to Endpoints](#api-endpoints)

## Create a new donation record

```
GET /Create a new donation record/
```

```json
This Can be blank
```

### response

```json
{
	"pk": 8,
	"amountdonated": 5,
	"created_at": "2022-04-23",
	"organization": "Prototype",
	"donationreceipt": null,
	"cause": "Environmental",
	"donationrecord": 1
}

```

<!-------------------------- Edit a specific donation record ------------------------------>


[Back to Endpoints](#api-endpoints)

## Edit a specific donation record

```
PUT /Edit a specific donation record/
```

```json
{
	"amountdonated": 5,
	"created_at": "2022-04-27",
	"organization": "womens rights",
	"cause": "Women's Rights",
	"donationrecord": 2
}

```

### response

```json
{
	"pk": 3,
	"amountdonated": 5,
	"created_at": "2022-04-27",
	"organization": "womens rights",
	"cause": "Women's Rights",
	"donationrecord": 2
}

```

<!-------------------------- Delete a specific donation record ------------------------------>


[Back to Endpoints](#api-endpoints)

## Delete a specific donation record

```
DELETE  /Delete a specific donation record/
```

```json
This can be blank

```

### response

```json
No body returned for response
```

<!-------------------------- Delete a specific donation record ------------------------------>


[Back to Endpoints](#api-endpoints)

## Delete a specific donation record

```
DELETE  /Delete a specific donation record/
```

```json
This can be blank

```

### response

```json
No body returned for response
```

<!-------------------------- View all volunteer records ------------------------------>


[Back to Endpoints](#api-endpoints)

## View all volunteer records

```
GET /View all volunteer records/
```

```json
This can be blank

```

### response

```json

{
	"pk": 1,
	"hours": 2,
	"created_at": "2022-04-22",
	"organization": "United Way",
	"description": "I pet dogs",
	"volunteerreceipt": "http://127.0.0.1:8000/reciepts/logo-shadowclan.png",
	"cause": "Education",
	"volunteerrecord": 2
}


```

<!-------------------------- Add a volunteer record ------------------------------>


[Back to Endpoints](#api-endpoints)

## Add a volunteer record

```
POST  /Add a volunteer record/
```

```json
{
	"hours": 5,
	"created_at": "2022-04-28",
	"organization": "Bellevue Presbyterian Church",
	"description": "-Sang for 20 minutes, practiced for 50, sang again, etc",
	"cause": "Religion",
	"volunteerrecord": 2
}

```

### response

```json
{
	"pk": 5,
	"hours": 5,
	"created_at": "2022-04-28",
	"organization": "Bellevue Presbyterian Church",
	"description": "-Sang for 20 minutes, practiced for 50, sang again, etc",
	"cause": "Religion",
	"volunteerrecord": 2
}


```

<!-------------------------- View a specific volunteer record ------------------------------>


[Back to Endpoints](#api-endpoints)

## View a specific volunteer record

```
GET  /View a specific volunteer record/
```

```json
This can be blank

```

### response

```json
{
	"pk": 5,
	"hours": 5,
	"created_at": "2022-04-28",
	"organization": "Bellevue Presbyterian Church",
	"description": "-Sang for 20 minutes, practiced for 50, sang again, etc",
	"cause": "Religion",
	"volunteerrecord": 2
}

```

<!-------------------------- Edit a specific volunteer record ------------------------------>


[Back to Endpoints](#api-endpoints)

## Edit a specific volunteer record

```
PUT  /Edit a specific volunteer record/
```

```json
{
	"pk": 5,
	"hours": 5,
	"created_at": "2022-04-28",
	"organization": "Test",
	"description": "-Sang for 20 minutes, practiced for 50, sang again, etc",
	"cause": "Religion",
	"volunteerrecord": 2
}


```

### response

```json
{
	"pk": 5,
	"hours": 5,
	"created_at": "2022-04-28",
	"organization": "Test",
	"description": "-Sang for 20 minutes, practiced for 50, sang again, etc",
	"cause": "Religion",
	"volunteerrecord": 2
}


```

<!-------------------------- Delete a specific volunteer record ------------------------------>


[Back to Endpoints](#api-endpoints)

## Delete a specific volunteer record

```
DELETE  /Delete a specific volunteer record/
```

```json
This can be blank

```

### response

```json
No body returned for response
```

<!-------------------------- LogIn ------------------------------>

[Back to Endpoints](#api-endpoints)

## Login

```
POST  /auth/login
```

```json
{
	"username":"Osama",
	"password":"osamamousa",
	"password2":"osamamousa"
}


```

### response

```json
{
	"key": "fb106dc266d3c98b20f1b969fb9a005435347ec1"
}


```


<!-------------------------- List how much Each user Makes ------------------------------>


[Back to Endpoints](#api-endpoints)

## List How much Each user Makes

```
GET  How much Each user Makes
```

```json
None

```

### response

```json
Not Sure yet no data in database
```

<!-------------------------- Create how much each user makes ------------------------------>


[Back to Endpoints](#api-endpoints)

## Create how much each user makes

```
POST  Create how much each user makes
```

```json
{
	"annual_income": 40000
}

```

### response

```json
{
	"annual_income": 40000
}
```

<!-------------------------- Edit how much each user makes ------------------------------>


[Back to Endpoints](#api-endpoints)

## Edit how much each user makes

```
PATCH  Edit how much each user makes
```

```json
{
	"annual_income": 30000
}

```

### response

```json
{
	"annual_income": 30000
}
```


<!-------------------------- DELETE how much each user makes ------------------------------>


[Back to Endpoints](#api-endpoints)

## DELETE how much each user makes

```
DELETE  DELETE how much each user makes
```

```json
None
```

### response

```json
None
```


<!-------------------------- Upload Img ------------------------------>


[Back to Endpoints](#api-endpoints)

## Upload Img

```
POST /Upload Img/
```


```
Select Img (.jpg), Have the following headers
Content-Disposition, attachment;filename=
	file name must match the uploaded img name
```

### response

```json

{
	"upload": "https://charitabletracker.s3.amazonaws.com/reciepts/aaaa.jpg"
}



```

<!-------------------------- View All Reminders ------------------------------>


[Back to Endpoints](#api-endpoints)

## View All Reminders

```
GET /View All Reminders/
```

```json
This Can be Empty
```

### response

```json

{
	"email": "osamamousa048@gmail.com",
	"subscribe": true,
	"interval": "BiWeekly",
	"your_reminder": "Hey u are awsome"
}


```