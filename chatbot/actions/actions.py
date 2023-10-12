from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from actions import actionsDb

class ValidateOrder1(Action):
    def name(self) -> Text:
        return "action_product"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product = tracker.get_slot("product")
        products = ["Phone", "TV", "Camera", "Air conditioner", "Computer", "Mouse", "Keyboard", "Headphones"]
        if product in products:
            dispatcher.utter_message(text=f"Yes, we have {product} in stock.")
        else:
            dispatcher.utter_message(text=f"Sorry, we don't have {product} in stock.")
        # db1 = actionsDb.ProductDB()
        # goods = db1.getProduct(product)
        # if goods is not None:
        #     dispatcher.utter_message(text=f"{product} in stock.")
        # else:
        #     dispatcher.utter_message(text=f"{product} out of stock.")
        return []


class ValidateOrder2(Action):
    def name(self) -> Text:
        return "action_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        order = tracker.get_slot("order")
        orders = ["10001", "10002", "10003", "10004", "10005", "10006", "10007"]
        if order == "10001":
            dispatcher.utter_message(text=f"Your order is pending, the delivery date is 2024-10-01.")
        elif order == "10002":
            dispatcher.utter_message(text=f"Your order is delivered.")
        elif order == "10003":
            dispatcher.utter_message(text=f"Your order is undelivered, the delivery date is 2024-10-04.")
        elif order == "10004":
            dispatcher.utter_message(text=f"Your order is unshipped, the delivery date is 2024-10-05.")
        elif order == "10005":
            dispatcher.utter_message(text=f"Your order is undelivered, the delivery date is 2024-10-06.")
        elif order == "10006":
            dispatcher.utter_message(text=f"Your order is unshipped, the delivery date is 2024-10-07.")
        elif order == "10007":
            dispatcher.utter_message(text=f"Your order is unshipped, the delivery date is 2024-10-08.")
        else:
            dispatcher.utter_message(text=f"Your order is not exist.")
        # db2 = actionsDb.OrdersDB()
        # data = db2.getOrder(order)[4]
        # status = db2.getOrder(order)[3]
        # if status == "Pending":
        #     dispatcher.utter_message(text=f"Your order is pending, the delivery date is {data}")
        # elif status == "Delivered":
        #     dispatcher.utter_message(text=f"Your order is delivered.")
        # elif status == "Undelivered":
        #     dispatcher.utter_message(text=f"Your order is undelivered, the delivery date is {data}")
        # elif status == "Unshipped":
        #     dispatcher.utter_message(text=f"Your order is unshipped, the delivery date is {data}")
        # else:
        #     dispatcher.utter_message(text=f"Your order is not exist.")
        return []

class ValidateOrder3(Action):
    def name(self) -> Text:
        return "action_order_delay_enquiry"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        order = tracker.get_slot("order")
        orders = ["10001", "10004", "10003"]
        if order == "10001":
            dispatcher.utter_message(text=f"Your order is delayed, the reason is Traffic jam, the delivery date is "
                                          f"2024-10-02.")
        elif order == "10004":
            dispatcher.utter_message(text=f"Your order is delayed, the reason is Contract timeout, the delivery date "
                                          f"is 2024-10-06.")
        elif order == "10003":
            dispatcher.utter_message(text=f"Your order is delayed, the reason is Unknown, the delivery date is "
                                          f"2024-10-04.")
        else:
            dispatcher.utter_message(text=f"Your order is not delayed.")
        # db3 = actionsDb.delayDB()
        # delay = db3.getDelay(order)
        # if delay is not None:
        #     dispatcher.utter_message(text=f"Your order is delayed, the reason is {db3.getDelay(order)[2]}.")
        # else:
        #     dispatcher.utter_message(text=f"Your order is not delayed.")
        return []

