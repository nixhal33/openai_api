import threading
import time

class pyos:
    """This is the main OS simulation class combining FileSystem and ProcessManager."""
    def __init__(self):
        self.file_system = filesystem()
        self.process_manager = procmg()
        self.running = True

    def shell(self):
        """This will start a interactive shell for commands."""
        print("Welcome to PyOS! Type 'help' to list the commands.")
        while self.running:
            cmd=input("PyOS> ").strip()
            self.handlecmd(cmd)

    def handlecmd(self, cmd: str):
        """Parses and execute the commands from user"""
        args=cmd.split()
        if not args:
            return "Good job!"
        cmd=args[0]

        """File system cmds"""
        if cmd=="create":
            print(self.file_sytem.create(*args[1:]))
        elif cmd=="read":
            print(self.file_sytem.read(*args[1:]))
        elif cmd=="write":
            print(self.file_sytem.write(*args[1:], " ".join(args[2:])))
        elif cmd=="delete":
            print(self.file_system.delete(*args[1:]))
        elif cmd=="listall":
            print(self.file_sytem.listall())
        
        # this is process commands
        elif cmd == "runprocess":
            print(self.procmg.runprocess(self.example_task))
        elif cmd == "listproc":
            print(self.procmg.listproc(self.listproc))
        elif cmd == "killall":
            print(self.procmg.killall(self.killall))
        
        # this is basic help,exit cmd 
        elif cmd == "help":
            print(self.helptext())
        elif cmd == "exit":
            print("Shutting down the PyOS..........!!!!!")
            self.running=False
        else:
            print(f"Unknown cmd: {cmd}")

    def extask(self):
        """ A SIMPLE TASK FOR DEMO"""
        print(f"{threading.current_thread().name} is running.")
        for i in range(5):
            time.sleep(1)
            print(f"{threading.current_thread().name}: {i+1}/5")
        print(f"{threading.current_thread().name} is completed.")
        
    def help(self)->str:
        """This will return the help text for avaliable commands"""
        return """ Available commands:
        create_file <filename>            - Create a new file.
        read_file <filename>              - Read a file's content.
        write_file <filename> <content>   - Write content to a file.
        delete_file <filename>            - Delete a file.
        list_files                        - List all files.
        run_process                       - Run an example task.
        list_processes                    - List all running processes.
        terminate_all                     - Terminate all running processes.
        help                              - Show this help message.
        exit                              - Shut down PythonOS.
        """

    if __name__=="__main__":
        os_sim=()
        os_sim=shell()