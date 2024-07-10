import django.dispatch

# providing_args=["batches", "sent", "sent_actual", "run_time"]
emitted_notices = django.dispatch.Signal()
