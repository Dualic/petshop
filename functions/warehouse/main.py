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

    SQL = "SELECT * FROM user;"
    try:
        conn = psycopg2.connect(host='/cloudsql/week10-1-324606:us-central1:petshop', dbname=dbname, user=user,  password=password)
        cursor = conn.cursor()
        cursor.execute(SQL,)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()
        cursor.close()