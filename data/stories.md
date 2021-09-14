## complete path all valid - with no email and no response
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_price_range
* restaurant_search{"price_range": "mid"}
    - slot{"price_range": "mid"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"restaurant_data": "No restaurants found for your criteria!"}
    - slot{"email_data": ""}
    - slot{"valid_search": false}
    - utter_thanks
    - action_reset_slot
    - reset_slots

## complete path all valid - with email and response
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_price_range
* restaurant_search{"price_range": "high"}
    - slot{"price_range": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"restaurant_data": "Found The Fusion Kitchen in Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC colony, Borivali West, Mumbai rated Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC colony, Borivali West, Mumbai with avg cost 1000 \n\nFound Yauatcha in Raheja Tower, Bandra Kurla Complex, Mumbai rated Raheja Tower, Bandra Kurla Complex, Mumbai with avg cost 2800 \n\nFound Butterfly High in Unit 4, Ground Floor, Jet Airways, Godrej G Block, Near MCA, Bandra Kurla Complex, Mumbai rated Unit 4, Ground Floor, Jet Airways, Godrej G Block, Near MCA, Bandra Kurla Complex, Mumbai with avg cost 1500 \n\nFound BKC  DIVE in Ground Floor, Pinnacle Corporate Park, Opposite MTNL Office, Bandra Kurla Complex, Mumbai rated Ground Floor, Pinnacle Corporate Park, Opposite MTNL Office, Bandra Kurla Complex, Mumbai with avg cost 1100 \n\nFound Bayview Cafe in Hotel Harbour View, Kerawala Chamber, Opposite Radio Club, 25, J P Ramchandani Marg, Colaba, Mumbai rated Hotel Harbour View, Kerawala Chamber, Opposite Radio Club, 25, J P Ramchandani Marg, Colaba, Mumbai with avg cost 1200 \n\n"}
    - slot{"email_data": "<li> <b>The Fusion Kitchen</b> in <b>Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC colony, Borivali West, Mumbai</b> rated <b>4.7</b> with avg cost <b>1000</b> </li><li> <b>Yauatcha</b> in <b>Raheja Tower, Bandra Kurla Complex, Mumbai</b> rated <b>4.6</b> with avg cost <b>2800</b> </li><li> <b>Butterfly High</b> in <b>Unit 4, Ground Floor, Jet Airways, Godrej G Block, Near MCA, Bandra Kurla Complex, Mumbai</b> rated <b>4.3</b> with avg cost <b>1500</b> </li><li> <b>BKC  DIVE</b> in <b>Ground Floor, Pinnacle Corporate Park, Opposite MTNL Office, Bandra Kurla Complex, Mumbai</b> rated <b>4.2</b> with avg cost <b>1100</b> </li><li> <b>Bayview Cafe</b> in <b>Hotel Harbour View, Kerawala Chamber, Opposite Radio Club, 25, J P Ramchandani Marg, Colaba, Mumbai</b> rated <b>4.2</b> with avg cost <b>1200</b> </li><li> <b>Tea Villa Cafe</b> in <b>31, Opposite Globus, Hill Road, Bandra West</b> rated <b>4.1</b> with avg cost <b>1000</b> </li><li> <b>Tea Villa Cafe</b> in <b>28, Aaram Nagar 1, Opposite Dariya Mahal, Versova, Andheri West</b> rated <b>4.1</b> with avg cost <b>1000</b> </li><li> <b>By The Bae - Kitchen And Bar</b> in <b>9A - 9B, Aram Nagar 2, JP Road, Versova, Andheri West, Mumbai</b> rated <b>4.0</b> with avg cost <b>2500</b> </li><li> <b>Tea Villa Cafe</b> in <b>Shop 1& 2, Y-Building, Flower Valley, Opposite Viviana Mall,Eastern Express Highway, Majiwada, Thane West</b> rated <b>3.9</b> with avg cost <b>1000</b> </li><li> <b>Mumbai Vibe</b> in <b>Ganga Jamuna Block, 14th Road, Linking Road, Bandra West</b> rated <b>3.8</b> with avg cost <b>1000</b> </li>"}
    - slot{"valid_search": true}
    - utter_ask_mail_preference
* affirm
    - utter_ask_email
* send_mail{"email": "dev.itis.spk@gmail.com"}
    - slot{"email": "dev.itis.spk@gmail.com"}
    - action_send_mail
    - slot{"email": "dev.itis.spk@gmail.com"}
    - utter_confirm_mail
    - utter_thanks
    - utter_goodbye
    - action_reset_slot
    - reset_slots

## path with invalid location and correction
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_check_location
    - slot{"valid_location": false}
    - utter_ask_location_again
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_check_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_price_range
* restaurant_search{"price_range": "high"}
    - slot{"price_range": "high"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"restaurant_data": "Found ECHOES Koramangala in 44, 4th B Cross, Koramangala 5th Block, Bangalore rated 44, 4th B Cross, Koramangala 5th Block, Bangalore with avg cost 950 \n\nFound AB's - Absolute Barbecues in 90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore rated 90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore with avg cost 1400 \n\nFound Big Brewsky in Behind MK Retail, Before WIPRO Corporate Office, Sarjapur Road, Bangalore rated Behind MK Retail, Before WIPRO Corporate Office, Sarjapur Road, Bangalore with avg cost 1800 \n\nFound The London Curry House - The Royale Senate Hotel in 19/3, Kumara Krupa Road, Race Course Road, Bangalore rated 19/3, Kumara Krupa Road, Race Course Road, Bangalore with avg cost 1700 \n\nFound The 13th Floor in 84/142, 12th And 13th Floor, Barton Center, MG Road, Bangalore rated 84/142, 12th And 13th Floor, Barton Center, MG Road, Bangalore with avg cost 2000 \n\n"}
    - slot{"email_data": "<li> <b>ECHOES Koramangala</b> in <b>44, 4th B Cross, Koramangala 5th Block, Bangalore</b> rated <b>4.7</b> with avg cost <b>950</b> </li><li> <b>AB's - Absolute Barbecues</b> in <b>90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore</b> rated <b>4.6</b> with avg cost <b>1400</b> </li><li> <b>Big Brewsky</b> in <b>Behind MK Retail, Before WIPRO Corporate Office, Sarjapur Road, Bangalore</b> rated <b>4.5</b> with avg cost <b>1800</b> </li><li> <b>The London Curry House - The Royale Senate Hotel</b> in <b>19/3, Kumara Krupa Road, Race Course Road, Bangalore</b> rated <b>4.5</b> with avg cost <b>1700</b> </li><li> <b>The 13th Floor</b> in <b>84/142, 12th And 13th Floor, Barton Center, MG Road, Bangalore</b> rated <b>4.4</b> with avg cost <b>2000</b> </li><li> <b>Biergarten</b> in <b>4th B Cross, Koramangala 5th Block, Bangalore</b> rated <b>4.4</b> with avg cost <b>2000</b> </li><li> <b>The Bier Library</b> in <b>14, Patel Narayana Reddy Layout, 80 Feet Main Road, Koramangala 6th Block, Bangalore</b> rated <b>4.4</b> with avg cost <b>2000</b> </li><li> <b>Flechazo</b> in <b>9/1, 1st Floor, Above Surya Nissan, VRR Orchid, Doddanakkundi, Marathahalli, Bangalore</b> rated <b>4.4</b> with avg cost <b>1200</b> </li><li> <b>Big Pitcher</b> in <b>4121, LR Arcade, Old Airport Road, Bangalore</b> rated <b>4.3</b> with avg cost <b>1600</b> </li><li> <b>Byg Brewski Brewing Company</b> in <b>22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore</b> rated <b>4.3</b> with avg cost <b>1600</b> </li>"}
    - slot{"valid_search": true}
    - utter_ask_mail_preference
* send_mail{"email": "dev.itis.spk@gmail.com"}
    - slot{"email": "dev.itis.spk@gmail.com"}
    - action_send_mail
    - slot{"email": "dev.itis.spk@gmail.com"}
    - utter_confirm_mail
    - utter_thanks
    - utter_goodbye
    - action_reset_slot
    - reset_slots

## path with invalid cuisine and correction
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_check_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine_again
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_check_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_location
* restaurant_search{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_price_range
* restaurant_search{"price_range": "high"}
    - slot{"price_range": "high"}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - slot{"restaurant_data": "Sorry, we couldn't find any restaurants that match your requirements. Hope to serve you better next time!"}
    - slot{"email_data": ""}
    - slot{"valid_search": false}
    - utter_thanks
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    
## path with cuisine and location as initial params and deny email
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "Mysore"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Mysore"}
    - action_check_location
    - slot{"valid_location": true}
    - action_check_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_price_range
* restaurant_search{"price_range": "mid"}
    - slot{"price_range": "mid"}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - slot{"restaurant_data": "Found Original Vinayaka Mylari in 79, Nazarbad Main Road, Near Police Station, Doora, Mysore rated 79, Nazarbad Main Road, Near Police Station, Doora, Mysore with avg cost 300 \n\nFound Vinayaka Mylari in 79, Nazarbad Main Road, Near Police Station, Doora, Mysore rated 79, Nazarbad Main Road, Near Police Station, Doora, Mysore with avg cost 300 \n\nFound Hotel RRR in Sri Harsha Road, Lasker Mohalla, Near Mahatma Gandhi Square, Mandi Mohalla, Mysore rated Sri Harsha Road, Lasker Mohalla, Near Mahatma Gandhi Square, Mandi Mohalla, Mysore with avg cost 300 \n\nFound Highway 18 in 2766/12, 6th Main, 8th Cross Road, Vani Vilas Mohalla, Gokulam, Mysore rated 2766/12, 6th Main, 8th Cross Road, Vani Vilas Mohalla, Gokulam, Mysore with avg cost 400 \n\nFound Hyderabadi Biryani House in 299, Opposite To Water Tank, 2nd Stage, Vijay Nagar, Mysore rated 299, Opposite To Water Tank, 2nd Stage, Vijay Nagar, Mysore with avg cost 350 \n\n"}
    - slot{"email_data": "<li> <b>Original Vinayaka Mylari</b> in <b>79, Nazarbad Main Road, Near Police Station, Doora, Mysore</b> rated <b>4.2</b> with avg cost <b>300</b> </li><li> <b>Vinayaka Mylari</b> in <b>79, Nazarbad Main Road, Near Police Station, Doora, Mysore</b> rated <b>4.2</b> with avg cost <b>300</b> </li><li> <b>Hotel RRR</b> in <b>Sri Harsha Road, Lasker Mohalla, Near Mahatma Gandhi Square, Mandi Mohalla, Mysore</b> rated <b>4.2</b> with avg cost <b>300</b> </li><li> <b>Highway 18</b> in <b>2766/12, 6th Main, 8th Cross Road, Vani Vilas Mohalla, Gokulam, Mysore</b> rated <b>4.1</b> with avg cost <b>400</b> </li><li> <b>Hyderabadi Biryani House</b> in <b>299, Opposite To Water Tank, 2nd Stage, Vijay Nagar, Mysore</b> rated <b>4.1</b> with avg cost <b>350</b> </li><li> <b>Green Leaf</b> in <b>Opposite Reebok Showroom, Kalidasa Road, Vani Vilas Mohalla, Gokulam, Mysore</b> rated <b>4.0</b> with avg cost <b>400</b> </li><li> <b>Mezzaluna</b> in <b>First Floor, Kuvempu Trust Building, Near Chandrakala Hospital, New Kalidasa Road, Vijayanagar, Vijay Nagar, Mysore</b> rated <b>3.8</b> with avg cost <b>650</b> </li><li> <b>Pakva Lounge</b> in <b>Livin Corner, Temple Road, Vani Vilas Mohalla, Gokulam, Mysore</b> rated <b>3.7</b> with avg cost <b>650</b> </li><li> <b>By The Way</b> in <b>Next to Bhartat Cancer Hospital, Opposite Infosys Circle Ring Road, Vijay Nagar, Mysore</b> rated <b>3.6</b> with avg cost <b>650</b> </li><li> <b>Green Leaf</b> in <b>Opposite Reebok Showroom, Kalidasa Road, Vani Vilas Mohalla, Gokulam, Mysore</b> rated <b>3.5</b> with avg cost <b>400</b> </li>"}
    - slot{"valid_search": true}
    - utter_ask_mail_preference
* deny
    - utter_thanks
    - utter_goodbye
    - action_reset_slot
    - reset_slots

## path with cuisine and location as initial params with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian", "location": "noida"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"valid_location": true}
    - action_check_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_price_range
* restaurant_search{"price_range": "low"}
    - slot{"price_range": "low"}
    - action_search_restaurants
    - slot{"location": "noida"}
    - slot{"restaurant_data": "Found KD's Hunger Point in Shop 1A, Hansraj Complex, Sector 31, Noida rated Shop 1A, Hansraj Complex, Sector 31, Noida with avg cost 200 \n\nFound Hurry's Paratha in J-44, Sector 18, Noida rated J-44, Sector 18, Noida with avg cost 200 \n\nFound Hurry's Paratha in Road 1-B, Lt. Vijayant Thapar Marg, Near Sector 16 Metro Station, Sector 16, Noida rated Road 1-B, Lt. Vijayant Thapar Marg, Near Sector 16 Metro Station, Sector 16, Noida with avg cost 200 \n\nFound Whomely in A-136, Sector 83, Noida rated A-136, Sector 83, Noida with avg cost 200 \n\nFound Sati Restaurant in Likhi Ram Market, Atta, Near Subzi Mandi, Sector 27, Noida rated Likhi Ram Market, Atta, Near Subzi Mandi, Sector 27, Noida with avg cost 200 \n\n"}
    - slot{"email_data": "<li> <b>KD's Hunger Point</b> in <b>Shop 1A, Hansraj Complex, Sector 31, Noida</b> rated <b>3.7</b> with avg cost <b>200</b> </li><li> <b>Hurry's Paratha</b> in <b>J-44, Sector 18, Noida</b> rated <b>3.5</b> with avg cost <b>200</b> </li><li> <b>Hurry's Paratha</b> in <b>Road 1-B, Lt. Vijayant Thapar Marg, Near Sector 16 Metro Station, Sector 16, Noida</b> rated <b>3.5</b> with avg cost <b>200</b> </li><li> <b>Whomely</b> in <b>A-136, Sector 83, Noida</b> rated <b>3.2</b> with avg cost <b>200</b> </li><li> <b>Sati Restaurant</b> in <b>Likhi Ram Market, Atta, Near Subzi Mandi, Sector 27, Noida</b> rated <b>3.2</b> with avg cost <b>200</b> </li><li> <b>Maa Vaishno Shudh Bhojnalaya</b> in <b>27, Subzi Mandi Market, Sector 27, Noida</b> rated <b>3.1</b> with avg cost <b>250</b> </li><li> <b>Mood 4 Food</b> in <b>Shop 5, JM Orchid, Sector 76, NOIDA, Sector 72, Noida</b> rated <b>3.1</b> with avg cost <b>150</b> </li><li> <b>Mom's Canteen</b> in <b>Sector 62, Noida</b> rated <b>3.0</b> with avg cost <b>200</b> </li><li> <b>Shadev Saini Dhaba</b> in <b>Main Dadri Road, Village Chhalera, Sector 44, Noida</b> rated <b>3.0</b> with avg cost <b>200</b> </li><li> <b>Aggarwal Kachori Wale</b> in <b>Shop 26, X Block, Near Metro Hospital, Sector 12, Noida</b> rated <b>3.0</b> with avg cost <b>100</b> </li>"}
    - slot{"valid_search": true}
    - utter_ask_mail_preference
* send_mail{"email": "dev.itis.spk@gmail.com"}
    - slot{"email": "dev.itis.spk@gmail.com"}
    - action_send_mail
    - slot{"email": "dev.itis.spk@gmail.com"}
    - utter_confirm_mail
    - utter_thanks
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    
## path without greet - start directly with price range and location and deny email
* restaurant_search{"price_range": "mid", "location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - slot{"price_range": "mid"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"valid_cuisine": true}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - slot{"restaurant_data": "Found Echoes Satyaniketan in 17, 1st Floor, Opposite Sri Venkateshwara College, Satyaniketan, New Delhi rated 17, 1st Floor, Opposite Sri Venkateshwara College, Satyaniketan, New Delhi with avg cost 600 \n\nFound Big Yellow Door in H-8 B, Near GTB Nagar Metro Station, Opposite Hudson Lane's NDPL Office, Vijay Nagar, New Delhi rated H-8 B, Near GTB Nagar Metro Station, Opposite Hudson Lane's NDPL Office, Vijay Nagar, New Delhi with avg cost 600 \n\nFound Big Yellow Door in 2521, 2nd Floor, Kingsway Camp, Hudson Lane, GTB Nagar, New Delhi rated 2521, 2nd Floor, Kingsway Camp, Hudson Lane, GTB Nagar, New Delhi with avg cost 600 \n\nFound Chill'm Bar & Cafe in 38, Bunglow Road, Kamla Nagar, New Delhi rated 38, Bunglow Road, Kamla Nagar, New Delhi with avg cost 600 \n\nFound Big Yellow Door in H-8, Opposite Venkateswara College, Satyaniketan, New Delhi rated H-8, Opposite Venkateswara College, Satyaniketan, New Delhi with avg cost 600 \n\n"}
    - slot{"email_data": "<li> <b>Echoes Satyaniketan</b> in <b>17, 1st Floor, Opposite Sri Venkateshwara College, Satyaniketan, New Delhi</b> rated <b>4.7</b> with avg cost <b>600</b> </li><li> <b>Big Yellow Door</b> in <b>H-8 B, Near GTB Nagar Metro Station, Opposite Hudson Lane's NDPL Office, Vijay Nagar, New Delhi</b> rated <b>4.3</b> with avg cost <b>600</b> </li><li> <b>Big Yellow Door</b> in <b>2521, 2nd Floor, Kingsway Camp, Hudson Lane, GTB Nagar, New Delhi</b> rated <b>4.3</b> with avg cost <b>600</b> </li><li> <b>Chill'm Bar & Cafe</b> in <b>38, Bunglow Road, Kamla Nagar, New Delhi</b> rated <b>4.2</b> with avg cost <b>600</b> </li><li> <b>Big Yellow Door</b> in <b>H-8, Opposite Venkateswara College, Satyaniketan, New Delhi</b> rated <b>4.2</b> with avg cost <b>600</b> </li><li> <b>Superstar Caf</b> in <b>288, Opposite Venkateshwara College, Satyaniketan, New Delhi</b> rated <b>4.2</b> with avg cost <b>600</b> </li><li> <b>QRO Gourmeteriia BY DARK HOUSE KAFE</b> in <b>9, Ground Floor, Benito Juarez Marg, Opposite Sri Venkateshwara College, Satyaniketan, New Delhi</b> rated <b>4.2</b> with avg cost <b>600</b> </li><li> <b>YOLO 21</b> in <b>2522, Ground Floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi</b> rated <b>4.2</b> with avg cost <b>700</b> </li><li> <b>Young Wild Free Cafe</b> in <b>13, 1st Floor, Opposite Venkateswara College, Satyaniketan, New Delhi</b> rated <b>4.1</b> with avg cost <b>500</b> </li><li> <b>Pepper Kitchen</b> in <b>C 51, Ground Floor, Main Market, Malviya Nagar, New Delhi</b> rated <b>4.0</b> with avg cost <b>500</b> </li>"}
    - slot{"valid_search": true}
    - utter_ask_mail_preference
* deny
    - utter_thanks
    - utter_goodbye
    - action_reset_slot
    - reset_slots

## path with location as initial params
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_price_range
* restaurant_search{"price_range": "high"}
    - slot{"price_range": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"restaurant_data": "Found The Fusion Kitchen in Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC colony, Borivali West, Mumbai rated Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC colony, Borivali West, Mumbai with avg cost 1000 \n\nFound Yauatcha in Raheja Tower, Bandra Kurla Complex, Mumbai rated Raheja Tower, Bandra Kurla Complex, Mumbai with avg cost 2800 \n\nFound Butterfly High in Unit 4, Ground Floor, Jet Airways, Godrej G Block, Near MCA, Bandra Kurla Complex, Mumbai rated Unit 4, Ground Floor, Jet Airways, Godrej G Block, Near MCA, Bandra Kurla Complex, Mumbai with avg cost 1500 \n\nFound BKC  DIVE in Ground Floor, Pinnacle Corporate Park, Opposite MTNL Office, Bandra Kurla Complex, Mumbai rated Ground Floor, Pinnacle Corporate Park, Opposite MTNL Office, Bandra Kurla Complex, Mumbai with avg cost 1100 \n\nFound Bayview Cafe in Hotel Harbour View, Kerawala Chamber, Opposite Radio Club, 25, J P Ramchandani Marg, Colaba, Mumbai rated Hotel Harbour View, Kerawala Chamber, Opposite Radio Club, 25, J P Ramchandani Marg, Colaba, Mumbai with avg cost 1200 \n\n"}
    - slot{"email_data": "<li> <b>The Fusion Kitchen</b> in <b>Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC colony, Borivali West, Mumbai</b> rated <b>4.7</b> with avg cost <b>1000</b> </li><li> <b>Yauatcha</b> in <b>Raheja Tower, Bandra Kurla Complex, Mumbai</b> rated <b>4.6</b> with avg cost <b>2800</b> </li><li> <b>Butterfly High</b> in <b>Unit 4, Ground Floor, Jet Airways, Godrej G Block, Near MCA, Bandra Kurla Complex, Mumbai</b> rated <b>4.3</b> with avg cost <b>1500</b> </li><li> <b>BKC  DIVE</b> in <b>Ground Floor, Pinnacle Corporate Park, Opposite MTNL Office, Bandra Kurla Complex, Mumbai</b> rated <b>4.2</b> with avg cost <b>1100</b> </li><li> <b>Bayview Cafe</b> in <b>Hotel Harbour View, Kerawala Chamber, Opposite Radio Club, 25, J P Ramchandani Marg, Colaba, Mumbai</b> rated <b>4.2</b> with avg cost <b>1200</b> </li><li> <b>Tea Villa Cafe</b> in <b>31, Opposite Globus, Hill Road, Bandra West</b> rated <b>4.1</b> with avg cost <b>1000</b> </li><li> <b>Tea Villa Cafe</b> in <b>28, Aaram Nagar 1, Opposite Dariya Mahal, Versova, Andheri West</b> rated <b>4.1</b> with avg cost <b>1000</b> </li><li> <b>By The Bae - Kitchen And Bar</b> in <b>9A - 9B, Aram Nagar 2, JP Road, Versova, Andheri West, Mumbai</b> rated <b>4.0</b> with avg cost <b>2500</b> </li><li> <b>Tea Villa Cafe</b> in <b>Shop 1& 2, Y-Building, Flower Valley, Opposite Viviana Mall,Eastern Express Highway, Majiwada, Thane West</b> rated <b>3.9</b> with avg cost <b>1000</b> </li><li> <b>Mumbai Vibe</b> in <b>Ganga Jamuna Block, 14th Road, Linking Road, Bandra West</b> rated <b>3.8</b> with avg cost <b>1000</b> </li>"}
    - slot{"valid_search": true}
    - utter_ask_mail_preference
* affirm
    - utter_ask_email
* send_mail{"email": "dev.itis.spk@gmail.com"}
    - slot{"email": "dev.itis.spk@gmail.com"}
    - action_send_mail
    - slot{"email": "dev.itis.spk@gmail.com"}
    - utter_confirm_mail
    - utter_thanks
    - utter_goodbye
    - action_reset_slot
    - reset_slots

## path with cuisine as initial params
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_price_range
* restaurant_search{"price_range": "high"}
    - slot{"price_range": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"restaurant_data": "Found The Fusion Kitchen in Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC colony, Borivali West, Mumbai rated Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC colony, Borivali West, Mumbai with avg cost 1000 \n\nFound Yauatcha in Raheja Tower, Bandra Kurla Complex, Mumbai rated Raheja Tower, Bandra Kurla Complex, Mumbai with avg cost 2800 \n\nFound Butterfly High in Unit 4, Ground Floor, Jet Airways, Godrej G Block, Near MCA, Bandra Kurla Complex, Mumbai rated Unit 4, Ground Floor, Jet Airways, Godrej G Block, Near MCA, Bandra Kurla Complex, Mumbai with avg cost 1500 \n\nFound BKC  DIVE in Ground Floor, Pinnacle Corporate Park, Opposite MTNL Office, Bandra Kurla Complex, Mumbai rated Ground Floor, Pinnacle Corporate Park, Opposite MTNL Office, Bandra Kurla Complex, Mumbai with avg cost 1100 \n\nFound Bayview Cafe in Hotel Harbour View, Kerawala Chamber, Opposite Radio Club, 25, J P Ramchandani Marg, Colaba, Mumbai rated Hotel Harbour View, Kerawala Chamber, Opposite Radio Club, 25, J P Ramchandani Marg, Colaba, Mumbai with avg cost 1200 \n\n"}
    - slot{"email_data": "<li> <b>The Fusion Kitchen</b> in <b>Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC colony, Borivali West, Mumbai</b> rated <b>4.7</b> with avg cost <b>1000</b> </li><li> <b>Yauatcha</b> in <b>Raheja Tower, Bandra Kurla Complex, Mumbai</b> rated <b>4.6</b> with avg cost <b>2800</b> </li><li> <b>Butterfly High</b> in <b>Unit 4, Ground Floor, Jet Airways, Godrej G Block, Near MCA, Bandra Kurla Complex, Mumbai</b> rated <b>4.3</b> with avg cost <b>1500</b> </li><li> <b>BKC  DIVE</b> in <b>Ground Floor, Pinnacle Corporate Park, Opposite MTNL Office, Bandra Kurla Complex, Mumbai</b> rated <b>4.2</b> with avg cost <b>1100</b> </li><li> <b>Bayview Cafe</b> in <b>Hotel Harbour View, Kerawala Chamber, Opposite Radio Club, 25, J P Ramchandani Marg, Colaba, Mumbai</b> rated <b>4.2</b> with avg cost <b>1200</b> </li><li> <b>Tea Villa Cafe</b> in <b>31, Opposite Globus, Hill Road, Bandra West</b> rated <b>4.1</b> with avg cost <b>1000</b> </li><li> <b>Tea Villa Cafe</b> in <b>28, Aaram Nagar 1, Opposite Dariya Mahal, Versova, Andheri West</b> rated <b>4.1</b> with avg cost <b>1000</b> </li><li> <b>By The Bae - Kitchen And Bar</b> in <b>9A - 9B, Aram Nagar 2, JP Road, Versova, Andheri West, Mumbai</b> rated <b>4.0</b> with avg cost <b>2500</b> </li><li> <b>Tea Villa Cafe</b> in <b>Shop 1& 2, Y-Building, Flower Valley, Opposite Viviana Mall,Eastern Express Highway, Majiwada, Thane West</b> rated <b>3.9</b> with avg cost <b>1000</b> </li><li> <b>Mumbai Vibe</b> in <b>Ganga Jamuna Block, 14th Road, Linking Road, Bandra West</b> rated <b>3.8</b> with avg cost <b>1000</b> </li>"}
    - slot{"valid_search": true}
    - utter_ask_mail_preference
* affirm
    - utter_ask_email
* send_mail{"email": "manojromina1997@gmail.com"}
    - slot{"email": "manojromina1997@gmail.com"}
    - action_send_mail
    - slot{"email": "manojromina1997@gmail.com"}
    - utter_confirm_mail
    - utter_thanks
    - utter_goodbye
    - action_reset_slot
    - reset_slots

## path with price as initial params
* greet
    - utter_greet
* restaurant_search{"price_range": "high"}
    - slot{"price_range": "high"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"valid_cuisine": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"restaurant_data": "Found The Fusion Kitchen in Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC colony, Borivali West, Mumbai rated Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC colony, Borivali West, Mumbai with avg cost 1000 \n\nFound Yauatcha in Raheja Tower, Bandra Kurla Complex, Mumbai rated Raheja Tower, Bandra Kurla Complex, Mumbai with avg cost 2800 \n\nFound Butterfly High in Unit 4, Ground Floor, Jet Airways, Godrej G Block, Near MCA, Bandra Kurla Complex, Mumbai rated Unit 4, Ground Floor, Jet Airways, Godrej G Block, Near MCA, Bandra Kurla Complex, Mumbai with avg cost 1500 \n\nFound BKC  DIVE in Ground Floor, Pinnacle Corporate Park, Opposite MTNL Office, Bandra Kurla Complex, Mumbai rated Ground Floor, Pinnacle Corporate Park, Opposite MTNL Office, Bandra Kurla Complex, Mumbai with avg cost 1100 \n\nFound Bayview Cafe in Hotel Harbour View, Kerawala Chamber, Opposite Radio Club, 25, J P Ramchandani Marg, Colaba, Mumbai rated Hotel Harbour View, Kerawala Chamber, Opposite Radio Club, 25, J P Ramchandani Marg, Colaba, Mumbai with avg cost 1200 \n\n"}
    - slot{"email_data": "<li> <b>The Fusion Kitchen</b> in <b>Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC colony, Borivali West, Mumbai</b> rated <b>4.7</b> with avg cost <b>1000</b> </li><li> <b>Yauatcha</b> in <b>Raheja Tower, Bandra Kurla Complex, Mumbai</b> rated <b>4.6</b> with avg cost <b>2800</b> </li><li> <b>Butterfly High</b> in <b>Unit 4, Ground Floor, Jet Airways, Godrej G Block, Near MCA, Bandra Kurla Complex, Mumbai</b> rated <b>4.3</b> with avg cost <b>1500</b> </li><li> <b>BKC  DIVE</b> in <b>Ground Floor, Pinnacle Corporate Park, Opposite MTNL Office, Bandra Kurla Complex, Mumbai</b> rated <b>4.2</b> with avg cost <b>1100</b> </li><li> <b>Bayview Cafe</b> in <b>Hotel Harbour View, Kerawala Chamber, Opposite Radio Club, 25, J P Ramchandani Marg, Colaba, Mumbai</b> rated <b>4.2</b> with avg cost <b>1200</b> </li><li> <b>Tea Villa Cafe</b> in <b>31, Opposite Globus, Hill Road, Bandra West</b> rated <b>4.1</b> with avg cost <b>1000</b> </li><li> <b>Tea Villa Cafe</b> in <b>28, Aaram Nagar 1, Opposite Dariya Mahal, Versova, Andheri West</b> rated <b>4.1</b> with avg cost <b>1000</b> </li><li> <b>By The Bae - Kitchen And Bar</b> in <b>9A - 9B, Aram Nagar 2, JP Road, Versova, Andheri West, Mumbai</b> rated <b>4.0</b> with avg cost <b>2500</b> </li><li> <b>Tea Villa Cafe</b> in <b>Shop 1& 2, Y-Building, Flower Valley, Opposite Viviana Mall,Eastern Express Highway, Majiwada, Thane West</b> rated <b>3.9</b> with avg cost <b>1000</b> </li><li> <b>Mumbai Vibe</b> in <b>Ganga Jamuna Block, 14th Road, Linking Road, Bandra West</b> rated <b>3.8</b> with avg cost <b>1000</b> </li>"}
    - slot{"valid_search": true}
    - utter_ask_mail_preference
* affirm
    - utter_ask_email
* send_mail{"email": "manojromina1997@gmail.com"}
    - slot{"email": "manojromina1997@gmail.com"}
    - action_send_mail
    - slot{"email": "manojromina1997@gmail.com"}
    - utter_confirm_mail
    - utter_thanks
    - utter_goodbye
    - action_reset_slot
    - reset_slots

## path with cuisine and price as initial params
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "price_range": "mid"}
    - slot{"cuisine": "South Indian"}
    - slot{"price_range": "mid"}
    - action_check_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_location
* restaurant_search{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - action_check_location
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - slot{"restaurant_data": "Found Original Vinayaka Mylari in 79, Nazarbad Main Road, Near Police Station, Doora, Mysore rated 79, Nazarbad Main Road, Near Police Station, Doora, Mysore with avg cost 300 \n\nFound Vinayaka Mylari in 79, Nazarbad Main Road, Near Police Station, Doora, Mysore rated 79, Nazarbad Main Road, Near Police Station, Doora, Mysore with avg cost 300 \n\nFound Hotel RRR in Sri Harsha Road, Lasker Mohalla, Near Mahatma Gandhi Square, Mandi Mohalla, Mysore rated Sri Harsha Road, Lasker Mohalla, Near Mahatma Gandhi Square, Mandi Mohalla, Mysore with avg cost 300 \n\nFound Highway 18 in 2766/12, 6th Main, 8th Cross Road, Vani Vilas Mohalla, Gokulam, Mysore rated 2766/12, 6th Main, 8th Cross Road, Vani Vilas Mohalla, Gokulam, Mysore with avg cost 400 \n\nFound Hyderabadi Biryani House in 299, Opposite To Water Tank, 2nd Stage, Vijay Nagar, Mysore rated 299, Opposite To Water Tank, 2nd Stage, Vijay Nagar, Mysore with avg cost 350 \n\n"}
    - slot{"email_data": "<li> <b>Original Vinayaka Mylari</b> in <b>79, Nazarbad Main Road, Near Police Station, Doora, Mysore</b> rated <b>4.2</b> with avg cost <b>300</b> </li><li> <b>Vinayaka Mylari</b> in <b>79, Nazarbad Main Road, Near Police Station, Doora, Mysore</b> rated <b>4.2</b> with avg cost <b>300</b> </li><li> <b>Hotel RRR</b> in <b>Sri Harsha Road, Lasker Mohalla, Near Mahatma Gandhi Square, Mandi Mohalla, Mysore</b> rated <b>4.2</b> with avg cost <b>300</b> </li><li> <b>Highway 18</b> in <b>2766/12, 6th Main, 8th Cross Road, Vani Vilas Mohalla, Gokulam, Mysore</b> rated <b>4.1</b> with avg cost <b>400</b> </li><li> <b>Hyderabadi Biryani House</b> in <b>299, Opposite To Water Tank, 2nd Stage, Vijay Nagar, Mysore</b> rated <b>4.1</b> with avg cost <b>350</b> </li><li> <b>Green Leaf</b> in <b>Opposite Reebok Showroom, Kalidasa Road, Vani Vilas Mohalla, Gokulam, Mysore</b> rated <b>4.0</b> with avg cost <b>400</b> </li><li> <b>Mezzaluna</b> in <b>First Floor, Kuvempu Trust Building, Near Chandrakala Hospital, New Kalidasa Road, Vijayanagar, Vijay Nagar, Mysore</b> rated <b>3.8</b> with avg cost <b>650</b> </li><li> <b>Pakva Lounge</b> in <b>Livin Corner, Temple Road, Vani Vilas Mohalla, Gokulam, Mysore</b> rated <b>3.7</b> with avg cost <b>650</b> </li><li> <b>By The Way</b> in <b>Next to Bhartat Cancer Hospital, Opposite Infosys Circle Ring Road, Vijay Nagar, Mysore</b> rated <b>3.6</b> with avg cost <b>650</b> </li><li> <b>Green Leaf</b> in <b>Opposite Reebok Showroom, Kalidasa Road, Vani Vilas Mohalla, Gokulam, Mysore</b> rated <b>3.5</b> with avg cost <b>400</b> </li>"}
    - slot{"valid_search": true}
    - utter_ask_mail_preference
* deny
    - utter_thanks
    - utter_goodbye
    - action_reset_slot
    - reset_slots

## path with location and price as initial params
* greet
    - utter_greet
* restaurant_search{"location": "Mysore", "price_range": "mid"}
    - slot{"location": "Mysore"}
    - slot{"price_range": "mid"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_check_cuisine
    - slot{"valid_cuisine": true}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - slot{"restaurant_data": "Found Original Vinayaka Mylari in 79, Nazarbad Main Road, Near Police Station, Doora, Mysore rated 79, Nazarbad Main Road, Near Police Station, Doora, Mysore with avg cost 300 \n\nFound Vinayaka Mylari in 79, Nazarbad Main Road, Near Police Station, Doora, Mysore rated 79, Nazarbad Main Road, Near Police Station, Doora, Mysore with avg cost 300 \n\nFound Hotel RRR in Sri Harsha Road, Lasker Mohalla, Near Mahatma Gandhi Square, Mandi Mohalla, Mysore rated Sri Harsha Road, Lasker Mohalla, Near Mahatma Gandhi Square, Mandi Mohalla, Mysore with avg cost 300 \n\nFound Highway 18 in 2766/12, 6th Main, 8th Cross Road, Vani Vilas Mohalla, Gokulam, Mysore rated 2766/12, 6th Main, 8th Cross Road, Vani Vilas Mohalla, Gokulam, Mysore with avg cost 400 \n\nFound Hyderabadi Biryani House in 299, Opposite To Water Tank, 2nd Stage, Vijay Nagar, Mysore rated 299, Opposite To Water Tank, 2nd Stage, Vijay Nagar, Mysore with avg cost 350 \n\n"}
    - slot{"email_data": "<li> <b>Original Vinayaka Mylari</b> in <b>79, Nazarbad Main Road, Near Police Station, Doora, Mysore</b> rated <b>4.2</b> with avg cost <b>300</b> </li><li> <b>Vinayaka Mylari</b> in <b>79, Nazarbad Main Road, Near Police Station, Doora, Mysore</b> rated <b>4.2</b> with avg cost <b>300</b> </li><li> <b>Hotel RRR</b> in <b>Sri Harsha Road, Lasker Mohalla, Near Mahatma Gandhi Square, Mandi Mohalla, Mysore</b> rated <b>4.2</b> with avg cost <b>300</b> </li><li> <b>Highway 18</b> in <b>2766/12, 6th Main, 8th Cross Road, Vani Vilas Mohalla, Gokulam, Mysore</b> rated <b>4.1</b> with avg cost <b>400</b> </li><li> <b>Hyderabadi Biryani House</b> in <b>299, Opposite To Water Tank, 2nd Stage, Vijay Nagar, Mysore</b> rated <b>4.1</b> with avg cost <b>350</b> </li><li> <b>Green Leaf</b> in <b>Opposite Reebok Showroom, Kalidasa Road, Vani Vilas Mohalla, Gokulam, Mysore</b> rated <b>4.0</b> with avg cost <b>400</b> </li><li> <b>Mezzaluna</b> in <b>First Floor, Kuvempu Trust Building, Near Chandrakala Hospital, New Kalidasa Road, Vijayanagar, Vijay Nagar, Mysore</b> rated <b>3.8</b> with avg cost <b>650</b> </li><li> <b>Pakva Lounge</b> in <b>Livin Corner, Temple Road, Vani Vilas Mohalla, Gokulam, Mysore</b> rated <b>3.7</b> with avg cost <b>650</b> </li><li> <b>By The Way</b> in <b>Next to Bhartat Cancer Hospital, Opposite Infosys Circle Ring Road, Vijay Nagar, Mysore</b> rated <b>3.6</b> with avg cost <b>650</b> </li><li> <b>Green Leaf</b> in <b>Opposite Reebok Showroom, Kalidasa Road, Vani Vilas Mohalla, Gokulam, Mysore</b> rated <b>3.5</b> with avg cost <b>400</b> </li>"}
    - slot{"valid_search": true}
    - utter_ask_mail_preference
* deny
    - utter_thanks
    - utter_goodbye
    - action_reset_slot
    - reset_slots

## path with location, cuisine and price as initial params
* greet
    - utter_greet
* restaurant_search{"location": "Mysore", "cuisine":"South Indian" ,"price_range": "mid"}
    - slot{"location": "Mysore"}
    - slot{"cuisine": "South Indian"}
    - slot{"price_range": "mid"}
    - action_check_location
    - slot{"valid_location": true}
    - action_check_cuisine
    - slot{"valid_cuisine": true}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - slot{"restaurant_data": "Found Original Vinayaka Mylari in 79, Nazarbad Main Road, Near Police Station, Doora, Mysore rated 79, Nazarbad Main Road, Near Police Station, Doora, Mysore with avg cost 300 \n\nFound Vinayaka Mylari in 79, Nazarbad Main Road, Near Police Station, Doora, Mysore rated 79, Nazarbad Main Road, Near Police Station, Doora, Mysore with avg cost 300 \n\nFound Hotel RRR in Sri Harsha Road, Lasker Mohalla, Near Mahatma Gandhi Square, Mandi Mohalla, Mysore rated Sri Harsha Road, Lasker Mohalla, Near Mahatma Gandhi Square, Mandi Mohalla, Mysore with avg cost 300 \n\nFound Highway 18 in 2766/12, 6th Main, 8th Cross Road, Vani Vilas Mohalla, Gokulam, Mysore rated 2766/12, 6th Main, 8th Cross Road, Vani Vilas Mohalla, Gokulam, Mysore with avg cost 400 \n\nFound Hyderabadi Biryani House in 299, Opposite To Water Tank, 2nd Stage, Vijay Nagar, Mysore rated 299, Opposite To Water Tank, 2nd Stage, Vijay Nagar, Mysore with avg cost 350 \n\n"}
    - slot{"email_data": "<li> <b>Original Vinayaka Mylari</b> in <b>79, Nazarbad Main Road, Near Police Station, Doora, Mysore</b> rated <b>4.2</b> with avg cost <b>300</b> </li><li> <b>Vinayaka Mylari</b> in <b>79, Nazarbad Main Road, Near Police Station, Doora, Mysore</b> rated <b>4.2</b> with avg cost <b>300</b> </li><li> <b>Hotel RRR</b> in <b>Sri Harsha Road, Lasker Mohalla, Near Mahatma Gandhi Square, Mandi Mohalla, Mysore</b> rated <b>4.2</b> with avg cost <b>300</b> </li><li> <b>Highway 18</b> in <b>2766/12, 6th Main, 8th Cross Road, Vani Vilas Mohalla, Gokulam, Mysore</b> rated <b>4.1</b> with avg cost <b>400</b> </li><li> <b>Hyderabadi Biryani House</b> in <b>299, Opposite To Water Tank, 2nd Stage, Vijay Nagar, Mysore</b> rated <b>4.1</b> with avg cost <b>350</b> </li><li> <b>Green Leaf</b> in <b>Opposite Reebok Showroom, Kalidasa Road, Vani Vilas Mohalla, Gokulam, Mysore</b> rated <b>4.0</b> with avg cost <b>400</b> </li><li> <b>Mezzaluna</b> in <b>First Floor, Kuvempu Trust Building, Near Chandrakala Hospital, New Kalidasa Road, Vijayanagar, Vijay Nagar, Mysore</b> rated <b>3.8</b> with avg cost <b>650</b> </li><li> <b>Pakva Lounge</b> in <b>Livin Corner, Temple Road, Vani Vilas Mohalla, Gokulam, Mysore</b> rated <b>3.7</b> with avg cost <b>650</b> </li><li> <b>By The Way</b> in <b>Next to Bhartat Cancer Hospital, Opposite Infosys Circle Ring Road, Vijay Nagar, Mysore</b> rated <b>3.6</b> with avg cost <b>650</b> </li><li> <b>Green Leaf</b> in <b>Opposite Reebok Showroom, Kalidasa Road, Vani Vilas Mohalla, Gokulam, Mysore</b> rated <b>3.5</b> with avg cost <b>400</b> </li>"}
    - slot{"valid_search": true}
    - utter_ask_mail_preference
* affirm
    - utter_ask_email
* send_mail{"email": "dev.itis.spk@gmail.com"}
    - slot{"email": "dev.itis.spk@gmail.com"}
    - action_send_mail
    - slot{"email": "dev.itis.spk@gmail.com"}
    - utter_confirm_mail
    - utter_thanks
    - utter_goodbye
    - action_reset_slot
    - reset_slots

## complete path all valid - with response and deny email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_price_range
* restaurant_search{"price_range": "high"}
    - slot{"price_range": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"restaurant_data": "Found The Fusion Kitchen in Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC colony, Borivali West, Mumbai rated Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC colony, Borivali West, Mumbai with avg cost 1000 \n\nFound Yauatcha in Raheja Tower, Bandra Kurla Complex, Mumbai rated Raheja Tower, Bandra Kurla Complex, Mumbai with avg cost 2800 \n\nFound Butterfly High in Unit 4, Ground Floor, Jet Airways, Godrej G Block, Near MCA, Bandra Kurla Complex, Mumbai rated Unit 4, Ground Floor, Jet Airways, Godrej G Block, Near MCA, Bandra Kurla Complex, Mumbai with avg cost 1500 \n\nFound BKC  DIVE in Ground Floor, Pinnacle Corporate Park, Opposite MTNL Office, Bandra Kurla Complex, Mumbai rated Ground Floor, Pinnacle Corporate Park, Opposite MTNL Office, Bandra Kurla Complex, Mumbai with avg cost 1100 \n\nFound Bayview Cafe in Hotel Harbour View, Kerawala Chamber, Opposite Radio Club, 25, J P Ramchandani Marg, Colaba, Mumbai rated Hotel Harbour View, Kerawala Chamber, Opposite Radio Club, 25, J P Ramchandani Marg, Colaba, Mumbai with avg cost 1200 \n\n"}
    - slot{"email_data": "<li> <b>The Fusion Kitchen</b> in <b>Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC colony, Borivali West, Mumbai</b> rated <b>4.7</b> with avg cost <b>1000</b> </li><li> <b>Yauatcha</b> in <b>Raheja Tower, Bandra Kurla Complex, Mumbai</b> rated <b>4.6</b> with avg cost <b>2800</b> </li><li> <b>Butterfly High</b> in <b>Unit 4, Ground Floor, Jet Airways, Godrej G Block, Near MCA, Bandra Kurla Complex, Mumbai</b> rated <b>4.3</b> with avg cost <b>1500</b> </li><li> <b>BKC  DIVE</b> in <b>Ground Floor, Pinnacle Corporate Park, Opposite MTNL Office, Bandra Kurla Complex, Mumbai</b> rated <b>4.2</b> with avg cost <b>1100</b> </li><li> <b>Bayview Cafe</b> in <b>Hotel Harbour View, Kerawala Chamber, Opposite Radio Club, 25, J P Ramchandani Marg, Colaba, Mumbai</b> rated <b>4.2</b> with avg cost <b>1200</b> </li><li> <b>Tea Villa Cafe</b> in <b>31, Opposite Globus, Hill Road, Bandra West</b> rated <b>4.1</b> with avg cost <b>1000</b> </li><li> <b>Tea Villa Cafe</b> in <b>28, Aaram Nagar 1, Opposite Dariya Mahal, Versova, Andheri West</b> rated <b>4.1</b> with avg cost <b>1000</b> </li><li> <b>By The Bae - Kitchen And Bar</b> in <b>9A - 9B, Aram Nagar 2, JP Road, Versova, Andheri West, Mumbai</b> rated <b>4.0</b> with avg cost <b>2500</b> </li><li> <b>Tea Villa Cafe</b> in <b>Shop 1& 2, Y-Building, Flower Valley, Opposite Viviana Mall,Eastern Express Highway, Majiwada, Thane West</b> rated <b>3.9</b> with avg cost <b>1000</b> </li><li> <b>Mumbai Vibe</b> in <b>Ganga Jamuna Block, 14th Road, Linking Road, Bandra West</b> rated <b>3.8</b> with avg cost <b>1000</b> </li>"}
    - slot{"valid_search": true}
    - utter_ask_mail_preference
* deny
    - utter_thanks
    - utter_goodbye
    - action_reset_slot
    - reset_slots
