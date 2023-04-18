# Minimal Example for GO AWAY messages

1. Install requirements
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Insert the IP address of your device (`look for INSERT YOUR IP ADDRESS`)

3. Run the code
```bash
python -m subscribe
```

4. Wait

After 8 minutes (4x120 seconds) the gNMI session will be terminated with:

```
grpclib.exceptions.StreamTerminatedError: Connection lost
```
