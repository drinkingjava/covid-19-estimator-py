import json

stats = {
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


def requestedTimeFactorCalculator(periodType, timeToElapse):
    if periodType == 'days':
        days = timeToElapse
        print(2 ** (int(days/3)))
        return 2 ** int(days/3)
    elif periodType == 'weeks':
        days = timeToElapse * 7
        return 2 ** int(days/3)
    elif periodType == 'months':
        days = timeToElapse * 30
        return 2 ** int(days/3)
    else:
        raise Exception(
            'Period should be days, months or years.'
            '{} was given'.format(periodType))


def impactCalculator(reportedCases, requestedTimeFactor):
    currentlyInfected = reportedCases * 10
    infectionsByRequestedTime = currentlyInfected * requestedTimeFactor
    severeCasesByRequestedTime = int(infectionsByRequestedTime * 0.15)
    return dict(currentlyInfected=currentlyInfected,
                infectionsByRequestedTime=infectionsByRequestedTime,
                severeCasesByRequestedTime=severeCasesByRequestedTime)


def severeImpactCalculator(reportedCases, requestedTimeFactor):
    currentlyInfected = reportedCases * 50
    infectionsByRequestedTime = currentlyInfected * requestedTimeFactor
    severeCasesByRequestedTime = int(infectionsByRequestedTime * 0.15)
    return dict(currentlyInfected=currentlyInfected,
                infectionsByRequestedTime=infectionsByRequestedTime,
                severeCasesByRequestedTime=severeCasesByRequestedTime)


def estimator(data):
    reportedCases = data['reportedCases']
    timeFactor = requestedTimeFactorCalculator(
        data['periodType'], data['timeToElapse'])
    data = {
        "data": data,
        "estimate": {
            "impact": impactCalculator(reportedCases, timeFactor),
            "severeImpact": severeImpactCalculator(reportedCases, timeFactor)
        }
    }
    return data


if __name__ == '__main__':
    print(json.dumps(estimator(stats), indent=4))
