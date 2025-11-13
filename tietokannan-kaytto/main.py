import sqlite3

# Time format YYYY-MM-DDTHH:MM-SS

# Variables.
months = {
    'Huhtikuu'  : 4,
    'Toukokuu'  : 5,
    'Kesäkuu'   : 6,
    'Heinäkuu'  : 7,
    'Elokuu'    : 8,
    'Syyskuu'   : 9,
    'Lokakuu'   : 10
}

weekdays = {
    'maanantai'     : 0,
    'tiistai'       : 1,
    'keskiviikko'   : 2,
    'torstai'       : 3,
    'perjantai'     : 4,
    'lauantai'      : 5,
    'sunnuntai'     : 6,
}

## Helpers.
get_rows    = lambda cursor: [column_value for column_value in cursor]  # Returns SQL query results as a list.
subtask     = lambda n: print('Osatehtävä', n)  # Prints a header for a subtask.

# Database connection.
c = sqlite3.Connection('bikes_2024.db')

# Functions.


# SUBTASK 1
def trips_from_station(station_name: str) -> int:
    query = f'''SELECT
                  COUNT(start_station_id)
                FROM
                  Stations, Trips
                WHERE
                  start_station_id = Stations.id AND Stations.name = \'{station_name}\''''
    return get_rows(c.execute(query))[0][0]

def trips_to_station(station_name: str) -> int:
    query = f'''SELECT
                  COUNT(end_station_id)
                FROM
                  Stations, Trips
                WHERE
                  end_station_id = Stations.id AND Stations.name = \'{station_name}\''''
    return get_rows(c.execute(query))[0][0]


# SUBTASK 2
def longest_distance_trips(limit: int) -> list:
    query = f'''SELECT
                  D.name, A.name, distance
                FROM
                  Stations as D, Stations as A, Trips
                WHERE
                  start_station_id = D.id AND end_station_id = A.id
                ORDER BY
                  distance DESC
                LIMIT
                  {limit}'''
    return get_rows(c.execute(query))

def longest_duration_trips(limit: int) -> list:
    query = f'''SELECT
                  D.name, A.name, duration
                FROM
                  Stations as D, Stations as A, Trips
                WHERE
                  start_station_id = D.id AND end_station_id = A.id
                ORDER BY
                  duration DESC
                LIMIT
                  {limit}'''
    return get_rows(c.execute(query))


# SUBTASK 3
def trips_during_month(month: int) -> int:
    month = '0'+str(month) if len(str(month)) == 1 else str(month)
    query = f'''SELECT
                  COUNT(start_time)
                FROM
                  Trips
                WHERE
                  strftime(\'%m\', start_time) = \'{month}\''''
    return get_rows(c.execute(query))[0][0]

def trips_during_weekday(day: int) -> int:
    day = day+1
    query = f'''SELECT
                  COUNT(start_time)
                FROM
                  Trips
                WHERE
                  strftime(\'%u\', start_time) = \'{day}\''''
    return get_rows(c.execute(query))[0][0]


# SUBTASK 4
def most_popular_start_stations(limit: int) -> list:
    query = f'''SELECT
                  name, COUNT(start_station_id)
                FROM
                  Stations, Trips
                WHERE
                  Stations.id = start_station_id
                GROUP BY
                  start_station_id
                ORDER BY
                  COUNT(start_station_id) DESC
                LIMIT
                 {limit}'''
    return get_rows(c.execute(query))

def least_popular_start_stations(limit: int) -> list:
    query = f'''SELECT
                  name, COUNT(start_station_id)
                FROM
                  Stations, Trips
                WHERE
                  Stations.id = start_station_id
                GROUP BY
                  start_station_id
                ORDER BY
                  COUNT(start_station_id)
                LIMIT
                 {limit}'''
    return get_rows(c.execute(query))


# SUBTASK 5
def largest_differences(limit: int) -> list:
    query = f'''WITH started AS (
    SELECT start_station_id AS station_id, COUNT(*) AS started_count
    FROM Trips
    GROUP BY start_station_id
),
ended AS (
    SELECT end_station_id AS station_id, COUNT(*) AS ended_count
    FROM Trips
    GROUP BY end_station_id
)
SELECT
    s.name AS "Asema",
    st.started_count AS "Alkaneet matkat",
    en.ended_count AS "Päättyneet matkat",
    ABS(st.started_count - en.ended_count) AS "Ero"
FROM Stations s
JOIN started st ON st.station_id = s.id
JOIN ended   en ON en.station_id = s.id
ORDER BY "Ero" DESC
LIMIT {limit};'''
    return get_rows(c.execute(query))


def main():
    subtask(1)
    print(f'Matkoja Intiankadulta: {trips_from_station('Intiankatu')}')
    print(f'Matkoja Intiankadulle: {trips_to_station('Intiankatu')}')

    print('')

    subtask(2)
    print('Viisi pisintä matkaa etäisyydellisesti (m):')
    for line in longest_distance_trips(5):
          print(line)
    print('Viisi pisintä matkaa ajallisesti (s):')
    for line in longest_duration_trips(5):
          print(line)

    print('')

    subtask(3)
    for month in months:
        print(f'Matkoja {month}ssa: {trips_during_month(months[month])}')
    for weekday in weekdays:
        print(f'Matkoja {weekday}na: {trips_during_weekday(weekdays[weekday])}')

    print('')

    subtask(4)
    print('Viisi suosituinta lähtöasemaa:')
    for line in most_popular_start_stations(5):
        print(line)
    print('Viisi vähiten suosittua lähtöasemaa:')
    for line in least_popular_start_stations(5):
        print(line)

    print('')

    subtask(5)
    print('Viisi suurinta eroa alkaneiden ja päättyneiden matkojen välillä:')
    for line in largest_differences(5):
        print(line)


if __name__ == '__main__':
    main()

