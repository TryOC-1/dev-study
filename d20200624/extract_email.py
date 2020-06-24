import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

json_file_name = "quickstart-1592876881384-420e674be176.json"
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)

spreadsheet_url = (
    "https://docs.google.com/spreadsheets/d/"
    "1FGmmcoIzava9G379ngKUX6YqvW-hQ9oAT7GwRp5cGHM/edit?usp=sharing"
)

doc = gc.open_by_url(spreadsheet_url)

worksheet = doc.worksheet("sheet")

column_data = worksheet.col_values(3)

with open("email.txt", "w") as f:
    f.write(str(column_data))
