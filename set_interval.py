import threading


class AlreadyRunning(Exception):
    pass


class IntervalNotValid(Exception):
    pass


class setInterval():
    def __init__(this, func=None, sec=None, args=[], autostart=True):
        this.running = False
        this.func = func  # the function to be run
        this.sec = sec            # interval in second
        this.Return = None  # The returned data
        this.args = args
        this.runOnce = None  # asociated with run_once() method
        this.runOnceArgs = None   # asociated with run_once() method

        if (func is not None) and (sec is not None) and autostart:
            this.running = True

            if (not callable(func)):
                raise TypeError("non-callable object is given")

            if (not isinstance(sec, int) and not isinstance(sec, float)):
                raise TypeError("A non-numeric object is given")

            this.TIMER = threading.Timer(this.sec, this.loop)
            this.TIMER.start()

    def start(this):
        if (not this.running):
            if (not this.isValid()):
                raise IntervalNotValid("The function and/or the " +
                                       "interval hasn't provided or invalid.")
            this.running = True
            this.TIMER = threading.Timer(this.sec, this.loop)
            this.TIMER.start()
        else:
            raise AlreadyRunning("Tried to run an already run interval")

    def stop(this):
        this.running = False

    def isValid(this):
        if (not callable(this.func)):
            return False

        cond1 = not isinstance(this.sec, int)
        cond2 = not isinstance(this.sec, float)
        if (cond1 and cond2):
            return False
        return True

    def loop(this):
        if (this.running):
            this.TIMER = threading.Timer(this.sec, this.loop)
            this.TIMER.start()
            function_, Args_ = this.func, this.args

            if (this.runOnce is not None):  # someone has provide the run_once
                runOnce, this.runOnce = this.runOnce, None
                result = runOnce(*(this.runOnceArgs))
                this.runOnceArgs = None

                # if and only if the result is False. not accept "None"
                # nor zero.
                if (result is False):
                    return  # cancel the interval right now

            this.Return = function_(*Args_)

    def change_interval(this, sec):

        cond1 = not isinstance(sec, int)
        cond2 = not isinstance(sec, float)
        if (cond1 and cond2):
            raise TypeError("A non-numeric object is given")

        # prevent error when providing interval to a blueprint
        if (this.running):
            this.TIMER.cancel()

        this.sec = sec

        # prevent error when providing interval to a blueprint
        # if the function hasn't provided yet
        if (this.running):
            this.TIMER = threading.Timer(this.sec, this.loop)
            this.TIMER.start()

    def change_next_interval(this, sec):

        if (not isinstance(sec, int) and not isinstance(sec, float)):
            raise TypeError("A non-numeric object is given")

        this.sec = sec

    def change_func(this, func, args=[]):

        if (not callable(func)):
            raise TypeError("non-callable object is given")

        this.func = func

        if args is not None:
            this.args = args

    def change_argument(this, newArgument=[]):
        this.args = newArgument

    def run_once(this, func, args=[]):
        this.runOnce = func
        this.runOnceArgs = args

    def get_return(this):
        return this.Return
