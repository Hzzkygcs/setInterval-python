
# setInterval-python
Sometimes, when you're writing code in python, you have to make a function that needs to be executed every certain amount of time. 
This class will help you do that easily and dynamically on python. Open all of the flexibility to maintain the interval.

Declaring 
---------
To declare an interval function, you just need to call the setInterval class. The parameter is as follows:
```setInterval(Function,Interval[, Arguments=[]  ])``` 
The `Interval` is in second, by using number data type.
The `Arguments` is the arguments you need to pass to the function in array.

Here's a simple example:
```Python
def interval(name="world"):
  print(f"Hello {name}!")

# function named interval will be called every two seconds
#output: "Hello world!"
interval1 = setInterval(interval, 2) 

# function named interval will be called every 1.5 seconds
#output: "Hello Jane!"
interval2 = setInterval(interval, 1.5, ["Jane"]) 
```

Anyway, you can also initiate a blueprint of the interval without run it immediately. To make a blueprint, you must initiate the class without pass any argument. example: 
```obj=setInterval()```
You can utilize blueprint to do shared-variable trick. Please note that blueprint interval **won't be executed** until you explicitly start it using `start()` method

## Stop / Clear interval
To clear the interval, you just need to call `.stop()` from the object of setInterval. This method will immediately stop the interval. It is allowed to stop a stopped interval.

## Start a blueprint
To start a blueprint, you must call `.start()`. But please ensure you have provided the function and the interval time by using `.change_interval()`  and `.change_func()`. If not, an error `IntervalNotValid` will be raised. Running an already run interval will raise an `AlreadyRunning` error.

## Change the interval
To change the interval, there are two options available:
1. you change the interval immediately. Use `.change_interval(new_interval)`
2. you change the interval after the next interval. Use `.change_next_interval(new_interval)`

The difference is, if you change it immediately to `x` seconds, your function will be called right `x` seconds after you call the `change_interval` method.
If you change it after the next interval, it will allow to run the remaining queued function. Your change will be applied after the next call, **and not immediately**. 

Here's the difference example:
```Python
from time import sleep

i1 = setInterval(print,5,["hello"])
i2 = setInterval(print,5,["world"])

sleep(1) 

#the first 'hello' will be printed after 3 seconds of execution time (sleep:1 second + new interval : 2 second)
#the second 'hello' will be printed after 5 seconds of execution time
i1.change_interval(2) 

#the first 'world' will be printed after 5 seconds (old interval: 5 seconds)
#the second 'world' will be printed after 8 seconds (old interval: 5 seconds + new interval: 3 seconds)
i2.change_next_interval(3)

#stop those intervals after 10 seconds of execution time
time.sleep(10)
i1.stop(); i2.stop() 
```

## Change the function
To change the function, you must call the method
```change_func(newFunction[,newArgument=[]  ])```
The changes will be immediately applied.

Example:
```Python
import time

def a():
	print('a')
def b():
	print('b')

i = setInterval(a, 3)
time.sleep(4)
i.change_func(b)
time.sleep(7)
i.stop()

# output:
# a
# b
# b
```

Please note that it'll cost too much to make the  `change_next_func()` version of this method, where there're not much people will need this feature. So for the substitute, I provide the change_next_func trick by using `run_once()` method.

## Get the return
To get the return of the interval, you need to call `.get_return()` from the object of setInterval. This method will give you the returned data from the latest call. Please remember that `.get_return()` will give you `None` if the function haven't ever called, or if your function gives no return. 

Here's the example to get the returned object and to use shared memory trick:

```Python 
import time

def f(sharedMemory):
	sharedMemory.shared+=1
	print(sharedMemory.shared)
	return f"returned {sharedMemory.shared}"
i = setInterval()
i.shared=0
i.change_interval(2)
i.change_func(f, [ i ] )
i.start()

time.sleep(5) 
#sleep until the f has been called twice, 
#get the returned object of the latest call (the second call).
print( i.get_return() )
i.stop()
```

Please when doing the shared variable trick, don't use some special and critical name/property that's important for the class to run the interval for example `setInterval().func` and `setInterval().running`.

It is recommended **to only use** property `setInterval().shared` for the shared variable because **it'll never be used** by the class in future updates. So if you need more than one shared variable, just assign a dict or array to the  `setInterval().shared`.


## Run once
To run a function only once in the next interval, you can use `run_once()` method. The parameter is as follows:

```run_once( function [, Arguments =[]  ])```

The `function` is the one-time-run-function. It is the function that you want it to be run only once in the next interval. This function is run before the scheduled interval function.  If the function return `False` (and not `0` nor `None`), the next interval scheduled at that time will be cancelled.

The `Arguments` is the argument you want to pass to the one-time-run-function. 

This `run_once()` method can **provide a lot of tricks**  and provide a great flexibility.

Example 1, change_next_func:
```Python

```
