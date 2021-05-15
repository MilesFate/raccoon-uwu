from SCP_data import scp_173,scp_076

Search = input()
while True:
    if (Search == "scp 173"):
        scp_173()
        Search = input()
    elif (Search == "scp 096"):
        scp_076()
        Search = input()
    elif(Search == "quit"):
        break
    else:
        print("Invalid entry")
        Search = input()