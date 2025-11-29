import requests

url = "https://docs.google.com/forms/d/e/1FAIpQLSfuj3MeHaFYq8pndme4um0ED9SXqiE6zBHGCnjmTKl05af_dQ/formResponse"

form_data = {
    "entry.548524210": "TestUser",
    "entry.1491378407": "Sim",
    "entry.1494130951": "TestSocialName",
    "entry.477940854": "test@example.com",
    "entry.1924454278": "11999999999",
    "entry.2032571322": "2000-01-01",
    "entry.1452228749": "12345-678",
    "entry.1726215924": "Rua Teste, 123",
    "entry.1526279772": "Bairro Teste",
    "entry.1456950590": "Cidade Teste",
    "entry.1752434772": "Superior",
    "entry.824618440": "",
    "entry.466314194": "Outro",
    "entry.128321115": "OutroGenero",
    "entry.775361342": "Parda",
    "entry.1352902010": "Produção Cultural",
    "entry.126170279": "",
    "entry.276516650": "1 ano",
    "entry.1635954645": "Trabalho teste",
    "entry.1502285931": "site.com",
    "entry.1364402133": "facebook.com/user",
    "entry.1150245970": "Não",
    "entry.554285331": "",
    "entry.858060365": "Sim",
    "entry.1110992509": "Sim",
    "entry.30914039": "Sim",
    "entry.1778170175": "Li e concordo com a Política de Privacidade",
    "fvv": "1",
    "fbzx": "6653372783592602984",
    "pageHistory": "0",
    # Sentinels
    "entry.1491378407_sentinel": "",
    "entry.1352902010_sentinel": "",
    "entry.1150245970_sentinel": "",
    "entry.858060365_sentinel": "",
    "entry.1110992509_sentinel": "",
    "entry.30914039_sentinel": "",
    "entry.1778170175_sentinel": ""
}

try:
    response = requests.post(url, data=form_data)
    response.encoding = 'utf-8'
    
    with open("python_response.html", "w", encoding="utf-8") as f:
        f.write(response.text)
        
    if "Sua resposta foi registrada" in response.text:
        print("SUCCESS: Form submitted successfully!")
    else:
        print("FAILURE: Submission rejected.")
        if "A pergunta mudou" in response.text:
            print("Reason: 'A pergunta mudou' error found.")
        if "data-validation-failed" in response.text:
            print("Reason: Data validation failed.")
            
except Exception as e:
    print(f"Error: {e}")
