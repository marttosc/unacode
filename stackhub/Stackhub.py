from stackhub.Database import Database
from stackhub.Environment import Environment
from stackhub.Static import Trend


class Stackhub:
    def __init__(self):
        self.environ = Environment()

        _db = Database(self.env('MONGO_URI'), self.env('MONGO_DATABASE')).get()

        self._db = _db

    @property
    def db(self):
        return self._db

    def env(self, key, default=None):
        return self.environ.get_env(key, default)

    def github_trends(self):
        """
        Return and save the Github Trends data into MongoDB.
        """
        trends = Trend().load()

        if len(trends) > 0:
            # Truncate the github_trends collection.
            self.db.get_collection('github_trends').delete_many({})

            self.db.get_collection('github_trends').insert_many(trends)

        return trends
