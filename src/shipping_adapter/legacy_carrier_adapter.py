
from .shipping_quote_provider import ShippingQuoteProvider
from .legacy_carrier import LegacyCarrier


class LegacyCarrierAdapter(ShippingQuoteProvider):
    KG_TO_LB = 2.20462

    def __init__(self, carrier: LegacyCarrier):
        self.carrier = carrier

    def quote(self, destination: str, weight_kg: float) -> float:
        # Convert kilograms to pounds
        weight_lb = weight_kg * self.KG_TO_LB

        # Translate the Target request to the legacy interface
        return self.carrier.get_price(
            postal_code=destination,
            weight_lb=weight_lb
        )
