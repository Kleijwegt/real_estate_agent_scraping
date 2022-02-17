"""
Tests for the calls to the real estate agents websites to check if they still work as intended.
Note: these test cases might fail in case no houses fall within the set requirements. (price/square meters)
"""
import unittest

from data_calls_real_estate_agent import get_arnold_taal_data, get_frisia_makelaars_data, get_bvl_data, get_langezaal_data, \
    get_elzenaar_data, get_oltshoorn_data, get_estata_data, get_nelisse_data, get_doen_data, get_van_aalst_data, \
    get_klap_makelaars_data, get_diva_makelaars_data, get_belderbos_data, get_hekking_data


class Test_data_calls_real_estate_agents(unittest.TestCase):
    def test_arnold(self):
        huizen_data = get_arnold_taal_data()
        self.assertIsInstance(huizen_data[0], list)
        self.assertGreaterEqual(len(huizen_data[0]), 1)

        # Links
        self.assertIsInstance(huizen_data[1], list)
        self.assertGreaterEqual(len(huizen_data[1]), len(huizen_data[0]))

    def test_get_frisiamakelaars_data(self):
        huizen_data = get_frisia_makelaars_data()
        self.assertIsInstance(huizen_data[0], list)
        self.assertGreaterEqual(len(huizen_data[0]), 1)

        # Links
        self.assertIsInstance(huizen_data[1], list)
        self.assertGreaterEqual(len(huizen_data[1]), len(huizen_data[0]))

    def test_get_bvl_data(self):
        huizen_data = get_bvl_data()
        self.assertIsInstance(huizen_data[0], list)
        self.assertGreaterEqual(len(huizen_data[0]), 1)

        # Links
        self.assertIsInstance(huizen_data[1], list)
        self.assertGreaterEqual(len(huizen_data[1]), len(huizen_data[0]))

    def test_get_langezaal_data(self):
        huizen_data = get_langezaal_data()
        self.assertIsInstance(huizen_data[0], list)
        self.assertGreaterEqual(len(huizen_data[0]), 1)

        # Links
        self.assertIsInstance(huizen_data[1], list)
        self.assertGreaterEqual(len(huizen_data[1]), len(huizen_data[0]))

    def test_get_elzenaar_data(self):
        huizen_data = get_elzenaar_data()
        self.assertIsInstance(huizen_data[0], list)
        self.assertGreaterEqual(len(huizen_data[0]), 1)

        # Links
        self.assertIsInstance(huizen_data[1], list)
        self.assertGreaterEqual(len(huizen_data[1]), len(huizen_data[0]))

    def test_get_oltshoorn_data(self):
        huizen_data = get_oltshoorn_data()
        self.assertIsInstance(huizen_data[0], list)
        self.assertGreaterEqual(len(huizen_data[0]), 1)

        # Links
        self.assertIsInstance(huizen_data[1], list)
        self.assertGreaterEqual(len(huizen_data[1]), len(huizen_data[0]))

    def test_get_nelisse_data(self):
        huizen_data = get_nelisse_data()
        self.assertIsInstance(huizen_data[0], list)
        self.assertGreaterEqual(len(huizen_data[0]), 1)

        # Links
        self.assertIsInstance(huizen_data[1], list)
        self.assertGreaterEqual(len(huizen_data[1]), len(huizen_data[0]))

    def test_get_estate_data(self):
        huizen_data = get_estata_data()
        self.assertIsInstance(huizen_data[0], list)
        self.assertGreaterEqual(len(huizen_data[0]), 1)

        # Links
        self.assertIsInstance(huizen_data[1], list)
        self.assertGreaterEqual(len(huizen_data[1]), len(huizen_data[0]))

    def test_get_doen_data(self):
        huizen_data = get_doen_data()
        self.assertIsInstance(huizen_data[0], list)
        self.assertGreaterEqual(len(huizen_data[0]), 1)

        # Links
        self.assertIsInstance(huizen_data[1], list)
        self.assertGreaterEqual(len(huizen_data[1]), len(huizen_data[0]))

    def test_get_belderbos_data(self):
        huizen_data = get_belderbos_data()
        self.assertIsInstance(huizen_data[0], list)
        self.assertGreaterEqual(len(huizen_data[0]), 1)

        # Links
        self.assertIsInstance(huizen_data[1], list)
        self.assertGreaterEqual(len(huizen_data[1]), len(huizen_data[0]))


    def test_get_van_aalst_data(self):
        huizen_data = get_van_aalst_data()
        self.assertIsInstance(huizen_data[0], list)
        self.assertGreaterEqual(len(huizen_data[0]), 1)

        # Links
        self.assertIsInstance(huizen_data[1], list)
        self.assertGreaterEqual(len(huizen_data[1]), len(huizen_data[0]))

    def test_get_hekking_data(self):
        huizen_data = get_hekking_data()
        self.assertIsInstance(huizen_data[0], list)
        self.assertGreaterEqual(len(huizen_data[0]), 1)

        # Links
        self.assertIsInstance(huizen_data[1], list)
        self.assertGreaterEqual(len(huizen_data[1]), len(huizen_data[0]))

    def test_get_klap_makelaars_data(self):
        huizen_data = get_klap_makelaars_data()
        self.assertIsInstance(huizen_data[0], list)
        self.assertGreaterEqual(len(huizen_data[0]), 1)

        # Links
        self.assertIsInstance(huizen_data[1], list)
        self.assertGreaterEqual(len(huizen_data[1]), len(huizen_data[0]))

    def test_get_diva_makelaars_data(self):
        huizen_data = get_diva_makelaars_data()
        self.assertIsInstance(huizen_data[0], list)
        self.assertGreaterEqual(len(huizen_data[0]), 1)

        # Links
        self.assertIsInstance(huizen_data[1], list)
        self.assertGreaterEqual(len(huizen_data[1]), len(huizen_data[0]))

if __name__ == '__main__':
    unittest.main()