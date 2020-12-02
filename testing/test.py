# from unittest import TestCase
# from server import app
# import flask

# class FlaskTests(TestCase):

#   def setUp(self):
#       """Stuff to do before every test."""

#       self.client = app.test_client()
#       app.config['TESTING'] = True

#   def tearDown(self):
#       """Stuff to do after each test."""

# # Testing routes
#   def test_about_route(self):
#       """it is a non-database test..."""

#       result = self.client.get("/about")
#       self.assertEqual(result.status_code, 200)
#       self.assertIn('<h1>Test</h1>', result.data)

#   def test_about_route(self):
#       """it is a non-database test..."""

#       result = self.client.get("/cuisine_list")
#       self.assertEqual(result.status_code, 200)
#       self.assertIn('<h1>Test</h1>', result.data)

#   def test_about_route(self):
#       """it is a non-database test..."""

#       result = self.client.get("/")
#       self.assertEqual(result.status_code, 200)
#       self.assertIn('<h1>Test</h1>', result.data)

#   def test_about_route(self):
#       """it is a non-database test..."""

#       result = self.client.get("/login")
#       self.assertEqual(result.status_code, 200)
#       self.assertIn('<h1>Test</h1>', result.data)

#   def test_about_route(self):
#       """it is a non-database test..."""

#       result = self.client.get("/sign_up")
#       self.assertEqual(result.status_code, 200)
#       self.assertIn('<h1>Test</h1>', result.data)

#   def test_about_route(self):
#       """it is a non-database test..."""

#       result = self.client.get("/sign_up/register")
#       self.assertEqual(result.status_code, 200)
#       self.assertIn('<h1>Test</h1>', result.data)

#   def test_about_route(self):
#       """it is a non-database test..."""

#       result = self.client.get("/dish_details")
#       self.assertEqual(result.status_code, 200)
#       self.assertIn('<h1>Test</h1>', result.data)

#   def test_about_route(self):
#       """it is a non-database test..."""

#       result = self.client.get("/about_project")
#       self.assertEqual(result.status_code, 200)
#       self.assertIn('<h1>Test</h1>', result.data)

#   def test_about_route(self):
#       """it is a non-database test..."""

#       result = self.client.get("/contact_us")
#       self.assertEqual(result.status_code, 200)
#       self.assertIn('<h1>Test</h1>', result.data)

#   def test2(self):
#       """Some other test"""