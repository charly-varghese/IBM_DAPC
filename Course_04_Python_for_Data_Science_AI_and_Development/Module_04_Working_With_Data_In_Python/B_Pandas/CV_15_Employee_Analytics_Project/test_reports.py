from analytics import *
from reports import *

df = load_dataset()

reports = generate_reports(df)

save_csv_reports(reports)

export_excel(reports)

generate_markdown_report(df)

generate_project_log()

list_generated_reports()