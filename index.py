from os import environ as env
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from datetime import date

# hydrating environment variables
load_dotenv()

engine = create_engine(
    'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        env['DB_USERNAME'],
        env['DB_PASSWORD'],
        env['DB_HOST'],
        env['DB_PORT'],
        env['DB_NAME']
    )
)

def is_it_a_holiday_today():
    """Prints if today is a holiday."""

    print('Executing is_it_a_holiday_today...')

    with engine.connect() as con:
        rs = con.execute(
            text('SELECT "id", "date", "name" FROM "Holiday" WHERE "date" = :date'), 
            {'date': date.today()}
        )
        
        count = rs.rowcount

        if (count == 0):
            print('It is not a holiday today')
        else:
            for row in rs:
                print('It is a holiday today, Id: {0}, Date: {1}, Name: {2}'.format(row.id, row.date, row.name))

def remaining_holidays_this_year():
    """Prints remaining holidays for current year (including today)."""
    
    print('Executing remaining_holidays_this_year...')
    
    start_date = date.today()
    end_date = date(start_date.year, 12, 31) 
    
    with engine.connect() as con:
        rs = con.execute(
            text('SELECT "id", "date", "name" FROM "Holiday" WHERE "date" >= :start_date AND "date" <= :end_date'), 
            {'start_date': start_date, 'end_date': end_date}
        )

        print('{0} holidays remaining for this year (including today)'.format(rs.rowcount))
        
        for row in rs:
            print('Id: {0}, Date: {1}, Name: {2}'.format(row.id, row.date, row.name))


is_it_a_holiday_today()
remaining_holidays_this_year()