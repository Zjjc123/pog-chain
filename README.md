# Pog Chain

A simple python block chain created by Jay Pog

## Implementation
- SHA 256 Hashing
- Leading 0s proof of work

## Example
### Blockchain Changes
```python
blockchain.add_new_transaction("transaction 1")
blockchain.add_block(Block(1, "fake transaction", time.time(), "dcc0c1d14ebb81949ec55f2d5e34dac902295101bcc3d17d70c7a1fb7d35460b"), "0000e156e2174c758494d05d793a68a7fcf5e9611e416b4b5f40a71062aa83ba")
blockchain.mine()

blockchain.add_new_transaction("transaction 2")
blockchain.mine()

blockchain.add_new_transaction("POG CHAIN TO THE MOON!!!!")
blockchain.mine()
```
### Resulted Block Chain

```
--------------------
Block:          0
Transactions:   []
Timestamp:      1615880349.357578
Hash:           fc1ae383d7b40253827dc0ca5a44f2c2d81b7857bc4b3226cf227b2350582c52
Previous Hash:  0
--------------------
Block:          1
Transactions:   ['transaction 1']
Timestamp:      1615880349.357578
Hash:           0000ddb32b106956d98d9a333306d611cd861c6356bea1a04f26ed0f4638801b
Previous Hash:  fc1ae383d7b40253827dc0ca5a44f2c2d81b7857bc4b3226cf227b2350582c52
--------------------
Block:          2
Transactions:   ['transaction 2']
Timestamp:      1615880349.584629
Hash:           000010eec9702f1e8f6fc9da7313fb17a859e2bb22d682bb74d44d88ca94dd9f
Previous Hash:  0000ddb32b106956d98d9a333306d611cd861c6356bea1a04f26ed0f4638801b
--------------------
Block:          3
Transactions:   ['POG CHAIN TO THE MOON!!!!']
Timestamp:      1615880349.7086565
Hash:           0000d0247ffdae66dc5d200976c51bc527605c2212c98f2d22bbdec3eed33dd4
Previous Hash:  000010eec9702f1e8f6fc9da7313fb17a859e2bb22d682bb74d44d88ca94dd9f
--------------------
```