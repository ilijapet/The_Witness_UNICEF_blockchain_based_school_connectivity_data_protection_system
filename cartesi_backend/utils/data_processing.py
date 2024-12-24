import datetime
import hashlib
import json
import os
from contextlib import contextmanager

from dotenv import load_dotenv
from sqlalchemy import Column, DateTime, Integer, String, create_engine, Float
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import func


print(f"Database file path: {os.path.abspath('utils/witness.db')}")

load_dotenv()

Base = declarative_base()

class SchoolNetworkData(Base):
    __tablename__ = "school_network_data"
    id = Column(Integer, primary_key=True, autoincrement=True)
    school_id = Column(String(100))
    timestamp = Column(DateTime, default=func.now())
    download_speed = Column(Float)
    upload_speed = Column(Float)
    latency = Column(Float)


engine = create_engine("sqlite:///utils/witness.db")
Base.metadata.create_all(engine)


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


class Helpers:
    @staticmethod
    def get_env_var(index):
        private_key = os.environ.get(f"PRIVATE_KEY_{index}").encode()
        public_key = os.environ.get(f"PUBLIC_KEY_{index}").encode()
        return private_key, public_key

    @staticmethod
    def hash_public_key(public_key):
        hash_obj = hashlib.sha256()

        hash_obj.update(public_key)

        hash_hex = hash_obj.hexdigest()

        return hash_hex

    @staticmethod
    def row2dict(row):
        row_dict = {column.name: getattr(row, column.name) for column in row.__table__.columns}
        return json.dumps(row_dict, cls=DateTimeEncoder)


class DatabaseSessionManager:
    def __init__(self, engine):
        self.engine = engine
        self.Session = sessionmaker(bind=self.engine)

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.Session()
        try:
            yield session
        except SQLAlchemyError as e:
            session.rollback()
            print(f"An error occurred: {e}")
            raise
        else:
            session.commit()
        finally:
            session.close()


class Database(DatabaseSessionManager, Helpers):
    def __init__(self, engine):
        super().__init__(engine)
        self.create_table()

    def create_table(self):
        try:
            Base.metadata.create_all(self.engine)  
        except SQLAlchemyError as e:
            print(f"An error occurred while creating tables: {e}")

    def insert_data(self, data):
        with self.session_scope() as session:
            new_school = SchoolNetworkData(
                school_id=data.get("school_id", 1),
                download_speed=data.get("download_speed", 0.0),
                upload_speed=data.get("upload_speed", 0.0),
                latency=data.get("latency", 0.0),
                timestamp=func.now(),
            )
            session.add(new_school)

    def get_data(self, school_id):
        with self.session_scope() as session:
            result = session.query(SchoolNetworkData).filter_by(id=school_id).first()
            if result:
                return Database.row2dict(result)
            else:
                return None

    def update_data(self, data):
        with self.session_scope() as session:
            school = session.query(SchoolNetworkData).filter_by(school_id=data["school_id"]).first()
            if school:
                print(f"Found school: {school}")
                for key, value in data.items():
                    if key == 'timestamp' and isinstance(value, str):
                        value = datetime.datetime.fromisoformat(value)
                    print(f"Updating {key} to {value}")
                    setattr(
                        school, key, value
                    )  
                session.commit()
                print("database updated!")
                updated_school = session.query(SchoolNetworkData).filter_by(school_id=data["school_id"]).first()
                print(f"Verified updated school data within session: {Database.row2dict(updated_school)}")
                self.verify_update(data["school_id"])
            else:
                print(f"No school found with this id: {data['school_id']}")

    def verify_update(self, school_id):
        with self.session_scope() as session:
            updated_school = session.query(SchoolNetworkData).filter_by(school_id=school_id).first()
            if updated_school:
                print(f"Verified updated school data: {Database.row2dict(updated_school)}")
            else:
                print(f"No school found with this id: {school_id}")


    def delete_data(self, school_id):
        with self.session_scope() as session:
            school = session.query(SchoolNetworkData).filter_by(id=school_id).first()
            if school:
                session.delete(school)
            else:
                print(f"No car found with public_key: {school_id}")


# if __name__ == "__main__":
#     database = Database(engine)
#     database.create_table()
#     data = {
#         "school_id": 1,
#         "download_speed": False,
#         "upload_speed": False,
#         "latency": False,
#         "timestamp": func.now(),
#     }
#     database.insert_data(data)
#     print(database.get_data(1))
