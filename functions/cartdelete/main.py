def getsecret(secretname):
    import google.cloud.secretmanager as secretmanager
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/week10-1-324606/secrets/{secretname}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

def cartdelete(request):
    import psycopg2
    dbname = getsecret("dbname")
    user = "postgres"
    password = getsecret("dbpassword")
    host = getsecret("host")
    conn = None
    request_json = request.get_json(silent=True)
    customer_id = request_json.get("customer_id")
    SQL = "DELETE FROM cart WHERE customer_id = %s;"
    result = "Delete failed"
    try:
        conn = psycopg2.connect(host=host, dbname=dbname, user=user,  password=password)
        cursor = conn.cursor()
        cursor.execute(SQL, (customer_id,))
        conn.commit()
        cursor.close()
        result = "Delete success"
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()      
    return result