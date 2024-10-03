import redis

# Configuración de Redis
redis_host = 'redis-18746.c100.us-east-1-4.ec2.redns.redis-cloud.com'
redis_port = 18746
redis_password = '8foYaTMG60wi5EvpywQGrRBEiQotCzri'

# Conexión a Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Suscriptor
def subscriber():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('canal_prueba')
    
    print("Esperando mensajes...")
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Recibido: {message['data']}")

if __name__ == "__main__":
    subscriber()