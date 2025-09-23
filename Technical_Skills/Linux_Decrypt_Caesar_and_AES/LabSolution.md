# Activity: Decrypt an encrypted message (Lab Solution)

The lab consists of three main tasks: identify initial encrypted assets, locate and decode a Caesar cipher hint, and decrypt the AES‑256‑CBC protected file. Commands and representative outputs are embedded under each task to mirror the execution flow used in other labs of the portfolio.

### Task 1. Inspect initial directory and read instructions
List current directory contents to establish available artifacts:
```bash
ls
```
Output:
```plaintext
Q1.encrypted  README.txt  caesar
```
Read the instructional file:
```bash
cat README.txt
```
Output excerpt:
```plaintext
Hello,
All of your data has been encrypted. To recover your data, you will need to solve a cipher...
```
Key takeaway: A hidden file in the `caesar` subdirectory contains the next clue.

### Task 2. Locate hidden file and derive decryption command
Enter the indicated subdirectory and include hidden entries in the listing:
```bash
cd caesar
ls -a
```
Output:
```plaintext
.  ..  .leftShift3
```

Display the hidden file’s contents (Caesar cipher, shift 3 to the left):
```bash
cat .leftShift3
```
Ciphertext snippet:
```plaintext
Lq rughu wr uhfryhu brxu ilohv brx zloo qhhg wr hqwhu wkh iroorzlqj frppdqg:

rshqvvo dhv-256-fef -sengi2 -d -g -lq T1.hqfubswhg -rxw T1.uhfryhuhg -n hwwxeuxwh
```
Reverse the shift (3 left) using `tr` mapping ranges (`d-za-cD-ZA-C` → `a-zA-Z`):
```bash
cat .leftShift3 | tr "d-za-cD-ZA-C" "a-zA-Z"
```
Decrypted hint:
```plaintext
In order to recover your files you will need to enter the following command:

openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute
```
Return to the home directory to run the decryption where the target file resides:
```bash
cd ~
```

### Task 3. Decrypt the AES-256-CBC file
Execute the revealed OpenSSL command (PBKDF2 strengthens the passphrase-derived key, `-a` handles Base64, `-d` decrypts):
```bash
openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute
```
List directory to confirm creation of the recovered plaintext file:
```bash
ls
```
Output:
```plaintext
Q1.encrypted  Q1.recovered  README.txt  caesar
```
Display recovered message:
```bash
cat Q1.recovered
```
Output:
```plaintext
If you are able to read this, then you have successfully decrypted the classic cipher text. You recovered the encryption key that was used to encrypt this file. Great work!
```
Optional inspection of original Base64/OpenSSL salted ciphertext:
```bash
cat Q1.encrypted
```
Excerpt:
```plaintext
U2FsdGVkX1/nxHZY2p53/6gRmQ9alkNrVwOwPOgpTeB09rdnvKnydLPQsnOYHjgR
42Mwdv0ye94Im+u100Fl2+Bx3SHjJ7wZjOxA7Jew1x7g3LcRsRnFcFLyfAnn0f3u
...
```

### Validation
- Hidden file `.leftShift3` discovered and interpreted (Caesar shift 3 left).
- Decryption command executed successfully producing `Q1.recovered`.
- Plaintext message readable and contextually coherent.
- Ciphertext format consistent with OpenSSL salted Base64 output.

### Notes
- `tr "d-za-cD-ZA-C" "a-zA-Z"` realinea alfabetos desplazados para revertir un shift de 3.
- `-pbkdf2` reemplaza el esquema heredado de derivación débil y endurece la clave contra ataques de fuerza bruta.
- Para escenarios reales se prefiere un modo autenticado (AES-GCM) para asegurar integridad además de confidencialidad.
- Evita incrustar la passphrase en el historial (alternativas: variable de entorno, `-pass stdin`).
- Se puede añadir verificación de integridad posterior: `sha256sum Q1.recovered` si se requiere evidencia.
