def getsecret(secretname):
    import google.cloud.secretmanager as secretmanager
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/week10-1-324606/secrets/{secretname}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

def cartadd(request):
    import psycopg2
    dbname = getsecret("dbname")
    user = "postgres"
    password = getsecret("dbpassword")
    host = getsecret("host")
    conn = None
    request_json = request.get_json(silent=True)
    #id = request_json.get("id")
    customer_id = request_json.get("customer_id")
    product_id = request_json.get("product_id")
    amount = request_json.get("amount")
    SQL = "INSERT INTO cart(customer_id, product_id, amount) VALUES (%s,%s,%s);"
    result = "Insert failed"
    try:
        conn = psycopg2.connect(host=host, dbname=dbname, user=user,  password=password)
        cursor = conn.cursor()
        cursor.execute(SQL, (customer_id, product_id, amount))
        conn.commit()
        cursor.close()
        result = "Insert success"
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()      
    return result