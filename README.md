
# Legacy Shipping Quote Adapter

## Description

This project implements the Adapter Design Pattern to integrate
an existing legacy shipping carrier with a modern Checkout system.

The goal is to make two incompatible interfaces work together
without modifying the client, the target contract, or the legacy carrier.

## Design Pattern: Adapter

The system includes four main components:

- Client: Checkout
- Target: ShippingQuoteProvider
- Adaptee: LegacyCarrier
- Adapter: LegacyCarrierAdapter

### Problem

Checkout expects the following interface:

    quote(destination, weight_kg)

However, LegacyCarrier provides:

    get_price(postal_code, weight_lb)

The interfaces are incompatible because they use different method
names, parameter names, and weight units.

### Solution

LegacyCarrierAdapter implements ShippingQuoteProvider and wraps
an instance of LegacyCarrier.

The Adapter translates:

- quote() into get_price()
- destination into postal_code
- weight_kg into weight_lb

The conversion is:

    1 kg = 2.20462 lb

This translation happens exclusively inside the Adapter.

## Project Structure

    src/
      shipping_adapter/
        __init__.py
        checkout.py
        shipping_quote_provider.py
        legacy_carrier.py
        legacy_carrier_adapter.py

    tests/
      test_checkout_legacy_adapter.py
      test_existing_system.py

    README.md
    requirements.txt
    pyproject.toml

## Installation

Create a virtual environment:

    python -m venv .venv

Activate it on Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

Or on macOS/Linux:

    source .venv/bin/activate

Install dependencies:

    python -m pip install -r requirements.txt

## Running Tests

Run all tests:

    python -m pytest -q

Run the focused integration test:

    python -m pytest tests/test_checkout_legacy_adapter.py -v

## Test Explanation

The test proves that Checkout can use LegacyCarrier through
the ShippingQuoteProvider interface.

Test scenario:

    Destination: 45100
    Weight: 2.0 kg

Conversion:

    2.0 * 2.20462 = 4.40924 lb

Legacy carrier calculation:

    6.0 + (4.40924 * 1.25) = 11.51155

Expected rounded result:

    11.51

The test verifies that the Adapter implements the Target
interface and that Checkout receives the expected result.

## Design Explanation

### Why use the Adapter Pattern?

The Adapter Pattern allows an existing object to be reused
even when its interface does not match what the client expects.

Instead of modifying Checkout or LegacyCarrier, we introduce
a separate class responsible for translating their interfaces.

### Why is Checkout unchanged?

Checkout already depends on ShippingQuoteProvider.

Since LegacyCarrierAdapter implements that contract, Checkout
can use it without knowing anything about the legacy API.

### What complexity cost does the Adapter introduce?

The Adapter introduces an additional abstraction and class
that developers must understand and maintain.

If the legacy API changes, the Adapter may also require
updates and additional testing.

However, this cost is justified because it reduces coupling
and keeps the existing components unchanged.

## Requirements Checklist

- [x] Correct Target / Adapter / Adaptee structure
- [x] Adapter uses composition
- [x] Checkout remains unchanged
- [x] ShippingQuoteProvider remains unchanged
- [x] LegacyCarrier remains unchanged
- [x] Kilograms are converted to pounds in the Adapter
- [x] Focused integration test included
- [x] Complexity cost explained

## Conclusion

The Adapter Pattern solves an interface compatibility problem
by placing translation logic inside a dedicated class.

Checkout continues using its original interface, while the
legacy carrier remains reusable without modification.

This implementation demonstrates the Object Adapter approach
using composition and a stable Target contract.
