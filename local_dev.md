### Git clone repo

    git clone git@github.com:ilijapet/the_witness_blockchain_base_IoT_data_protection_system.git
    cd the_witness_blockchain_base_IoT_data_protection_system

### Adding envirnomet variables

Add `.env` file to `cartesi_frontend` and to `cartesi_backend`. Then add `.env_dev` to backend

### Create, activate venv's, install dependencies, build docker image and run containers and servers

#### Backend

    cd backend
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python -m manage createsuperuser # or use ilijapet@gmail.com

This user should be used for loging into frontend. or you can register user via frontend # ones react server is up and runing locally

#### Cartesi backend

In separate terminal (before this step make sure that you don't have active venv from backend inside
cartesi_backend)

    cd cartesi_backend
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    cartesi build

#### React fronetend

In separate terminal

    cd cartesi_frontend
    npm install

### Run Server

### Test The Witness dapp

From cartesi_frontend

    npm run dev

From cartesi_backend

    cartesi run

From backend folder

    python -m manage runserver 8005

From postman or temirnal register new IoT device:

curl --location 'http://localhost:8005/api/v1/iot-registration' \
--header 'Content-Type: application/json' \
--form 'public_key="-----BEGIN PUBLIC KEY-----\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzS7RpUWk+rREuUjU6lFL\\ngeqsQmnydlBDsUhOVMDWR9sxtyjckRjk3lvqnK3IMEVJITs4xZLXk04mnOAHxgI0\\nWyzBsaYV7OG0iVU6Pj4GMVsLiAo9uqzUNJuUUx51BVf0lXezAucM+p5kfn6GewtG\\nyNImfWD/xWJpadNeMSM5souNZQUF6na04+NlLAnyuHhLlfv5pdKS8zg5FvYUzubX\\nGaKRVNMcZGyl85IrnIeNr3Gbl5biATesQ1+9U12/2zWc7auQi3Str7ro9hsOk4eI\\n3OXeXfVmPml/HpupFsXHZ4RA3ne4jHnKxmqjIO4S5GJxkiq5Dz+3UpoxwWGxsspu\\nIwIDAQAB\\n-----END PUBLIC KEY-----"'

Then go to the front-end, log as superuser for example and check how The Witness dapp is working
(test mail: ilijapet@gmail.com test password: Meridseli1986!)
