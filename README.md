## Contributors

[Mert Kosan](https://github.com/mertkosan) and [Zexi Huang](https://github.com/zexihuang)

## Introduction
This fork is a modification to scale **Squad 2.0** dataset using a **RTX 2070 MaxQ (8GB) GPU**.
We inspired from [renatoviolin](https://github.com/renatoviolin/xlnet) who forked and modified slightly as well
from the [original repository](https://github.com/zihangdai/xlnet).

We reduce batch size from 8 to 4. We do sensitivity analysis on different sequence length, partial
fine-tuning and output layer structure by optimizing them under limited computational power and memory.

Please check our [slides] (deliverables/slides.pdf) (based on XLNet's original authors' NeurIPS'19 slides) and [report] (deliverables/report.pdf)
about our contribution and explanation of the experiments we have conducted.

## How to Run

Please follow the instruction in [original repository](https://github.com/zihangdai/xlnet) to able to run this
code. You will have to create folders and download some data, and preprocess that data using prepro_squad.sh.
Then you will be able to run using gpu_squad_base.sh. We updated with optimized parameters inside of the script.

