import pandas as pd
from sqlalchemy import create_engine, text

def insert_db():
    # 엑셀 파일 경로
    company_xlsx_file_path = (
        r"C:/N02-1st-4Team-main/data/company.xlsx"
    )
    df_company = pd.read_excel(company_xlsx_file_path, engine="openpyxl")


    year2019_xlsx_file_path = (
        r"C:/N02-1st-4Team-main/data/2019.xlsx"
    )
    df_year2019 = pd.read_excel(year2019_xlsx_file_path, engine="openpyxl")


    year2020_xlsx_file_path = (
        r"C:/N02-1st-4Team-main/data/2020.xlsx"
    )
    df_year2020 = pd.read_excel(year2020_xlsx_file_path, engine="openpyxl")


    year2021_xlsx_file_path = (
        r"C:/N02-1st-4Team-main/data/2021.xlsx"
    )
    df_year2021 = pd.read_excel(year2021_xlsx_file_path, engine="openpyxl")


    year2022_xlsx_file_path = (
        r"C:/N02-1st-4Team-main/data/2022.xlsx"
    )
    df_year2022 = pd.read_excel(year2022_xlsx_file_path, engine="openpyxl")


    year2023_xlsx_file_path = (
        r"C:/N02-1st-4Team-main/data/2023.xlsx"
    )
    df_year2023 = pd.read_excel(year2023_xlsx_file_path, engine="openpyxl")


    faq_data_xlsx_file_path = (
        r"C:/N02-1st-4Team-main/data/faq.xlsx"
    )
    df_faq = pd.read_excel(faq_data_xlsx_file_path, engine="openpyxl")

    car_total_xlsx_file_path = (
        r"C:/N02-1st-4Team-main/data/car_total.xlsx"
    )
    df_car = pd.read_excel(car_total_xlsx_file_path, engine="openpyxl")


    # 필요 없는 'Unnamed: 0' 열 제거
    if "Unnamed: 0" in df_company.columns:
        df_company = df_company.drop(columns=["Unnamed: 0"])

    if "Unnamed: 0" in df_year2019.columns:
        df_year2019 = df_year2019.drop(columns=["Unnamed: 0"])

    if "Unnamed: 0" in df_year2020.columns:
        df_year2020 = df_year2020.drop(columns=["Unnamed: 0"])

    if "Unnamed: 0" in df_year2021.columns:
        df_year2021 = df_year2021.drop(columns=["Unnamed: 0"])

    if "Unnamed: 0" in df_year2022.columns:
        df_year2022 = df_year2022.drop(columns=["Unnamed: 0"])

    if "Unnamed: 0" in df_year2023.columns:
        df_year2023 = df_year2023.drop(columns=["Unnamed: 0"])
    
    if "Unnamed: 0" in df_faq.columns:
        df_faq = df_faq.drop(columns=["Unnamed: 0"])

    if "Unnamed: 0" in df_car.columns:
        df_car = df_car.drop(columns=["Unnamed: 0"])


    # MySQL connection 세팅
    db_user = "root"
    db_password = "2718"
    db_host = "192.168.0.121"
    db_port = "3306"
    db_name = "prj01"


    # SQLAlchemy 엔진 생성 (데이터베이스 생성 전용)
    create_engine_without_db = create_engine(
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}"
    )

    # 데이터베이스 생성
    with create_engine_without_db.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name};"))

    # SQLAlchemy 엔진 생성
    engine = create_engine(
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    
    try:
        with engine.connect() as conn:
            conn.execute(text(f"USE prj01;"))


            # 중복되지 않도록 테이블 DROP하기
            conn.execute((text)(f"DROP TABLE IF EXISTS year2019;"))
            conn.execute((text)(f"DROP TABLE IF EXISTS year2020;"))
            conn.execute((text)(f"DROP TABLE IF EXISTS year2021;"))
            conn.execute((text)(f"DROP TABLE IF EXISTS year2022;"))
            conn.execute((text)(f"DROP TABLE IF EXISTS year2023;"))
            conn.execute((text)(f"DROP TABLE IF EXISTS faq;"))
            conn.execute((text)(f"DROP TABLE IF EXISTS company;"))
            conn.execute((text)(f"DROP TABLE IF EXISTS car;"))


            create_company_table = """
            CREATE TABLE IF NOT EXISTS company(
                id int AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(20) NOT NULL
            );
            """
            create_year2019_table = """
            CREATE TABLE IF NOT EXISTS year2019(
                id int AUTO_INCREMENT PRIMARY KEY,
                revenue bigint,
                profit bigint,
                debt_ratio float,
                FOREIGN KEY (id) REFERENCES company(id)
            );
            """

            create_year2020_table = """
            CREATE TABLE IF NOT EXISTS year2020(
                id int AUTO_INCREMENT PRIMARY KEY,
                revenue bigint,
                profit bigint,
                debt_ratio float,
                FOREIGN KEY (id) REFERENCES company(id)
            );
            """

            create_year2021_table = """
            CREATE TABLE IF NOT EXISTS year2021(
                id int AUTO_INCREMENT PRIMARY KEY,
                revenue bigint,
                profit bigint,
                debt_ratio float,
                FOREIGN KEY (id) REFERENCES company(id)
            );
            """

            create_year2022_table = """
            CREATE TABLE IF NOT EXISTS year2022(
                id int AUTO_INCREMENT PRIMARY KEY,
                revenue bigint,
                profit bigint,
                debt_ratio float,
                FOREIGN KEY (id) REFERENCES company(id)
            );
            """

            create_year2023_table = """
            CREATE TABLE IF NOT EXISTS year2023(
                id int AUTO_INCREMENT PRIMARY KEY,
                revenue bigint,
                profit bigint,
                debt_ratio float,
                FOREIGN KEY (id) REFERENCES company(id)
            );
            """

            create_faq_table = """
            CREATE TABLE IF NOT EXISTS faq(
            id int AUTO_INCREMENT PRIMARY KEY,
            question VARCHAR(300),
            answer TEXT
            );
            """

            create_car_table = """
            CREATE TABLE IF NOT EXISTS car(
            year int not null,
            total bigint
            );
            """

            # 테이블 만들기
            conn.execute(text(create_company_table))
            conn.execute(text(create_year2019_table))
            conn.execute(text(create_year2020_table))
            conn.execute(text(create_year2021_table))
            conn.execute(text(create_year2022_table))
            conn.execute(text(create_year2023_table))
            conn.execute(text(create_faq_table))
            conn.execute(text(create_car_table))


            # Dataframe.to_sql을 사용해서 데이터 넣기
            df_company.to_sql('company', con=engine, index=False, if_exists="append", method="multi")
            df_year2019.to_sql('year2019', con=engine, index=False, if_exists="append", method="multi")
            df_year2020.to_sql('year2020', con=engine, index=False, if_exists="append", method="multi")
            df_year2021.to_sql('year2021', con=engine, index=False, if_exists="append", method="multi")
            df_year2022.to_sql('year2022', con=engine, index=False, if_exists="append", method="multi")
            df_year2023.to_sql('year2023', con=engine, index=False, if_exists="append", method="multi")
            df_faq.to_sql('faq', con=engine, index=False, if_exists="append", method="multi")
            df_car.to_sql('car', con=engine, index=False, if_exists="append", method="multi")
    
    except Exception as e:
        print(f"Error: {e}")

    # Connection 닫기
    engine.dispose()
insert_db()