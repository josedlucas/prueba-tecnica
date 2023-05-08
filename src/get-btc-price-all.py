from datetime import date
import json
import boto3
import arrow
def getBtcPriceAll(event, context):
	# get all prices saved in dynamodb
	try:
		client = boto3.client('dynamodb')
		data = client.scan(
			TableName='BTCPriceTable',
			Select='ALL_ATTRIBUTES'
		)

		dates = []
		prices = []
		for item in data['Items']:
			# formatear fecha
			dates.append(arrow.get(item['date']['S']).format('YYYY-MM-DD HH:mm:ss'))
			prices.append(round(float(item['price']['N']), 2))

		data = {
			'dates': dates,
			'prices': prices
		}

		return {
			"statusCode": 200,
			"body": json.dumps(data),
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