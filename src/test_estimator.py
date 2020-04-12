import unittest
from estimator import estimator

sample_data = {
    'region': {
        'name': 'Africa',
        'avgAge': 19.7,
        'avgDailyIncomeInUSD': 4,
        'avgDailyIncomePopulation': 0.73
    },
    'periodType': 'days',
    'timeToElapse': 38,
    'reportedCases': 2747,
    'population': 92931687,
    'totalHospitalBeds': 678874
}


sample_output = {
    'data': data,
    'estimate': {
        'impact': {
            "currentlyInfected": 27470,
            "infectionsByRequestedTime": 112517120,
            "severeCasesByRequestedTime": 16877568,
            "hospitalBedsByRequestedTime": -16639962,
        },
        'severeImpact': {
            "currentlyInfected": 137350,
            "infectionsByRequestedTime": 562585600,
            "severeCasesByRequestedTime": 84387840
        }
    }
}


class estimatorTestCase(unittest.TestCase):
    def test_estimator_output(self):
        self.maxDiff = None
        self.output = estimator(sample_data)
        self.assertDictEqual(sample_output, self.output)


if __name__ == "__main__":
    unittest.main()
