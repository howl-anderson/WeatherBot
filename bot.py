from typing import List

from rasa_core.actions import Action
from rasa_core.dispatcher import Dispatcher
from rasa_core.domain import Domain
from rasa_core.events import SlotSet, Event
from rasa_core.trackers import DialogueStateTracker

from api import get_weather_by_day


class ActionReportWeather(Action):
    def name(self):
        # type: () -> Text
        return "action_report_weather"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

        address = tracker.get_slot('address')
        date_time = tracker.get_slot('date-time')

        date_time_number = text_date_to_number_date(date_time)

        if isinstance(date_time_number, str):  # parse date_time failed
            return [SlotSet("matches", "天气情况：{}".format([address, date_time_number]))]
        else:
            weather_data = get_text_weather_date(address, date_time, date_time_number)
            return [SlotSet("matches", weather_data)]


def get_text_weather_date(address, date_time, date_time_number):
    result = get_weather_by_day(address, date_time_number)
    text_message_tpl = "{} {} ({}) 的天气情况为：白天：{}；夜晚：{}；气温：{}-{} °C"
    text_message = text_message_tpl.format(
        result['location']['name'],
        date_time,
        result['result']['date'],
        result['result']['text_day'],
        result['result']['text_night'],
        result['result']["high"],
        result['result']["low"],
    )

    return text_message


def text_date_to_number_date(text_date):
    if text_date == "今天":
        return 0
    if text_date == "明天":
        return 1
    if text_date == "后天":
        return 2
    if text_date == "大后天":
        return 3

    if text_date.startswith("星期"):
        # TODO: using calender to compute relative date
        return text_date

    if text_date.startswith("下星期"):
        # TODO: using calender to compute relative date
        return text_date

    # follow APIs are not supported by weather API provider
    if text_date == "昨天":
        return text_date
    if text_date == "前天":
        return text_date
    if text_date == "大前天":
        return text_date
