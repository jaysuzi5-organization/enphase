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


### Table was created manually with:
```bash
CREATE TABLE enphase (
    id SERIAL PRIMARY KEY,
    system_id INTEGER NOT NULL,
    current_power INTEGER NOT NULL,
    energy_lifetime BIGINT NOT NULL,
    energy_today INTEGER NOT NULL,
    last_interval_end_at BIGINT NOT NULL,
    last_report_at BIGINT NOT NULL,
    modules INTEGER NOT NULL,
    operational_at BIGINT NOT NULL,
    size_w INTEGER NOT NULL,
    status VARCHAR(50) NOT NULL,
    summary_date DATE NOT NULL,
    events TEXT,
    alarms TEXT,
    create_date TIMESTAMPTZ DEFAULT now() NOT NULL,
    update_date TIMESTAMPTZ DEFAULT now() NOT NULL
);

-- Optional: Index for faster lookups by system_id
CREATE UNIQUE INDEX idx_enphase_create_date ON enphase(create_date);
CREATE UNIQUE INDEX idx_enphase_last_report_at ON enphase(last_report_at);

```