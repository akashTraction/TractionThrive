from cumulusci.tasks.salesforce import BaseSalesforceApiTask

class NgmSqlReset(BaseSalesforceApiTask):
    def _run_task(self):

        # Resets nmg-load filed back to it's original state based on a template file
        with open("datasets/nmg-load-template.sql") as f:
            with open("datasets/nmg-load.sql", "w") as f1:
                for line in f:
                    f1.write(line)

        # Reset nmg-extrat to empty
        open('datasets/nmg-extract.sql', 'w').close()