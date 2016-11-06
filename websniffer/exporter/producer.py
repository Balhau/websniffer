from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')


try:
    for i in range(100):
        future=producer.send('org.balhau.websniffer.hosts', b'Cena '+str(i))
        record_metadata = future.get(timeout=10)
        print record_metadata
except KafkaError:
    # Decide what to do if produce request failed...
    print "Excepcao"
    pass
