# Zyxel VMG8825-T50 Supervisor Keygen

In this project contains the following functions implemented in Python 3:

| Function name                                     | Validity |
|:------------------------------------------------- |:--------:|
| `zcfgBeCommonGenKeyBySerialNum_CBT              ` |    ❓    |
| `zcfgBeCommonGenKeyBySerialNumMethod2           ` |    ✅    |
| `zcfgBeCommonGenKeyBySerialNumMethod3           ` |    ✅    |
| `zcfgBeCommonGenKeyBySerialNumConfigLength(1)   ` |    ❓    |
| `zcfgBeCommonGenKeyBySerialNumConfigLength(2)   ` |    ❌    |
| `zcfgBeCommonGenKeyBySerialNumConfigLength(3)   ` |    ❓    |
| `zcfgBeCommonGenKeyBySerialNumConfigLengthOld(1)` |    ❌    |
| `zcfgBeCommonGenKeyBySerialNumConfigLengthOld(2)` |    ❌    |
| `zcfgBeCommonGenKeyBySerialNumConfigLengthOld(3)` |    ❌    |

A validity of ✅ denotes that the function has been confirmed to produce the expected result, while a denotation of ❌ means that it confirmably does not produce the correct output. The validity ❓ simply means that it has not been confirmed or denied whether or not it produces the expected result.

## Usage

```bash
./main.py S123Y12345678
```

If a particular function has your interest then you can run only that function by specifying it with the `--function` or `-f` argument.

Usually, `zcfgBeCommonGenKeyBySerialNumMethod2` or `zcfgBeCommonGenKeyBySerialNumMethod3` to generate passwords for the `supervisor` user, dependening on the router and its version.
It should also be noted, that some versions have passwords that are longer, or shorter than what the abovementioned functions produce, but the contents should be the same.

## Tests

Some of the functions might not function as expected. The folder `./tests` contains some expected results, produced by the actual functions from `libzcfg_be.so` for reference. The script `./test.py` runs the functions in this repository against the expected results.
