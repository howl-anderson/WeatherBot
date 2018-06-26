## simple path with greet
* greet
  - utter_greet
* weather_address_date-time{"address": "上海", "date-time": "明天"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather

## simple path
* weather_address_date-time{"address": "上海", "date-time": "明天"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather

## address + date-time path with greet
* greet
  - utter_greet
* weather_address{"address": "上海"}
  - utter_ask_date-time
* weather_date-time{"date-time": "明天"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather

## address + date-time path
* weather_address{"address": "上海"}
  - utter_ask_date-time
* weather_date-time{"date-time": "明天"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather

## date-time + address path with greet
* greet
  - utter_greet
* weather_date-time{"date-time": "明天"}
  - utter_ask_address
* weather_address{"address": "上海"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather

## date-time + address path
* weather_date-time{"date-time": "明天"}
  - utter_ask_address
* weather_address{"address": "上海"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather

## None + date-time + address path
* weather{}
  - utter_ask_date-time
* weather_date-time{"date-time": "明天"}
  - utter_ask_address
* weather_address{"address": "上海"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather

## None + date-time + address path with greet
* greet
  - utter_greet
* weather{}
  - utter_ask_date-time
* weather_date-time{"date-time": "明天"}
  - utter_ask_address
* weather_address{"address": "上海"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather

## say goodbye
* goodbye
  - utter_goodbye