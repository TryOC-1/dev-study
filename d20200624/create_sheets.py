import ezsheets

ss = ezsheets.Spreadsheet("1aYxrHYYRUlQdFr7YP2Um9dpBgEYhcK5VbEDYPyRUDC4")

sh = ss.sheets[0]
cnt = sh.columnCount
row_sh = sh.getRows()
row_list = []

if cnt > 2:
    for i in range(cnt, 2, -1):
        sh.updateColumn(i + 1, sh.getColumn(i))

for i, row in enumerate(row_sh):
    num1 = row[0]
    num2 = row[1]

    if i == 0:
        row_list.append("Total")
        continue

    if num1.isdigit() and num2.isdigit():
        row_list.append(int(num1) + int(num2))
    else:
        row_list.append("")

sh.updateColumn(3, row_list)
