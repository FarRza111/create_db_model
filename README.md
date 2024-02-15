#### Steps #####

1. flask shell
2. fariz = Customer(id=123438783743,firstname= 'Fariz',lastname= 'Rzayev',age = 32,customer_id='FarizCustomer12332',workplace='Bank', private_info = 'Married and living in Estonia') 
3. db.session.add(fariz)
4. db.session.commit()

#### Checking Class ####
6. Csutomer.query.filter_by(firstname='Fariz').all()
