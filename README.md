# PDF Stack Template API

Simple Fastapi template for PDF stack - pugsql + dbmate + fastapi.
Other than that it includes simple login with httponly cookie and a simple user model.

## Core
1. the API will be written using [fastapi](https://github.com/tiangolo/fastapi)
2. no ORM for us. Instead we will roll with [pugsql](https://github.com/mcfunley/pugsql)
3. migrations will be done using plain sql and [dbMate](https://github.com/mcfunley/pugsql).
4. on the db/persistance front - [postgres](https://www.postgresql.org/)
5. lastly, the app will be containerised - [docker](https://www.docker.com/)
6. Poetry for package
7. Sentry
8. Example of basic synchronous stripe integration
9. Example of basic httponly cookie magic link auth flow
10. Example of basic synchronous email sending

All of this works very simply.

If you need to remove stripe service, just delete the stripe dir and remove the router in main.py

## Getting started
To get up and running you need to copy .env.template and fill in the values.
Then you can run the following commands:

```bash
docker compose up
```
for one click deployment or
```bash
docker compose up -d database
docker compose run api dbmate up
poetry install
make run-dev
```
for local development.

Then head over to http://localhost:8000/docs to see the swagger docs.

## dmbate/pugsql
How to handle db querying and persistence? 

We will do that using plain SQL, wrapped with pugSQL and with the migrations run using dbMate. Weird choice? It is indeed, my dear.

PDF-stack. PugSQL, dbMate & FastAPI. I came to like it quite much. I've never seen this name before, so for now I'll assume to be the father of this acronym.

fastapi-pdf. Now that's cool!

To check out how all of that is ran, I encourage you to read pugsql & dbmate's documentation.

In short, dbmate is a tool that runs our sql across our databases and makes sure the migrations go as planned, everything is nice and dandy. If they fail, it cleans up.

Who generates the migrations and based on what? Well, you do! You write them in plain SQL. YUP. Feeling the 90s vibes yet? Hope you do.

Now, install dbmate. It's a single binary as it's a project written in go. You can just download it and...

```bash
sudo curl -fsSL -o /usr/local/bin/dbmate https://github.com/amacneil/dbmate/releases/latest/download/dbmate-linux-amd64
sudo chmod +x /usr/local/bin/dbmate
```

or on mac go with:

```bash
brew install dbmate
```

That's about it.

Now navigate to our project's root dir and type:

```bash
dbmate new create_models # dbmate new <desciprtion_of_the_migrations>
```

Which will create db/migrations/ directory that'll contain our migrations.

Inside of it you'll find a new file.

```bash 
-- migrate:up
<migration code goes here>

-- migrate:down
<rollback code goes here>
```
Surprisingly empty, right?
