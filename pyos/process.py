import threading


class procmg:
    """This will manage the process creation for multitasking using threads."""
    def __init__(self):
        self.processes=[]
        self.process_id=1

    def runprocess(self,target,*args)->str:
        """This will start a new process or a thread for a task."""
        procname=f"Process-{self.process_id}"
        self.process_id+=1
        thread=threading.Thread(target=target,args=args,name=procname)
        self.processes.append(thread)
        thread.start()
        return f"{procname} has started!!!"

    def listproc(self)->str:
        """This function will list all the running process in the system."""
        runningproc=[t.name for t in self.processes if t.is_alive()]
        if not runningproc:
            return "No running any current processes found!!!"
        return "Running process:  "+", ".join(runningproc)

    def killall(self)->str:
        """This will kill or terminate all the process that are running in the system"""
        for thread in self.processes:
            if thread.is_alive():
                print(f"Process killed {thread.name} (Simulation).")
        self.processes.clear()
        return "All process has been killed!!!"

