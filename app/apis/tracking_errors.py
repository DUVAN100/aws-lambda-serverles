import json
import logging
import traceback

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
	try:
		logger.info(f"event error---> {event}")
		logger.info(f"context error---> {context}")
		response = {
			'statusCode': 500,
			'body': json.dumps({"message": "Error in operation"})
		}
		return response
	except Exception as e:
		logger.error(traceback.format_exc())
		logger.error(f"error in subtimes_info -> {e}")
		return {
			'statusCode': 500,
			'body': json.dumps({"error": "Internal server error"})
		}