import speedtest
st = speedtest.Speedtest()
option = int(input('what speed would you like to test?, \n'
                   '1) download speed? \n'
                   '2)upload speed? \n'
                   '3)ping? \n'
                   'Enter your choice'"  "))
if option == 1:
    print(st.download())
elif option ==2:
    print(st.upload())
elif option ==3:
    servernames =[]
    st.get_servers(servernames)
    print(st.results.ping)

else:
    print("Kindly select another choice")