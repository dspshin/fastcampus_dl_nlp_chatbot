from solver import Solver
from data_loader import get_loader
from configs import get_config
from pprint import pprint

if __name__ == '__main__':
    config = get_config()
    pprint(vars(config))

    data_loader = get_loader(
        batch_size=config.batch_size,
        max_size=config.vocab_size,
        is_train=True,
        data_dir=config.data_dir)

    solver = Solver(config, data_loader)
    solver.build(is_train=True)
    solver.train()
