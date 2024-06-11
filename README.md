# Contact
My services are for hire. Contact me if you need me to build your pump.fun trading bot or algo.

Telegram: OxEight33n (L0rd~~0xEight33n)

## Pump.fun Trading Bot using PumpPortal API

This repository contains a simple Python script to buy and sell meme tokens on the Pump.fun platform using the unofficial PumpPortal API. The script allows users to programmatically execute trades by sending HTTP requests to the PumpPortal API.

## Prerequisites

Before using this script, ensure you have the following:

- Python 3.x installed on your machine.
- An API key for PumpPortal. You can obtain this by signing up on the PumpPortal website.
- The `requests` library installed. You can install it using pip:
  ```sh
  pip install requests
  ```

## Getting Started

1. **Clone the Repository**


2. **Update the Script**

   Open the script file `trade_bot.py` and update the following variables with your own details:
   ```python
   api_key = 'your-wallet-api-key'
   action = 'buy'  # or 'sell'
   mint = 'pump-token-mint-address'
   amount = 0.001
   denominated_in_sol = 'true'  # or 'false'
   slippage = 10
   priority_fee = 0.005
   ```


### Parameters

- `api_key`: Your PumpPortal API key.
- `action`: The action to perform (`"buy"` or `"sell"`).
- `mint`: The contract address of the token you want to trade.
- `amount`: The amount of SOL or tokens to trade.
- `denominated_in_sol`: `"true"` if `amount` is in SOL, `"false"` if `amount` is in tokens.
- `slippage`: The percent slippage allowed.
- `priority_fee`: The amount to use as a priority fee or Jito tip.
- `pool`: (Optional) The exchange to trade on. Default is `"pump"`, other option is `"raydium"`.

### Response Handling

The script logs the full response from the PumpPortal API for debugging purposes. If the request is successful, it returns the transaction signature or errors. If an error occurs, it prints the HTTP status code and response content.

## Error Handling

The script includes basic error handling to manage and log any issues that occur during the execution of the trade.

## Contributing

If you have any suggestions or improvements, feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

By following these instructions, you should be able to execute trades on the Pump.fun platform programmatically using the provided Python script. If you encounter any issues, please refer to the PumpPortal API documentation or open an issue in this repository.
