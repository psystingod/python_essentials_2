def btc_usd(btc_amount, ref_price):
    try:
        if isinstance(btc_amount, float) or isinstance(btc_amount, int):
            return btc_amount * ref_price;
        raise ValueError("Ingresa una cantidad correcta de Bitcoin o Satoshis");
    except ValueError:
        print(ValueError.args);

print(btc_usd(0.0050));
btc_usd("0056");
