import json
from pathlib import Path

import requests


BASE_URL = "https://baubook.io"


def load_credentials(path="credentials.json"):
    """
    Return (user, password) from credentials.json.

    Expected credentials.json:

    {
        "user": "your_username",
        "api_key": "your_password_or_api_key"
    }
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Credentials file not found: {path}")

    with path.open("r", encoding="utf-8") as f:
        d = json.load(f)
        return (
            d.get("user", "no field 'user' found"),
            d.get("api_key", "no field 'api_key' found"),
        )


def create_baubook_session(user, password, base_url=BASE_URL):
    """
    Create an authenticated baubook session.

    Endpoint
    --------
    POST /@login

    Example
    -------
    >>> u, pw = load_credentials()
    >>> session = create_baubook_session(u, pw)
    """
    base_url = base_url.rstrip("/")

    login_response = requests.post(
        f"{base_url}/@login",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
        json={
            "login": user,
            "password": password,
        },
        timeout=30,
    )

    if login_response.status_code == 401:
        raise PermissionError(
            "Login failed with 401. Check username/password or API access permission."
        )

    login_response.raise_for_status()

    token = login_response.json()["token"]

    session = requests.Session()
    session.headers.update({
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
    })

    return session


def get_products(session, b_size=150, b_start=0, base_url=BASE_URL):
    """
    Fetch baubook products. (https://baubook.io/documentation_v3/products.html)

    Endpoint
    --------
    GET /@bb_v3_products

    Query parameters
    ----------------
    b_size:
        Number of products per batch.
    b_start:
        Start offset for pagination.

    Example
    -------
    >>> u, pw = load_credentials()
    >>> session = create_baubook_session(u, pw)
    >>> products = get_products(session, b_size=10)
    >>> products["items"][0]
    """
    response = session.get(
        f"{base_url.rstrip('/')}/@bb_v3_products",
        params={
            "b_size": b_size,
            "b_start": b_start,
        },
        timeout=30,
    )

    response.raise_for_status()
    return response.json()


def get_categories(session, base_url=BASE_URL):
    """
    Fetch baubook product categories. (https://baubook.io/documentation_v3/categories.html)

    Endpoint
    --------
    GET /@bb_v3_categories

    Example
    -------
    >>> u, pw = load_credentials()
    >>> session = create_baubook_session(u, pw)
    >>> categories = get_categories(session)
    >>> categories.keys()
    """
    response = session.get(
        f"{base_url.rstrip('/')}/@bb_v3_categories",
        timeout=30,
    )

    response.raise_for_status()
    return response.json()


def get_reference_values(session, reference_type, reference_id=None, base_url=BASE_URL):
    """
    Fetch baubook reference values. (https://baubook.io/documentation_v3/referencevalues.html)

    Endpoints
    ---------
    GET /@bb_v3_referencevalues/{reference_type}

    GET /@bb_v3_referencevalues/{reference_type}/{reference_id}

    Examples
    --------
    Fetch all reference values of one type:

    >>> u, pw = load_credentials()
    >>> session = create_baubook_session(u, pw)
    >>> zg_values = get_reference_values(session, "ZG")

    Fetch one specific reference value:

    >>> zg_value = get_reference_values(session, "ZG", "2142740773")
    """
    base_url = base_url.rstrip("/")

    if reference_id is None:
        url = f"{base_url}/@bb_v3_referencevalues/{reference_type}"
    else:
        url = f"{base_url}/@bb_v3_referencevalues/{reference_type}/{reference_id}"

    response = session.get(url, timeout=30)

    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    u, pw = load_credentials()
    session = create_baubook_session(u, pw)

    print(session)

    products = get_products(session, b_size=5)
    print("products:", len(products.get("items", [])))

    categories = get_categories(session)
    print("categories:", len(categories))

    zg_values = get_reference_values(session, "ZG")
    print("ZG reference values:", len(zg_values.get("items", {})))