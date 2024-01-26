import django_setup
from tasks.models import Status, User, Task

in_process = Status.objects.get(title="In process")
completed = Status.objects.get(title="Completed")
postponed = Status.objects.get(title="Postponed")

john_doe = User.objects.get(name="John Doe", email="johndoe@johndoe.johndoe")
jane_doe = User.objects.get(name="Jane Doe", email="janedoe@email.com")

task1 = Task.objects.get(id=1)
task2 = Task.objects.get(id=2)
task3 = Task.objects.get(id=3)

task3.creator = jane_doe
task3.save()
