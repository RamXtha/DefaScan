import argparse
import datetime
def parse_args():
    current_date = datetime.datetime.now()

    parser = argparse.ArgumentParser(
        description="DefaScan: Defacement Scanner and Alert",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )


    parser.add_argument(
            "--min",
            # dest="minimum_delay_between_dork_searches_in_seconds",
            # action="store",
            required=False,
            type=int,
            default=20,
            help="Minimum delay (in seconds) between a Google dork search.  Default: 37"
        )
    parser.add_argument(
            "--max",
            # dest="maximum_delay_between_dork_searches_in_seconds",
            required=False,
            type=int,
            default=40,
            help="Maximum delay (in seconds) between a Google dork search.  Default: 60"
        )
    parser.add_argument(
            "--sender",
            help="Sender's email",
            dest="sender_mail"


         )
    parser.add_argument(
        "--admin",
        help="Admin's email you want to send the scan report to",
        dest="admin_mail"


         )
    parser.add_argument(
            "--pass",
            help="Sender's password for email",
            dest="sender_pass"
        ) 
    parser.add_argument(
            "--perm",
            "-p",
            # dest="maximum_delay_between_dork_searches_in_seconds",
            # required=False,
            # type=int,
            # default=60,
            action='store_true',
            help="Permission to run scanner without APIs.",
            dest="noapi_permission"
        )
    parser.add_argument(
            "--noperm",
            # dest="maximum_delay_between_dork_searches_in_seconds",
            # required=False,
            # type=int,
            # default=60,
            action='store_true',
            help="Permission to run scanner without APIs.",
            dest="negative_noapi_permission"
        )
    parser.add_argument(
            "--query",
            "-q",
            # dest="maximum_delay_between_dork_searches_in_seconds",
            # required=False,
            # type=int,
            default='site:.np intitle:"hacked by"',
            help="query search for Google dork",
            dest="query"
        )
    parser.add_argument(
            "-n",
            default=1,
            help="number of search queries for scraping",
            dest="number_of_pages"

        )

     
    # parser.add_argument('--name', type=str, required=True)


    args= parser.parse_args()


    if args.min < 0:
        print(f'[{current_date.strftime("%H:%M:%S")}] [Error] Minimum delay between dork searches (--min) must be greater than 0')
        quit()

    if args.max < 0:
        print(f'[{current_date.strftime("%H:%M:%S")}] [Error] maximum_delay_between_dork_searches_in_seconds (--max) must be greater than 0')
        quit()
    if args.max <= args.min:
        print(
            f"[{current_date.strftime('%H:%M:%S')}] [Error] maximum_delay_between_dork_searches_in_seconds (--max) must be greater than "
            "minimum_delay_between_dork_searches_in_seconds (--min)"
            )
        quit()
    return args