def getsecret(secretname, version):
    import google.cloud.secretmanager as secretmanager
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/week10-1-324606/secrets/{secretname}/versions/{version}"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

def productgetall(request):
    import psycopg2, json
    dbname = getsecret("dbname", 1)
    user = "postgres"
    password = getsecret("dbpassword", 1)
    host = getsecret("host", 1)
    conn = None
    SQL = "SELECT * FROM product;"
    results = {}
    try:
        conn = psycopg2.connect(host=host, dbname=dbname, user=user,  password=password)
        cursor = conn.cursor()
        cursor.execute(SQL)
        #conn.commit()
        row = cursor.fetchone()
        while row is not None:
            results[row[0]]["name"] = row[1]
            results[row[0]]["price"] = row[2]
            results[row[0]]["category"] = row[3]
            #results.append(str(row))
            row = cursor.fetchone()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()      
    return json.dumps(results), 200, {'ContentType':'application/json'}