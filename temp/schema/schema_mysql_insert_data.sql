use sservice;

insert into service_db(name, connect, comment, checked) values 
    ('ЕИС БД Калининского УСЗН',        'DRIVER={SQL Server};SERVER=172.153.153.104\\MINSOC_DB_SQL;DATABASE=NDA_CHEL_KALIL_201709;UID=sa;PWD=FREIDER5', 'Id=214', 1),
    ('ЕИС БД Курчатовского УСЗН',       'DRIVER={SQL Server};SERVER=172.153.153.104\\MINSOC_DB_SQL;DATABASE=NDA_CHEL_KURCH_201709;UID=sa;PWD=FREIDER5', 'Id=219', 1),
    ('ЕИС БД Ленинского УСЗН',          'DRIVER={SQL Server};SERVER=172.153.153.104\\MINSOC_DB_SQL;DATABASE=NDA_CHEL_LENIN_201709;UID=sa;PWD=FREIDER5', 'Id=195', 1),
    ('ЕИС БД Металлургического УСЗН',   'DRIVER={SQL Server};SERVER=172.153.153.104\\MINSOC_DB_SQL;DATABASE=NDA_CHEL_METALL_201709;UID=sa;PWD=FREIDER5', 'Id=200', 1),
    ('ЕИС БД Советского УСЗН',          'DRIVER={SQL Server};SERVER=172.153.153.104\\MINSOC_DB_SQL;DATABASE=chel_SOVET_20170922;UID=sa;PWD=FREIDER5', 'Id=160', 1),
    ('ЕИС БД Тракторозаводского УСЗН',  'DRIVER={SQL Server};SERVER=172.153.153.104\\MINSOC_DB_SQL;DATABASE=NDA_CHEL_TRACK_201709;UID=sa;PWD=FREIDER5', 'Id=191', 1),
    ('ЕИС БД Центрального УСЗН',        'DRIVER={SQL Server};SERVER=172.153.153.104\\MINSOC_DB_SQL;DATABASE=NDA_CENTR_201709_2;UID=sa;PWD=FREIDER5', 'Id=234', 1);

insert into service_type(name) values
    ('Возвращается строка из выборки (одна)'),
    ('Возвращаются строки из выборки (все)'),
    ('Возвращается ответ, если в первом поле выборки значение \>0, иначе далее'),
    ('Возвращается ответ, если в первом поле выборки значение \=0, иначе далее'),
    ('Возвращается ответ, если в первом поле выборки значение \=1, иначе далее'),
    ('Возвращается ответ, если записей в выборке \>0, иначе далее'),
    ('Возвращается ответ, если записей в выборке \=0, иначе далее'),
    ('Возвращается ответ, если записей в выборке \=1, иначе далее');

insert into service_service(name, comment, checked) values
    ('Проезд', 'Проезд в муниципальном общественном транспорте города Челябинска', 1),
    ('Учетные данные', 'Основные данные гражданина по СНИЛС', 1);

insert into service_query(name, s_service_id, script, priority, comment, s_type_id, result) values
    ('Основные данные гражданина по СНИЛС', 
    2, 
    'select FAMIL as "Фамилия", IMJA as "Имя", OTCH as "Отчество", DROG as "Дата рожд.", POL as "Пол" from F2 where nps = ?',
    1,
    'Выборка из таблицы F2',
    1,
    null);

insert into service_page(name, content, user_id) values
    ('О приложении (About)',
    '<div class="jumbotron">
      <h1>ПО "SService"</h1>

      <p>Предоставление единой точки входа для получения сервисов социальной направленности.</p>
      <p>Сервисы обрабатывают информацию, хранящуюся в отраслевых БД ...</p>
      <p><a class="btn btn-lg btn-primary" href="about" role="button">Подробнее &raquo;</a></p>
    </div>', 1),

    ('Главная (Home)', 
    '<div class="jumbotron">
      <h1>ПО "SService"</h1>
      
      <p>Предоставление единой точки входа для получения сервисов социальной направленности.</p>
      <p>Сервисы обрабатывают информацию, хранящуюся в отраслевых БД.</p>
      <p>Ниже представлены основные возможности программного обеспечения:</p>
      <p>
        <ul>
          <li>Планируемые к реализации сервисы</li>
            <ul>
              <li>подтверждение права граждан в льготном проезде в муниципальном общественном транспорте</li>
              <li>получение перечня признаков учета граждан, числящихся на учете в органах социальной защите</li>
            </ul>
            <li>Программное обеспечение предоставляет следующие интерфейсы</li>
            <ul>
              <li>Web</li>
              <li>API для автоматического взаимодействия со сторонними ИС</li>
            </ul>
            <li>Гибкая система добавления новых сервисов позволяет "покрыть" практически все потенциальные потребности в получении информации для web-пользователей и сторонних ИС</li>
          </ul>
      </p>
      <p><a class="btn btn-lg btn-primary" href="/" role="button">На Главную &raquo;</a></p>
    </div>', 1),

    ('Контакты (Contacts)',
    '<div class="jumbotron">
      <h1>Контакты</h1>
                    
      <p>Комитет социальной политики города Челябинска</p>
      <p>Отдел программного обеспечения предоставления и финансирования льгот и субсидий</p>
      <p>Контактное лицо: Тутаев Р. Х.</p>
      <p>Телефон: 8 (351) 729 82 23</p>
      <p>Email: usz@cheladmin.ru</p>
      <p>Сайт: http://socchel.ru</p>
      <p><a class="btn btn-lg btn-primary" href="/" role="button">На Главную &raquo;</a></p>
    </div>', 1);