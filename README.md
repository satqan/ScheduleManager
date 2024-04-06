# Coach Schedule Manager


## Prerequisites

- [Python](https://www.python.org/) 3.10.x
- [Django Rest Framework](http://www.django-rest-framework.org/) 3.15.x
- [Docker](https://docs.docker.com) 23.0.5
- [Docker Compose](https://docs.docker.com/compose/) v2.17.3
- [PostgreSQL](https://www.postgresql.org) 14.6


## Features

- JWT authorizarion
- Create Coach Schedule
- Create Record (handles time clashes)

Database Visualizer [link](https://gh.atlasgo.cloud/explore/0b60aa15
)

## Installation

Clone this repository:

```shell
$ git clone git@github.com:satqan/ScheduleManager.git && cd ScheduleManager
```

Build and Start Docker containers:

```shell
$ docker-compose up --build
```

Now you can access the application at http://localhost:8000.




    
## Major API Reference

#### Create Client or Coach

```http
  POST /users/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**.  |
| `password` | `string` | **Required**. |
| `first_name` | `string` ||
| `last_name` | `string` |  |
| `role` | `string` | **Required**. |
| `date_of_birth` | `string` | Birth date of a coach |
| `gender` | `string` | gender of a coach |
| `gyms` | `string` | gyms related to a coach |


#### Create Schedule (coach)

```http
  POST /schedules/
```

| Parameter    | Type     | Description                               |
|:-------------|:---------|:------------------------------------------|
| `coach`      | `string` | **Required**. coach ID                    |
| `gym`        | `string` | **Required**. gym ID                      |
| `weekday`    | `string` | **Required**. week day for given schedule |
| `start_time` | `string` | **Required**.                             |
| `end_time`   | `string` | **Required**.                             |


#### Create Record (client-coach)

```http
  POST /records/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `coach`      | `string` | **Required**. coach ID|
| `client`      | `string` | **Required**. client ID  |
| `gym`      | `string` | **Required**. gym ID |
| `start_time`      | `string` | **Required**. desired start time of training session |
| `end_time`      | `string` | **Required**. desired end time of training session|


