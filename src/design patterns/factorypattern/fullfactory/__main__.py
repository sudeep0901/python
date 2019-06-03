from autofactory import AutoFactory

factory = AutoFactory()

for carname in "Maruti" , "Tata":
    car = factory.create_instance(carname)
    car.start()
    car.end()