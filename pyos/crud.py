class filesystem:
    """This will simulate a simple in-memory in the system to complete basic operations."""
    def __init__(self):
        self.files = {}

    def create(self,filenm:str,content: str="")->str:
        """this function will create a file where you can put some content in it..."""
        if filenm in self.files:
            return f"Error: File '{filenm}' already exists"
        self.files[filenm]=content
        return f"File '{filenm}' has been created sucessfully!!"

    def read(self,filenm:str)->str:
        """this function will read the contents in the file"""
        if filenm not in self.files:
            return f"Error File '{filenm}' does not exist in the system..."
        return self.files[filenm]

    def write(self,filenm:str,content:str)->str:
        """This will update the contents inside of the existing file"""
        if filenm not in self.files:
            return f"Error File '{filenm}' does not exist in the system...."
        self.files[filenm]=content
        return f"File '{filenm}' has been updated sucessfully!!!"

    def delete(self,filenm:str)->str:
        """This will delete the file from the system"""
        if filenm not in self.files:
            return f"Error File '{filenm}' does not exist in the system...."
        del self.files[filenm]
        return f"File '{filenm}' has been deleted sucessfully!!!"

    def listall(self)->str:
        if not self.files:
            return "No files avaliable!!!!!!"
        return "Files: "+",  ".join(self.files.keys())