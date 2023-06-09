# Generated by Django 4.2.2 on 2023-06-08 17:13

from django.db import migrations


def fill_data(apps, schema_editor):
    schedule_data = [
        {'date': '2023-06-05',
          'items': [
              {'title': 'Разговоры о важном', 'period': [(9, 0), (9, 45)]},
              {'title': 'Математика', 'period': [(9, 45), (10, 30)]},
              {'title': 'Английский язык', 'period': [(11, 0), (11, 45)]},
              {'title': 'Спорт', 'period': [(11, 0), (11, 45)]},
              {'title': 'История', 'period': [(11, 45), (12, 30)]},
              {'title': 'Физика', 'period': [(13, 55), (14, 40)]},
              {'title': 'Биология', 'period': [(14, 50), (15, 35)]},
              {'title': 'Литература', 'period': [(15, 35), (16, 20)]},
              {'title': 'Актерское мастерство', 'period': [(16, 40), (17, 25)]},
              {'title': 'Немецкий язык', 'period': [(17, 35), (18, 20)]}
          ]
        },
        {'date': '2023-06-06',
          'items': [
              {'title': 'Английский язык', 'period': [(9, 0), (9, 45)]},
              {'title': 'Английский язык', 'period': [(9, 45), (10, 30)]},
              {'title': 'Русский язык', 'period': [(11, 0), (11, 45)]},
              {'title': 'Русский язык', 'period': [(11, 45), (12, 30)]},
              {'title': 'Математика', 'period': [(13, 10), (13, 55)]},
              {'title': 'Йога', 'period': [(13, 55), (14, 40)]},
              {'title': 'Математика', 'period': [(14, 50), (15, 35)]},
              {'title': 'Математика', 'period': [(15, 35), (16, 20)]},
              {'title': 'Человек мира', 'period': [(16, 40), (17, 25)]},
              {'title': 'Человек мира', 'period': [(17, 35), (18, 20)]}
          ]
        },
        {'date': '2023-06-07',
          'items': [
              {'title': 'DATA', 'period': [(9, 0), (9, 45)]},
              {'title': 'Путь к успеху', 'period': [(9, 45), (10, 30)]},
              {'title': 'Английский язык', 'period': [(11, 0), (11, 45)]},
              {'title': 'Английский язык', 'period': [(11, 45), (12, 30)]},
              {'title': 'Коуч', 'period': [(13, 10), (13, 55)]},
              {'title': 'Физика', 'period': [(13, 55), (14, 40)]},
              {'title': 'История', 'period': [(14, 50), (15, 35)]},
              {'title': 'Математика', 'period': [(15, 35), (16, 20)]},
              {'title': 'Танцы', 'period': [(16, 40), (17, 25)]},
              {'title': 'Актёрское мастерство', 'period': [(17, 35), (18, 20)]}
          ]
        },
        {'date': '2023-06-08',
          'items': [
              {'title': 'DATA', 'period': [(9, 0), (9, 45)]},
              {'title': 'Путь к успеху', 'period': [(9, 45), (10, 30)]},
              {'title': 'Русский язык', 'period': [(11, 0), (11, 45)]},
              {'title': 'Русский язык', 'period': [(11, 45), (12, 30)]},
              {'title': 'Математика', 'period': [(13, 10), (13, 55)]},
              {'title': 'Математика', 'period': [(13, 55), (14, 40)]},
              {'title': 'Биология', 'period': [(14, 50), (15, 35)]},
              {'title': 'География', 'period': [(15, 35), (16, 20)]},
              {'title': 'Человек мира', 'period': [(16, 40), (17, 25)]},
              {'title': 'VIP Театр', 'period': [(17, 35), (18, 20)]}
          ]
        },
        {'date': '2023-06-09',
          'items': [
              {'title': 'Русский язык', 'period': [(9, 0), (9, 45)]},
              {'title': 'Общество знание', 'period': [(9, 45), (10, 30)]},
              {'title': 'Английский язык', 'period': [(11, 0), (11, 45)]},
              {'title': 'Английский язык', 'period': [(11, 45), (12, 30)]},
              {'title': 'Математика', 'period': [(13, 10), (13, 55)]},
              {'title': 'Математика', 'period': [(13, 55), (14, 40)]},
              {'title': 'Биология', 'period': [(14, 50), (15, 35)]},
              {'title': 'Литература', 'period': [(15, 35), (16, 20)]},
              {'title': 'Футбол', 'period': [(16, 40), (17, 25)]}
          ]
        }
    ]
    import datetime
    Event = apps.get_model("core", "Event")
    EventTemplate = apps.get_model("core", "EventTemplate")
    template = EventTemplate.objects.all().order_by('id')[0]
    for sch in schedule_data:
        date = sch['date']
        year, month, day = sch['date'].split('-')
        for i in sch['items']:
            date = datetime.date(year, month, day)
            date_start = datetime.datetime(int(year), int(month), int(day), i['period'][0][0], i['period'][0][1])
            date_end = datetime.datetime(int(year), int(month), int(day), i['period'][1][0], i['period'][1][1])
            ev = Event(template=template, title=i['title'], description='7-й класс', date=date, start_date=date_start, end_date=date_end)
            ev.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_eventtemplate_event_title_alter_event_template'),
    ]

    operations = [
        migrations.RunPython(fill_data)
    ]