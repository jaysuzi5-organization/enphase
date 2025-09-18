# Documentation for enphase
### fastAPI: Used for collecting and retrieving data from Enphase Energy APIs which stores data about my solar panels.


This application has two generic endpoints:

| Method | URL Pattern           | Description             |
|--------|-----------------------|--------------------|
| GET    | /api/v1/enphase/info         | Basic description of the application and container     |
| GET    | /api/v1/enphase/health    | Health check endpoint     |



## CRUD Endpoints:
| Method | URL Pattern           | Description             | Example             |
|--------|-----------------------|--------------------|---------------------|
| GET    | /api/v1/enphase         | List all enphase     | /api/v1/enphase       |
| GET    | /api/v1/enphase/{id}    | Get enphase by ID     | /api/v1/enphase/42    |
| POST   | /api/v1/enphase         | Create new enphase    | /api/v1/enphase       |
| PUT    | /api/v1/enphase/{id}    | Update enphase (full) | /api/v1/enphase/42    |
| PATCH  | /api/v1/enphase/{id}    | Update enphase (partial) | /api/v1/enphase/42 |
| DELETE | /api/v1/enphase/{id}    | Delete enphase        | /api/v1/enphase/42    |


### Access the info endpoint
http://home.dev.com/api/v1/enphase/info

### View test page
http://home.dev.com/enphase/test/enphase.html

### Swagger:
http://home.dev.com/api/v1/enphase/docs

