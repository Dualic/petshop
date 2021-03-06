def getsecret(secretname):
    import google.cloud.secretmanager as secretmanager
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/week10-1-324606/secrets/{secretname}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

def warehouseget(request):
    import psycopg2, json
    dbname = getsecret("dbname")
    user = "postgres"
    password = getsecret("dbpassword")
    host = getsecret("host")
    conn = None
    id = request.args.get('id')
    SQL = f"SELECT * FROM warehouse WHERE id={id};"
    results = {}
    try:
        conn = psycopg2.connect(host=host, dbname=dbname, user=user,  password=password)
        cursor = conn.cursor()
        cursor.execute(SQL)
        #conn.commit()
        row = cursor.fetchone()
        while row is not None:
            results["id"] = row[0]
            results["name"] = row[1]
            results["product_id"] = row[2]
            results["amount"] = row[3]
            row = cursor.fetchone()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()      
    return json.dumps(results), 200, {'ContentType':'application/json'}