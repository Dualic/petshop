def getsecret(secretname):
    import google.cloud.secretmanager as secretmanager
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/week10-1-324606/secrets/{secretname}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email_notification(boughtitems):
    message = Mail(
        from_email='ilkka.pekkala@awacademyconsultant.fi',
        to_emails='ilkka.pekkala@awacademyconsultant.fi',
        subject='Your receipt',
        html_content=boughtitems)
    try:
        sg = SendGridAPIClient(getsecret("SENDGRID_EMAIL_API_KEY"))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

def checkout(request):
    import psycopg2, json
    dbname = getsecret("dbname")
    user = "postgres"
    password = getsecret("dbpassword")
    host = getsecret("host")
    conn = None
    request_json = request.get_json(silent=True)
    customer_id = request_json.get("customer_id")
    SQL1 = "SELECT id, product_id, amount FROM cart WHERE customer_id =%s;"
    SQL2 = "SELECT amount FROM warehouse WHERE product_id = %s;"
    SQL3 = "UPDATE warehouse SET amount = %s WHERE product_id = %s;"
    SQL4 = "DELETE FROM cart WHERE customer_id = %s;"
    SQL5 = "SELECT name, price FROM product WHERE id = %s;"
    basket= {}
    receipt = []
    receipt.append("You bought the following items:")
    totalsum = 0
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
            cursor.execute(SQL2, (basket[item]["product_id"],))
            row = cursor.fetchone()
            itemsinwarehouse = row[0]
            boughtamount = basket[item]["amount"]
            if itemsinwarehouse < boughtamount:
                return "You can't buy that many!"
            #Transaction can continue. Reduce the amount of warehouse items.
            newamount = itemsinwarehouse - boughtamount
            cursor.execute(SQL3, (newamount, basket[item]["product_id"]))
            cursor.execute(SQL5, (basket[item]["product_id"],))
            row2 = cursor.fetchone()
            receipt.append(f"Product: {row2[0]}, amount: {boughtamount},  price per item: {row2[1]}")
            totalsum += (boughtamount * row2[1])

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