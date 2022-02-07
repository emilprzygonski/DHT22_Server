import time
import calendar
from datetime import date, datetime, timedelta


class State():
    max_length = 720
    data = {
        'labels': [],
        'series': [[], []]}

    def add_data_temperature(self, single_value):
        handler = self.data['series'][0]

        if len(handler) >= self.max_length:
            handler.pop(0)
        handler.append(single_value)
        return

    def add_data_humidity(self, single_value):
        handler = self.data['series'][1]

        if len(handler) >= self.max_length:
            handler.pop(0)
        handler.append(single_value)
        return

    def add_data_time(self):
        my_date = date.today()
        week_day = calendar.day_name[my_date.weekday()]

        current_time = (datetime.now() + timedelta(hours=1)).strftime("%H:%M")


        y_label = week_day + ' ' + current_time
        handler = self.data['labels']
        if len(handler) >= self.max_length:
            handler.pop(0)
        handler.append(y_label)
        return

    def get_data_temperature(self):
        return self.data['series'][0]

    def get_data_humidity(self):
        return self.data['series'][1]

    def get_data_time(self):
        return self.data['labels']

    def get_data(self):
        return self.data

    def add_data(self, temp_value, humidity_value):
        self.add_data_temperature(temp_value)
        self.add_data_humidity(humidity_value)
        self.add_data_time()
