# ----------------------------------------------------------------
# manipulando datas
import pytz
import datetime

# criando data e hora
d = datetime.datetime(2024, 7, 19, 13, 45)
print(d)  # 2024-97-19 13:45:00

# Adicionando uma semana
d = d + datetime.timedelta(days=10)
print(d)


# ----------------------------------------------------------------
# Convertendo String para datetime
data = datetime.datetime.now()

# Formatando daa e hora
print(data.strftime("%d/%m/%Y %H:%M"))

# Convertendo string para datetime
date_string = "20/07/2023 15:30"
data = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(data)

# ----------------------------------------------------------------
# Lidando com fuso horário

# Criando datetime com timezone
d = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
print(d)
