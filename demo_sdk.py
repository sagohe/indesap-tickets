from sdk.indesap_client import IndesapClient

client = IndesapClient(base_url="http://127.0.0.1:8000")

t1 = client.create_ticket("Checkout falla", "500 en /checkout", priority="high")
t2 = client.create_ticket("Lento al iniciar sesión", "LCP alto", priority="medium")

print("CREADOS:", t1, t2, sep="\n")

print("\nLISTA:")
for t in client.list_tickets():
    print(f"- #{t.id} [{t.status}] {t.title} ({t.priority})")

cerrado = client.close_ticket(t1.id)
print("\nCERRADO:", cerrado)