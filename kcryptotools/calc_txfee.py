# Caculate tx fe
# This is done quite primitively. Only takes into account fee per kilobyte and does not consider priority.
import cryptoconfig

def calc_txfee(tx,crypto):
    tx_fee_per_kilobyte=cryptoconfig.TX_FEE_PER_KILOBYTE[crypto.lower()]
    kilo_bytes=len(tx)/2/1000 + 1 
    fee=tx_fee_per_kilobyte*kilo_bytes
    return fee
