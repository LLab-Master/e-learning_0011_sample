import logging

# フォーマットを定義
formatter = '%(levelname)s : %(asctime)s : %(message)s'

# ログレベルを DEBUG に変更
logging.basicConfig(filename='sample7_5.log', level=logging.DEBUG, format=formatter)

logging.info('info')