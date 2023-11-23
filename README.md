
## Requirements:

1. python == 3.11
2. aiogram == 3.1.1
3. postgresql == 16.1
4. asyncpg == 4.0.3

___

## How to install:

1. Create a project in your IDE/IDLE
2. Create a local repository:
```
git init
```
3. Push down this git:
```
git clone https://github.com/wannadieintears/todobot.git
```
4. Create a table in your database:
```
CREATE TABLE IF NOT EXISTS public.todos
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 376856534427 CACHE 1 ),
    todo text COLLATE pg_catalog."default" NOT NULL,
    user_id bigint NOT NULL,
    CONSTRAINT todos_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.todos
    OWNER to postgres;
```
5.  Install libraries/frameworks: 
```
pip install aiogram, asyncpg
```
6. Create and fill settings.py with: 
token, user, password, port, host, database 