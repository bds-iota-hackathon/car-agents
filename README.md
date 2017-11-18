# PlugInBaby
### The Decentralized E-Car Charge Station Marketplace

#### Idea

+ Advertise private E-car charging stations to public 
+ P2P settlement on using IOTA
+ Decentralize E-car charing provides --> incentivize quicker adoption

First PoC for charging stations using IOTA: https://medium.com/@harmvandenbrink/how-elaadnl-built-a-poc-charge-station-running-fully-on-iota-and-iota-only-e16ed4c4d4d5


Payment approach: trust in IOT device OR pay per minute in advance (worst case: loose payment for a minute)






### iotawrapper functions

##### IotaWrapper class

```
iota = IotaWrapper(url, seed)
```

- url: url for the test server
- seed: seed you got for your wallet

##### Connecting

```
iota.connect()
```

- returns: node_info

##### Send transfer

```
iota.send_transfer(transfers, inputs, depth, min_weight_magnitude)
```

- transfers: array of transfers (check main.py)
- inputs: information about your wallets etc (optional)
- depth: default value 3
- min_weight_magnitude: default value 16
- returns: bundle dictionary
