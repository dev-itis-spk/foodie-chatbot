# Foodie Chatbot
An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. You have been hired as the lead data scientist for creating this product.

### Objective
The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. 
- Your bot should be able to work in all the cities which are mentioned in the dataset provided to you(Zomato.csv).
- The bot should show the result if the location doesn't necessarily have 5 restaurants. For e.g: Location A serves only 1 restaurant then the bot should result for that as well.
- The bot should be able to identify common synonyms of city names, such as Bangalore/Bengaluru, Mumbai/Bombay etc.

Your chatbot should provide results for all the relevant locations mentioned in the dataset while for other locations, it should reply back with something like "We do not operate in that area yet".

Questions asked by Bot:
- Cuisine Preference
- Average budget for two people

While showing the results to the user, the bot should display the top 5 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest). The format should be: {restaurant_name} in {restaurant_address} has been rated {rating}.

Finally, the bot should ask the user whether he/she wants the details of the top 10 restaurants on email. If the user replies 'yes', the bot should ask for user’s email id and then send it over email. Else, just reply with a 'goodbye' message. The mail should have the following details for each restaurant:
- Restaurant Name
- Restaurant locality address
- Average budget for two people
- Zomato user rating
