def getsecret(secretname):
    import google.cloud.secretmanager as secretmanager
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/week10-1-324606/secrets/{secretname}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

def productupdate(request):
    import psycopg2
    dbname = getsecret("dbname")
    user = "postgres"
    password = getsecret("dbpassword")
    host = getsecret("host")
    conn = None
    request_json = request.get_json(silent=True)
    id = request_json.get("id")
    name = request_json.get("name")
    price = request_json.get("price")
    category = request_json.get("category")
    SQL = "UPDATE product SET name = %s, price = %s, category = %s WHERE id = %s;"
    result = "Update failed"
    try:
        conn = psycopg2.connect(host=host, dbname=dbname, user=user,  password=password)
        cursor = conn.cursor()
        cursor.execute(SQL, (name, price, category, id))
        conn.commit()
        cursor.close()
        result = "Update success"
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()      
    return result