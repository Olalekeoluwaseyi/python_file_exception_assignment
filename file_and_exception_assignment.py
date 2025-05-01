def modefyFileContent ():
    #Asking user to enter file name
    file_name = input("Please Enter File Name: ")

    try:
        #trying to open the file the user entered its name
        with open(file_name, "r+") as file:
            readlines = file.readlines()
            
            #If the file exist and readable, then we modify it save it to ofter file
            try:
                #adding prefix of modefied_ the the file name
                with open("modefied_"+file_name, "w+") as modefied:
                    m_line = []

                for line in readlines:
                    #modifying the content of the file, by change the content to upper case
                    m_line.append(line.upper())
                    
                #writing to the modified file
                modefied.writelines(m_line)              
            except Exception as m:
                print(m)
            
    except FileNotFoundError:
        print(f"Error: Sorry, {file_name} does not exist")
            
    except IOError:
        print(f"Error: Sorry {file_name} coluld not be read")

if __name__ == "__main__":
    modefyFileContent()