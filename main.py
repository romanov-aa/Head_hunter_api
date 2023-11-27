import pandas as pd
import requests

table = pd.DataFrame(columns=['id','name','salary_from','salary_to','salary_currency','salary_gross','area','adress_city', 'adress_street', 'adress_building','type','schedule','employer_id','employer_name', 'snippet_requirement','snippet_responsibility','text','date'])
table

url = 'https://api.hh.ru/vacancies'
#параметры, которые будут добавлены к запросу
zapros = ("Программист", "Менеджер", "Оператор", "Курьер", "Кассир", "Администратор", "Продавец", "Водитель", "Аналитик", "Строитель", "Сварщик", "Инженер", "Директор", "Бухгалтер", "Секретарь", "Дизайнер", "Электрик", "Повар", 
          "Экономист", "Юрист", "Руководитель", "Официант", "Супервайзер", "Мерчендайзер", "Кладовщик", "Грузчик", "Уборщик", "Охранник", "Системный администратор", "Агент")

for y in range(len(zapros)):
  for i in range(200):
    par = {'text': zapros[y], 'area':'113',"vacancy_search_order": {"id": "publication_time", "name": "по дате"},'per_page':'10', 'page':i}
    r = requests.get(url, params=par)
    e=r.json()
    for vacancy in e['items']:
      id=vacancy['id']
      name=vacancy['name']
      try:
        salary_from=vacancy['salary']['from']
      except:
        salary_from=''
      try:
        salary_to=vacancy['salary']['to']
      except:
        salary_to=''
      try:
        salary_cur=vacancy['salary']['currency']
      except:
        salary_cur=''
      try:
        salary_gross=vacancy['salary']['gross']
      except:
        salary_gross=''
      try:
        area=vacancy['area']['id']
      except:
        area=''
      try:
        adress_city=vacancy['address']['city']
      except:
        adress_city=''
      try:
        adress_street=vacancy['address']['street']
      except:
        adress_street=''
      try:
        adress_building=vacancy['address']['building']
      except:
        adress_building=''
        #----
      #try:
      #  metro=vacancy['address']['metro']
      #except:
      #  metro=''
      try:
        type123=vacancy['type']['name']
      except:
        type123=''
      try:
        schedule=vacancy['schedule']['name']
      except:
        schedule=''
      try:
        employer_id = vacancy['employer']['id']
      except:
        employer_id = ''
      try:
        employer_name = vacancy['employer']['name']
      except:
        employer_name = ''
      try:
        snippet_requirement = vacancy['snippet']['requirement']
      except:
        snippet_requirement = ''
      try:
        snippet_responsibility = vacancy['snippet']['responsibility']
      except:
        snippet_responsibility = ''
      now_zapros = zapros[y]
      try:
        date1 = vacancy['published_at']
        date1 = date1[:10]
      except:
        date1 = ''

      table.loc[len(table)]=[id,name,salary_from,salary_to,salary_cur,salary_gross,area,adress_city,adress_street,adress_building,type123,schedule,employer_id,employer_name,snippet_requirement,snippet_responsibility,now_zapros,date1]

table.to_excel('hh_collection.xlsx', index=False)