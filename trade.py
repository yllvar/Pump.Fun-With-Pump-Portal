import requests

def execute_trade(api_key, action, mint, amount, denominated_in_sol, slippage, priority_fee, pool='pump'):
    url = f"https://pumpportal.fun/api/trade?api-key={api_key}"
    data = {
        "action": action,             # "buy" or "sell"
        "mint": mint,                 # contract address of the token you want to trade
        "amount": amount,             # amount of SOL or tokens to trade
        "denominatedInSol": denominated_in_sol,  # "true" if amount is amount of SOL, "false" if amount is number of tokens
        "slippage": slippage,         # percent slippage allowed
        "priorityFee": priority_fee,  # amount to use as Jito tip or priority fee
        "pool": pool                  # exchange to trade on. "pump" or "raydium"
    }
    
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        response_json = response.json()
        # Log the entire response for debugging
        print("Full response:", response_json)
        return response_json  # Tx signature or error(s)
    else:
        # Print the response content for debugging
        print("HTTP Error:", response.status_code)
        print("Response content:", response.content)
        response.raise_for_status()

# Example usage
api_key = 'your-wallet-api-key'
action = 'buy'  # or 'sell'
mint = 'pump-token-mint-address'
amount = 0.001
denominated_in_sol = 'true'  # or 'false'
slippage = 10
priority_fee = 0.005

try:
    trade_response = execute_trade(api_key, action, mint, amount, denominated_in_sol, slippage, priority_fee)
    print(trade_response)
except Exception as e:
    print(f"An error occurred: {e}")
