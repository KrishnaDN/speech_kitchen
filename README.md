# speech_kitchen

This package contains utility functions for speech processing a

## Installation

```bash
$ pip install speech_kitchen
```

## Usage

```python
from speech_kitchen.speech_kitchen import count_words
from speech_kitchen.speech_kitchen import plot_words
import matplotlib.pyplot as plt
file_path = ”test.txt” # path to your file
counts = count_words(file_path)
fig = plot_words(counts, n=10)
plt.show()
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`speech_kitchen` was created by Krishna D N. It is licensed under the terms of the MIT license.

## Credits

`speech_kitchen` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
