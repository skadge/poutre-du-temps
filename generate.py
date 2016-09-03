import datetime

jour = datetime.date.today()
jour2 = datetime.date.today()
un_jour = datetime.timedelta(days=1)

# demarre demain
jour += un_jour
jour2 += un_jour

annee_prochaine = jour + datetime.timedelta(days=365)

weekdays = {0:'m',
            1:'t',
            2:'w',
            3:'t',
            4:'f',
            5:'s',
            6:'s'}

page_idx = 1

with open("template.svg",'r') as tpl:
    lines = tpl.readlines()

while jour < annee_prochaine:

    with open("page%s.svg" % page_idx, "w") as page:
            for l in lines:
                up = l.replace("99 </tspan>f", "%s </tspan>%s" % (jour.day, weekdays[jour.weekday()]))
                if up != l:
                    jour += un_jour
                    print(jour)

                up_weekend = up.replace("123456", "000000" if jour2.weekday() in [5,6] else "ffffff")
                if up_weekend != up:
                    jour2 += un_jour
                    up = up_weekend

                page.write(up)

    page_idx += 1
    if page_idx > 10:
        print("Erreur! Aborting")
        break
