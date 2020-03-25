import threading

class setInterval():
    def __init__(this,func, sec,args=[]):
        this.running=True       
        this.func=func                     #the function to be run
        this.sec=sec                          #interval in second
        this.Return=None               #The returned data
        this.args=args
        this.runOnce=None           #asociated with run_once() method
        this.runOnceArgs=None   #asociated with run_once() method
        this.TIMER=threading.Timer(this.sec, this.loop)
        this.TIMER.start()
        
    def stop(this):
        this.running=False
        
    def loop(this):
        if (this.running):
            this.TIMER=threading.Timer(this.sec, this.loop)
            this.TIMER.start()
            if (this.runOnce!=None): #someone has run the run_once
                runOnce,this.runOnce=this.runOnce,None
                result=runOnce( *(this.runOnceArgs)  )
                this.runOnceArgs=None
                if ( result ==False ): #if and only if the result is False. not accept "None" nor zero.
                    return ; #cancel the interval right now
            this.Return=this.func(*this.args)
            
    def change_interval(this,sec):
        this.TIMER.cancel(); this.sec=sec
        this.TIMER=threading.Timer(this.sec, this.loop); this.TIMER.start()
        
    def change_next_interval(this,sec):
        this.sec=sec
        
    def change_func(this,func,args=[]):
        this.func=func
        this.args=args
        
    def run_once(this,func,args=[]):
        this.runOnce=func
        this.runOnceArgs=args
    def get_return(this):
        return this.Return
