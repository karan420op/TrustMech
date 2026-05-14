import sys
from scraper import scrape_project
from analyzer import analyze_project
from report import save_report

def main():
    if len(sys.argv) < 2:
        print("TrustMech — Crypto Project Due Diligence Tool")
        print("\nUsage:")
        print("  python main.py <project-url>")
        print("\nExamples:")
        print("  python main.py https://x.com/TrustMech")
        print("  python main.py https://coingecko.com/en/coins/bitcoin")
        print("  python main.py https://myproject.xyz")
        sys.exit(0)

    url = sys.argv[1]

    print(f"\nTrustMech analyzing: {url}\n")
    print("Step 1/3: Scraping project data...")
    project_data = scrape_project(url)

    print("Step 2/3: Running analysis...")
    report = analyze_project(project_data)

    print("Step 3/3: Generating report...")
    filename = save_report(report)

    print(f"\n{'='*50}")
    print(f"Project: {report['project_name']}")
    print(f"Trust Score: {report['trust_score']}/100")
    print(f"Summary: {report['summary']}")
    print(f"\nRed Flags: {len(report['red_flags'])}")
    for flag in report['red_flags']:
        print(f"  - {flag}")
    print(f"\nGreen Flags: {len(report['green_flags'])}")
    for flag in report['green_flags']:
        print(f"  + {flag}")
    print(f"\nFull report saved to: {filename}")
    print(f"{'='*50}\n")

if name == "main":
    main()
