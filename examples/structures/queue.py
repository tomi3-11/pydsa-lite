from pydsa_lite.structures import Queue
jobs=Queue[str]()
for job in ["report.pdf","notes.txt","photo.png"]:jobs.enqueue(job)
while not jobs.is_empty():print("Printing:",jobs.dequeue())
