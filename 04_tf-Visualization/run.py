import funktions as f

data = f.dataImport('Shakespeare')
c = 0.1

terms = f.makeObj(data[0], data[1], c)

# f.exportCSV(terms)

# f.plot(terms)
f.plotZipf(terms, c)