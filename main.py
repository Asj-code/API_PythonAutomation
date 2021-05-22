import requests
import unittest


class ApiTest(unittest.TestCase):
    def test_email_verification(self):
        req = requests.get("https://jsonplaceholder.typicode.com/comments?postId=2")
        result = req.json()
        self.assertEqual("Presley.Mueller@myrl.com", result[0]["email"])

    def test_id_verification(self):
        req = requests.get("https://jsonplaceholder.typicode.com/comments?postId=2")
        result = req.json()
        self.assertEqual(6, result[0]["id"])

    def test_complete_update(self):
        req = requests.put("https://jsonplaceholder.typicode.com/posts/1", {"id": 1, "title": "Mi nuevo titulo", "body": "lorem lorem", "userId": 4})
        print(req.status_code)
        self.assertEqual(req.status_code, 200)

    def test_partial_update(self):
        req = requests.put("https://jsonplaceholder.typicode.com/posts/1", {"id": 1, "title": "Mi nuevo titulo", "body": "lorem lorem", "userId": 4})
        print(req.status_code)
        self.assertEqual(req.status_code, 200)

    def test_delete(self):
        req = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
        print(req.status_code)
        self.assertEqual(req.status_code, 200)


if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()




