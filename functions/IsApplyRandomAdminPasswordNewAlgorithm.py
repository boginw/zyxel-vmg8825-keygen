def zcfgBeCommonIsApplyRandomAdminPasswordNewAlgorithm(serialNumber: str) -> bool:
    return zcfgBeCommonIsSerailNumAfterYyWw(serialNumber, 2100, 48)

def zcfgBeCommonIsSerailNumAfterYyWw(serialNumber: str, yy: int, ww: int) -> bool:
    serialNumberYy = int(serialNumber[1:3]) + 2000
    serialNumberWw = int(serialNumber[5:7])

    return (yy == serialNumberYy and ww <= serialNumberWw) or (yy < serialNumberYy)
