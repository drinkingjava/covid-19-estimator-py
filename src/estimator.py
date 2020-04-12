import json
import logging

logging.basicConfig(level=logging.DEBUG)

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


def bedAvailabilityCalculator(totalHospitalBeds, severeCasesByRequestedTime):
    occupied = int(totalHospitalBeds * 0.65)
    available = totalHospitalBeds - occupied
    availableForPatients = available - severeCasesByRequestedTime
    return availableForPatients
    logging.debug('availablebeds: {}'.format(available))
    print('total:', totalHospitalBeds)
    print('occupied:', occupied)
    print('available:', available)
    print('available for covid patients:', availableForPatients)
    print('available plus occupied:', available + occupied)


def impact(data, impactType):
    reportedCases = data['reportedCases']
    if impactType == 'normal':
        currentlyInfected = reportedCases * 10
    elif impactType == 'severe':
        currentlyInfected = reportedCases * 50
    else:
        raise Exception('Unsupported impact type given')

    totalBeds = data['totalHospitalBeds']
    timeToElapse = data['timeToElapse']
    timeFactor = requestedTimeFactorCalculator(
        data['periodType'], data['timeToElapse'])
    avgIncome = data['region']['avgDailyIncomeInUSD']
    avgIncomePop = data['region']['avgDailyIncomePopulation']
    infectionsByRequestedTime = currentlyInfected * timeFactor
    severeCasesByRequestedTime = int(infectionsByRequestedTime * 0.15)
    hospitalBedsByRequestedTime = bedAvailabilityCalculator(
        totalBeds, severeCasesByRequestedTime)
    casesForICUByRequestedTime = int(infectionsByRequestedTime * 0.05)
    casesForVentilators = int(infectionsByRequestedTime * 0.02)
    dollarsInFlight = int((infectionsByRequestedTime *
                           avgIncomePop * avgIncome) * timeToElapse)
    return dict(currentlyInfected=currentlyInfected,
                infectionsByRequestedTime=infectionsByRequestedTime,
                severeCasesByRequestedTime=severeCasesByRequestedTime,
                hospitalBedsByRequestedTime=hospitalBedsByRequestedTime,
                casesForICUByRequestedTime=casesForICUByRequestedTime,
                casesForVentilatorsByRequestedTime=casesForVentilators,
                dollarsInFlight=dollarsInFlight)


def estimator(data):
    data = {
        "data": data,
        "estimate": {
            "impact": impact(data, 'normal'),
            "severeImpact": impact(data, 'severe')
        }
    }
    return data


if __name__ == '__main__':
    print(json.dumps(estimator(stats), indent=4))
