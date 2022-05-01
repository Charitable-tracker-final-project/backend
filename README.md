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

|  Method  |  Endpoint  |  Description |  Deployed  |  URL  |
| -------- | ---------- | ------------ | ---------- | ----- |
|GET|[/api/Dgoals/](#view-all-donation-goals)|View All Donation Goals filter form newest to oldest| Yes|[https://charitable-tracker.herokuapp.com/api/Dgoals/]|
|POST|[/api/Dgoals/](#add-a-donation-goal)|Add a donation goal|Yes|[https://charitable-tracker.herokuapp.com/api/Dgoals/]|
|GET|[/api/Dgoal/<int:pk>/](#view-a-singular-donation-goal)|View a singular donation goal|Yes|[https://charitable-tracker.herokuapp.com/api/Dgoal/<int:pk>/]|
|PUT|[/api/Dgoal/<int:pk>/](#edit-a-singular-donation-goal)|Edit a singular donation goal|Yes|[https://charitable-tracker.herokuapp.com/api/Dgoal/<int:pk>/]|
|DELETE|[/api/Dgoal/<int:pk>/](#delete-a-singular-donation-goal)|Delete a singular donation goal|Yes|[https://charitable-tracker.herokuapp.com/api/Dgoal/<int:pk>/]|
|GET|[/api/Vgoals/](#view-all-volunteer-goals)|View all volunteer goals filter from newest to oldest|Yes|[https://charitable-tracker.herokuapp.com/api/Vgoals/]|
|POST|[/api/Vgoals/](#create-a-volunteer-goal)|Create a volunteer goal|Yes|[https://charitable-tracker.herokuapp.com/api/Vgoals/]|
|PUT|[/api/Vgoal/<int:pk>/](#edit-a-volunteer-goal)|Edit a volunteer goal|Yes|[https://charitable-tracker.herokuapp.com/api/Vgoal/<int:pk>/]|
|Delete|[/api/Vgoal/<int:pk>/](#delete-a-volunteer-goal)|Delete a volunteer goal|Yes|[https://charitable-tracker.herokuapp.com/api/Vgoal/<int:pk>/]|
|GET|[/api/Drecords/](#View-all-donation-records)|View all donation records|Yes|[https://charitable-tracker.herokuapp.com/api/Drecords/]|
|POST|[/api/Drecords/](#Create-a-new-donation-record)|Create a new donation record|Yes|[https://charitable-tracker.herokuapp.com/api/Drecords/]|
|PUT|[/api/Drecord/<int:pk>/](#Edit-a-specific-donation-record)|Edit a specific donation record|Yes|[https://charitable-tracker.herokuapp.com/api/Drecord/<int:pk>/]|
|DELETE|[/api/Drecord/<int:pk>/](#Delete-a-specific-donation-record)|Delete a specific donation record|Yes|[https://charitable-tracker.herokuapp.com/api/Drecord/<int:pk>/]|
|GET|[/api/Vrecords/](#view-all-volunteer-goals)|View all volunteer records|Yes|[https://charitable-tracker.herokuapp.com/api/Vrecords/]|
|POST|[/api/Vrecords/](#add-a-volunteer-record)|Add a volunteer record|Yes|[https://charitable-tracker.herokuapp.com/api/Vrecords/]|
|GET|[/api/Vrecord/<int:pk>/](#view-a-specific-volunteer-record)|View a specific volunteer record|Yes|[https://charitable-tracker.herokuapp.com/api/Vrecord/<int:pk>]|
|PUT|[/api/Vrecord/<int:pk>/](#edit-a-specific-volunteer-record)|Edit a specific volunteer record|Yes|[https://charitable-tracker.herokuapp.com/api/Vrecord/<int:pk>]|
|DELETE|[/api/Vrecord/<int:pk>/](#delete-a-specific-volunteer-record)|Delete a specific volunteer record|Yes|[https://charitable-tracker.herokuapp.com/api/Vrecord/<int:pk>/]|
|GET|[/auth/login](#login)|Login|Yes|[https://charitable-tracker.herokuapp.com/auth/login]|
|GET|[api/annualincome/](#how-much-each-user-makes)|How much Each user Makes|Yes|[https://charitable-tracker.herokuapp.com/api/annualincome/]|
|POST|[api/annualincome/](#how-much-each-user-makes)|How much Each user Makes|Yes|[https://charitable-tracker.herokuapp.com/api/annualincome/]|
|PUT|[api/annualincome/<int:pk>/](#edit-how-much-each-user-makes)|Edit How much Each user Makes|Yes|[https://charitable-tracker.herokuapp.com/api/annualincome/<int:pk>/]|
|DELETE|[api/annualincome/<int:pk>/](#delete-how-much-each-user-makes)|Delete How much Each user Makes|Yes|[https://charitable-tracker.herokuapp.com/api/annualincome/<int:pk>/]|
|GET|[/api/reminders/](#view-all-reminders)|View All Reminders|No|[https://charitable-tracker.herokuapp.com/api/reminders/]]|
|POST|[/api/reminders/](#Post-all-reminders)|Add a Reminder|No|[https://charitable-tracker.herokuapp.com/api/reminders/]|
|PUT|[/api/reminders/<int:pk>/](#edit-a-reminder)|Edit a Reminder|No|[https://charitable-tracker.herokuapp.com/api/reminders/<int:pk>/]|
|DELETE|[/api/reminders/<int:pk>/](#delete-a-reminder)|Delete a Reminder|NO|[https://charitable-tracker.herokuapp.com/api/reminders/<int:pk>/]|
|POST|[/auth/registration/](#registration)|regiestration|Yes|[https://charitable-tracker.herokuapp.com/auth/registration/]|
|GET|[/api/causetime/](#view-cause-and-time)|View cause and time|[https://charitable-tracker.herokuapp.com/api/causetime/]|
|GET|[/api/causedonation/](#view-cause-and-donation)|View cause and donation|[https://charitable-tracker.herokuapp.com/api/causedonation/]|
|GET|[/api/organizationtime/](#view-organization-and-time)|View organization and time|Yes|[https://charitable-tracker.herokuapp.com/api/organizationtime/]|
|GET|[/api/organizationdonation/](#view-organization-and-donation)|View organization and donation|Yes|[https://charitable-tracker.herokuapp.com/api/organizationdonation/]|
|POST|[/api/upload/](#upload-img)|Upload Img|Yes|[https://charitable-tracker.herokuapp.com/api/upload/]|
|GET|[/api/upload/](#List-upload-img)|List of all Imgs|[https://charitable-tracker.herokuapp.com/api/upload/]|
|PUT|[/api/upload/<int:pk>](#edit-upload-img)|Edit a spicific img upload|[https://charitable-tracker.herokuapp.com/api/upload/<int:pk>]|
|DELETE|[/api/upload/<int:pk>](#delete-upload-img)|Delete a spicific img|[https://charitable-tracker.herokuapp.com/api/upload/<int:pk>]|


<!-------------------------- View all donation goals ------------------------------>


[Back to Endpoints](#api-endpoints)

## View all donation goals

```
GET /api/Dgoals/
https://charitable-tracker.herokuapp.com/api/Dgoals/
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
POST /api/Dgoals/
https://charitable-tracker.herokuapp.com/api/Dgoals/
```


```json
{
"goaltitle": "Wy are u working",
"donationgoal": 5,
"interval": "Week",
"created_at": "2022-04-30"
}

```

### response

```json

{
	"pk": 11,
	"goaltitle": "hello osama",
	"donationgoal": 5,
	"interval": "Week",
	"created_at": "2022-04-30"
},


```

<!-------------------------- View a singular donation goal ------------------------------>


[Back to Endpoints](#api-endpoints)

## View a singular donation goal

```
GET /api/Dgoals/<int:pk>/ 
https://charitable-tracker.herokuapp.com/api/Dgoals/<int:pk>/
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
PUT /api/Dgoal/<int:pk>/
https://charitable-tracker.herokuapp.com/api/Dgoal/<int:pk>/
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
DELETE /api/Dgoal/<int:pk>/
https://charitable-tracker.herokuapp.com/api/Dgoal/<int:pk>/
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
GET /api/Vgoals/
https://charitable-tracker.herokuapp.com/api/Vgoals/
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
POST /api/Vgoals/
https://charitable-tracker.herokuapp.com/api/Vgoals/
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
PUT /api/Vgoal/<int:pk>/
https://charitable-tracker.herokuapp.com/api/Vgoal/<int:pk>/
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
DELETE /api/Vgoal/<int:pk>/
https://charitable-tracker.herokuapp.com/api/Vgoal/<int:pk>/
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
GET /api/Vgoals/
https://charitable-tracker.herokuapp.com/api/Vgoals/
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
GET /api/Drecords/
https://charitable-tracker.herokuapp.com/api/Drecords/
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
POST /api/Drecords/
https://charitable-tracker.herokuapp.com/api/Drecords/
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

<!-------------------------- Edit a specific donation record ------------------------------>


[Back to Endpoints](#api-endpoints)

## Edit a specific donation record

```
PUT /api/Drecord/<int:pk>/
https://charitable-tracker.herokuapp.com/api/Drecord/<int:pk>/
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
DELETE  /api/Drecord/<int:pk>/
https://charitable-tracker.herokuapp.com/api/Drecord/<int:pk>/
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
https://charitable-tracker.herokuapp.com/api/Vrecords/
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
POST  /api/Vrecords/
https://charitable-tracker.herokuapp.com/api/Vrecords/
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
GET  /api/Vrecord/<int:pk>/
https://charitable-tracker.herokuapp.com/api/Vrecord/<int:pk>/
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
PUT  /api/Vrecord/<int:pk>/
https://charitable-tracker.herokuapp.com/api/Vrecord/<int:pk>/
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
DELETE  /api/Vrecord/<int:pk>/
https://charitable-tracker.herokuapp.com/api/Vrecord/<int:pk>/
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
https://charitable-tracker.herokuapp.com/auth/login
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
GET  /api/annualincome/
https://charitable-tracker.herokuapp.com/api/annualincome/
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
POST  /api/annualincome/
https://charitable-tracker.herokuapp.com/api/annualincome/
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
PATCH  /api/annualincome/<int:pk>/
https://charitable-tracker.herokuapp.com/api/annualincome/<int:pk>/
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
DELETE  /api/annualincome/<int:pk>/
https://charitable-tracker.herokuapp.com/api/annualincome/<int:pk>/
```

```json
None
```

### response

```json
None
```


<!-------------------------- List Upload Img ------------------------------>


[Back to Endpoints](#api-endpoints)

## List Upload Img

```
GET /api/upload/
https://charitable-tracker.herokuapp.com/api/upload/
```


```
None
```

### response

```json

{
	"upload": "https://charitabletracker.s3.amazonaws.com/reciepts/aaaa.jpg"
}



```


<!-------------------------- Upload Img ------------------------------>


[Back to Endpoints](#api-endpoints)

## Upload Img

```
POST /api/upload/
https://charitable-tracker.herokuapp.com/api/upload/
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
<!-------------------------- Edit Upload Img ------------------------------>


[Back to Endpoints](#api-endpoints)

## Edit Upload Img

```
PATCH /api/upload/<int:pk>/
https://charitable-tracker.herokuapp.com/api/upload/<int:pk>/
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
<!-------------------------- DELETE Upload Img ------------------------------>


[Back to Endpoints](#api-endpoints)

## DELETE Upload Img

```
POST /api/upload/<int:pk>/
https://charitable-tracker.herokuapp.com/api/upload/<int:pk>/
```


```
Select Img (.jpg), Have the following headers
Content-Disposition, attachment;filename=
	file name must match the uploaded img name
```

### response

```json

deleted



```



<!-------------------------- View All Reminders ------------------------------>


[Back to Endpoints](#api-endpoints)

## View All Reminders

```
GET /api/reminders/
https://charitable-tracker.herokuapp.com/api/reminders/
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
<!-------------------------- POST A Reminder ------------------------------>


[Back to Endpoints](#api-endpoints)

## POST A Reminder

```
POST /api/reminders/
https://charitable-tracker.herokuapp.com/api/reminders/
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
<!-------------------------- Edit All Reminders ------------------------------>


[Back to Endpoints](#api-endpoints)

## Edit A Reminder

```
PATCH /api/reminders/<int:pk>
https://charitable-tracker.herokuapp.com/api/reminders/api/reminders/<int:pk>
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
<!-------------------------- DELETE A Reminder ------------------------------>


[Back to Endpoints](#api-endpoints)

## DELETE A Reminder

```
DELETE /api/reminders/<int:pk>
https://charitable-tracker.herokuapp.com/api/reminders//api/reminders/<int:pk
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

<!-------------------------- registration ------------------------------>

[Back to Endpoints](#api-endpoints)

## registration

```
POST  /auth/registration/
https://charitable-tracker.herokuapp.com/auth/registration/
```

```json
{
	"username":"insomniatest",
	"password1":"o76218333",
	"password2":"o76218333"
}


```

### response

```json
{
	"key": "45973839a6219a439d9ae6608904b6c35abee88e"
}


```

<!-------------------------- View cause and time ------------------------------>

[Back to Endpoints](#api-endpoints)

## View cause and time

```
GET  /api/causetime/
https://charitable-tracker.herokuapp.com/api/causetime/
```

```json

This Can Be blank

```

### response

```json

needs updated

```

<!-------------------------- View cause and donation ------------------------------>

[Back to Endpoints](#api-endpoints)

## View cause and donation

```
GET  /api/causedonation/
https://charitable-tracker.herokuapp.com/api/causedonation/
```

```json

This Can Be blank

```

### response

```json
needs updated
```

<!-------------------------- View cause and donation ------------------------------>

[Back to Endpoints](#api-endpoints)

## View cause and donation

```
GET  /api/causedonation/
https://charitable-tracker.herokuapp.com/api/causedonation/
```

```json

This Can Be blank

```

### response

```json
needs updated
```

<!-------------------------- View organization and time ------------------------------>

[Back to Endpoints](#api-endpoints)

## View organization and time

```
GET api/organizationtime/
https://charitable-tracker.herokuapp.com/api/organizationtime/
```

```json

This Can Be blank

```

### response

```json

needs updated


```

<!-------------------------- View organization and donation ------------------------------>

[Back to Endpoints](#api-endpoints)

## View organization and donation

```
GET api/organizationdonation/
https://charitable-tracker.herokuapp.com/api/organizationdonation/
```

```json

This Can Be blank

```

### response

```json

needs updated

```