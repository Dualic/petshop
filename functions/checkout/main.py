def getsecret(secretname, version):
    import google.cloud.secretmanager as secretmanager
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/week10-1-324606/secrets/{secretname}/versions/{version}"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

def checkout(request):
    import psycopg2, json
    dbname = getsecret("dbname", 1)
    user = "postgres"
    password = getsecret("dbpassword", 1)
    host = getsecret("host", 1)
    conn = None
    request_json = request.get_json(silent=True)
    customer_id = request_json.get("customer_id")
    SQL1 = "SELECT id, product_id, amount FROM cart WHERE customer_id =%s;"
    SQL2 = "SELECT amount FROM warehouse WHERE product_id = %s;"
    SQL3 = "UPDATE warehouse SET amount = %s WHERE product_id = %s;"
    SQL4 = "DELETE FROM cart WHERE customer_id = %s;"
    basket= {}
    try:
        conn = psycopg2.connect(host=host, dbname=dbname, user=user,  password=password)
        cursor = conn.cursor()
        #Get the shopping cart for one customer.
        cursor.execute(SQL1, (customer_id,))
        row = cursor.fetchone()
        while row is not None:
            basket[row[0]] = {}
            basket[row[0]]["product_id"] = row[1]
            basket[row[0]]["amount"] = row[2]
            #results.append(str(row))
            row = cursor.fetchone()
        #Check that there is enough of each item.
        for item in basket:
            cursor.execute(SQL2, (item["product_id"],))
            row = cursor.fetchone()
            itemsinwarehouse = row[0]
            if itemsinwarehouse < item["amount"]:
                return "You can't buy that many!"
            #Transaction can continue. Reduce the amount of warehouse items.
            newamount = itemsinwarehouse - item["amount"]
            cursor.execute(SQL3, (newamount, item["product_id"],))
        #Empty the cart if all successful this far. Then commit the changes.
        cursor.execute(SQL4, (customer_id,))
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()      
    return json.dumps(basket), 200, {'ContentType':'application/json'}