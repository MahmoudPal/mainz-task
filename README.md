# Project Documentation

## Prerequisites
Ensure you have Initialized SnowFlake and the SQL database:

- [Snowflake Initialization Script](mainz-task/migrations/snowflake_init.sql).
- [Azure SQL Initialization Script](mainz-task/migrations/sql_init.sql).

Ensure you created .env file and updated the keys
```sh
cp .env.example .env
```


## Setup Instructions
Follow these steps to set up the project environment:

### 1️⃣ Create a Conda Environment
```sh
conda create -n vp_task python=3.8
```

### 2️⃣ Activate the Environment
```sh
conda activate vp_task
```

### 3️⃣ Install Dependencies
Ensure all required Python packages are installed:
```sh
pip install -r requirements.txt
```

## Usage Instructions

Run the python script from BIT directory
```sh
Python main.py
```