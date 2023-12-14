import math
import random

def lambda_handler(event, context):

    x = random.random()
    y = math.pi
    l = math.ceil(random.randint(0, 6000))


    return {
        'statusCode': 200,
        'body': l
    }
