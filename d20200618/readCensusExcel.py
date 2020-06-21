# 스프레드시트에서 데이터 읽기
# 각 카운티의 총 인구와 인구조사 지역단위(census tract)의 수를 모두 계산
# 1. 엑셀 스프레드시트에서 데이터를 읽는다.
# 2. 각 카운티의 인구조사 지역 단위의 수를 계산한다.
# 3. 각 카운티의 총 인구수를 계산한다.
# 4. 결과 출력

# openpyxl 모듈로 엑셀 문서를 열고 각 셀을 읽는다.
# 모든 지역단위와 인구 데이터를 계산하고 이를 데이터 구조에 저장한다.
# pprint 모듈을 사용하여 데이터 구조를 .py 확장자를 가진 텍스트 파일에 저장한다.

import pprint

import openpyxl

print("Opening workbook...")
wb = openpyxl.load_workbook("censuspopdata.xlsx")
sheet = wb.get_sheet_by_name("Population by Census Tract")
countyData = {}

# fill in countyData with each county's population and tracts.
print("Reading rows...")
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet["B" + str(row)].value
    county = sheet["C" + str(row)].value
    pop = sheet["D" + str(row)].value

    # Make sure the key for this state exists.
    countyData.setdefault(state, {})
    # Make sure the key for this county in this state exists.
    countyData[state].setdefault(county, {"tracts": 0, "pop": 0})

    # Each row represents one census tract, so increment by one.
    countyData[state][county]["tracts"] += 1
    # increse the county pop by the pop in this census tract.
    countyData[state][county]["pop"] += int(pop)

# Open a new text file and write the contents of countyData to it.
print("Writing results...")
resultFile = open("census2010.py", "w")
resultFile.write("allData= " + pprint.pformat(countyData))
resultFile.close()
print("Done.")
