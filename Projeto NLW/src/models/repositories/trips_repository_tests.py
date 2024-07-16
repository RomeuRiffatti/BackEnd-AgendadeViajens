import pytest
import uuid
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler
from datetime import datetime, timedelta

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason='interação com o bando de dados')
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_infos = {
        "id" : str(uuid.uuid4()),
        "destination" : "osasco",
        "start_date": datetime.strptime("02-01-2024", r"%d-%m-%Y" ),
        "end_date": datetime.strptime("02-01-2024", r"%d-%m-%Y" ) + timedelta(days=5),
        "owner_name": "Oswaldo",
        "owner_email": "oswaldo@email.com"
    }

    trips_repository.create_trip(trips_infos)

@pytest.mark.skip(reason='interação com o bando de dados')
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trip = trips_repository.find_trip_by_id(trip_id[1])
    print()
    print(trip)

@pytest.mark.skip(reason='interação com o bando de dados')
def test_update_trip_status():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    trips_repository.update_trip_status(trip_id)
    

