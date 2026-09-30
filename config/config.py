
# Vendor globale in cui vengono storicizzare informazioni relative ai singoli vendor
class Vendor:
    def __init__(self, nome: str, link: str, token: int = 1000000):
        self.nomeVendor = nome
        self.link = link
        self.token = token

openAi = Vendor("OpenAi", "https://developers.openai.com/api/docs/pricing?latest-pricing=standard")
antrophic = Vendor("Claude", "https://platform.claude.com/docs/en/about-claude/pricing")