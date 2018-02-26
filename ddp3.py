from ddpy.ddan.ddan import DDAN


ddan = DDAN(api_key="68D29E0B-97D8-4ED0-8B8A-78671B3AF4E2", analyzer_ip="10.52.141.207")

resp = ddan.test_connection()

print(resp)

