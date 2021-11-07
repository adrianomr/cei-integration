from cei_crawler import CeiCrawler    


class CeiService:

    async def fetchData(username:str, password:str):
        crawler = CeiCrawler(username=username, password=password)
    
        assets_extract = await crawler.get_assets_extract()
        print(assets_extract) # seus ativos negociados no CEI

        await crawler.close()
        
        return assets_extract

