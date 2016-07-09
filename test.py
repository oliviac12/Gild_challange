from name_parse import NameParse
import pandas as pd

test = pd.read_csv('test_data.csv')
test['Result'] = [s.lower() for s in test['Result']]
yes = 0
no = 0
for index, row in test.iterrows():
    first = NameParse(row['Test']).parsed_name[0]
    last = NameParse(row['Test']).parsed_name[1]
    r_first = row['Result'].split(',')[0]
    r_last = row['Result'].split(',')[1]
    if (first == r_first) & (last == r_last.strip()) :
        yes += 1
    else:
        no += 1

print yes
print no
