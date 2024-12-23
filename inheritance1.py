class OTTSubscription:
    def __init__(self,subscription_id, plan, total_payment):
        self.id = subscription_id
        self.plan = plan
        self.total_payment = total_payment


    def subscribe(self):
        print(f"Subscriber with {self.id} id subscribed to the {self.plan} plan")

    def unsubscribe(self):
        print(f"Subscriber with {self.id} id Unsubscribed to the {self.plan} plan")
    
