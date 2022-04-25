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
    - hours: IntField
    - created_at: DateField
    - organization: CharField
    - description: CharField
    - volunteerreceipt: ImgField
    - volunteerrecord: FK
    - cause: CharField


## API Endpoints

|  Method  |  Endpoint  |  Description |  Deployed  |
| -------- | ---------- | ------------ | ---------- |
|GET|[/api/Dgoals/](#view-all-donation-goals)|View All Donation Goals| Yes|
|POST|[/api/Dgoals/](#add-a-donation-goal)|Add a donation goal|Yes
|GET|[/api/Dgoal/<int:pk>/](#view-a-singular-donation-goal)|View a singular donation goal|Yes|
|PUT|[/api/Dgoal/<int:pk>/](#edit-a-singular-donation-goal)|Edit a singular donation goal|Yes|
|DELETE|[/api/goal/<int:pk>/](#delete-a-singular-donation-goal)|Delete a singular donation goal|Yes|
|GET|[/api/Vgoals/](#view-all-volunteer-goals)|View all volunteer goals|Yes|
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


<!-------------------------- View all donation goals ------------------------------>


[Back to Endpoints](#api-endpoints)

## View all donation goals

```
GET /View all donation goals/
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
	"pk": 2,
	"user": 1,
	"goaltitle": "Women Empowerment",
	"donationgoal": 50,
	"interval": "Year"
}
```

### response

```json

{
	"pk": 2,
	"user": 1,
	"goaltitle": "Women Empowerment",
	"donationgoal": 50,
	"interval": "Year"
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
GET /View all volunteer goals/
```

```json
This Can be blank
```

### response

```json
{
	"user": 1,
	"goaltitle": "Women Empowerment",
	"volunteergoal": 50,
	"interval": "Year"
}
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
	"pk": 2,
	"amountdonated": 50,
	"created_at": "2022-04-23",
	"organization": "BLM",
	"donationreceipt": "http://127.0.0.1:8000/reciepts/Maroon_Circle_Political_Logo_1_K2oFHBE.png",
	"cause": "Black Rights"
},
{
	"pk": 3,
	"amountdonated": 2,
	"created_at": "2022-04-23",
	"organization": "Venture Outdoors",
	"donationreceipt": null,
	"cause": "Environmental"
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
	"amountdonated": 5,
	"created_at": "2022-04-23",
	"organization": "Prototype",
	"cause": "Environmental",
    "donationrecord": 1
}
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
	"created_at": "2022-04-23",
	"organization": "PrototypePGH",
	"cause": "Environmental",
    "donationrecord": 1
}

```

### response

```json
{
	"pk": 8,
	"amountdonated": 5,
	"created_at": "2022-04-23",
	"organization": "PrototypePGH",
	"donationreceipt": null,
	"cause": "Environmental",
	"donationrecord": 1
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
	"hours": 3,
	"created_at": "2022-04-20",
	"organization": "Venture Outdoors",
	"description": "Led a hike",
	"cause": "Education",
	"volunteerrecord": 2
}

```

### response

```json
{
	"pk": 2,
	"hours": 3,
	"created_at": "2022-04-20",
	"organization": "Venture Outdoors",
	"description": "Led a hike",
	"volunteerreceipt": null,
	"cause": "Education",
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
	"pk": 2,
	"hours": 3,
	"created_at": "2022-04-20",
	"organization": "Venture Outdoors",
	"description": "Led a hike",
	"volunteerreceipt": null,
	"cause": "Education",
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
	"pk": 2,
	"hours": 3,
	"created_at": "2022-04-20",
	"organization": "Venture Outdoors",
	"description": "Led a hike",
	"volunteerreceipt": null,
	"cause": "Education",
	"volunteerrecord": 2
}


```

### response

```json
{
	"pk": 2,
	"hours": 3,
	"created_at": "2022-04-20",
	"organization": "Venture Outdoors",
	"description": "Led a hike",
	"volunteerreceipt": null,
	"cause": "Education",
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