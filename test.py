{
  'fulfilling_store.id': {
    '$in': [6662]
  },
  '$or': [{
      'bags.bag_status': {
        '$all': [
        {
          '$elemMatch': {
            'status': 'bag_invoiced'
          },
        },
        {
          '$elemMatch': {
            'status': {
              '$in': ['cancelled_fynd', 'cancelled_customer']
            },
            'updated_at': {
              '$gte': new Date('2020-09-10T00:00:00.000Z'),
              '$lt': new Date('2020-09-10T23:59:59.000Z')
            }
          }
        }
        ]
      }
    },
    {
      'shipment_status.status': {
        '$in': ['rto_bag_delivered', 'return_bag_delivered']
      },
      'shipment_status.created_at': {
        '$gte': new Date('2020-09-10T00:00:00.000Z'),
        '$lt': new Date('2020-09-10T23:59:59.000Z')
      },
      'lock_status': false
    }
  ]
}