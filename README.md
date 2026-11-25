[![Make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![Rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/firlifirrizqi/vending-pickup-line-makefun/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![Reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/firlifirrizqi/vending-pickup-line-makefun/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

# One Line, One Minute: The Vending Machine Pickup Line Contest

One-line entry for the [Make.fun bounty](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee) of the same name: a single pickup line, 200 characters at most, as if a vending machine were flirting with a passing human.

## The line

> If I get stuck, it's not the chips — it's you. One coin in and my whole row lights up.

The machine speaks in the first person and flirts through its own world: getting stuck, the chips, a coin, a row lighting up. The classic stuck-snack moment is turned into the crush itself — deadpan, specific, charming rather than creepy.

## How it works

`main.py` writes that single line (86 characters, within the 200-character limit) to `/output/entry.txt`, then re-reads the file and verifies it is byte-identical to the line, 1–200 characters, and not only whitespace. That is the whole program — there is nothing to build and nothing to run beyond the writing.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
