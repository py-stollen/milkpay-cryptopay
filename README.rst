
#################
milkpay-cryptopay
#################

**milkpay** is a set of lightweight crypto payment system SDKs.

Installation
------------

..  code-block:: bash

    pip install -U milkpay-cryptopay

Simple example
--------------

.. code-block:: python

    import asyncio
    import logging
    import uuid
    from typing import Final

    from milkpay.cryptopay import Cryptopay
    from milkpay.cryptopay.enums import Asset

    API_TOKEN: Final[str] = "API_TOKEN_HERE"


    async def main() -> None:
        logging.basicConfig(level=logging.DEBUG)
        async with Cryptopay(
            api_token=API_TOKEN,
            production=False,
            force_detailed_errors=True,
        ) as cryptopay:
            logging.info(
                await cryptopay.transfer(
                    user_id=5945468457,
                    asset=Asset.USDT,
                    amount=1.1,
                    spend_id=int(uuid.uuid4()),
                )
            )


    if __name__ == "__main__":
        asyncio.run(main())

