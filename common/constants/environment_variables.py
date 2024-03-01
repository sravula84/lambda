from os import getenv

ENVIRONMENT_VARIABLES = {
    "USERNAME": getenv("API_USERNAME"),
    "PASSWORD": getenv("API_PASSWORD"),
    "API_URL": getenv("API_URL"),
}