import pytest

from shipping_adapter.checkout import Checkout
from shipping_adapter.legacy_carrier import LegacyCarrier
from shipping_adapter.legacy_carrier_adapter import LegacyCarrierAdapter
from shipping_adapter.shipping_quote_provider import ShippingQuoteProvider


def test_checkout_uses_legacy_carrier_through_target_interface():
    # Arrange: create the legacy carrier and its adapter
    adapter = LegacyCarrierAdapter(LegacyCarrier())
    checkout = Checkout(adapter)

    # Act: request a shipping quote using kilograms
    result = checkout.shipping_quote("45100", 2.0)

    # Assert: the adapter implements the expected interface
    assert isinstance(adapter, ShippingQuoteProvider)

    # Assert: Checkout receives the correctly converted quote
    assert result == pytest.approx(11.51)
