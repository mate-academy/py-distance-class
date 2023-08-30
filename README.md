# Distance class
- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start
- Follow [Python magic methods](https://rszalski.github.io/magicmethods/) if you stuck
Every day you have morning running. You want to store your result. 
For easier calculating, comparison and printing your result write class
`Distance`.
`Distance`'s `__init__` method takes only
one argument `km` and saves it to `self.km`.
For `Distance` class you should implement such magic
methods:
```python
__init__
distance = Distance(20)  # distance.km == 20

__str__
distance = Distance(20)
	@@ -45,7 +45,7 @@ distance2 = Distance(30)
distance1 += distance2  # distance1.km is 50

distance = Distance(20)
distance += 30  # distance.km == 50

__mul__
distance1 = Distance(20)
	@@ -64,13 +64,13 @@ distance2 = distance1 / 7

__lt__, __gt__, __eq__, __le__, __ge__
distance = Distance(50)
distance < Distance(60)  # True  # distance.km < 60 == True
distance > Distance(120)  # False
distance == Distance(100)  # False
distance <= Distance(49)  # False
distance >= Distance(50)  # True

distance < 60  # True  # distance.km < 60 == True
distance > 120  # False
distance == 100  # False
distance <= 49  # False
distance >= 50  # True
```
