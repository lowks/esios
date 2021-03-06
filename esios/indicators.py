from datetime import datetime

from libsaas import http, parsers
from libsaas.services import base


class Indicator(base.RESTResource):
    path = 'indicators'


class ProfilePVPC(Indicator):

    @base.apimethod
    def get(self, start_date, end_date):
        assert isinstance(start_date, datetime)
        assert isinstance(end_date, datetime)
        if start_date.tzinfo is None:
            raise Exception('Start date must have time zone')
        if end_date.tzinfo is None:
            raise Exception('End date must have time zone')
        time_trunc = 'hour'
        start_date = start_date.isoformat()
        end_date = end_date.isoformat()
        params = base.get_params(
            ('start_date', 'end_date', 'time_trunc'), locals()
        )
        request = http.Request('GET', self.get_url(), params)
        return request, parsers.parse_json


class ProfilePVPC20A(ProfilePVPC):
    path = 'indicators/526'


class ProfilePVPC20DHA(ProfilePVPC):
    path = 'indicators/527'


class ProfilePVPC20DHS(ProfilePVPC):
    path = 'indicators/528'
