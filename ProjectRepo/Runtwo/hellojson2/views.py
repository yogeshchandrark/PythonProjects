from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
from django.http import HttpResponse
import json
##from commons.dbutils import exec_query
from django.views.decorators.csrf import ensure_csrf_cookie
from entities.models import Employee

#list
def index(request):
    data = []
    jsondata = json.dumps(data, ensure_ascii=False, indent=2)
    return render(request,
                  'hellojson2/index.html',
                  {'form_name': 'hellojson2', 'data': jsondata})

def getlist(request):
    sqltext="""SELECT
        a.id
      , a.empid
      , a.empname
      , a.deptid
      , a.mailaddress
      , b.deptname
    FROM
      public.entities_employee a
    INNER JOIN
      public.entities_department b
      on a.deptid=b.deptid
    ORDER BY
      a.id
        ;  """
    emplist=exec_query(sqltext);

    jsondata = json.dumps(emplist, ensure_ascii=False);

    return HttpResponse(jsondata)

@ensure_csrf_cookie
def senddata(request):
    txt = request.POST['query']
    datas = json.loads(txt)

    for element in datas:
#        print(element)
        entity = Employee.objects.filter(id=element['id']).first()
        entity.mailaddress = 'bbb@localhost.com'
        entity.save()

    data = {'status': 'OK'}

    json_str = json.dumps(data, ensure_ascii=False, indent=2)

    return HttpResponse(json_str)
