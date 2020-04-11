import json

stats = {
    'region': {
        'name': 'Africa',
        'avgAge': 19.7,
        'avgDailyIncomeInUSD': 5,
        'avgDailyIncomePopulation': 0.71
    },
    'periodType': 'days',
    'timeToElapse': 58,
    'reportedCases': 674,
    'population': 66622705,
    'totalHospitalBeds': 1380614
}


def requestedTimeFactorCalculator(periodType, timeToElapse):
    if periodType == 'days':
        days = timeToElapse
        return 2 ^ int(days/3)
    elif periodType == 'months':
        days = timeToElapse * 30
        return 2 ^ int(days/3)
    elif periodType == 'years':
        days = timeToElapse * 12 * 30
        return 2 ^ int(days/3)
    else:
        raise Exception(
            'Period should be days, months or years.'
            '{} was given'.format(periodType))


def impactCalculator(reportedCases, requestedTimeFactor):
    currentlyInfected = reportedCases * 10
    infectionsByRequestedTime = currentlyInfected * requestedTimeFactor
    return dict(currentlyInfected=currentlyInfected,
                infectionsByRequestedTime=infectionsByRequestedTime)


def severeImpactCalculator(reportedCases, requestedTimeFactor):
    currentlyInfected = reportedCases * 50
    infectionsByRequestedTime = currentlyInfected * requestedTimeFactor
    return dict(currentlyInfected=currentlyInfected,
                infectionsByRequestedTime=infectionsByRequestedTime)


def estimator(data):
    reportedCases = data['reportedCases']
    timeFactor = requestedTimeFactorCalculator(
        data['periodType'], data['timeToElapse'])
    data = dict(data=data,
                impact=impactCalculator(reportedCases, timeFactor),
                severeImpact=severeImpactCalculator(reportedCases, timeFactor))
    return data


if __name__ == '__main__':
    print(json.dumps(estimator(stats)))
