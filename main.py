import argparse
from parser import parse_all_pages
from storage import save_to_excel


def main():
    parser = argparse.ArgumentParser(
        description="Web scraper for collecting product data")

    parser.add_argument("--url", type=str, required=True,
                        help="URL of category page")
    parser.add_argument("--pages", type=int, default=1,
                        help="Number of pages to parse")
    parser.add_argument("--output", type=str,
                        default="products.xlsx", help="Output Excel file")

    args = parser.parse_args()

    products = parse_all_pages(args.url, max_pages=args.pages)

    save_to_excel(products, args.output)

    print(f"Done. Total products: {len(products)}")


if __name__ == "__main__":
    main()
