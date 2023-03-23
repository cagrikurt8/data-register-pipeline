from azureml.core import Workspace, Dataset, Run, Datastore
import argparse


def main():
    ws = Workspace(subscription_id="bc387bcb-42e5-4ef4-9d60-8c36a83b5778",
                   resource_group="AI-ML_RG",
                   workspace_name="aml-workspace")

    ds = Datastore.get(ws, 'analyticsblob')
    dataset = Dataset.Tabular.from_delimited_files(path=(ds, 'data/salesdata.csv'),
                                                   header='ALL_FILES_HAVE_SAME_HEADERS')
    dataset.register(workspace=ws, 
                    name='sample-data',
                    create_new_version=True)


if __name__ == "__main__":
    main()
