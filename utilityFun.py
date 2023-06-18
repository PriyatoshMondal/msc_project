
def inputTaker():
    inputDict = {}

    temp = input("Provide the accn: ")
    accn = temp if(temp) else None

    temp = input("Provide the site id: ")
    siteid = temp if(temp) else None

    temp = input("Provide the metal name: ")
    metal_name = temp if(temp) else None

    temp = int(input("Provide the metal resid: "))
    metal_resid = temp if(temp) else None

    temp = input("Provide the bases name1: ")
    bases_name1 = temp if(temp) else None

    temp = input("Provide the bases chain1: ")
    bases_chain1 = temp if(temp) else None

    temp = input("Provide the bases name2: ")
    bases_name2 = temp if(temp) else None

    temp = input("Provide the bases chain2: ")
    bases_chain2 = temp if(temp) else None
    
    temp = input("Provide the attrib bptype: ")
    attrib_bptype = temp if(temp) else None

    # adding the provided values to the input dictionary
    inputDict['accn'] = accn
    inputDict['siteid'] = siteid
    inputDict['metal_name'] = metal_name
    inputDict['metal_resid'] = metal_resid
    inputDict['bases_name1'] = bases_name1
    inputDict['bases_name2'] = bases_name2
    inputDict['bases_chain1'] = bases_chain1
    inputDict['bases_chain2'] = bases_chain2
    inputDict['attrib_bptype'] = attrib_bptype

    return inputDict


def matchString(inpString, fileString):
    if(len(inpString)>len(fileString)):
        return 0
    else:
        for i in range(len(inpString)):
            if(inpString[i] != fileString[i]):
                return 0
        return 1

def isPresent(inputVal, fileDataVal):
    if(inputVal == None):
        return -1
    if(isinstance(inputVal, str)):
        return matchString(inputVal, fileDataVal)
    else:
        if(inputVal == fileDataVal):
            return 1
        else:
            return 0

def isSiteIdPresent(inputVal, fileDataVal):
    return isPresent(inputVal, fileDataVal)

def isMetalPresent(input_metal_name, input_metal_resid, fileData):
    return isPresent(input_metal_name, fileData.get('name')) and isPresent(input_metal_resid, fileData.get('resid'))

def isBases1Present(input_bases_name1, input_bases_chain1, fileData):
    return isPresent(input_bases_name1, fileData.get('name1')) and isPresent(input_bases_chain1, fileData.get('chain1'))

def isBases2Present(input_bases_name2, input_bases_chain2, fileData):
    return isPresent(input_bases_name2, fileData.get('name1')) and isPresent(input_bases_chain2, fileData.get('chain1'))

def isAttribPresent(input_attrib_bptype, fileData):
    return isPresent(input_attrib_bptype, fileData.get('bptype'))

def checkDataAndReturn(inputDict, fileData):
    if(inputDict.get('accn') == fileData.get('accn')):
        for item in fileData.get('metbp_sites'):
            pFlag = isSiteIdPresent(inputDict.get('siteid'), item.get('siteid'))
            pFlag = pFlag and isMetalPresent(inputDict.get('metal_name'), inputDict.get('metal_resid'), item.get('metal'))
            pFlag = pFlag and isBases1Present(inputDict.get('bases_name1'), inputDict.get('bases_chain1'), item.get('bases'))
            pFlag = pFlag and isBases2Present(inputDict.get('bases_name2'), inputDict.get('bases_chain2'), item.get('bases'))
            pFlag = pFlag and isAttribPresent(inputDict.get('attrib_bptype'), item.get('attrib'))
            if(pFlag):
                return item
    else:
        return 0