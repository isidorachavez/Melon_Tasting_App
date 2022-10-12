"""Model for Melon Tasting app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def connect_to_db(flask_app, db_uri="postgresql:///melon_tasting_app", echo=False, pool_size = 10, max_overflow = -1 ): #name of the db is melon_tasting_app, added pool_size and max_overflow becuase of timeout error
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!!! Yay!")


#User Class
class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f"<User user_id={self.user_id} username={self.username} email={self.email}>"


#Melon Class
class Melon(db.Model):

    __tablename__ = "melons"

    melon_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    melon_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Melon melon_id={self.melon_id} melon_name={self.melon_name}>"

#Appointments Class
class Timeslot(db.Model):

    __tablename__ = "timeslots"

    timeslot_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    melon_id = db.Column(db.Integer, db.ForeignKey("melons.melon_id"))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    #Relationship melons
    melon = db.relationship("Melon", backref="melon")

    def __repr__(self):
        return f"<Timeslot timeslot_id={self.timeslot_id} melon_id={self.melon_id}>"



#Bookings Class
class Booking(db.model):

    __tablename__ = "bookings"

    booking_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    appointment_id = db.Column(db.Integer, db.ForeignKey("appointments.appointment_id"))
    booked_on = db.Column(db.DateTime, default=db.func.now())




if __name__ == "__main__":
    from server import app

    connect_to_db(app)

