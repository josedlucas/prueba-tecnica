import json
import requests
import boto3
def getBtcPrice(event, context):
	try:
		url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
		headers = {'X-CMC_PRO_API_KEY': 'a72fe67c-6e76-45ea-9af0-e9ddc4e072de'}
		parameters = {'symbol': 'BTC'}

		response = requests.get(url, headers=headers, params=parameters)
		data = json.loads(response.text)
		date = data['data']['BTC']['quote']['USD']['last_updated']
		price = data['data']['BTC']['quote']['USD']['price']
		# insert into dynamodb
		client = boto3.client('dynamodb')
		data = client.put_item(
			TableName='BTCPriceTable',
			Item={
				'date': {'S': date},
				'price': {'N': str(price)}
			}
		)
		return {
			"statusCode": 200,
			"body": json.dumps({'time':date, 'price_usd':price}),
			"headers": {
				'Access-Control-Allow-Origin': '*',
				'Access-Control-Allow-Credentials': True,
			}
		}
	except Exception as e:
		return {
			"statusCode": 500,
			"body": json.dumps('Error: '+str(e)),
			"headers": {
				'Access-Control-Allow-Origin': '*',
				'Access-Control-Allow-Credentials': True,
			}
		}