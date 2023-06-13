import datetime


class BaseDate:

    @staticmethod
    def date_now(delta=0, date_format: str = "%Y-%m-%d") -> str:
        now = datetime.datetime.now()
        return str((now + datetime.timedelta(days=delta)).strftime(date_format))
