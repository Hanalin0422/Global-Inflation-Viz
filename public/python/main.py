import crowling
import json

# 정보 리스트
# list = crowling.latest_global_cpi_list

list = [{'country': 'Austria', 'lat': '47.516231', 'lng': '14.550072', 'cpi': 11.047}, {'country': 'Belgium', 'lat': '50.503887', 'lng': '4.469936', 'cpi': 10.629}, {'country': 'Brazil', 'lat': '-14.235004', 'lng': '-51.92528', 'cpi': 6.47}, {'country': 'Canada', 'lat': '56.130366', 'lng': '-106.346771', 'cpi': 6.88}, {'country': 'Switzerland', 'lat': '46.818188', 'lng': '8.227512', 'cpi': 2.96}, {'country': 'Chile', 'lat': '-35.675147', 'lng': '-71.542969', 'cpi': 13.338}, {'country': 'China', 'lat': '35.86166', 'lng': '104.195397', 'cpi': 2.172}, {'country': 'Czech Republic', 'lat': '49.817492', 'lng': '15.472962', 'cpi': 15.093}, {'country': 'Germany', 'lat': '51.165691', 'lng': '10.451526', 'cpi': 10.388}, {'country': 'Denmark', 'lat': '56.26392', 'lng': '9.501785', 'cpi': 10.112}, {'country': 'Estonia', 'lat': '58.595272', 'lng': '25.013607', 'cpi': 21.314}, {'country': 'Spain', 'lat': '40.463667', 'lng': '-3.74922', 'cpi': 7.265}, {'country': 'Finland', 'lat': '61.92411', 'lng': '25.748151', 'cpi': 8.311}, {'country': 'France', 'lat': '46.227638', 'lng': '2.213749', 'cpi': 6.2}, {'country': 'Greece', 'lat': '39.074208', 'lng': '21.824312', 'cpi': 9.065}, {'country': 'Hungary', 'lat': '47.162494', 'lng': '19.503304', 'cpi': 22.492}, {'country': 'Indonesia', 'lat': '-0.789275', 'lng': '113.921327', 'cpi': 5.418}, {'country': 'Ireland', 'lat': '53.41291', 'lng': '-8.24389', 'cpi': 9.16}, {'country': 'Israel', 'lat': '31.046051', 'lng': '34.851612', 'cpi': 5.078}, {'country': 'India', 'lat': '20.593684', 'lng': '78.96288', 'cpi': 6.085}, {'country': 'Iceland', 'lat': '64.963051', 'lng': '-19.020835', 'cpi': 9.333}, {'country': 'Italy', 'lat': '41.87194', 'lng': '12.56738', 'cpi': 11.837}, {'country': 'Japan', 'lat': '36.204824', 'lng': '138.252924', 'cpi': 3.804}, {'country': 'South Korea', 'lat': '35.907757', 'lng': '127.766922', 'cpi': 5.035}, {'country': 'Luxembourg', 'lat': '49.815273', 'lng': '6.129583', 'cpi': 5.936}, {'country': 'Mexico', 'lat': '23.634501', 'lng': '-102.552784', 'cpi': 8.407}, {'country': 'Norway', 'lat': '60.472024', 'lng': '8.468946', 'cpi': 7.509}, {'country': 'Poland', 'lat': '51.919438', 'lng': '19.145136', 'cpi': 18.036}, {'country': 'Portugal', 'lat': '39.399872', 'lng': '-8.224454', 'cpi': 10.139}, {'country': 'Russia', 'lat': '61.52401', 'lng': '105.318756', 'cpi': 16.698}, {'country': 'Sweden', 'lat': '60.128161', 'lng': '18.643501', 'cpi': 10.853}, {'country': 'Slovenia', 'lat': '46.151241', 'lng': '14.995463', 'cpi': 10.027}, {'country': 'Slovakia', 'lat': '48.669026', 'lng': '19.699024', 'cpi': 14.892}, {'country': 'Turkey', 'lat': '38.963745', 'lng': '35.243322', 'cpi': 84.389}, {'country': 'United States', 'lat': '37.09024', 'lng': '-95.712891', 'cpi': 7.745}, {'country': 'South Africa', 'lat': '-30.559482', 'lng': '22.937506', 'cpi': 7.778}]

for entity in list:
    if entity['cpi'] < 5:
        entity['color'] = 'blue'
    elif 5 <= entity['cpi'] < 10:
        entity['color'] = 'green'
    elif 10 <= entity['cpi'] < 15:
        entity['color'] = 'yellow'
    elif 15 <= entity['cpi'] < 20:
        entity['color'] = 'darkorange'
    else:
        entity['color'] = 'red'



print(list)
