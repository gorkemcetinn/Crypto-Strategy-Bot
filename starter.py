import threading
import time
from producer import start_producer
from consumer import start_consumer

if __name__ == "__main__":
    # Producer thread
    t1 = threading.Thread(target=start_producer)
    t1.daemon = True
    t1.start()

    # Consumer thread
    t2 = threading.Thread(target=start_consumer)
    t2.daemon = True
    t2.start()

    print("🚀 Producer ve Consumer başlatıldı.")

    # Sonsuz döngüde ana thread'i açık tut
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("🛑 Program durduruldu.")
