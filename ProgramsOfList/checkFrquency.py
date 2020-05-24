def checkFrequency(list):
    result={}
    for frquency in list:
        keys=result.keys()
        if frquency in keys:
            result[frquency]+=1
        else:
            result[frquency]=1
    return result

print(checkFrequency("Monu Kumar Shukla"))