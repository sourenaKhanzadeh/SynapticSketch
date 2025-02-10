from diagrams import Diagram, Cluster
from diagrams.programming.language import Python
from diagrams.onprem.compute import Server
from diagrams.onprem.database import MongoDB
from diagrams.onprem.monitoring import Prometheus
from diagrams.onprem.client import User
from diagrams.generic.os import Windows
from diagrams.generic.device import Mobile

with Diagram("SoloRL - Solidity RL Architecture", show=False, filename="solidity_rl_architecture", outformat="png"):

    user = User("Developer")
    dashboard = Prometheus("Benchmarking & Reporting")

    with Cluster("Solidity RL Optimization System"):

        # Environment Layer
        environment = Python("Environment Layer\n(Solidity Simulation)")

        # RL Agent Layer
        agent = Python("Agent Layer\n(RL Optimizer)")

        # Optimization Layer
        optimization = Python("Optimization Layer\n(Bytecode-Level)")

        # External Tools Integration
        external_tools = Server("External Optimization\nTools")

        # Database
        db = MongoDB("Performance Metrics DB")

    # Connecting Components
    user >> environment
    environment >> agent
    agent >> optimization
    optimization >> db
    optimization >> external_tools
    db >> dashboard
    dashboard >> user

    # Optional Integration with Other Devices
    windows_pc = Windows("Windows PC\n(Your Setup)")
    mobile_app = Mobile("Mobile Notifications")

    dashboard >> windows_pc
    dashboard >> mobile_app
