from splent_framework.seeders.BaseSeeder import BaseSeeder

from splent_io.splent_feature_tools.models import Tool

TOOLS = [
    {
        "name": "FLAMAPY",
        "summary": "FLAMA is a Python-based AAFM (Automated Analysis of Feature "
        "Models) framework that takes into consideration previous AAFM tool "
        "designs and enables multi-solver and multi-metamodel support for the "
        "integration of AAFM tooling on the Python ecosystem.",
        "website": "https://www.flamapy.org/",
        "github": "https://github.com/flamapy/",
        "status": "active",
    },
    {
        "name": "FLAMAPY CONF",
        "summary": "Web application providing tools to perform Interactive "
        "Configuration of Feature Models defined in UVL and other formats. It "
        "delegates execution of operations to a web worker that runs Flamapy via "
        "Pyodide (Python in the browser).",
        "website": "https://www.flamapy.org/",
        "github": "https://github.com/flamapy/flamapy.conf",
        "status": "active",
    },
    {
        "name": "FLAMAPY IDE",
        "summary": "Web application providing tools to perform Automated Analysis "
        "of Feature Models defined in UVL (Universal Variability Language). It "
        "delegates execution to a web worker running Flamapy compiled to "
        "WebAssembly/Pyodide in the browser.",
        "website": "https://www.flamapy.org/",
        "github": "https://github.com/flamapy/flamapy-ide",
        "status": "active",
    },
    {
        "name": "UVL",
        "summary": "UVL (Universal Variability Language) is a textual and formal "
        "language for modeling variability in software product lines. It allows "
        "features, relationships (mandatory, optional, alternative) and "
        "constraints to be described in a clear, readable and automatically "
        "processable way.",
        "website": "https://universal-variability-language.github.io/",
        "github": "https://github.com/universal-variability-language",
        "status": "active",
    },
    {
        "name": "UVLHUB",
        "summary": "Web platform for managing, publishing and exploring UVL models "
        "based on Open Science principles. A centralized repository where "
        "researchers and developers can upload, version, search and analyze "
        "variability models, supporting reuse, reproducibility and research.",
        "website": "https://www.uvlhub.io/",
        "github": "https://github.com/diverso-lab/uvlhub",
        "status": "active",
    },
    {
        "name": "PERFORMANCE TRACKER",
        "summary": "Tool designed to track and compare different aspects of OSS "
        "repositories to assess their quality regarding performance metrics.",
        "website": "",
        "github": "https://github.com/diverso-lab/performance-tracker",
        "status": "active",
    },
    {
        "name": "TRANSFORMO",
        "summary": "Framework to perform migrations between relational databases "
        "using software product lines, obtaining custom SQL scripts compatible "
        "with each other.",
        "website": "",
        "github": "https://github.com/diverso-lab/transformo",
        "status": "prototype",
    },
    {
        "name": "DEPEX",
        "summary": "Tool to automate the extraction of the dependency graph "
        "attributed to a software project along with its vulnerabilities, to "
        "facilitate subsequent automatic analysis in search of security risks.",
        "website": "",
        "github": "https://github.com/GermanMT/depex",
        "status": "prototype",
    },
    {
        "name": "WEBSPL",
        "summary": "Provides an interface for website modeling through different "
        "technologies, implementing a software product line of WordPress sites "
        "using an internal feature model. It delegates to FLAMA for feature model "
        "analysis.",
        "website": "",
        "github": "https://github.com/diverso-lab/webspl",
        "status": "prototype",
    },
    {
        "name": "FM FACT LABEL",
        "summary": "Online web-based application that builds a feature-model "
        "characterization and generates its visualization as a fact label. Offers "
        "a web form to upload the FM and its metadata; currently UVL and "
        "FeatureIDE formats are supported.",
        "website": "",
        "github": "https://github.com/jmhorcas/fm_characterization",
        "status": "prototype",
    },
    {
        "name": "SPL VISUALIZATION",
        "summary": "An implementation of a software product line (SPL) for the "
        "visualization design process (VDP) that allows generating customized "
        "visualizations following the best design practices in data "
        "visualization.",
        "website": "",
        "github": "https://github.com/diverso-lab/spl_visualization_design",
        "status": "prototype",
    },
    {
        "name": "FAMA-FW",
        "summary": "FaMa-FW is a framework for automated analysis of feature models "
        "integrating some of the most commonly used logic representations and "
        "solvers proposed in the literature (BDD, SAT and CSP solvers). FaMa is "
        "the first tool integrating different solvers for automated AAFM.",
        "website": "",
        "github": "https://github.com/diverso-lab/FaMa",
        "status": "other",
    },
    {
        "name": "BETTY",
        "summary": "BeTTy is an extensible and highly configurable framework "
        "supporting BEnchmarking and TesTing on the analYses of feature models. "
        "Written in Java and distributed as a jar file, facilitating integration "
        "into external projects.",
        "website": "",
        "github": "https://github.com/isa-group/BeTTy",
        "status": "other",
    },
]


def _slugify(name: str) -> str:
    return "-".join(name.lower().replace("/", " ").split())


class ToolsSeeder(BaseSeeder):
    def run(self):
        self.seed(
            [
                Tool(
                    name=t["name"],
                    slug=_slugify(t["name"]),
                    summary=t["summary"],
                    description="<p>{}</p>".format(t["summary"]),
                    github=t["github"],
                    website=t["website"],
                    status=t["status"],
                    order=i,
                    published=True,
                )
                for i, t in enumerate(TOOLS, start=1)
            ]
        )
