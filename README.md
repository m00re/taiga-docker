# taiga-docker

A small Docker Image for the open-source project management software Taiga.io  - compressed image size is 344 MB. The recipe is based on the existing recipe by [benhutchins](https://github.com/benhutchins): see https://github.com/benhutchins/docker-taiga for his approach.

Tested / supported versions of Taiga:

- Version 3.0.0

## Image details

- The image contains Taiga backend and Taiga frontend. 
- Frontend and backend are served by a Nginx server instance running on port 80.
- The Nginx server instance accepts HTTP connections only (no HTTPS), but you can create an own image that enables HTTPS by adjusting the nginx.conf template.
- PostgreSQL database server is not included, i.e. a db server instance is expected to be running elsewhere (either in a different container that is linked, or hosted somewhere else).
- The image is published on Dockerhub as `m00re/taiga`

Important environment parameters for configuration:
- `TAIGA_HOSTNAME`: The name of the server/domain, through which the Taiga instance will be accessed in the end, e.g. `taiga.yourdomain.tld` (default: `localhost`).
- `TAIGA_SSL`: Defines whether the Taiga instance will be accessible through SSL or not, (default: `false`).
- `TAIGA_SECRET_KEY`: Defines the secret key used internally by Taiga (default: `!!!PLEASE-REPLACE-ME!!!`), e.g. for password hashing or similar operations. Please change the default value.
- `TAIGA_DB_HOST`: Defines the hostname of the server on which the PostgreSQL instance is running (default: `localhost`).
- `TAIGA_DB_NAME`: Defines the database name on the PostgreSQL instance (default: `postgres`).
- `TAIGA_DB_USER`: Defines the database username for PostgreSQL connections (default: `postgres`).
- `TAIGA_DB_PASSWORD`: Defines the password for database connections (default: `!!!PLEASE-REPLACE-ME!!!`).
- `TAIGA_PUBLIC_REGISTER_ENABLED`: Defines whether new user registrations are enabled (default: `false`).
- `TAIGA_BACKEND_DEBUG`: Enables or disables backend debugging (default: `false` ).
- `TAIGA_FRONTEND_DEBUG`: Enables or disables frontend debugging (default: `false`).
- `TAIGA_FEEDBACK_ENABLED`: Enables sending of feedback to Taiga.io developers (default: `false`).
- `TAIGA_DEFAULT_LANGUAGE`: Defines the default language in the frontend (default: `en`).
- `TAIGA_DEFAULT_THEME`: Defines the default theme to be used (default: `material-design`).

Important directories inside of the image:
- Backend distribution is located in `/taiga.io/taiga-back`
- Frontend distribution is located in `/taiga.io/taiga-front`
- Uploaded media files (e.g. attachments, project logos, profile pcitures) are stored in `/taiga.io/taiga-back/media`

## Example usage with docker-compose

The following docker-compose.yml recipe shows how you can easily start your own Taiga instance, in combination with an own PostgreSQL container image. The important directories of both containers are linked as volumes, for easy backup.

```
postgres:
  image: postgres:9.6.1-alpine
  environment:
    POSTGRES_DB: "taiga"
    POSTGRES_USER: "taiga"
    POSTGRES_PASSWORD: "3MwR95cj9YAP7zm2lKrU"
  volumes:
    - taiga-db:/var/lib/postgresql/data

taiga:
  image: m00re/taiga
  ports:
    - 80:80
  links:
    - postgres
  environment:
    TAIGA_HOSTNAME: "localhost"
    TAIGA_DB_HOST: "postgres"
    TAIGA_DB_NAME: "taiga"
    TAIGA_DB_USER: "taiga"
    TAIGA_DB_PASSWORD: "3MwR95cj9YAP7zm2lKrU"
    TAIGA_SECRET_KEY: "<YOUR_SECRET_KEY_HERE>"
    TAIGA_PUBLIC_REGISTER_ENABLED: "true"
    TAIGA_BACKEND_DEBUG: "false"
    TAIGA_FRONTEND_DEBUG: "false"
    TAIGA_FEEDBACK_ENABLED: "false"
    TAIGA_DEFAULT_LANGUAGE: "de"
    TAIGA_SSL: "false"
    TAIGA_DEFAULT_THEME: "material-design"
  volumes:
    - taiga-media:/taiga.io/taiga-back/media
```

To bring both up, simply type:

`docker-compose -f ./docker-compose.yml -p taiga up -d`
