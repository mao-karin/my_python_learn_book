def convert_sec_to_h_m_s(T):
    hour = T//3600           #3600 secs in an hour
    T%=3600                  #get remaining hour T= T % 3600
    minutes=T//60            #60 sec in a min
    T%=60                    #get remaining time in sec
    seconds = T              #result from line 5 is the seconds but this line just puts in variable seconds

    return "{}h {}m {}s".format(hour,minutes,seconds)

time= int(input("Enter time in seconds: "))
ouput_time= convert_sec_to_h_m_s(time)
print (ouput_time)


#check results:
#T = 7500 ...... 2h 5m 0s
#T= 83643 ...... 23h 14m 3 s