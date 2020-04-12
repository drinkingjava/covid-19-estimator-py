import unittest
from estimator import estimator
data = {
    'region': {
        'name': 'Africa',
        'avgAge': 19.7,
        'avgDailyIncomeInUSD': 5,
        'avgDailyIncomePopulation': 0.71
    },
    'periodType': 'days',
    'timeToElapse': 38,
    'reportedCases': 2747,
    'population': 66622705,
    'totalHospitalBeds': 1380614
}

correct_output = {
    'data': data,
    'estimate': {
        'impact': {
            "currentlyInfected": 27470,
            "infectionsByRequestedTime": 112517120,
            "severeCasesByRequestedTime": 16877568
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
        self.output = estimator(data)
        self.assertDictEqual(correct_output, self.output)


if __name__ == "__main__":
    unittest.main()
