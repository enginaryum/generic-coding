sample_query = {
  'count': -1,
  "page": 0,
  "where": [
    {
      "type": "equal",
      "column": "firstName",
      "value": "muhammet"
    },
    {
      "type": "equal",
      "column": "lastName",
      "value": "enginar"
    },
    {
      "type": "equal",
      "column": "age",
      "value": 24
    },
    {
      "type": "equal",
      "column": "homeTown",
      "value": "Konya"
    },
    {
      "type": "equal",
      "column": "phone",
      "value": "5054187393"
    }
  ]
}


sample_request = {
  'firstName': 'Muhammet',
  'lastName': 'Enginar',
  'age': 24,
  'homeTown': 'Konya',
  'phone': '5054187393'
}


# def queryBuilder(**kwargs):
#   return {
#     'count': -1,
#     'page': 0,
#     'where':
#       map(lambda (x, y): {
#         "type": "equal",
#         "column": x,
#         "value": y
#       }, kwargs.iteritems())
#   }

# print queryBuilder(firstName="muhammet", lastName="enginar", age=24, hometown="Konya")

# TO-DO:  handle different keys than expected in request