# lib/models/network.py
from models.__init__ import CURSOR, CONN

class Network:
    all = {}

    def __init__(self, name, location, id="None"):
        self.id = id
        self.name = name
        self.location = location
       


    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS networks (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Network instances """
        sql = """
            DROP TABLE IF EXISTS networks;
        """
        CURSOR.execute(sql)
        CONN.commit()   

    def save(self):
        """ Insert a new row with the name, location values of the current Networks object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO networks (name, location)
                VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, location):
        """ Initialize a new Network instance and save the object to the database """
        network = cls(name, location)
        network.save()
        return network
    
    @classmethod
    def get_all(cls):
        """Return a list containing one Network object per table row"""
        sql = """
            SELECT *
            FROM networks
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a Network object having the attribute values from the table row."""

        network = cls.all.get(row[0])
        if network:
            network.name = row[1]
            network.location = row[2]
        else:
            network = cls(row[1], row[2])
            network.id = row[0]
            cls.all[network.id] = network
        return network
    
    @classmethod
    def find_by_id(cls, id):
        """Return a Network object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM networks
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Return a Network object corresponding to the table row matching the specified name"""
        sql = """
            SELECT *
            FROM networks
            WHERE name = ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
   
    def delete_network(self):
        """Delete the table row corresponding to the current Network instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM networks
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        # Set the id to None
        self.id = None
    
    def shows(self):
        from models.show import Show
        sql = """
        SELECT * FROM shows
        WHERE network_id = ?
    """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()  # Fetch all rows from the query
        return [Show.instance_from_db(row) for row in rows]

        # add instance method called Shows to call this given networks shows