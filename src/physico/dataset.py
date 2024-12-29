import json
import operator

import requests
from datasets import DatasetDict, load_dataset

__all__ = ["PhysiCoDataset"]

EVAL_ENDPOINT = "https://physico-benchmark-eval.shunchizhang-cs.workers.dev/api/eval-test"


class PhysiCoDataset(DatasetDict):
    def __init__(self, subset):
        assert subset in ("core", "associative")
        dataset = load_dataset("ShunchiZhang/PhysiCo", subset)
        super().__init__(dataset)
        self.subset = subset

    def _check_prediction_list(self, predictions, split):
        assert len(predictions) == len(self[split])
        for prediction, choices in zip(predictions, self[split]["choices"]):
            assert prediction in choices

    def eval_test(self, predictions):
        self._check_prediction_list(predictions, split="test")

        response = requests.post(
            EVAL_ENDPOINT,
            headers={"Content-Type": "application/json"},
            data=json.dumps({"key": self.subset, "list": predictions}),
        )

        if response.status_code == 200:
            assert response.json()["success"] == True
            return response.json()["accuracy"]
        else:
            raise Exception(
                f"Request failed with status code {response.status_code}: {response.text}"
            )

    def eval_dev(self, predictions):
        self._check_prediction_list(predictions, split="dev")

        if self.subset == "associative":
            raise ValueError("No dev set for associative")
        else:
            correct = sum(map(operator.eq, predictions, self["dev"]["label"]))
            return correct / len(predictions)
