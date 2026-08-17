"""
===============================================================================
Employee Analytics & Business Intelligence System

Main Application

IBM Data Analyst Professional Certificate (IBM DAPC)

Author : Varghese
Version : 2.0
===============================================================================
"""

import time

from analytics import (
    load_dataset,
    dataset_overview,
    generate_reports,
    save_csv_reports,
)

from reports import (
    export_excel,
    generate_markdown_report,
    generate_project_log,
    list_generated_reports,
)

from charts import (
    generate_all_charts,
)

from dashboard import (
    display_dashboard,
)

from utils import (
    project_banner,
    execution_timer,
    print_error,
)

from config import (
    PROJECT_NAME,
    VERSION,
)

# =============================================================================
# Main Function
# =============================================================================


def main():
    """
    Main controller of the Employee Analytics System.
    """

    start_time = time.time()

    try:

        # ---------------------------------------------------------------------
        # Project Banner
        # ---------------------------------------------------------------------

        project_banner(PROJECT_NAME, VERSION)

        # ---------------------------------------------------------------------
        # Step 1 : Load Dataset
        # ---------------------------------------------------------------------

        df = load_dataset()

        if df is None:

            return

        # ---------------------------------------------------------------------
        # Step 2 : Dataset Overview
        # ---------------------------------------------------------------------

        dataset_overview(df)

        # ---------------------------------------------------------------------
        # Step 3 : Analytics
        # ---------------------------------------------------------------------

        reports = generate_reports(df)

        # ---------------------------------------------------------------------
        # Step 4 : CSV Reports
        # ---------------------------------------------------------------------

        save_csv_reports(reports)

        # ---------------------------------------------------------------------
        # Step 5 : Excel Workbook
        # ---------------------------------------------------------------------

        export_excel(reports)

        # ---------------------------------------------------------------------
        # Step 6 : Charts
        # ---------------------------------------------------------------------

        generate_all_charts(df)

        # ---------------------------------------------------------------------
        # Step 7 : Executive Report
        # ---------------------------------------------------------------------

        generate_markdown_report(df)

        # ---------------------------------------------------------------------
        # Step 8 : Project Log
        # ---------------------------------------------------------------------

        generate_project_log()

        # ---------------------------------------------------------------------
        # Step 9 : Display Dashboard
        # ---------------------------------------------------------------------

        display_dashboard(df)

        # ---------------------------------------------------------------------
        # Step 10 : Display Generated Reports
        # ---------------------------------------------------------------------

        list_generated_reports()

    except Exception as error:

        print_error(f"Unexpected Error : {error}")

    finally:

        execution_timer(start_time)


# =============================================================================
# Program Entry
# =============================================================================

if __name__ == "__main__":

    main()
