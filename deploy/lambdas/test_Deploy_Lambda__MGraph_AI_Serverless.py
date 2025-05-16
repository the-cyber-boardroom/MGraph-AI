from unittest                                import TestCase
from mgraph_ai.utils.Version                 import version__mgraph_ai
from deploy.lambdas.Deploy_Lambda__MGraph_AI import Deploy_Lambda__MGraph_AI


class test_Deploy_Lambda__MGraph_AI_Serverless(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.deploy_lambda = Deploy_Lambda__MGraph_AI()

    def test_deploy_lambda(self):
        with self.deploy_lambda as _:
            result = _.lambda_deploy()
            assert result == {'body': 'Hello from Docker Lambda!', 'statusCode': 200}

    def test_ecr_image_uri(self):
        account_id = "180929110226"
        target_region = "eu-west-2"
        with self.deploy_lambda as _:
            ecr_image_uri = _.ecr_image_uri()       # todo: change values below to aws_config.account_id() and aws_config.region_name()
            assert ecr_image_uri == f'{account_id}.dkr.ecr.{target_region}.amazonaws.com/osbot_flows:{version__mgraph_ai}'
