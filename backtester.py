import csv
# import matplotlib.pyplot as plt

REPORT_FILE_PATH = 'report.csv'
rows = []
NUMBER_OF_SIGNALS = 0
NUBMER_OF_CORRECT_SIGNALS = 0
NUBMER_OF_CORRECT_BUY_SIGNALS = 0
NUBMER_OF_CORRECT_SELL_SIGNALS = 0
NUBMER_OF_WRONG_BUY_SIGNALS = 0
NUBMER_OF_WRONG_SELL_SIGNALS = 0
SUM_CORRECT_BUY = 0
SUM_CORRECT_SELL = 0
SUM_WRONG_BUY = 0
SUM_WRONG_SELL = 0
NUBMER_OF_ACTUAL_BUY_SIGNALS = 0
NUBMER_OF_ACTUAL_SELL_SIGNALS = 0
with open(REPORT_FILE_PATH, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        rows.append(row)
    NUMBER_OF_SIGNALS = len(rows)
    # for row in rows:
    for i in range(len(rows)-1):
        if rows[i]['model signal'] == rows[i+1]['actual signal']:
            rows[i]['is correct'] = 1
            NUBMER_OF_CORRECT_SIGNALS += 1
            if rows[i]['model signal'] == 'Buy':
                # correct buy prediction
                NUBMER_OF_CORRECT_BUY_SIGNALS += 1
                SUM_CORRECT_BUY += float(rows[i]['price action'])
            else:
                # correct sell prediction
                NUBMER_OF_CORRECT_SELL_SIGNALS += 1
                SUM_CORRECT_SELL -= float(rows[i]['price action'])

        else:
            rows[i]['is correct'] = 0
            if rows[i]['model signal'] == 'Buy':
                # wrong buy prediction
                NUBMER_OF_WRONG_BUY_SIGNALS += 1
                SUM_WRONG_BUY += float(rows[i]['price action'])
            else:
                # wrong sell prediction
                NUBMER_OF_WRONG_SELL_SIGNALS += 1
                SUM_WRONG_SELL -= float(rows[i]['price action'])

NUBMER_OF_CORRECT_SIGNALS = NUBMER_OF_CORRECT_BUY_SIGNALS + NUBMER_OF_CORRECT_SELL_SIGNALS
WIN_RATE = NUBMER_OF_CORRECT_SIGNALS / NUMBER_OF_SIGNALS
NET_PROFIT = SUM_CORRECT_BUY + SUM_CORRECT_SELL + SUM_WRONG_BUY + SUM_WRONG_SELL
print('number of trades ', NUMBER_OF_SIGNALS)
print('net profit ', NET_PROFIT)
print('win rate ', WIN_RATE)
print('sum of correct buy ', SUM_CORRECT_BUY)
print('sum of correct sell ', SUM_CORRECT_SELL)
print('sum of wrong buy ', SUM_WRONG_BUY)
print('sum of wrong sell ', SUM_WRONG_SELL)
