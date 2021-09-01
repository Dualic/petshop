def getsecret(secretname, version):
    import google.cloud.secretmanager as secretmanager
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/week10-1-324606/secrets/{secretname}/versions/{version}"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

def warehouseupdate(request):
    import psycopg2
    dbname = getsecret("dbname", 1)
    user = "postgres"
    password = getsecret("dbpassword", 1)
    host = getsecret("host", 1)
    conn = None
    request_json = request.get_json(silent=True)
    id = request_json.get("id")
    name = request_json.get("name")
    product_id = request_json.get("product_id")
    amount = request_json.get("amount")
    SQL = "UPDATE warehouse SET name = %s, product_id = %s, amount = %s WHERE id = %s;"
    result = "Update failed"
    try:
        conn = psycopg2.connect(host=host, dbname=dbname, user=user,  password=password)
        cursor = conn.cursor()
        cursor.execute(SQL, (name, product_id, amount, id))
        conn.commit()
        cursor.close()
        result = "Update success"
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()      
    return result