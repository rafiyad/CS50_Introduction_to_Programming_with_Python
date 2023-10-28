import requests
import sys

if len(sys.argv)==1:
    sys.exit("Missing command-line argument")

else:
    try:
        if float(sys.argv[1]):
            try:
                multi=float(sys.argv[1])
                re=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
                o=re.json()
                coin=float((o["bpi"]["USD"]["rate_float"]))
                amount=coin*multi
                print(f"${amount:,.4f}")

            except requests.RequestException:
                sys.exit()


    except:
        sys.exit("Command-line argument is not a number")

