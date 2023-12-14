#!/usr/bin/env python
# coding: utf-8

from google.cloud import enterpriseknowledgegraph as ekg

project_id = '<your_project>'
dataset_id = 'Chapter9'

client = ekg.EnterpriseKnowledgeGraphServiceClient()
parent = client.common_location_path(project=project_id, location='global')

input_config = ekg.InputConfig(
        bigquery_input_configs=[
            ekg.BigQueryInputConfig(
                bigquery_table=client.table_path(
                    project=project_id, dataset=dataset_id, table='mari'
                ),
                gcs_uri='gs://<your_bucket>/handsonentityresolution/Chapter9SchemaMari',
            ),
             ekg.BigQueryInputConfig(
                bigquery_table=client.table_path(
                    project=project_id, dataset=dataset_id, table='basic'
                ),
                gcs_uri='gs://<your_bucket>/handsonentityresolution/Chapter9SchemaBasic',
            )   
        ],
        entity_type=ekg.InputConfig.EntityType.ORGANIZATION,
    )

output_config = ekg.OutputConfig(
        bigquery_dataset=client.dataset_path(project=project_id, dataset=dataset_id)
    )

entity_reconciliation_job = ekg.EntityReconciliationJob(
        input_config=input_config, output_config=output_config
)

request = ekg.CreateEntityReconciliationJobRequest(
        parent=parent, entity_reconciliation_job=entity_reconciliation_job
)

response = client.create_entity_reconciliation_job(request=request)

print(f"Job: {response.name}")
