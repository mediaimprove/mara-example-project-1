from mara_schema.entity import Entity
from mara_schema.attribute import Type

order_entity = Entity(
    name='Order',
    description='Valid orders for which an invoice was created',
    schema_name='ec_dim')

order_entity.add_attribute(
    name='Order ID',
    description='The ID of the order in the backend',
    column_name='order_id',
    type=Type.ID,
    high_cardinality=True)

order_entity.add_attribute(
    name='Order date',
    description='The date when the order was placed (stored in the backend)',
    column_name='order_date',
    important_field=True,
    type=Type.DATE)

order_entity.add_attribute(
    name='Order status',
    description='The current status of the order (created, approved, shipped, etc)',
    column_name='order_status',
    type=Type.ENUM)

order_entity.add_attribute(
    name='Payment approval date',
    description='The date when the customer\'s payment was approved by the seller',
    column_name='payment_approval_date',
    type=Type.DATE)

order_entity.add_attribute(
    name='Delivery date',
    description='The date when the order was delivered to the customer',
    column_name='delivery_date',
    important_field=True,
    type=Type.DATE)

order_entity.add_attribute(
    name='Delivery time in days',
    description='The number of days from placing the order to delivery to the customer',
    column_name='delivery_time_in_days',
    type=Type.DURATION)

order_entity.add_attribute(
    name='Days since first order',
    description='The number of days from the first order of the customer to the placement of this order',
    column_name='days_since_first_order',
    type=Type.DURATION)

from .customer import customer_entity

order_entity.link_entity(target_entity=customer_entity,
                         description='The customer who placed the order')
