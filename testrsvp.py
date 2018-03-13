import rsvp
import mongomock
import unittest
import json

class BaseTest:
    def setup_method(self):
        print ("Running testcases")
        rsvp.client = mongomock.MongoClient()
        rsvp.db = rsvp.client.mock_db_function
        self.client = rsvp.app.test_client()
        

    def test_dict(self):
        print ("Checking variables")
        doc = rsvp.RSVP("test name", "test@example.com", "1")
        with rsvp.app.test_request_context():
            assert doc.dict() == {
                "_id": "1",
                "name": "test name",
                "mail": "test@example.com",
                "links": {
                    "self": "http://localhost/api/rsvps/1"
                }
            }

def main():
  obj=BaseTest()
  obj.setup_method()
  obj.test_dict()

if __name__ == "__main__":
  main()
