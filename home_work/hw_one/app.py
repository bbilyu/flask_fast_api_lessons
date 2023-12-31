from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/jackets/')
def jackets():
    _info = [{'img_name': 'one', 'title': 'North Face 3-in-1', 'text': 'Комфорт и функциональность объединены в этой универсальной куртке. Прочная и водонепроницаемая внешняя оболочка защитит вас от непогоды, а съемный внутренний слой с утеплителем обеспечит тепло в холодную погоду.', 'price': '200'},
             {'img_name': 'two', 'title': 'Patagonia Nano Puff', 'text': 'Легкая и компактная, эта куртка обладает отличной теплоизоляцией. Изготовлена из водоотталкивающего и ветрозащитного материала, что делает ее идеальным выбором для активного отдыха.', 'price': '150'},
             {'img_name': 'three', 'title': 'Columbia Titanium OutDry', 'text': 'Инновационная куртка с технологией OutDry, которая обеспечивает полную защиту от влаги и ветра. Она дышит и легко справляется с экстремальными условиями, что делает ее незаменимой для любителей приключений.', 'price': '250'},
             {'img_name': 'four', 'title': 'Arcteryx Atom LT', 'text': 'Эта куртка сочетает в себе легкость и прочность. Она обеспечит идеальную теплоизоляцию, а также отлично дышит, что позволит вам чувствовать себя комфортно в любых погодных условиях.', 'price': '300'},
             {'img_name': 'five', 'title': 'Canada Goose Expedition', 'text': 'Эта легендарная куртка предназначена для экстремальных условий. С утеплителем из пуха с долей пера она обеспечивает непревзойденную теплоизоляцию, а уникальная система вентиляции позволяет регулировать температуру внутри куртки.', 'price': '800'},
             {'img_name': 'six', 'title': 'Marmot PreCip Eco', 'text': 'Эта куртка изготовлена из экологически чистых материалов и предоставляет надежную защиту от воды. Она легкая, компактная и отлично подходит для путешествий и активного отдыха на природе.', 'price': '100'}, ]
    context = {'cards': _info, 'title': 'Магазин'}
    return render_template('jackets.html', **context)


@app.route('/t_shirts/')
def t_shirts():
    _info = [{'img_name': 'one', 'title': 'Nike Flex Running', 'text': 'Эти комфортные шорты предназначены для бега. Изготовлены из высококачественного материала, обладают хорошей влагоотводящей способностью и отличной вентиляцией.', 'price': '40'},
             {'img_name': 'two', 'title': 'Adidas 3-Stripes', 'text': 'Шорты с тремя полосками Adidas идеально подходят для тренировок и спортивных мероприятий. Они обеспечивают превосходную посадку и свободу движения.', 'price': '30'},
             {'img_name': 'three', 'title': 'Puma Active Training ', 'text': 'Эти стильные шорты от Puma идеально подходят для активных тренировок. Они обладают отличной вентиляцией и хорошо отводят влагу, что помогает оставаться сухими и комфортными во время упражнений.', 'price': '35'},
             {'img_name': 'four', 'title': 'Under Armour HeatGea', 'text': 'Шорты Under Armour HeatGear созданы для максимального комфорта и поддержки во время тренировок. Они обладают отличной вентиляцией и быстросохнущей технологией, а также имеют эластичный пояс для идеальной посадки.', 'price': '45'},
             {'img_name': 'five', 'title': 'Reebok CrossFit Games', 'text': 'Эти шорты являются официальной экипировкой CrossFit Games. Они обладают высокими техническими характеристиками, включая быстросохнущий материал, усиленные швы и эластичный пояс для комфорта и свободы движения.', 'price': '50'},
             {'img_name': 'six', 'title': 'Lululemon Surge', 'text': 'Шорты Lululemon Surge созданы для тренировок на открытом воздухе. Они обладают отличной вентиляцией и влагоотводящими свойствами, а также имеют специальные карманы для хранения необходимых вещей.', 'price': '55'}, ]
    context = {'cards': _info, 'title': 'Магазин'}
    return render_template('t_shirts.html', **context)


@app.route('/polos/')
def polos():
    _info = [{'img_name': 'one', 'title': 'Ralph Lauren Classic', 'text': 'Это классическое поло от Ralph Lauren, изготовленное из высококачественного хлопка. Оно имеет прямой крой для комфортной посадки и идеально подходит для повседневной носки.', 'price': '90'},
             {'img_name': 'two', 'title': 'Lacoste Slim', 'text': 'Это стильное поло от Lacoste с узким силуэтом, созданное для модных мужчин. Оно изготовлено из мягкого и прочного хлопка и имеет характерный логотип крокодила на груди.', 'price': '95'},
             {'img_name': 'three', 'title': 'Tommy Hilfiger Custom', 'text': 'Это настроенное под фигуру поло от Tommy Hilfiger, которое обеспечивает идеальную посадку. Оно изготовлено из высококачественного хлопка и отлично подходит для повседневного использования.', 'price': '80'},
             {'img_name': 'four', 'title': 'Hugo Boss Regular', 'text': 'Это поло Hugo Boss с обычной посадкой, идеальное для создания элегантного и стильного образа. Оно изготовлено из качественного хлопка и имеет дискретный логотип на груди.', 'price': '110'},
             {'img_name': 'five', 'title': 'Fred Perry Twin Tipped', 'text': 'Это знаменитое поло от Fred Perry с узнаваемым двухцветным орнаментом на воротнике и манжетах. Оно изготовлено из мягкого хлопка и имеет классическую посадку.', 'price': '120'},
             {'img_name': 'six', 'title': 'Calvin Klein Slim', 'text': 'Это поло Calvin Klein со средней посадкой, которое подчеркивает фигуру. Оно изготовлено из комфортного хлопка с добавлением эластана для дополнительной эластичности.', 'price': '85'}, ]
    context = {'cards': _info, 'title': 'Магазин'}
    return render_template('polos.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
