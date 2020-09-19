def fillable(stock, merch, n):
    if merch in stock and n <= stock.get(merch): return True
    else: return False

stock = {
}
fillable(stock, 'action figure', 1)