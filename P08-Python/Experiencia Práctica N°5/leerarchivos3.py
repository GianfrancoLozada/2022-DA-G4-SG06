def file_read(fname):
    with open (fname, "r") as myfile:
        data=myfile.readlines()
        print(data,"\n")
file_read('teste.txt')
file_read('test.txt')