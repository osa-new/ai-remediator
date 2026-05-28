from graph.workflow import build_graph
from services.vector_store import initialize_db


def main():

    initialize_db()

    incident = """
    nginx returning 502 bad gateway
    CPU usage at 95%
    upstream connection timeout
    """

    app = build_graph()

    result = app.invoke({
        "incident": incident
    })

    print("\n")
    print("========== INCIDENT ==========")
    print(incident)

    print("\n")
    print("========== DIAGNOSIS ==========")
    print(result["diagnosis"])

    print("\n")
    print("========== FIX ==========")
    print(result["fix"])


if __name__ == "__main__":
    main()