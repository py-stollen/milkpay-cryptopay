from stollen.exceptions import StollenAPIError


class CryptopayAPIError(StollenAPIError):
    pass


class CryptopayBadRequestError(CryptopayAPIError):
    pass


class CryptopayUnauthorizedError(CryptopayAPIError):
    pass


class CryptopayForbiddenError(CryptopayAPIError):
    pass


class CryptopayNotFoundError(CryptopayAPIError):
    pass
