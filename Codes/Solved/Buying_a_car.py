def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    print(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth)
    cash = 0
    SPM = savingperMonth
    month = 0
    while cash <= 0:
        if startPriceOld>startPriceNew: return [0, startPriceOld-startPriceNew]
        elif(startPriceOld == startPriceNew): return [0, 0]
        month += 1
        if month % 2 == 0: percentLossByMonth += 0.5
        startPriceOld = startPriceOld - startPriceOld * percentLossByMonth / 100
        startPriceNew = startPriceNew - startPriceNew * percentLossByMonth / 100
        cash = startPriceOld - startPriceNew + savingperMonth
        savingperMonth+=SPM
    return [month, int(round(cash, 0))]
nbMonths(7500, 32000, 300, 1.55)