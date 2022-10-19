from .models import User, Location, TravelRecord, InfectionRecord
from datetime import timedelta

FUTURE = 30
DELTA_DAY = timedelta(days=1)
STR_FORMAT = "%Y-%m-%d"


def getSigma(userIDs):
    sigma = 1
    for user_id in userIDs:
        sigma *= User.objects.get(
            pk=user_id).infection_probability/100
    return sigma


def updateInfection(user, infection_factor, sigma_factor):
    delta = (100 - user.infection_probability)*infection_factor*sigma_factor
    user.infection_probability = user.infection_probability + delta
    user.save()
    return user


def updateRecords(infection_record_id):
    infection_start = InfectionRecord.objects.get(pk=infection_record_id)
    start_date = infection_start.arrived_at
    travel_records = TravelRecord.objects.filter(
        arrived_at__gte=start_date.strftime(STR_FORMAT))
    locations = Location.objects.all()

    # print(infection_record_id)
    # print(travel_records)

    END_DATE = (FUTURE*DELTA_DAY + start_date)
    date = start_date
    while (date != END_DATE):
        # get users who were at the specific location on the given day
        for location in locations:
            userIDs = [trecord.user.id
                       for trecord in travel_records
                       if
                       (trecord.arrived_at.strftime(STR_FORMAT)
                        == date.strftime(STR_FORMAT)
                        and trecord.location.id == location.id)]
            if len(userIDs) > 1:
                # change infection probability for all of them
                # and update database
                sigma = getSigma(userIDs)

                updated_users = [updateInfection(User.objects.get(pk=user_id),
                                                 location.infection_factor,
                                                 sigma)
                                 for user_id in userIDs]
                print(updated_users)
        date += DELTA_DAY

        # inputID = [(trecord.user.id, trecord.location.infection_factor)
        #            for trecord in travel_records
        #            if
        #            trecord.arrived_at.strftime(STR_FORMAT)
        #            == date.strftime(STR_FORMAT)]
        # if len(inputID) > 1:
        #     # change infection probability for all of them and update database
        #     sigma = 1
        #     for user_id, _ in inputID:
        #         sigma *= User.objects.get(pk=user_id).infection_probability/100
        #     print(sigma)
        #
        #     updated_users = [updateInfection(User.objects.get(pk=user_id),
        #                                      inf_fact, sigma)
        #                      for user_id, inf_fact in inputID]
        #     print(updated_users)
        # date += DELTA_DAY
