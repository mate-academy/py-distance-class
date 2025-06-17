# Distance class

class TestDistance(unittest.TestCase):
    def test_addition(self):
        d1 = Distance(10)
        d2 = Distance(5)
        self.assertEqual((d1 + d2).km, 15)
        self.assertEqual((d1 + 5).km, 15)

    def test_comparison(self):
        d = Distance(20)
        self.assertTrue(d < 25)
        self.assertTrue(d >= 20)