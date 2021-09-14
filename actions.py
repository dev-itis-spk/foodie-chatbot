from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted
import pandas as pd
from email.message import EmailMessage
import smtplib

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi',
             'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun',
             'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore',
             'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa',
             'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']


def sendmail(mail_id, response):
    html_body = F"""
                    <html>
                        <head></head>
                        <body>
                            <p>Dear User, Greetings from <b>Foodie</b>!</p>
                            <p>Please find below the details of restaurants you have requested for:</p>
                            <ul>
                                {response}
                            </ul><br>
                            <p>Have a great time! Thank you.</p>
                        </body>
                    </html>
                """

    EMAIL_ADDRESS = 'webautomation89@gmail.com'
    EMAIL_PASSWORD = "test@9876"

    msg = EmailMessage()
    msg['Subject'] = "Restaurant Search Result"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = mail_id

    msg.add_alternative(html_body, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


def restaurant_search(location, cuisine, budget):
    """Method to search for restaurants for given parameters"""
    res_data = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: cuisine.lower() in x.lower())) & (
        ZomatoData['City'].apply(lambda x: location.lower() in x.lower()))]

    # Filtering on the basis of Price Range
    if budget == "low":
        res_data = res_data[res_data["Average Cost for two"] < 300]
    elif budget == "mid":
        res_data = res_data[(res_data["Average Cost for two"] >= 300) & (res_data["Average Cost for two"] <= 700)]
    else:
        res_data = res_data[res_data["Average Cost for two"] > 700]

    # Sorting the filter result on the basis of Aggregate ratings
    res_data.sort_values(["Aggregate rating"], ascending=False, inplace=True)

    return res_data[['Restaurant Name', 'Address', 'Average Cost for two', 'Aggregate rating']]


class ActionSearchRestaurants(Action):
    """Action class to search restaurants"""
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        response = ""
        email_message = ""
        valid_search = True

        # get the location, cuisine and budget from slots
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price_range = tracker.get_slot('price_range')

        # check validity of location
        lc_we_operate = [x.lower() for x in WeOperate]
        if loc.lower() not in lc_we_operate:
            valid_search = False
            response = "Apologies, we do not operate in this area yet 🙁!"
            return [SlotSet('location', loc), SlotSet('restaurant_data', response)]

        # check validity of cuisine
        available_cuisines = ('chinese', 'italian', 'south indian', 'north indian', 'mexican', 'american')
        if cuisine.lower() not in available_cuisines:
            valid_search = False
            response = "Apologies, we do not offer this cuisine 🙁!"
            return [SlotSet('location', loc), SlotSet('restaurant_data', response)]

        # perform restaurant search
        results = restaurant_search(location=loc, cuisine=cuisine, budget=price_range)

        if results.shape[0] == 0 or results.shape[0] < 5:
            response = "Sorry, we couldn't find any restaurants that match your requirements. " \
                       "Hope to serve you better next time!"
            valid_search = False
        else:
            for restaurant in results.iloc[:5].iterrows():
                restaurant = restaurant[1]
                response = response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated " \
                                      F"{restaurant['Aggregate rating']} with avg cost " \
                                      F"{restaurant['Average Cost for two']} \n\n"

            for restaurant in results.iloc[:10].iterrows():
                restaurant = restaurant[1]
                email_message = email_message + F"<li> <b>{restaurant['Restaurant Name']}</b> in <b>" \
                                                F"{restaurant['Address']}</b> rated <b>" \
                                                F"{restaurant['Aggregate rating']}</b> with avg cost <b>" \
                                                F"{restaurant['Average Cost for two']}</b> </li>"

        dispatcher.utter_message("----- " + response)
        return [SlotSet('location', loc), SlotSet('restaurant_data', response), SlotSet('email_data', email_message),
                SlotSet('valid_search', valid_search)]


class ActionSendMail(Action):
    """Action class to send email"""
    def name(self):
        return 'action_send_mail'

    def run(self, dispatcher, tracker, domain):
        mail_id = tracker.get_slot('email')
        restaurant_data = tracker.get_slot('email_data')
        sendmail(mail_id, restaurant_data)
        return [SlotSet('email', mail_id)]


class ActionCheckLocation(Action):
    """Action class to check if location valid"""
    def name(self):
        return 'action_check_location'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        valid_loc = True
        lc_we_operate = [x.lower() for x in WeOperate]
        if loc.lower() not in lc_we_operate:
            valid_loc = False
            dispatcher.utter_message("We do not operate in this area yet")
        return [SlotSet('valid_location', valid_loc)]


class ActionCheckCuisine(Action):
    """Action class to check if cuisine valid"""
    def name(self):
        return 'action_check_cuisine'

    def run(self, dispatcher, tracker, domain):
        cuisine = tracker.get_slot('cuisine')
        available_cuisines = ('chinese', 'italian', 'south indian', 'north indian', 'mexican', 'american')
        valid_cuisine = True
        if cuisine.lower() not in available_cuisines:
            valid_cuisine = False
            dispatcher.utter_message("Apologies, we do not cater to the requested cuisine.")
        return [SlotSet('valid_cuisine', valid_cuisine)]


class ActionResetSlot(Action):
    """Action class to reset slots"""
    def name(self):
        return 'action_reset_slot'

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]


class ActionRestartBot(Action):
    """Action class to restart bot"""
    def name(self):
        return 'action_restart_bot'

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]
