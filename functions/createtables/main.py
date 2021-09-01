def getsecret(secretname, version):
    import google.cloud.secretmanager as secretmanager
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/week10-1-324606/secrets/{secretname}/versions/{version}"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

def warehousedelete(request):
    import psycopg2
    dbname = getsecret("dbname", 1)
    user = "postgres"
    password = getsecret("dbpassword", 1)
    host = getsecret("host", 1)
    conn = None
    SQL1 = ";"
    SQL2 = ";"
    SQL3 = ";"
    SQL4 = ";"
    result = "Creation of tables failed"
    try:
        conn = psycopg2.connect(host=host, dbname=dbname, user=user,  password=password)
        cursor = conn.cursor()
        cursor.execute(SQL1)
        cursor.execute(SQL2)
        cursor.execute(SQL3)
        cursor.execute(SQL4)
        conn.commit()
        cursor.close()
        result = "Creation of tables success!"
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()      
    return result