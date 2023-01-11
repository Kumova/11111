import csv

from django.core.management.base import BaseCommand
#from phones.models import Phone



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            for row in phones:
                phone=phone()
                self.stdout.write(
                    'Created phone {} {} {} {} {} {}'.format(phone.name,  phone.price,
                                                    phone.image, phone.release_date, phone.lte_exists,  phone.slug )
                )
  #
  #              Phone.objects.create(id=row[0], name=row[1], price=row[2], image=row[3],
 #                                    release_date=row[4], lte_exists=row[5], slug=row[6])
                phone.save










 #           try:
  #                  phone = Phone.request.GET.get(id=id)
 #               except Phone.DoesNotExist:
  #                  raise CommandError('Phone "%s" does not exist' % id)

  #          for row in phones:
  #              emp = Employee()
                # etc...
 #               self.stdout.write(
  #                  'Created employee {} {}'.format(emp.first_name, emp.last_name)
  #              )
 #               phone.opened = False
  #              phone.save()
 #           for phone in options['phone_name']:
#                self.stdout.write(self.style.SUCCESS('Successfully closed phone "%s"' % id))
#                phones=Phone.objects.all()
 #               phone=[f'{phone.name}:{phone.price}:{phone.image}' for phone in phones]
 #               return HttpResponse('<br>'.join(phone))
#            phones.save()

 #       print(Phone)


            # TODO: Добавьте сохранение модели
  #          pass
