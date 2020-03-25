import threading

class AlreadyRunning(Exception):
    pass
class IntervalNotValid(Exception):
    pass
class setInterval():
    def __init__(this,func=None, sec=None,args=[]):
        this.running=False       
        this.func=func          #the function to be run
        this.sec=sec            #interval in second
        this.Return=None        #The returned data
        this.args=args
        this.runOnce=None       #asociated with run_once() method
        this.runOnceArgs=None   #asociated with run_once() method
        if (func!=None and sec!=None):
            this.running=True
            if (not callable(func)):
                raise TypeError("non-callable object is given")
            if (type(sec)!=type(1) and type(sec)!=type(0.1)):
                raise TypeError("A non-numeric object is given")
            this.TIMER=threading.Timer(this.sec, this.loop)
            this.TIMER.start()

    def start(this):
        if (not this.running):
            if (not this.isValid()):
                raise IntervalNotValid("The function and/or the interval hasn't provided or invalid.")
            this.running=True
            this.TIMER=threading.Timer(this.sec, this.loop)
            this.TIMER.start()
        else:
            raise AlreadyRunning("Tried to run an already run interval")
        
    def stop(this):
        this.running=False

    def isValid(this):
        if (not callable(this.func)):
            return False
        if (type(this.sec)!=type(1) and type(this.sec)!=type(0.1)):
            return False
        return True
    
    def loop(this):
        if (this.running):
            this.TIMER=threading.Timer(this.sec, this.loop)
            this.TIMER.start()
            function_,Args_=this.func,this.args
            if (this.runOnce!=None): #someone has provide the run_once
                runOnce,this.runOnce=this.runOnce,None
                result=runOnce( *(this.runOnceArgs)  )
                this.runOnceArgs=None
                if ( result == False ): #if and only if the result is False. not accept "None" nor zero.
                    return ; #cancel the interval right now
            this.Return=function_(*Args_)
            
    def change_interval(this,sec):
        if (type(sec)!=type(1) and type(sec)!=type(0.1)):
            raise TypeError("A non-numeric object is given")
        if (this.running): #prevent error when providing interval to a blueprint
            this.TIMER.cancel()
        this.sec=sec
        if (this.running): #prevent error when providing interval to a blueprint if the function hasn't provided yet
            this.TIMER=threading.Timer(this.sec, this.loop); this.TIMER.start()
        
    def change_next_interval(this,sec):
        if (type(sec)!=type(1) and type(sec)!=type(0.1)):
            raise TypeError("A non-numeric object is given")
        this.sec=sec
        
    def change_func(this,func,args=[]):
        if (not callable(func)):
            raise TypeError("non-callable object is given")
        this.func=func
        this.args=args
        
    def run_once(this,func,args=[]):
        this.runOnce=func
        this.runOnceArgs=args
    def get_return(this):
        return this.Return
