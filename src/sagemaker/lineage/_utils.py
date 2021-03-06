# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
"""SageMaker lineage utility methods."""
from __future__ import absolute_import
from importlib import import_module
from sagemaker.lineage import association


def _disassociate(source_arn=None, destination_arn=None, sagemaker_session=None):
    """Remove the association.

    Remove incoming association when source_arn is provided, remove outgoing association when
    destination_arn is provided.
    """
    association_summaries = association.Association.list(
        source_arn=source_arn, destination_arn=destination_arn, sagemaker_session=sagemaker_session
    )

    for association_summary in association_summaries:

        curr_association = association.Association(
            sagemaker_session=sagemaker_session,
            source_arn=association_summary.source_arn,
            destination_arn=association_summary.destination_arn,
        )
        curr_association.delete()


def get_module(module_name):
    """Import a module.

    Args:
        module_name (str): N_utiame of the module to importt.

    Returns:
        [obj]: The imported module
    """
    return import_module(module_name)
