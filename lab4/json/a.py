import json

data = json.load(open('sample-data.json', 'r', encoding='utf-8'))
arr = data['imdata']
#print(arr[0]['l1PhysIf']['attributes']['dn'])
print('Interface Status')
print('='*80)
print(f"{'DN':<50} {'Description':<20}  {'Speed':<7}  {'MTU':<6}")
print(f"{'-'*50} {'-'*20}  {'-'*6}  {'-'*6}")
# Print header
for i in arr:
    print(f"{i['l1PhysIf']['attributes']['dn']:<50} {i['l1PhysIf']['attributes']['descr']:<20}  {i['l1PhysIf']['attributes']['speed']:<6}  {i['l1PhysIf']['attributes']['mtu']:<6}")

#By Bekzhan

















