from environs import Env

env = Env()
env.read_env()

SHOP_ID = env.str("SHOP_ID")
SECRET_KEY = env.str("SECRET_KEY")
PAYWAY = env.str("PAYWAY")
