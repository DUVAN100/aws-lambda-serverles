import json
import logging
import traceback

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
	try:
		logger.info(f"event---> {event}")
		logger.info(f"event---> {context}")
		body = json.loads(event.get("body", "{}"))
		result = body.get("Country",{})
		body["processed_info"] = {"Country":result}
		response = {
			'statusCode': 200,
			'body': json.dumps(body)
		}
		return response
	except Exception as e:
		logger.error(traceback.format_exc())
		logger.error(f"error in subcountries_info -> {e}")
		raise Exception(event)