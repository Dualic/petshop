import psycopg2
import google.cloud.secretmanager as secretmanager

def getsecret(secretname):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/week10-1-324606/secrets/{secretname}/versions/1"
    response = client.access_secret_version(request={"name": name})
    payload = response.payload.data.decode("UTF-8")
    secret = "Plaintext: {}".format(payload)
    return secret

def warehouse(request):
    dbname = getsecret("dbname")
    user = "postgres"
    password = getsecret("dbpassword")
    conn = psycopg2.connect(host='/cloudsql/week10-1-324606:us-central1:petshop', dbname=dbname, user=user,  password=password)