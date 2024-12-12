def logger_set():
    global logger
    if logger is not None:
        return logger

    logger = logging.getLogger("ロガーさん")
    logger.setLevel(logging.WARNING)

    if not logger.handlers:
        file_handler = logging.FileHandler("sales_analysis.log", encoding= "utf-8")
        file_handler.setLevel(logging.WARNING)
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.WARNING)
        console_formatter = logging.Formatter("%(levelname)-9s  %(asctime)s [%(filename)s:%(lineno)d] %(message)s")
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
        return logger

def import_csv():
    try:
        logger = logger_set()
        if logger is None:
            raise ValueError

        df = pd.read_csv("sales_data.csv")
        logger.info("CSVファイルの読み込みに成功しました")
        return  df
    except FileNotFoundError:
        logging.warning("CSVファイルが見つかりませんでした")
        raise
    except Exception:
        logging.error("ファイル読み込み時にエラー発生しました")
        raise
    except ValueError as e:
        logging.error("ロガー作成に失敗しました")
        raise Exception from e


def analysis(df):
    try:
        df["date"] = pd.to_datetime(df["date"])
        df["purchase_amount"] = df["amount"] * df["quantity"]

        #月ごとの合計売上金額
        month_sales = df.groupby(df["date"].dt.strftime('%Y-%m'))["purchase_amount"].sum().round(1)
        #商品ごとの売上個数
        product_quantity = df.groupby("product_name")["quantity"].sum().round(1)