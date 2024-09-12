import os

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL","postgresql://book_catalog_0sml_user:9T5Pxbby74ZAowwwHWibKE8gkHbcuww9@dpg-crhaf7l6l47c73c5512g-a.singapore-postgres.render.com/book_catalog_0sml")

settings = Settings()
