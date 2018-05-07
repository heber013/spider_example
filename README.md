# GetOffers
This is a Scrapy project example to scrape offers from a website.


## Extracted data

This project extracts offers, combined with the respective author names and tags.
The extracted data looks like this sample:

    {
        'description': 'TV',
        'price': 1.50,
        'old_price': 2.50,
        'discount': '40% OFF'
    }


## Spiders

This project contains one spider and you can list it using the `list`
command:

    $ scrapy list
    get_offers


## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl get_offers

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl get_offers -o offers.json
