import re

class Json():

    '''Just a small clone of Json library 
    - **As of now it processes string keys and string values only'''


    def __init__(self):

        # self.pattern = r"{([a-zA-Z]+:[a-zA-Z\s]+)+}"
        self.pattern = r"{([a-zA-Z\s]+:[a-zA-Z\s\,]+)+}"
        self.comma = r","


    def process(self, s):
        if "'" in s:
            s = s.replace("'", "")
        if re.search(self.pattern, s):
            splits = re.split(self.comma, s)
            d = {}
            for i, vals in enumerate(splits):
                if i  == 0:
                    vals = vals[vals.index("{")+1:]
                    a, b = vals.split(":")
                    # print(a, b)
                    d[a] = b
                elif i == len(splits)-1:
                    vals = vals[:vals.index("}")]
                    a, b =  vals.split(":")
                    # print(a,b)
                    d[a] = b
                else:
                    a, b = vals.split(":")
                    # print(a,b)
                    d[a] = b
            return d
        else:
            raise "Error reading string from file"


    def dumps(self, d: dict):
        '''Returns dictionary as a string 's' '''
        s = str(d)
        return s

    def find(self, s):
        print(re.search(self.pattern, s))

    def find_pairs(self, s):
        # print(re.search(self.comma, s))
        print(re.split(self.comma, s))

if __name__ == "__main__":

    d = {"hello":'was',"hi":'asd',"bye":'absd'}
    s = str(d).replace("'","")

    print(s)
    json = Json()
    # json.find("{aaobdoaASs:obdaso asdn:obdsao}")
    # json.find("{aaobdoaASs: obdaso,asdn: obdsao}")
    # json.find(s)
    # json.find_pairs(s)
    d = json.process(s)
    # print(d)
    # print(re.search(num, "1921a"))
    
    with open("test.txt","w") as f:
        s = json.dumps(d)
        f.write(s)

    with open('test.txt', 'r') as f:
        s = f.read()
        print(s)
        
        d = json.process(s)

    print(d)