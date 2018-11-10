from faker import Faker
import json
import random

f = Faker('ru_RU')

pp = []
for i in range(10):
    persona = {}
    persona['name'] = f.name()
    persona['email'] = f.email()
    pp.append(persona)

cc = []
for i in range(10):
    company = {}
    company['name company'] = f.company()
    cc.append(company)

r = random.randint(1, 100)
s = random.randint(1, 10000)/100
d = random.choice(pp)
g = random.choice(cc)

print(json.dumps(d))
print(json.dumps(g))
print(json.dumps(r))
print(json.dumps(s))
f = open('persona.json', 'w', encoding='utf8')
f.write(json.dumps(d) + '\n' + json.dumps(g) + '\n' + json.dumps(r) + '\n' + json.dumps(s))
f.close()
