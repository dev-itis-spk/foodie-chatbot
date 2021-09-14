## intent:affirm
- yes
- yep
- yup
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- thank you
- fine, thanks
- that's great
- this is good
- sounds great
- sounds good
- perfect
- that's perfect
- this would do

## intent:deny
- no
- nope
- negative
- nah
- no need
- dont need
- not required
- no, thanks
- no thanks
- nope thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one
- catch you later
- bye for now
- see you

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hi there
- hello friend
- Heya
- Whats up my bot
- hey bruh
- hello it is me again
- whats up
- yoo supp
- Hi
- Yo bud
- supp bud
- Hey
- Hey bud
- Hey friend
- Hola
- hola amigo

## intent:restaurant_search
- i m looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price_range", "value": "mid"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- can you book a table in [rome](location) in a [mid](price_range) price range with [british](cuisine) food
- can you book a table in [rome](location) in a [low](price_range) price range with [british](cuisine) food
- can you book a table in [rome](location) in a [high](price_range) price range with [british](cuisine) food
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurant in [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- I’m hungry. Looking out for some good restaurants
- [Mumbai](location)
- Can you suggest some good restaurants in [kolkata](location)
- Can you suggest some good restaurants in [Kolkata](location)
- I want to find a [high](price_range) price range restaurant in [Mumbai](location) for chiense food
- I want to find a [mid](price_range) price range restaurants in [Mumbai](location) for [chinese](cuisine) foods
- I want to find a [high](price_range) price range restaurants in [Mumbai](location) for [chinese](cuisine) food
- show restaurants
- [bombay]{"entity": "location", "value": "Mumbai"}
- [mid](price_range)
- show good restaurants
- [Bombay]{"entity": "location", "value": "Mumbai"}
- [high](price_range)
- show restaurants in [rishikesh](location)
- show in [bangalore]{"entity": "location", "value": "Bangalore"}
- show some [thai](cuisine) restaurants
- [south indian]{"entity": "cuisine", "value": "South Indian"}
- [mysuru]{"entity": "location", "value": "Mysore"}
- show [south indian](cuisine) restaurants in [mysuru]{"entity": "location", "value": "Mysore"}
- show [north indian]{"entity": "cuisine", "value": "North Indian"} restaurants in [noida](location)
- [low](price_range)
- show [mid](price_range) range restaurants in [delhi]{"entity": "location", "value": "New Delhi"}
- [Italian](cuisine)
- [<300]{"entity": "price_range", "value": "low"}
- [>700]{"entity": "price_range", "value": "high"}
- [300-700]{"entity": "price_range", "value": "mid"}
- show me some [luxury](price_range) restaurants
- can you book a table in [rome](location) in a [lower]{"entity": "price_range", "value": "low"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- can you book a table in [rome](location) in a [higher]{"entity": "price_range", "value": "high"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people

## intent:send_mail
- can u mail me the information to [abc@abc.com](email)?
- can u mail to [test@tes.com](email)?
- please send me an email
- please share this with me
- send me an email
- yeah send me
- yes email me
- yes send me please
- share some more restaurant names with me
- share this over mail
- share this information with me over email
- can u mail me at [test-123.456@dom.123.co.in](email)?
- email address - test.some@gmail.co.in. Mail this list.
- email me at email-[123@domina.com](email)
- mail me [emial@domain.io](email)
- please mail me the list to [123-email@domain.co.in](email)
- please send me the list to [123@domain.net](email)
- send this to [abc-email@abc.com](email)
- yes send me at [123-email@domain.co](email)
- yeah email me at [123-email@domain.co](email)
- [abc-email@abc.com](email)
- [email-abc_123@abc.com.edu](email)
- this is my email address - [email-abc_123@abc.com.edu](email). send me an email.
- can u share this information over email?
- can u send me an email?
- mail me the list
- yes, please
- yeah please
- yeah send me at [dev.itis.spk@gmail.com](email)

## synonym:4
- four

## synonym:low
- <300
- 299
- less than 300
- lower
- low range
- low price

## synonym:mid
- 300-700
- moderate
- medium price

## synonym:high
- >700
- higher
- luxurious
- luxury

## synonym:Allahabad
- allahabad
- prayagraj
- Prayagraj

## synonym:American
- american

## synonym:Bangalore
- bangalore
- Bengaluru
- bengaluru
- bngalore
- b'luru
- Bangalor

## synonym:Chandigarh
- chandigarh
- Chandighar
- chandighar

## synonym:Chennai
- chennai
- madras
- Madras

## synonym:Chinese
- chines
- chinese
- Chines
- chini
- Chini

## synonym:Coimbatore
- coimbatore
- Kovai
- kovai

## synonym:Delhi
- New Delhi

## synonym:Gurgaon
- gurugaon
- Gurugram
- gurugram

## synonym:Hyderabad
- hyderabad
- Secunderabad
- secunderabad

## synonym:Italian
- italian
- Italy
- italy

## synonym:Kochi
- kochi
- cochin
- Cochin

## synonym:Kolkata
- Kolkatta
- Calcutta
- kolkatta
- calcutta
- calcuta
- kolkata

## synonym:Mangalore
- Mangaluru
- mangaluru
- mangalore

## synonym:Mexican
- mexican
- Mex
- mex
- Mexicano
- mexicano

## synonym:Mumbai
- bombay
- Bombay
- mumbai

## synonym:Mysore
- mysuru
- Mysuru
- mysore

## synonym:Nashik
- nashik
- Nasik
- nasik

## synonym:New Delhi
- Delhi
- Dilli
- dilli
- Delhi NCR
- delhi ncr
- new delhi
- new Delhi
- newdelhi
- delhi

## synonym:North Indian
- north indian
- northindian
- North Indian
- north Indian
- North indian

## synonym:Puducherry
- Pondicherry
- pondicherry
- puducherry
- Pondy
- pondy
- pondi
- Pondi

## synonym:South Indian
- south indian
- southindian
- South Indian
- south Indian
- South indian

## synonym:Varanasi
- varanasi
- Kashi
- Kasi
- kasi
- kashi
- Banaras
- banaras

## synonym:Vizag
- visakhapatnam
- Visakhapatnam
- vizag

## synonym:chinese
- Chinese

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg
- veg

## regex:email
- ^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}
