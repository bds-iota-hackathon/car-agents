# Car Agents

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
