import signal
#gestion du timeout
def timeout_handler():
    print("\nAssistant Doctolib : Temps terminé, au revoir ! 👋")
    exit(0)

def start_counter():
    signal.alarm(60)

def stop_counter():
    signal.alarm(0)