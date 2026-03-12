from self_architecture.architecture_scanner import scan_architecture
from self_architecture.module_evaluator import evaluate_module
from self_architecture.architecture_optimizer import optimize_architecture


def self_architecture():

    modules = scan_architecture()

    report = []

    for module in modules:

        result = evaluate_module(module)

        action = optimize_architecture(result)

        report.append({

            "module":module,
            "score":result["score"],
            "action":action

        })

    return report
