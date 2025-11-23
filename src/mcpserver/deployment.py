from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("crypto")

@mcp.tool()
def get_crypto_currency_price(crypto: str) -> str:
    """
    Get the current price of a cryptocurrency.
    Args:
        crypto (str): The symbol of the cryptocurrency (e.g., 'bitcoin', 'ethereum', etc.).
    """
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price"
        params = {
            'ids': crypto.lower(),
            'vs_currencies': 'usd'
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        price = data.get(crypto.lower(), {}).get("usd")
        if price is not None:
            return f"The current price of {crypto.upper()} is ${price:.2f} USD."
        else:
            return f"Could not retrieve the price for {crypto.upper()}. Please check the cryptocurrency symbol."
    except Exception as e:
        return f"An error occurred while fetching the price: {str(e)}"



if __name__ == "__main__":
    mcp.run()
